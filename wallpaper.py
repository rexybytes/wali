import sys
import subprocess
import time
import random
from random import shuffle

path = sys.argv[1]
itvl = float(sys.argv[2])
while(1):
 files=subprocess.check_output(["ls","-1",path]).splitlines()
 random.shuffle(files)
 for f in files:
   wall="file:///"+path+f
   subprocess.call (["gsettings","set","org.gnome.desktop.background", "picture-uri",wall])
   time.sleep(itvl)
