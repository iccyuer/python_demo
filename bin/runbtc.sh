#!/bin/bash

cd /root/code/python_demo/bin
source /root/code/python_demo/venv/bin/activate

# nohup python3 trader_t.py > ../logs/trader_t.log 2>&1 &
python3 trader_btc.py > ../logs/trader_btc.log 2>&1 &