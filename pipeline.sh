#!/bin/bash

SRC=./src
DATA=./Data

cat $DATA/train.csv \
	| python $SRC/prepare.py \
	| python $SRC/crossValidate.py
