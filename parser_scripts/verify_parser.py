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

    #Verify Serial benchmarks
    for benchmark in dirList:
        inputEvents = os.getcwd()+'/uprof_results_cumulative/'+benchmark+"/events.csv"
        inputMetrics = os.getcwd()+'/uprof_results_cumulative/'+benchmark+"/metrics.csv"
        verifyData(inputEvents, inputMetrics, benchmark)

def verifyData(inputEvents, inputMetrics, benchmark):
    events = []
    metrics = []

    #read in events data
    with open(inputEvents, 'r') as file:
        reader = csv.reader(file)

        #skip column headers
        next(reader)

        for row in reader:
            events.append(row)

    #read in metrics data
    with open(inputMetrics, 'r') as file:
        reader = csv.reader(file)

        #skip column headers
        next(reader)

        for row in reader:
            metrics.append(row)
    
    if(verifyIPC(events,metrics,benchmark) and verifyCPI(events,metrics,benchmark) 
        and verifyL3Miss(events, metrics, benchmark) and verifyL3Access(events, metrics, benchmark)):
        print("Verified: "+benchmark)
    else:
        error = "Inconsistent: "+benchmark
        if (intRate.count(benchmark) > 0):
            print(error+" in IntRate")
        elif (intSpeed.count(benchmark) > 0):
            print(error+" in IntSpeed")
        elif (fpRate.count(benchmark) > 0):
            print(error+" in FPRate")
        elif (fpSpeed.count(benchmark) > 0):
            print(error+" in FPSpeed")
    
    
def verifyIPC(events, metrics, benchmark):
    correct = False
    ipc = round(float(events[4][1])/float(events[3][1]), 2)
    if (ipc == round(float(metrics[2][1]), 2)):
        correct = True
    else:
        print("IPC FAILED with Difference of "+str(abs(round(ipc - round(float(metrics[2][1]),2),2))))
        print(benchmark+" Metrics: "+str(round(float(metrics[2][1]),2)))
        print(benchmark+" Events: "+str(ipc))

    return correct

def verifyCPI(events, metrics, benchmark):
    correct = False
    cpi = round(float(events[3][1])/float(events[4][1]), 2)
    if (cpi == round(float(metrics[3][1]), 2)):
        correct = True
    else:
        print("CPI FAILED with Difference of "+str(abs(round(cpi - round(float(metrics[3][1]),2),2))))
        print(benchmark+" Metrics: "+str(round(float(metrics[3][1]),2)))
        print(benchmark+" Events: "+str(cpi))

    return correct

def verifyL3Miss(events, metrics, benchmark):
    correct = False
    l3miss = round(float(events[25][1]), 2)
    if (l3miss == round(float(metrics[18][1]), 2)):
        correct = True
    else:
        print("L3 Miss FAILED with Difference of "+str(abs(round(l3miss - round(float(metrics[18][1]),2),2))))
        print(benchmark+" Metrics: "+str(round(float(metrics[18][1]),2)))
        print(benchmark+" Events: "+str(l3miss))

    return correct

def verifyL3Access(events, metrics, benchmark):
    correct = False
    l3access = round(float(events[24][1]), 2)
    if (l3access == round(float(metrics[17][1]), 2)):
        correct = True
    else:
        print("L3 Miss FAILED with Difference of "+str(abs(round(l3access - round(float(metrics[17][1]),2),2))))
        print(benchmark+" Metrics: "+str(round(float(metrics[17][1]),2)))
        print(benchmark+" Events: "+str(l3access))

    return correct

# Call to invoke main method to begin program.
if __name__ == "__main__":
    main()

# End of Program
