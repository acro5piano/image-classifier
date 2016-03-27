#!/bin/bash

virtualenv env || exit
. env/bin/activate || exit
pip3 install -r requirements.txt || exit
