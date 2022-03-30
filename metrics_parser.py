import csv
import os

def main():
    cwd = os.getcwd()+"/uprof_results"
    
    #500.perlbench_r
    inputFile = cwd+"/500.perlbench_r/metrics.csv"
    outputFile = os.getcwd()+"/uprof_results_cumulative/500_perlbench_r_metrics_cumulative.csv"
    processCSVFile(inputFile, outputFile, True)

    #502.gcc_r
    inputFile = cwd+"/502.gcc_r/metrics.csv"
    outputFile = os.getcwd()+"/uprof_results_cumulative/502_gcc_r_metrics_cumulative.csv"
    processCSVFile(inputFile, outputFile, True)

    #503.bwaves_r
    inputFile = cwd+"/503.bwaves_r/metrics.csv"
    outputFile = os.getcwd()+"/uprof_results_cumulative/503_bwaves_r_metrics_cumulative.csv"
    processCSVFile(inputFile, outputFile, True)

    #505.mcf_r
    inputFile = cwd+"/505.mcf_r/metrics.csv"
    outputFile = os.getcwd()+"/uprof_results_cumulative/505_mcf_r_metrics_cumulative.csv"
    processCSVFile(inputFile, outputFile, True)

    #507.cactuBSSN_r
    inputFile = cwd+"/507.cactuBSSN_r/metrics.csv"
    outputFile = os.getcwd()+"/uprof_results_cumulative/507_cactuBSSN_r_metrics_cumulative.csv"
    processCSVFile(inputFile, outputFile, True)

    #508.namd_r
    inputFile = cwd+"/508.namd_r/metrics.csv"
    outputFile = os.getcwd()+"/uprof_results_cumulative/508_namd_r_metrics_cumulative.csv"
    processCSVFile(inputFile, outputFile, True)

    #510.parest_r
    inputFile = cwd+"/510.parest_r/metrics.csv"
    outputFile = os.getcwd()+"/uprof_results_cumulative/510_parest_r_metrics_cumulative.csv"
    processCSVFile(inputFile, outputFile, True)

    #511.povray_r
    inputFile = cwd+"/511.povray_r/metrics.csv"
    outputFile = os.getcwd()+"/uprof_results_cumulative/511_povray_r_metrics_cumulative.csv"
    processCSVFile(inputFile, outputFile, True)

    #519.lbm_r
    inputFile = cwd+"/519.lbm_r/metrics.csv"
    outputFile = os.getcwd()+"/uprof_results_cumulative/519_lbm_r_metrics_cumulative.csv"
    processCSVFile(inputFile, outputFile, True)

    #520.omnetpp_r
    inputFile = cwd+"/520.omnetpp_r/metrics.csv"
    outputFile = os.getcwd()+"/uprof_results_cumulative/520_omnetpp_r_metrics_cumulative.csv"
    processCSVFile(inputFile, outputFile, True)

    #521.wrf_r
    inputFile = cwd+"/521.wrf_r/metrics.csv"
    outputFile = os.getcwd()+"/uprof_results_cumulative/521_wrf_r_metrics_cumulative.csv"
    processCSVFile(inputFile, outputFile, True)

    #523.xalancbmk_r
    inputFile = cwd+"/523.xalancbmk_r/metrics.csv"
    outputFile = os.getcwd()+"/uprof_results_cumulative/523_xalancbmk_r_metrics_cumulative.csv"
    processCSVFile(inputFile, outputFile, True)

    #525.x264_r
    inputFile = cwd+"/525.x264_r/metrics.csv"
    outputFile = os.getcwd()+"/uprof_results_cumulative/525_x264_r_metrics_cumulative.csv"
    processCSVFile(inputFile, outputFile, True)

    #526.blender_r
    inputFile = cwd+"/526.blender_r/metrics.csv"
    outputFile = os.getcwd()+"/uprof_results_cumulative/526_blender_r_metrics_cumulative.csv"
    processCSVFile(inputFile, outputFile, True)

    #527.cam4_r
    inputFile = cwd+"/527.cam4_r/metrics.csv"
    outputFile = os.getcwd()+"/uprof_results_cumulative/527_cam4_r_metrics_cumulative.csv"
    processCSVFile(inputFile, outputFile, True)

    #531.deepsjeng_r
    inputFile = cwd+"/531.deepsjeng_r/metrics.csv"
    outputFile = os.getcwd()+"/uprof_results_cumulative/531_deepsjeng_r_metrics_cumulative.csv"
    processCSVFile(inputFile, outputFile, True)

    #538.imagick_r
    inputFile = cwd+"/538.imagick_r/metrics.csv"
    outputFile = os.getcwd()+"/uprof_results_cumulative/538_imagick_r_metrics_cumulative.csv"
    processCSVFile(inputFile, outputFile, True)

    #541.leela_r
    inputFile = cwd+"/541.leela_r/metrics.csv"
    outputFile = os.getcwd()+"/uprof_results_cumulative/541_leela_r_metrics_cumulative.csv"
    processCSVFile(inputFile, outputFile, True)

    #544.nab_r
    inputFile = cwd+"/544.nab_r/metrics.csv"
    outputFile = os.getcwd()+"/uprof_results_cumulative/544_nab_r_metrics_cumulative.csv"
    processCSVFile(inputFile, outputFile, True)

    #548.exchange2_r
    inputFile = cwd+"/548.exchange2_r/metrics.csv"
    outputFile = os.getcwd()+"/uprof_results_cumulative/548_exchange2_r_metrics_cumulative.csv"
    processCSVFile(inputFile, outputFile, True)

    #549.fotonik3d_r
    inputFile = cwd+"/549.fotonik3d_r/metrics.csv"
    outputFile = os.getcwd()+"/uprof_results_cumulative/549_fotonik3d_r_metrics_cumulative.csv"
    processCSVFile(inputFile, outputFile, True)

    #554.roms_r
    inputFile = cwd+"/554.roms_r/metrics.csv"
    outputFile = os.getcwd()+"/uprof_results_cumulative/554_roms_r_metrics_cumulative.csv"
    processCSVFile(inputFile, outputFile, True)

    #557.xz_r
    inputFile = cwd+"/557.xz_r/metrics.csv"
    outputFile = os.getcwd()+"/uprof_results_cumulative/557_xz_r_metrics_cumulative.csv"
    processCSVFile(inputFile, outputFile, True)

    #600.perlbench_s
    inputFile = cwd+"/600.perlbench_s/metrics.csv"
    outputFile = os.getcwd()+"/uprof_results_cumulative/600_perlbench_s_metrics_cumulative.csv"
    processCSVFile(inputFile, outputFile, False)

    #602.gcc_s
    inputFile = cwd+"/602.gcc_s/metrics.csv"
    outputFile = os.getcwd()+"/uprof_results_cumulative/602_gcc_s_metrics_cumulative.csv"
    processCSVFile(inputFile, outputFile, False)
    
    #603.bwaves_s
    inputFile = cwd+"/603.bwaves_s/metrics.csv"
    outputFile = os.getcwd()+"/uprof_results_cumulative/603_bwaves_s_metrics_cumulative.csv"
    processCSVFile(inputFile, outputFile, False)
    
    #605.mcf_s
    inputFile = cwd+"/605.mcf_s/metrics.csv"
    outputFile = os.getcwd()+"/uprof_results_cumulative/605_mcf_s_metrics_cumulative.csv"
    processCSVFile(inputFile, outputFile, False)
    
    #607.cactuBSSN_s
    inputFile = cwd+"/607.cactuBSSN_s/metrics.csv"
    outputFile = os.getcwd()+"/uprof_results_cumulative/607_cactuBSSN_s_metrics_cumulative.csv"
    processCSVFile(inputFile, outputFile, False)
    
    #619.lbm_s
    inputFile = cwd+"/619.lbm_s/metrics.csv"
    outputFile = os.getcwd()+"/uprof_results_cumulative/619_lbm_s_metrics_cumulative.csv"
    processCSVFile(inputFile, outputFile, False)
    
    #620.omnetpp_s
    inputFile = cwd+"/620.omnetpp_s/metrics.csv"
    outputFile = os.getcwd()+"/uprof_results_cumulative/620_omnetpp_s_metrics_cumulative.csv"
    processCSVFile(inputFile, outputFile, False)
    
    #621.wrf_s
    inputFile = cwd+"/621.wrf_s/metrics.csv"
    outputFile = os.getcwd()+"/uprof_results_cumulative/621_wrf_s_metrics_cumulative.csv"
    processCSVFile(inputFile, outputFile, False)
    
    #623.xalancbmk_s
    inputFile = cwd+"/623.xalancbmk_s/metrics.csv"
    outputFile = os.getcwd()+"/uprof_results_cumulative/623_xalancbmk_s_metrics_cumulative.csv"
    processCSVFile(inputFile, outputFile, False)
    
    #625.x264_s
    inputFile = cwd+"/625.x264_s/metrics.csv"
    outputFile = os.getcwd()+"/uprof_results_cumulative/625_x264_s_metrics_cumulative.csv"
    processCSVFile(inputFile, outputFile, False)
    
    #628.pop2_s
    inputFile = cwd+"/628.pop2_s/metrics.csv"
    outputFile = os.getcwd()+"/uprof_results_cumulative/628_pop2_s_metrics_cumulative.csv"
    processCSVFile(inputFile, outputFile, False)
    
    #631.deepsjeng_s
    inputFile = cwd+"/631.deepsjeng_s/metrics.csv"
    outputFile = os.getcwd()+"/uprof_results_cumulative/631_deepsjeng_s_metrics_cumulative.csv"
    processCSVFile(inputFile, outputFile, False)
    
    #638.imagick_s
    inputFile = cwd+"/638.imagick_s/metrics.csv"
    outputFile = os.getcwd()+"/uprof_results_cumulative/638_imagick_s_metrics_cumulative.csv"
    processCSVFile(inputFile, outputFile, False)
    
    #641.leela_s
    inputFile = cwd+"/641.leela_s/metrics.csv"
    outputFile = os.getcwd()+"/uprof_results_cumulative/641_leela_s_metrics_cumulative.csv"
    processCSVFile(inputFile, outputFile, False)
    
    #644.nab_s
    inputFile = cwd+"/644.nab_s/metrics.csv"
    outputFile = os.getcwd()+"/uprof_results_cumulative/644_nab_s_metrics_cumulative.csv"
    processCSVFile(inputFile, outputFile, False)
    
    #648.exchange2_s
    inputFile = cwd+"/648.exchange2_s/metrics.csv"
    outputFile = os.getcwd()+"/uprof_results_cumulative/648_exchange2_s_metrics_cumulative.csv"
    processCSVFile(inputFile, outputFile, False)
    
    #649.fotonik3d_s
    inputFile = cwd+"/649.fotonik3d_s/metrics.csv"
    outputFile = os.getcwd()+"/uprof_results_cumulative/649_fotonik3d_s_metrics_cumulative.csv"
    processCSVFile(inputFile, outputFile, False)
    
    #654.roms_s
    inputFile = cwd+"/654.roms_s/metrics.csv"
    outputFile = os.getcwd()+"/uprof_results_cumulative/654_roms_s_metrics_cumulative.csv"
    processCSVFile(inputFile, outputFile, False)
    
    #657.xz_s
    inputFile = cwd+"/657.xz_s/metrics.csv"
    outputFile = os.getcwd()+"/uprof_results_cumulative/657_xz_s_metrics_cumulative.csv"
    processCSVFile(inputFile, outputFile, False)
    

