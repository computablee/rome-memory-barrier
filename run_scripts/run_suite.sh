#!/bin/bash

ulimit -s unlimited

cd /home/student/pal0009/CPE-631-Term-Project/benchspec/CPU

function run_benchmark {
    local benchmark=$1
    local instance=$2

    echo "instance $instance"

    case $benchmark in
        500.perlbench_r)
            echo "running perlbench_r"
        ;;
        502.gcc_r)
            echo "running gcc_r"
        ;;
        503.bwaves_r)
            echo "running bwaves_r"
        ;;
        505.mcf_r)
            echo "running mcf_r"
        ;;
        507.cactuBSSN_r)
            echo "running cactuBSSN_r"
        ;;
        508.namd_r)
            echo "running namd_r"
        ;;
        510.parest_r)
            echo "running parest_r"
        ;;
        511.povray_r)
            echo "running povray_r"
        ;;
        519.lbm_r)
            echo "running lbm_r"
        ;;
        520.omnetpp_r)
            echo "running omnetpp_r"
        ;;
        521.wrf_r)
            echo "running wrf_r"
        ;;
        523.xalancbmk_r)
            echo "running xalancbmk_r"
        ;;
        525.x264_r)
            echo "running x264_r"
        ;;
        526.blender_r)
            echo "running blender_r"
        ;;
        527.cam4_r)
            echo "running cam4_r"
        ;;
        531.deepsjeng_r)
            echo "running deepsjeng_r"
        ;;
        538.imagick_r)
            echo "running imagick_r"
        ;;
        541.leela_r)
            echo "running leela_r"
        ;;
        544.nab_r)
            echo "running nab_r"
        ;;
        548.exchange2_r)
            echo "running exchange2_r"
        ;;
        549.fotonik3d_r)
            echo "running fotonik3d_r"
        ;;
        554.roms_r)
            echo "running roms_r"
        ;;
        557.xz_r)
            echo "running xz_r"
        ;;
    esac
    sleep 1 &
}

for i in $(ls -1 | grep "_r"); do
    cd $i/run/run_base_refrate_aocc-3-3.1.0-m64.0000
    for j in 1 3 6 24 48 ; do
        rm -rf /home/student/pal0009/CPE-631-Term-Project/scale_results/$i\_$j
        mkdir /home/student/pal0009/CPE-631-Term-Project/scale_results/$i\_$j
        echo "Running $i with $j instances"
        for (( k=1; k<=$j; k++ )); do
            run_benchmark $i $k
        done
        wait
    done
    cd ../../..
done