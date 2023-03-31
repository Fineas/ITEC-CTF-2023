#!/bin/sh

gcc test.c -o ./chall
timeout --kill-after=1s 10m ./chall
