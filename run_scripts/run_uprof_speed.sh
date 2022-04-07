#!/bin/bash

ulimit -s unlimited
export OMP_STACKSIZE=192M
export OMP_NUM_THREADS=48
#export OMP_SCHEDULE=static
source /opt/setenv_AOCC.sh
source /opt/intel/oneapi/setvars.sh

export single_threaded="perlbench_s gcc_s mcf_s omnetpp_s xalancbmk_s x264_s deepsjeng_s leela_s exchange2_s"

cd /home/student/pal0009/CPE-631-Term-Project/benchspec/CPU

function flags {
    local benchname=$1

    case $benchname in 
        perlbench_s)
            echo "-I./lib checkspam.pl 2500 5 25 11 150 1 1 1 1"
        ;;
        gcc_s)
            echo "gcc-pp.c -O5 -fipa-pta -o gcc-pp.opts-O5_-fipa-pta.s"
        ;;
        bwaves_s)
            echo "bwaves_1 < bwaves_1.in"
        ;;
        mcf_s)
            echo "inp.in"
        ;;
        cactuBSSN_s)
            echo "spec_ref.par"
        ;;
        lbm_s)
            echo "2000 reference.dat 0 0 200_200_260_ldc.of"
        ;;
        omnetpp_s)
            echo "-c General -r 0"
        ;;
        wrf_s)
            echo ""
        ;;
        xalancbmk_s)
            echo "-v t5.xml xalanc.xsl"
        ;;
        x264_s)
            echo "--pass 1 --stats x264_stats.log --bitrate 1000 --frames 1000 -o BuckBunny_New.264 BuckBunny.yuv 1280x720"
        ;;
        cam4_s)
            echo ""
        ;;
        pop2_s)
            echo ""
        ;;
        deepsjeng_s)
            echo "ref.txt"
        ;;
        imagick_s)
            echo "-limit disk 0 refspeed_input.tga -resize 817% -rotate -2.76 -shave 540x375 -alpha remove -auto-level -contrast-stretch 1x1% -colorspace Lab -channel R -equalize +channel -colorspace sRGB -define histogram:unique-colors=false -adaptive-blur 0x5 -despeckle -auto-gamma -adaptive-sharpen 55 -enhance -brightness-contrast 10x10 -resize 30% refspeed_output.tga"
        ;;
        leela_s)
            echo "ref.sgf"
        ;;
        nab_s)
           echo "3j1n 20140317 220" 
        ;;
        exchange2_s)
            echo "6"
        ;;
        fotonik3d_s)
            echo ""
        ;;
        roms_s)
            echo "< ocean_benchmark2.in.x"
        ;;
        xz_s)
            echo "cpu2006docs.tar.xz 6643 055ce243071129412e9dd0b3b69a21654033a9b723d874b2015c774fac1553d9713be561ca86f74e4f16f22e664fc17a79f30caa5ad2c04fbc447549c2810fae 1036078272 1111795472 4"
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

    let core=$instance-1

    if [ "$(echo "$single_threaded" | grep $benchname)" != "" ] ; then
        export CORE_PIN="taskset -c $core"
    else 
        export CORE_PIN=""
    fi

    if [ $core = 0 ]; then
        rm -rf /home/student/pal0009/CPE-631-Term-Project/uprof_results/$benchmark
        mkdir /home/student/pal0009/CPE-631-Term-Project/uprof_results/$benchmark
        export UPROF="AMDuProfPcm -r -i /home/student/pal0009/CPE-631-Term-Project/spec-config.conf -a -C -D /home/student/pal0009/CPE-631-Term-Project/uprof_results/$benchmark/events.csv -o /home/student/pal0009/CPE-631-Term-Project/uprof_results/$benchmark/metrics.csv -- "
    else
        export UPROF=""
    fi

    #benchmarks with different names for the executable than the folder
    if [ $benchname = "gcc_s" ] ; then
        echo "detected gcc, running on core $core"
        $UPROF $CORE_PIN $rundir/sgcc_base.aocc-3-3.1.0-m64 $(flags $benchname) > $outloc/$instance.out 2>> $outloc/$instance.err &
    elif [ $benchname = "pop2_s" ] ; then
        echo "detected pop2, running on core $core"
        $UPROF $CORE_PIN $rundir/speed_pop2_base.aocc-3-3.1.0-m64 $(flags $benchname) > $outloc/$instance.out 2>> $outloc/$instance.err &
    #benchmarks that use bash tokens in the parameters
    elif [ $benchname = "bwaves_s" ] ; then
        echo "detected bwaves, running on core $core"
        $UPROF $CORE_PIN $rundir/speed_bwaves_base.aocc-3-3.1.0-m64 bwaves_1 < bwaves_1.in > $outloc/$instance.out 2>> $outloc/$instance.err &
    elif [ $benchname = "roms_s" ] ; then
        echo "detected roms, running on core $core"
        $UPROF $CORE_PIN $rundir/sroms_base.aocc-3-3.1.0-m64 < ocean_benchmark3.in > $outloc/$instance.out 2>> $outloc/$instance.err &
    #everything else
    else
        echo "running on core $core"
        $UPROF $CORE_PIN $rundir/$benchname\_base.aocc-3-3.1.0-m64 $(flags $benchname) > $outloc/$instance.out 2>> $outloc/$instance.err &
    fi
}

for i in $(ls -1 | grep "_s"); do
    export RUN_DIR=$(pwd)/$i/run/run_base_refspeed_aocc-3-3.1.0-m64.0000

    cd /home/student/pal0009/CPE-631-Term-Project/run_scripts
    ./debug_suite.sh $i &
    sleep 30
    export bname=$(cut -d '.' -f2- <<< $i)
    if [ $bname = "gcc_s" ] ; then
        export bname="sgcc"
    elif [ $bname = "pop2_s" ] ; then
        export bname="speed_pop2"
    #benchmarks that use bash tokens in the parameters
    elif [ $bname = "bwaves_s" ] ; then
        export bname="speed_bwaves"
    elif [ $bname = "roms_s" ] ; then
        export bname="sroms"
    fi
    pkill $bname\*
    pkill AMDuProfPcm

    sleep 5

    cd $RUN_DIR

    for j in 1 ; do
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