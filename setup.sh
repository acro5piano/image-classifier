#!/bin/bash

virtualenv -p python3 env || exit
. env/bin/activate || exit
pip3 install -r requirements.txt || exit
