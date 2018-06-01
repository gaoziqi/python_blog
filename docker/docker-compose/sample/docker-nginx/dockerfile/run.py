import os
import sys

def System(cmd):
    r = os.system(cmd)
    if r:
        print('ERROR: %s' % cmd)
        sys.exit(0)

os.chdir('../../1/src')
System('docker build -t gzq_web .')