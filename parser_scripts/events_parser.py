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
    dirList.remove('997.specrand_fr')
    dirList.remove('998.specrand_is')
    dirList.remove('999.specrand_ir')
    dirList.remove('996.specrand_fs')
    

    #Check if any benchmark directories are missing, if any are print them
    benchmarks_total = intSpeed+intRate+fpSpeed+fpRate
    set_difference = set(benchmarks_total).symmetric_difference(set(dirList))
    list_difference = list(set_difference)
    if (len(list_difference) > 0):
        print("Some benchmark(s) are missing.")
        for entry in list_difference:
            print(entry)

    #Parse Serial benchmarks
    for benchmark in dirList:
        inputFile = cwd+'/'+benchmark+"/events.csv"
        outputDir = os.getcwd()+'/uprof_results_cumulative/'+benchmark
        if (not (os.path.exists(outputDir))):
            os.makedirs(outputDir)
        outputFile = outputDir+"/events.csv"
        processCSVFile(inputFile, outputFile)

def processCSVFile(inputFile, outputFile):
    #entire csv file read into data easier to handle odd csv spacing of data
    data = []

    coreMetrics = []
    ccxMetrics = []
    pkgMetrics = []

    with open(inputFile, 'r') as file:
        reader = csv.reader(file)

        #skip to column headers
        next(reader)

        for row in reader:
            data.append(row)
    
    coreMetrics = processCoreMetrics(data)
    ccxMetrics = processCCXMetrics(data)
    pkgMetrics = processPKGMetrics(data)

    #write results to new 'metrics.csv' file
    rows = []
    for i in range(len(coreMetrics)):
        rows.append(coreMetrics[i])
    for i in range(len(ccxMetrics)):
        rows.append(ccxMetrics[i])
    for i in range(len(pkgMetrics)):
        rows.append(pkgMetrics[i])

    with open(outputFile, 'w') as csvfile:
        writer = csv.writer(csvfile)
        fields = ['Metric Name', 'Cumulative']
        writer.writerow(fields)
        writer.writerows(rows)

def processCoreMetrics(data):
    headers = []
    core = []

    for i in range(22):
        headers.append(data[0][i])

    for i in range(22):
        sum = 0
        row = []
        for j in range(0+i,1035+i,22):
            sum = sum + float(data[1][j])
        row.append(headers[i])
        row.append(sum)
        core.append(row)

    return core

def processCCXMetrics(data):
    headers = []
    ccx = []

    for i in range(1056,1062):
        headers.append(data[0][i])

    for i in range(6):
        sum = 0
        row = []
        for j in range(1056+i,1151+i,6):
            sum = sum + float(data[1][j])
        row.append(headers[i])
        row.append(sum)
        ccx.append(row)

    return ccx

def processPKGMetrics(data):
    headers = []
    pkg = []

    for i in range(1152,1169):
        headers.append(data[0][i])

    for i in range (17):
        sum = 0
        row = []
        for j in range(1152+i,1186+i,17):
            sum = sum + float(data[1][j])
        row.append(headers[i])
        row.append(sum)
        pkg.append(row)

    return pkg

# Call to invoke main method to begin program.
if __name__ == "__main__":
    main()

# End of Program