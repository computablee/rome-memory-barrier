#!/bin/bash

ulimit -s unlimited
source /opt/intel/oneapi/setvars.sh

cd ~/CPE-631-Term-Project
export CFFILE=aocc-3.1.0-linux.cfg

#cp ./$CFFILE /apps/arch/cpu2017/config

export ROOTDIR=/apps/arch/cpu2017
export CONFIG=$ROOTDIR/config/$CFFILE
export RUNCPU=$ROOTDIR/bin/runcpu
export BUILD="$1"

$RUNCPU --config=$CONFIG $BUILD
