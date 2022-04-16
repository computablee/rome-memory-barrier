import csv
import os

intSpeed = ['600.perlbench_s', '602.gcc_s', '605.mcf_s', '620.omnetpp_s', '623.xalancbmk_s',
            '625.x264_s', '631.deepsjeng_s', '641.leela_s', '648.exchange2_s', '657.xz_s']
intRate = ['500.perlbench_r', '502.gcc_r', '505.mcf_r', '520.omnetpp_r', '523.xalancbmk_r',
            '525.x264_r', '531.deepsjeng_r', '541.leela_r', '548.exchange2_r', '557.xz_r']
fpSpeed = ['603.bwaves_s', '607.cactuBSSN_s', '619.lbm_s', '621.wrf_s', '628.pop2_s',
           '638.imagick_s', '644.nab_s','649.fotonik3d_s', '654.roms_s']
fpRate = ['503.bwaves_r', '507.cactuBSSN_r', '508.namd_r', '510.parest_r', '511.povray_r',
          '519.lbm_r', '521.wrf_r', '526.blender_r', '527.cam4_r', '538.imagick_r', '544.nab_r',
          '549.fotonik3d_r', '554.roms_r']
fpIntSpeedSerial = ['600.perlbench_s',  '602.gcc_s', '605.mcf_s', '620.omnetpp_s', '623.xalancbmk_s',
            '625.x264_s', '631.deepsjeng_s', '641.leela_s', '648.exchange2_s']
fpIntSpeedParallel = ['603.bwaves_s', '607.cactuBSSN_s', '619.lbm_s', '621.wrf_s', '628.pop2_s',
           '638.imagick_s', '644.nab_s','649.fotonik3d_s', '654.roms_s', '657.xz_s']
# ADD 627.cam4_s back in if available!
#fpSpeed = ['603.bwaves_s', '607.cactuBSSN_s', '619.lbm_s', '621.wrf_s', '627.cam4_s', '628.pop2_s',
           #'638.imagick_s', '644.nab_s','649.fotonik3d_s', '654.roms_s']

def main():
    os.chdir("..")

    #create /uprof_results_cumulative directory is doesn't exist
    directory = os.getcwd()+"/uprof_results_cumulative"
    if (not (os.path.exists(directory))):
        os.makedirs(directory)

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

    serial = fpIntSpeedSerial
    parallel = intRate+fpRate+fpIntSpeedParallel

    #Parse Serial benchmarks
    for benchmark in serial:
        inputFile = cwd+'/'+benchmark+"/metrics.csv"
        outputDir = os.getcwd()+'/uprof_results_cumulative/'+benchmark
        if (not (os.path.exists(outputDir))):
            os.makedirs(outputDir)
        outputFile = outputDir+"/metrics.csv"
        processCSVFile(inputFile, outputFile, True)

    #Parse Parallel benchmarks
    for benchmark in parallel:
        inputFile = cwd+'/'+benchmark+"/metrics.csv"
        outputDir = os.getcwd()+'/uprof_results_cumulative/'+benchmark
        if (not (os.path.exists(outputDir))):
            os.makedirs(outputDir)
        outputFile = outputDir+"/metrics.csv"
        processCSVFile(inputFile, outputFile, False)
    

def processCSVFile(inputFile, outputFile, s):
    #entire csv file read into data easier to handle odd csv spacing of data
    data = []

    #boolean for serial or parallel
    serial = s

    coreMetrics = []
    l3Metrics = []
    dfMetrics = []

    with open(inputFile, 'r') as file:
        reader = csv.reader(file)

        #skip to column headers of core metrics section
        for i in range(49): next(reader)

        for row in reader:
            data.append(row)

    #PROCESS METRICS
    coreMetrics = processCoreMetrics(data, serial)
    l3Metrics = processL3Metrics(data, serial)
    dfMetrics = processDFMetrics(data, serial)

    #write results to new file
    rows = []
    for i in range(len(coreMetrics)):
        rows.append(coreMetrics[i])
    for i in range(len(l3Metrics)):
        rows.append(l3Metrics[i])
    for i in range(len(dfMetrics)):
        rows.append(dfMetrics[i])

    with open(outputFile, 'w') as csvfile:
        writer = csv.writer(csvfile)
        fields = ['Metric Name', 'Cumulative']
        writer.writerow(fields)
        writer.writerows(rows)
    

#This function processes the core metrics of one 'metrics.csv' file
def processCoreMetrics(data, serial):
    headers =[]
    metrics = []
    core = []

    for i in range(17):
        headers.append(data[i][0])
        del data[i][0] #get rid of metric header from that row
        metrics.append(data[i])
    
    #if serial only grab Core-0 data
    if (serial):
        for i in range(17):
            row = []
            row.append(headers[i])
            row.append(metrics[i][0])
            core.append(row)     
    else: 
        #avg everything
        for i in range(len(metrics)):
            row = []
            row.append(headers[i])
            sum = 0
            avg = 0
            for j in range(48):
                sum = sum + float(metrics[i][j])
            avg = sum/len(metrics[0])
            row.append(avg)
            core.append(row)

    return core

#This function processes the L3 metrics of one 'metrics.csv' file
def processL3Metrics(data, serial):
    headers =[]
    metrics = []
    l3 = []

    for i in range(20, 25):
        headers.append(data[i][0])
        del data[i][0] #get rid of metric header from that row
        metrics.append(data[i])

    #if serial only grab CCX-0 data
    if (serial):
        for i in range(5):
            row = []
            row.append(headers[i])
            row.append(metrics[i][0])
            l3.append(row)
    else:
        # sum the accesses and misses
        for i in range(2):
            sum = 0
            row = []
            for j in range(16):
                sum = sum + float(metrics[i][j])
            row.append(headers[i])
            row.append(sum)
            l3.append(row)

        # avg the hit rate, miss rate, and miss latency
        for i in range(2,5):
            sum = 0
            avg = 0
            row = []
            for j in range(16):
                sum = sum + float(metrics[i][j])
            avg = sum/len(metrics[0])
            row.append(headers[i])
            row.append(avg)
            l3.append(row)

    return l3

#This function processes the DF metrics of one 'metrics.csv' file
def processDFMetrics(data, serial):
    headers =[]
    metrics = []
    df = []

    for i in range(28, 47):
        headers.append(data[i][0])
        del data[i][0] #get rid of metric header from that row
        metrics.append(data[i])

    #if serial only grab CCX-0 data
    if (serial):
        for i in range(len(metrics)):
            row = []
            row.append(headers[i])
            row.append(metrics[i][0])
            df.append(row)
    else:
        for i in range(len(metrics)):
            sum = 0
            row = []
            for j in range(2):
                sum = sum + float(metrics[i][j])
            row.append(headers[i])
            row.append(sum)
            df.append(row)

    return df

# Call to invoke main method to begin program.
if __name__ == "__main__":
    main()

# End of Program
