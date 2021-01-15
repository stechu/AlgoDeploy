#!/bin/sh
export PATH=$PATH:/home/ubuntu/go/bin
git clone https://github.com/zhenfeizhang/go-algorand.git
cd go-algorand
./scripts/configure_dev.sh
make install
goal network create -n lbvrf -t lbvrf_2.json -r ~/lbvrf-2nodes
