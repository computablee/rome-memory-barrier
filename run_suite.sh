#!/bin/bash

ulimit -s unlimited

export CFFILE=aocc-3.1.0-linux.cfg
export REFFILE=aocc-reportable-3.1.0-linux.cfg

cp ./$CFFILE /apps/arch/cpu2017/config
cp ./$REFFILE /apps/arch/cpu2017/config

export ROOTDIR=/apps/arch/cpu2017
export CONFIG=$ROOTDIR/config/$CFFILE
export REFCFG=$ROOTDIR/config/$REFFILE
export RUNCPU=$ROOTDIR/bin/runcpu
export BUILD="all"
#export BUILD="603.bwaves_s"

$RUNCPU --size=ref --config=$CONFIG $BUILD
$RUNCPU --size=ref --reportable --config=$REFCFG $BUILD
