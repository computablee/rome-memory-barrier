import csv
import os

def main():
    cwd = os.getcwd()+"/uprof_results"
    
    #500.perlbench_r
    inputFile = cwd+"/500.perlbench_r/events.csv"
    outputFile = os.getcwd()+"/uprof_results_cumulative/500_perlbench_r_events_cumulative.csv"
    processCSVFile(inputFile, outputFile)

    #502.gcc_r
    inputFile = cwd+"/502.gcc_r/events.csv"
    outputFile = os.getcwd()+"/uprof_results_cumulative/502_gcc_r_events_cumulative.csv"
    processCSVFile(inputFile, outputFile)

    #503.bwaves_r
    inputFile = cwd+"/503.bwaves_r/events.csv"
    outputFile = os.getcwd()+"/uprof_results_cumulative/503_bwaves_r_events_cumulative.csv"
    processCSVFile(inputFile, outputFile)

    #505.mcf_r
    inputFile = cwd+"/505.mcf_r/events.csv"
    outputFile = os.getcwd()+"/uprof_results_cumulative/505_mcf_r_events_cumulative.csv"
    processCSVFile(inputFile, outputFile)

    #507.cactuBSSN_r
    inputFile = cwd+"/507.cactuBSSN_r/events.csv"
    outputFile = os.getcwd()+"/uprof_results_cumulative/507_cactuBSSN_r_events_cumulative.csv"
    processCSVFile(inputFile, outputFile)

    #508.namd_r
    inputFile = cwd+"/508.namd_r/events.csv"
    outputFile = os.getcwd()+"/uprof_results_cumulative/508_namd_r_events_cumulative.csv"
    processCSVFile(inputFile, outputFile)

    #510.parest_r
    inputFile = cwd+"/510.parest_r/events.csv"
    outputFile = os.getcwd()+"/uprof_results_cumulative/510_parest_r_events_cumulative.csv"
    processCSVFile(inputFile, outputFile)

    #511.povray_r
    inputFile = cwd+"/511.povray_r/events.csv"
    outputFile = os.getcwd()+"/uprof_results_cumulative/511_povray_r_events_cumulative.csv"
    processCSVFile(inputFile, outputFile)

    #519.lbm_r
    inputFile = cwd+"/519.lbm_r/events.csv"
    outputFile = os.getcwd()+"/uprof_results_cumulative/519_lbm_r_events_cumulative.csv"
    processCSVFile(inputFile, outputFile)

    #520.omnetpp_r
    inputFile = cwd+"/520.omnetpp_r/events.csv"
    outputFile = os.getcwd()+"/uprof_results_cumulative/520_omnetpp_r_events_cumulative.csv"
    processCSVFile(inputFile, outputFile)

    #521.wrf_r
    inputFile = cwd+"/521.wrf_r/events.csv"
    outputFile = os.getcwd()+"/uprof_results_cumulative/521_wrf_r_events_cumulative.csv"
    processCSVFile(inputFile, outputFile)

    #523.xalancbmk_r
    inputFile = cwd+"/523.xalancbmk_r/events.csv"
    outputFile = os.getcwd()+"/uprof_results_cumulative/523_xalancbmk_r_events_cumulative.csv"
    processCSVFile(inputFile, outputFile)

    #525.x264_r
    inputFile = cwd+"/525.x264_r/events.csv"
    outputFile = os.getcwd()+"/uprof_results_cumulative/525_x264_r_events_cumulative.csv"
    processCSVFile(inputFile, outputFile)

    #526.blender_r
    inputFile = cwd+"/526.blender_r/events.csv"
    outputFile = os.getcwd()+"/uprof_results_cumulative/526_blender_r_events_cumulative.csv"
    processCSVFile(inputFile, outputFile)

    #527.cam4_r
    inputFile = cwd+"/527.cam4_r/events.csv"
    outputFile = os.getcwd()+"/uprof_results_cumulative/527_cam4_r_events_cumulative.csv"
    processCSVFile(inputFile, outputFile)

    #531.deepsjeng_r
    inputFile = cwd+"/531.deepsjeng_r/events.csv"
    outputFile = os.getcwd()+"/uprof_results_cumulative/531_deepsjeng_r_events_cumulative.csv"
    processCSVFile(inputFile, outputFile)

    #538.imagick_r
    inputFile = cwd+"/538.imagick_r/events.csv"
    outputFile = os.getcwd()+"/uprof_results_cumulative/538_imagick_r_events_cumulative.csv"
    processCSVFile(inputFile, outputFile)

    #541.leela_r
    inputFile = cwd+"/541.leela_r/events.csv"
    outputFile = os.getcwd()+"/uprof_results_cumulative/541_leela_r_events_cumulative.csv"
    processCSVFile(inputFile, outputFile)

    #544.nab_r
    inputFile = cwd+"/544.nab_r/events.csv"
    outputFile = os.getcwd()+"/uprof_results_cumulative/544_nab_r_events_cumulative.csv"
    processCSVFile(inputFile, outputFile)

    #548.exchange2_r
    inputFile = cwd+"/548.exchange2_r/events.csv"
    outputFile = os.getcwd()+"/uprof_results_cumulative/548_exchange2_r_events_cumulative.csv"
    processCSVFile(inputFile, outputFile)

    #549.fotonik3d_r
    inputFile = cwd+"/549.fotonik3d_r/events.csv"
    outputFile = os.getcwd()+"/uprof_results_cumulative/549_fotonik3d_r_events_cumulative.csv"
    processCSVFile(inputFile, outputFile)

    #554.roms_r
    inputFile = cwd+"/554.roms_r/events.csv"
    outputFile = os.getcwd()+"/uprof_results_cumulative/554_roms_r_events_cumulative.csv"
    processCSVFile(inputFile, outputFile)

    #557.xz_r
    inputFile = cwd+"/557.xz_r/events.csv"
    outputFile = os.getcwd()+"/uprof_results_cumulative/557_xz_r_events_cumulative.csv"
    processCSVFile(inputFile, outputFile)

    #600.perlbench_s
    inputFile = cwd+"/600.perlbench_s/events.csv"
    outputFile = os.getcwd()+"/uprof_results_cumulative/600_perlbench_s_events_cumulative.csv"
    processCSVFile(inputFile, outputFile)

    #602.gcc_s
    inputFile = cwd+"/602.gcc_s/events.csv"
    outputFile = os.getcwd()+"/uprof_results_cumulative/602_gcc_s_events_cumulative.csv"
    processCSVFile(inputFile, outputFile)
    
    #603.bwaves_s
    inputFile = cwd+"/603.bwaves_s/events.csv"
    outputFile = os.getcwd()+"/uprof_results_cumulative/603_bwaves_s_events_cumulative.csv"
    processCSVFile(inputFile, outputFile)
    
    #605.mcf_s
    inputFile = cwd+"/605.mcf_s/events.csv"
    outputFile = os.getcwd()+"/uprof_results_cumulative/605_mcf_s_events_cumulative.csv"
    processCSVFile(inputFile, outputFile)
    
    #607.cactuBSSN_s
    inputFile = cwd+"/607.cactuBSSN_s/events.csv"
    outputFile = os.getcwd()+"/uprof_results_cumulative/607_cactuBSSN_s_events_cumulative.csv"
    processCSVFile(inputFile, outputFile)
    
    #619.lbm_s
    inputFile = cwd+"/619.lbm_s/events.csv"
    outputFile = os.getcwd()+"/uprof_results_cumulative/619_lbm_s_events_cumulative.csv"
    processCSVFile(inputFile, outputFile)
    
    #620.omnetpp_s
    inputFile = cwd+"/620.omnetpp_s/events.csv"
    outputFile = os.getcwd()+"/uprof_results_cumulative/620_omnetpp_s_events_cumulative.csv"
    processCSVFile(inputFile, outputFile)
    
    #621.wrf_s
    inputFile = cwd+"/621.wrf_s/events.csv"
    outputFile = os.getcwd()+"/uprof_results_cumulative/621_wrf_s_events_cumulative.csv"
    processCSVFile(inputFile, outputFile)
    
    #623.xalancbmk_s
    inputFile = cwd+"/623.xalancbmk_s/events.csv"
    outputFile = os.getcwd()+"/uprof_results_cumulative/623_xalancbmk_s_events_cumulative.csv"
    processCSVFile(inputFile, outputFile)
    
    #625.x264_s
    inputFile = cwd+"/625.x264_s/events.csv"
    outputFile = os.getcwd()+"/uprof_results_cumulative/625_x264_s_events_cumulative.csv"
    processCSVFile(inputFile, outputFile)
    
    #628.pop2_s
    inputFile = cwd+"/628.pop2_s/events.csv"
    outputFile = os.getcwd()+"/uprof_results_cumulative/628_pop2_s_events_cumulative.csv"
    processCSVFile(inputFile, outputFile)
    
    #631.deepsjeng_s
    inputFile = cwd+"/631.deepsjeng_s/events.csv"
    outputFile = os.getcwd()+"/uprof_results_cumulative/631_deepsjeng_s_events_cumulative.csv"
    processCSVFile(inputFile, outputFile)
    
    #638.imagick_s
    inputFile = cwd+"/638.imagick_s/events.csv"
    outputFile = os.getcwd()+"/uprof_results_cumulative/638_imagick_s_events_cumulative.csv"
    processCSVFile(inputFile, outputFile)
    
    #641.leela_s
    inputFile = cwd+"/641.leela_s/events.csv"
    outputFile = os.getcwd()+"/uprof_results_cumulative/641_leela_s_events_cumulative.csv"
    processCSVFile(inputFile, outputFile)
    
    #644.nab_s
    inputFile = cwd+"/644.nab_s/events.csv"
    outputFile = os.getcwd()+"/uprof_results_cumulative/644_nab_s_events_cumulative.csv"
    processCSVFile(inputFile, outputFile)
    
    #648.exchange2_s
    inputFile = cwd+"/648.exchange2_s/events.csv"
    outputFile = os.getcwd()+"/uprof_results_cumulative/648_exchange2_s_events_cumulative.csv"
    processCSVFile(inputFile, outputFile)
    
    #649.fotonik3d_s
    inputFile = cwd+"/649.fotonik3d_s/events.csv"
    outputFile = os.getcwd()+"/uprof_results_cumulative/649_fotonik3d_s_events_cumulative.csv"
    processCSVFile(inputFile, outputFile)
    
    #654.roms_s
    inputFile = cwd+"/654.roms_s/events.csv"
    outputFile = os.getcwd()+"/uprof_results_cumulative/654_roms_s_events_cumulative.csv"
    processCSVFile(inputFile, outputFile)
    
    #657.xz_s
    inputFile = cwd+"/657.xz_s/events.csv"
    outputFile = os.getcwd()+"/uprof_results_cumulative/657_xz_s_events_cumulative.csv"
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

    #write results to new 'cumulativeMetrics.csv' file
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

    for i in range (22):
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

    for i in range (6):
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