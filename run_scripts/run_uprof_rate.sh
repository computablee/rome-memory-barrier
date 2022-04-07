#!/bin/bash

ulimit -s unlimited
#export OMP_STACKSIZE=192M
#export OMP_NUM_THREADS=1
#export OMP_SCHEDULE=static
source /opt/setenv_AOCC.sh
source /opt/intel/oneapi/setvars.sh
#issues running:
# 510
# 511
# 520
# 521
# 523
# 526
# 527
# 531
# 541
# 548
# 549
# 554

cd /home/student/pal0009/CPE-631-Term-Project/benchspec/CPU

function flags {
    local benchname=$1

    case $benchname in 
        perlbench_r)
            echo "-I./lib checkspam.pl 2500 5 25 11 150 1 1 1 1"
        ;;
        gcc_r)
            echo "gcc-pp.c -O3 -finline-limit=0 -fif-conversion -fif-conversion2 -o gcc-pp.opts-O3_-finline-limit_0_-fif-conversion_-fif-conversion2.s"
        ;;
        bwaves_r)
            echo "bwaves_1 < bwaves_1.in"
        ;;
        mcf_r)
            echo "inp.in"
        ;;
        cactuBSSN_r)
            echo "spec_ref.par"
        ;;
        namd_r)
            echo "--input apoa1.input --output apoa1.ref.output --iterations 65"
        ;;
        parest_r)
            echo "ref.prm"
        ;;
        povray_r)
            echo "SPEC-benchmark-ref.ini"
        ;;
        lbm_r)
            echo "3000 reference.dat 0 0 100_100_130_ldc.of"
        ;;
        omnetpp_r)
            echo "-c General -r 0"
        ;;
        wrf_r)
            echo ""
        ;;
        xalancbmk_r)
            echo "-v t5.xml xalanc.xsl"
        ;;
        x264_r)
            echo "--pass 1 --stats x264_stats.log --bitrate 1000 --frames 1000 -o BuckBunny_New.264 BuckBunny.yuv 1280x720"
        ;;
        blender_r)
            echo "sh3_no_char.blend --render-output sh3_no_char_ --threads 1 -b -F RAWTGA -s 849 -e 849 -a"
        ;;
        cam4_r)
            echo ""
        ;;
        deepsjeng_r)
            echo "ref.txt"
        ;;
        imagick_r)
            echo "-limit disk 0 refrate_input.tga -edge 41 -resample 181% -emboss 31 -colorspace YUV -mean-shift 19x19+15% -resize 30% refrate_output.tga"
        ;;
        leela_r)
            echo "ref.sgf"
        ;;
        nab_r)
           echo "1am0 1122214447 122" 
        ;;
        exchange2_r)
            echo "6"
        ;;
        fotonik3d_r)
            echo ""
        ;;
        roms_r)
            echo "< ocean_benchmark2.in.x"
        ;;
        xz_r)
            echo "cld.tar.xz 160 19cf30ae51eddcbefda78dd06014b4b96281456e078ca7c13e1c0c9e6aaea8dff3efb4ad6b0456697718cede6bd5454852652806a657bb56e07d61128434b474 59796407 61004416 6"
        ;;
    esac
}

function run_benchmark {
    local benchmark=$1
    local instance=$2
    local outloc=$3
    local rundir=$4

    echo "instance $instance"
    local benchname=$(cut -d '.' -f2- <<< $benchmark)

    #printf './%s_base.aocc-3.3.1.0-m64 %s > %s/%s.out 2>> %s/%s.err\n' \
    #    $benchname \
    #    "$(flags $benchname)" \
    #    $outloc \
    #    $instance \
    #    $outloc \
    #    $instance   

    let core=$instance-1

    export CORE_PIN="taskset -c $core"

    if [ $core = 0 ]; then
        rm -rf /home/student/pal0009/CPE-631-Term-Project/uprof_results/$benchmark
        mkdir /home/student/pal0009/CPE-631-Term-Project/uprof_results/$benchmark
        export UPROF="AMDuProfPcm -r -i /home/student/pal0009/CPE-631-Term-Project/spec-config.conf -a -C -D /home/student/pal0009/CPE-631-Term-Project/uprof_results/$benchmark/events.csv -o /home/student/pal0009/CPE-631-Term-Project/uprof_results/$benchmark/metrics.csv -- "
    else
        export UPROF=""
    fi

    echo $(pwd)
    #benchmarks with different names for the executable than the folder
    if [ $benchname = "gcc_r" ] ; then
        echo "detected gcc, running on core $core"
        $UPROF $CORE_PIN $rundir/cpugcc_r_base.aocc-3-3.1.0-m64 $(flags $benchname) > $outloc/$instance.out 2>> $outloc/$instance.err &
    elif [ $benchname = "xalancbmk_r" ] ; then
        echo "detected xalancbmk, running on core $core"
        $UPROF $CORE_PIN $rundir/cpuxalan_r_base.aocc-3-3.1.0-m64 $(flags $benchname) > /dev/null 2>> $outloc/$instance.err &
    elif [ $benchname = "cactuBSSN_r" ] ; then
        echo "detected cactuBSSN, running on core $core"
        $UPROF $CORE_PIN $rundir/cactusBSSN_r_base.aocc-3-3.1.0-m64 $(flags $benchname) > $outloc/$instance.out 2>> $outloc/$instance.err &
    #benchmarks that use bash tokens in the parameters
    elif [ $benchname = "bwaves_r" ] ; then
        echo "detected bwaves, running on core $core"
        $UPROF $CORE_PIN $rundir/$benchname\_base.aocc-3-3.1.0-m64 bwaves_1 < bwaves_1.in > $outloc/$instance.out 2>> $outloc/$instance.err &
    elif [ $benchname = "roms_r" ] ; then
        echo "detected roms, running on core $core"
        $UPROF $CORE_PIN $rundir/$benchname\_base.aocc-3-3.1.0-m64 < ocean_benchmark2.in.x > $outloc/$instance.out 2>> $outloc/$instance.err &
    #everything else
    else
        echo "running on core $core"
        $UPROF $CORE_PIN $rundir/$benchname\_base.aocc-3-3.1.0-m64 $(flags $benchname) > $outloc/$instance.out 2>> $outloc/$instance.err &
    fi
}

for i in $(ls -1 | grep "$1"); do
    export RUN_DIR=$(pwd)/$i/run/run_base_refrate_aocc-3-3.1.0-m64.0000
    cd $RUN_DIR
    for j in 48 ; do
        export RESULT_LOC=/home/student/pal0009/CPE-631-Term-Project/uprof_results/$i
        rm -rf $RESULT_LOC
        mkdir $RESULT_LOC
        
        echo "Running $i with $j instances"
        for (( k=1; k<=$j; k++ )); do
            run_benchmark $i $k $RESULT_LOC $RUN_DIR
        done
        wait

        rm -f $RESULT_LOC/*.out
    done
    cd ../../..
done