def processCSVFile(inputFile, outputFile, r):
    #entire csv file read into data easier to handle odd csv spacing of data
    data = []

    #boolean for rate or speed
    rate = r

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
    coreMetrics = processCoreMetrics(data, rate)
    l3Metrics = processL3Metrics(data)
    dfMetrics = processDFMetrics(data)

    #write results to new 'cumulativeMetrics.csv' file
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
def processCoreMetrics(data, rate):
    headers =[]
    metrics = []
    core = []

    for i in range(17):
        headers.append(data[i][0])
        del data[i][0] #get rid of metric header from that row
        metrics.append(data[i])
    
    if (rate):
        #sum utilization
        for i in range(1):
            sum = 0
            row = []
            for j in range(48):
                sum = sum + float(metrics[i][j])
            row.append(headers[i])
            row.append(sum)
            core.append(row)

        #maximum of efficiency
        for i in range(1,2):
            max = 0
            row = []
            for j in range(48):
                if (max < float(metrics[i][j])):
                    max = float(metrics[i][j])
            row.append(headers[i])
            row.append(max)
            core.append(row)

        #average for all other metrics
        for i in range(2,17):
            row = []
            row.append(headers[i])
            sum = 0
            avg = 0
            for j in range(48):
                sum = sum + float(metrics[i][j])
            avg = sum/len(metrics[0])
            row.append(avg)
            core.append(row)      
    else:  
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
def processL3Metrics(data):
    headers =[]
    metrics = []
    l3 = []

    for i in range(20, 25):
        headers.append(data[i][0])
        del data[i][0] #get rid of metric header from that row
        metrics.append(data[i])

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
def processDFMetrics(data):
    #return values: headers and metrics
    headers =[]
    metrics = []
    df = []

    for i in range(28, 47):
        headers.append(data[i][0])
        del data[i][0] #get rid of metric header from that row
        metrics.append(data[i])

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