#!/bin/bash

cd /root/code/python_demo/bin
source /root/code/python_demo/venv/bin/activate

# nohup python3 trader_t.py > ../logs/trader_t.log 2>&1 &
python3 trader_bnbdown.py > ../logs/trader_bnbdown.log 2>&1 &