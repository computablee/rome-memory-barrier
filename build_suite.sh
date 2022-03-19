#!/bin/bash

ulimit -s unlimited
source /opt/intel/oneapi/setvars.sh

export CFFILE=icx-2021.3.0-linux.cfg

#cp ./$CFFILE /apps/arch/cpu2017/config

export ROOTDIR=/apps/arch/cpu2017
export CONFIG=$ROOTDIR/config/$CFFILE
export RUNCPU=$ROOTDIR/bin/runcpu
export BUILD="all"
#export BUILD="602.gcc_s"

$RUNCPU --size=test --config=$CONFIG --action build $BUILD
