#!/bin/bash

ulimit -s unlimited

export CFFILE=aocc-3.1.0-linux.cfg
export REFFILE=aocc-reportable-3.1.0-linux.cfg

cp ./$CFFILE /apps/arch/cpu2017/config
#cp ./$REFFILE /apps/arch/cpu2017/config

export ROOTDIR=/apps/arch/cpu2017
export CONFIG=$ROOTDIR/config/$CFFILE
export REFCFG=$ROOTDIR/config/$REFFILE
export RUNCPU=$ROOTDIR/bin/runcpu
#export BUILD="all"
export BUILD="603.bwaves_s 607.cactuBSSN_s 619.lbm_s 621_wrf_s 628.pop2_s 638.imagick_s 644.nab_s 649.fotonik3d_s 654.roms_s 996.specrand_fs"

$RUNCPU --size=ref --config=$CONFIG $BUILD
#$RUNCPU --size=ref --reportable --config=$REFCFG $BUILD
