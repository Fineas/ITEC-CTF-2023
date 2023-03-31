#!/bin/sh

gcc pacala.c -o ./pacala20
timeout --kill-after=1s 10m ./pacala20