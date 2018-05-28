import os
import sys
print('RUN %s' % sys.argv[1])
with open(sys.argv[1], 'r') as r:
    for i in r.readlines():
        os.system(i)

print('finished')