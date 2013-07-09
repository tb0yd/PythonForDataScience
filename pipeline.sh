#!/bin/bash

SRC=../src
DATA=../data

cat $DATA/train.csv \
	| python $SRC/subsample.py -r 0.1 \
	| python $SRC/cleandata.py \
	> $DATA/outputfile.csv
