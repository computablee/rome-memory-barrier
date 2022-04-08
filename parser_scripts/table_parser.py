import csv
import os
from pathlib import Path

intSpeed = ['600.perlbench_s', '602.gcc_s', '605.mcf_s', '620.omnetpp_s', '623.xalancbmk_s',
            '625.x264_s', '631.deepsjeng_s', '641.leela_s', '648.exchange2_s', '657.xz_s']
intRate = ['500.perlbench_r', '502.gcc_r', '505.mcf_r', '520.omnetpp_r', '523.xalancbmk_r',
            '525.x264_r', '531.deepsjeng_r', '541.leela_r', '548.exchange2_r', '557.xz_r']
fpSpeed = ['603.bwaves_s', '607.cactuBSSN_s', '619.lbm_s', '621.wrf_s', '628.pop2_s',
           '638.imagick_s', '644.nab_s','649.fotonik3d_s', '654.roms_s']
fpRate = ['503.bwaves_r', '507.cactuBSSN_r', '508.namd_r', '510.parest_r', '511.povray_r',
          '519.lbm_r', '521.wrf_r', '526.blender_r', '527.cam4_r', '538.imagick_r', '544.nab_r',
          '549.fotonik3d_r', '554.roms_r']

# ADD 627.cam4_s back in if available!
#fpSpeed = ['603.bwaves_s', '607.cactuBSSN_s', '619.lbm_s', '621.wrf_s', '627.cam4_s', '628.pop2_s',
           #'638.imagick_s', '644.nab_s','649.fotonik3d_s', '654.roms_s']

def main():
    os.chdir("..")

    verifyDirectoriesNeededExist()
    attachHeaders()
    

    cwd = os.getcwd()+"/uprof_results"
    dirList = os.listdir(cwd)

    dirList.remove('.placeholder') #remove non-benchmark entry
    #remove benchmarks that are not in the 43
    #dirList.remove('997.specrand_fr')
    #dirList.remove('998.specrand_is')
    #dirList.remove('999.specrand_ir')
    #dirList.remove('996.specrand_fs')

    #Check if any benchmark directories are missing, if any are print them
    benchmarks_total = intSpeed+intRate+fpSpeed+fpRate
    set_difference = set(benchmarks_total).symmetric_difference(set(dirList))
    list_difference = list(set_difference)
    if (len(list_difference) > 0):
        print("Some benchmark(s) are missing.")
        for entry in list_difference:
            print(entry)

    #Create CSV for graphing by suite
    for benchmark in dirList:
        inputEvents = os.getcwd()+'/uprof_results_cumulative/'+benchmark+"/events.csv"
        parseCSVsForGraphCSVs(inputEvents, benchmark)

def parseCSVsForGraphCSVs(inputEvents, benchmark):
    events = []
    metrics = []

    ipc = []
    pipelineUtil = []
    cpiDF = []

    #read in events data
    with open(inputEvents, 'r') as file:
        reader = csv.reader(file)

        #skip column headers
        next(reader)

        for row in reader:
            events.append(row)

    genParams = processCSVsGenParams(events, benchmark)
    cacheBreak = processCSVsCacheBreakdown(events, benchmark)

    #check which suite this benchmark belongs to
    if (intRate.count(benchmark) > 0):
        writeToSuiteMetricSpecificCSV(genParams, (os.getcwd()+"/graph_data/int_rate"+"/general_parameters.csv"))
        writeToSuiteMetricSpecificCSV(cacheBreak, (os.getcwd()+"/graph_data/int_rate"+"/cache_breakdown.csv"))
    elif (intSpeed.count(benchmark) > 0):
        writeToSuiteMetricSpecificCSV(genParams, (os.getcwd()+"/graph_data/int_speed"+"/general_parameters.csv"))
        writeToSuiteMetricSpecificCSV(cacheBreak, (os.getcwd()+"/graph_data/int_speed"+"/cache_breakdown.csv"))
    elif (fpRate.count(benchmark) > 0):
        writeToSuiteMetricSpecificCSV(genParams, (os.getcwd()+"/graph_data/fp_rate"+"/general_parameters.csv"))
        writeToSuiteMetricSpecificCSV(cacheBreak, (os.getcwd()+"/graph_data/fp_rate"+"/cache_breakdown.csv"))
    elif (fpSpeed.count(benchmark) > 0):
        writeToSuiteMetricSpecificCSV(genParams, (os.getcwd()+"/graph_data/fp_speed"+"/general_parameters.csv"))
        writeToSuiteMetricSpecificCSV(cacheBreak, (os.getcwd()+"/graph_data/fp_speed"+"/cache_breakdown.csv"))

