#!/bin/python3
import subprocess

def toFloat(i):
    return float(subprocess.check_output(i, shell=True))
