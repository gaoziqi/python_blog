import os
import sys

def System(cmd):
    r = os.system(cmd)
    if r:
        print('ERROR: %s' % cmd)
        sys.exit(0)

name = sys.argv[1]
print('RUN %s' % name)
os.chdir(sys.argv[1])
System('docker build -t %s .' % name)
print('build finish')
System('docker run --name={0}_test -v {1}/{0}:/code  -w /code {0} python3 test.py'.format(name, sys.path[0]))
System('docker logs %s_test' % name)
print('clear')
System('docker rm %s_test' % name)
System('docker rmi %s' % name)