def attachHeadersCSVs(headers, filename):
    with open(filename, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)

def writeToSuiteMetricSpecificCSV(data, filename):
    #make sure csv exists for appending
    Path(filename).touch()

    with open(filename, 'a') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(data)

def processCSVsGenParams(events, benchmark):
    cycles = float(float(events[3][1])/1000000000)
    instr = float(float(events[4][1])/1000000000)
    branches = float(float(events[5][1])/1000000000)
    loads = float(float(events[6][1])/1000000000)
    stores = float(float(events[7][1])/1000000000)
    ipc = round((float(instr/cycles)),2)
    
    row = []
    row.append(benchmark)
    row.append(str(cycles))
    row.append(str(instr))
    row.append(str(branches))
    row.append(str(loads))
    row.append(str(stores))
    row.append(str(ipc))

    return row


def processCSVsCacheBreakdown(events, benchmark):
    l2Access = float(float(events[11][1])+float(events[12][1])/1000)
    l2Miss = float(float(events[17][1])+float(events[18][1])/1000)
    l2MissRate = round((float(l2Miss/l2Access)*100),2)
    l3Access = float(float(events[24][1])/1000)
    l3Miss = float(float(events[25][1])/1000)
    l3MissRate = round((float(l3Miss/l3Access)*100),2)
    row = []
    row.append(benchmark)
    row.append(str(l2Access))
    row.append(str(l2Miss))
    row.append(str(l2MissRate))
    row.append(str(l3Access))
    row.append(str(l3Miss))
    row.append(str(l3MissRate))

    return row

def verifyDirectoriesNeededExist():
    home = os.getcwd()

    #create /graph_data directory is doesn't exist
    directory = os.getcwd()+"/graph_data"
    if (not (os.path.exists(directory))):
        os.makedirs(directory)
    os.chdir(directory)

    #create /graph_data/int_speed directory is doesn't exist
    subdir1 = os.getcwd()+"/int_speed"
    if (not (os.path.exists(subdir1))):
        os.mkdir(subdir1)
    

    #create /graph_data/int_rate directory is doesn't exist
    subdir2 = os.getcwd()+"/int_rate"
    if (not (os.path.exists(subdir2))):
        os.mkdir(subdir2)

    #create /graph_data/fp_speed directory is doesn't exist
    subdir3 = os.getcwd()+"/fp_speed"
    if (not (os.path.exists(subdir3))):
        os.mkdir(subdir3)

    #create /graph_data/fp_rate directory is doesn't exist
    subdir4 = os.getcwd()+"/fp_rate"
    if (not (os.path.exists(subdir4))):
        os.mkdir(subdir4)
    
    os.chdir(home)
    
def attachHeaders():
    genParamHeaders = ['Benchmark', 'Cycles [Billions]', 'Instr. [Billions]', 'Branches [Billions]', 'Loads [Billions]', 'Stores [Billions]', 'IPC']
    cacheBreakHeaders = ['Benchmark','L2 Access Per 1K Instr.', 'L2 Miss Per 1K Instr.', 'L2 Miss Rate (%)', 'L3 Access Per 1K Instr.', 'L3 Miss Per 1K Instr.', 'L3 Miss Rate (%)']
    attachHeadersCSVs(genParamHeaders, (os.getcwd()+"/graph_data/int_rate"+"/general_parameters.csv"))
    attachHeadersCSVs(genParamHeaders, (os.getcwd()+"/graph_data/int_speed"+"/general_parameters.csv"))
    attachHeadersCSVs(genParamHeaders, (os.getcwd()+"/graph_data/fp_rate"+"/general_parameters.csv"))
    attachHeadersCSVs(genParamHeaders, (os.getcwd()+"/graph_data/fp_speed"+"/general_parameters.csv"))

    attachHeadersCSVs(cacheBreakHeaders, (os.getcwd()+"/graph_data/int_rate"+"/cache_breakdown.csv"))
    attachHeadersCSVs(cacheBreakHeaders, (os.getcwd()+"/graph_data/int_speed"+"/cache_breakdown.csv"))
    attachHeadersCSVs(cacheBreakHeaders, (os.getcwd()+"/graph_data/fp_rate"+"/cache_breakdown.csv"))
    attachHeadersCSVs(cacheBreakHeaders, (os.getcwd()+"/graph_data/fp_speed"+"/cache_breakdown.csv"))

# Call to invoke main method to begin program.
if __name__ == "__main__":
    main()

# End of Program
