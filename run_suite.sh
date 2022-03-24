#!/bin/bash

ulimit -s unlimited
source /opt/intel/oneapi/setvars.sh

export CFFILE=aocc-3.1.0-linux.cfg

cp ./$CFFILE /apps/arch/cpu2017/config

export ROOTDIR=/apps/arch/cpu2017
export CONFIG=$ROOTDIR/config/$CFFILE
export RUNCPU=$ROOTDIR/bin/runcpu
export BUILD="all"
#export BUILD="603.bwaves_s"

$RUNCPU --size=ref --config=$CONFIG $BUILD
$RUNCPU --size=ref --reportable --config=$CONFIG $BUILD
