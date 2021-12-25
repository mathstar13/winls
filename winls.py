import argparse
from os import listdir,getcwd,system
from os.path import isfile,isdir,join
system("")
def format(item,p):
    onlyfiles = [f for f in listdir(p) if isfile(join(p,f))]
    if item in onlyfiles:
        if item.endswith('.exe'):
            print('\33[32m'+str(item),end=' ')
        elif item.endswith('.tar.gz') or item.endswith('.tgz') or item.endswith('.zip'):
            print('\33[91m'+str(item),end=' ')
        else:
            print('\33[0m'+str(item),end=' ')
    else:
        print('\33[34m'+str(item),end=' ')
def ls(p,hidden=False):
    for item in listdir(p):
        if item.startswith('.'):
            if hidden:
                format(item,p)
        else:
            format(item,p)
parser = argparse.ArgumentParser()
parser.add_argument('dir',nargs='?',type=str)
parser.add_argument('-a', action='store_true')
args = parser.parse_args()
h = args.a
if args.dir:
    di = args.dir
else:
    di = getcwd()
ls(di,h)
print('\33[0m')