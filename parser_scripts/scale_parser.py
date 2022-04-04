import csv
import os
from pathlib import Path


intRate = ['500.perlbench_r', '502.gcc_r', '505.mcf_r', '520.omnetpp_r', '523.xalancbmk_r',
            '525.x264_r', '531.deepsjeng_r', '541.leela_r', '548.exchange2_r', '557.xz_r']

fpRate = ['503.bwaves_r', '507.cactuBSSN_r', '508.namd_r', '510.parest_r', '511.povray_r',
          '519.lbm_r', '521.wrf_r', '526.blender_r', '527.cam4_r', '538.imagick_r', '544.nab_r',
          '549.fotonik3d_r', '554.roms_r']

def main():
    os.chdir("..")
    
    home = os.getcwd()

    verifyDirectoriesNeededExist()
    
    integerAVG = []
    floatPtAVG = []
    integerMAX = []
    floatPtMAX = []

    intRowHeaders = []
    fpRowHeaders = []

    avgHeaders = ['AVG','1','3','6','24','48']
    maxHeaders = ['MAX','1','3','6','24','48']
   
    outputInt = os.getcwd()+"/graph_data/int_scalability.csv"
    outputFP = os.getcwd()+"/graph_data/fp_scalability.csv"

    cwd = os.getcwd()+"/scale_results"
    benchmarkDirList = os.listdir(cwd)
    benchmarkDirList.remove('.placeholder') #remove non-benchmark entry
    benchmarkDirList.remove('520.omnetpp_r_1')

    #sort directories in scaling order
    grouped_dirs = []

    for i in range(0, len(benchmarkDirList), 5):
        grouped_dirs.append(benchmarkDirList[i:i+5])

    sorted_dirs = []
    for group in grouped_dirs:
        sorted_dirs.append(list(map(lambda i: '_'.join(i), sorted(list(map(lambda i: i.split('_'), group)), key=lambda a: int(a[2])))))

    #get int and fp avg and max data into their own lists
    for benchmark in sorted_dirs:
        count = 0
        for benchmarkScale in benchmark:
            benchmarkName = benchmarkScale[:benchmarkScale.index("_r")+len("_r")]
            timeDirList = os.listdir(cwd+"/"+benchmarkScale)
            sum = 0.0
            max = 0.0
            if (count%5 == 0):
                rowA = []
                rowM = []

            for time in timeDirList:
                file = cwd+"/"+benchmarkScale+"/"+time
                with open(file, "r") as f:
                    realTimeLine = f.readline().strip()
                    realTime =  realTimeLine[5:]
                sum = sum + float(realTime)
                if (float(realTime) > max):
                    max = float(realTime)
            avg = round(sum/len(timeDirList), 2)
            rowA.append(str(avg))
            rowM.append(str(max))
        
            #is int or fp
            if (count%5 == 0):
                if (benchmarkName in intRate):
                    intRowHeaders.append(benchmarkName)
                    integerAVG.append(rowA)
                    integerMAX.append(rowM)
                else:
                    fpRowHeaders.append(benchmarkName)
                    floatPtAVG.append(rowA)
                    floatPtMAX.append(rowM)
            
            count = count + 1
    
    #format the data with benchmarkName, scale_1, scale_3, scale_6, scale_24, scale_48
    intAVGData = formatForCSV(intRowHeaders, integerAVG)
    intMAXData = formatForCSV(intRowHeaders, integerMAX)
    fpAVGData = formatForCSV(fpRowHeaders, floatPtAVG)
    fpMAXData = formatForCSV(fpRowHeaders, floatPtMAX)

    #write the integer and floating point data for max and average their csv files
    writeToSpecificCSV(avgHeaders, maxHeaders, intAVGData, intMAXData, outputInt)
    writeToSpecificCSV(avgHeaders, maxHeaders, fpAVGData, fpMAXData, outputFP)

    
def writeToSpecificCSV(headers1, headers2, data1, data2, filename):
    #write results to new file
    avg = []
    for i in range(len(data1)):
        avg.append(data1[i])
    maX = []
    for i in range(len(data2)):
        maX.append(data2[i])

    with open(filename, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers1)
        writer.writerows(avg)
        writer.writerow('')
        writer.writerow(headers2)
        writer.writerows(maX)

def formatForCSV(headers, data):
    newData = []
    for i in range(len(headers)):
        row = []
        row.append(headers[i])
        for j in range(len(data[i])):
            row.append(data[i][j])
        newData.append(row)
    return newData

def verifyDirectoriesNeededExist():
    #create /graph_data directory is doesn't exist
    directory = os.getcwd()+"/graph_data"
    if (not (os.path.exists(directory))):
        os.makedirs(directory)

    

# Call to invoke main method to begin program.
if __name__ == "__main__":
    main()

# End of Program