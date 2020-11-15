# for menu backup

#imports

import os
from shutil import copyfile

# create backup folder
# Python program to explain os.mkdir() method 
  
# importing os module 
  
# Directory 
directory = "backups-modlunky2"
  
# Parent Directory path 
pwd = os.getcwd()
parent_dir = pwd
  
# Path 
path = os.path.join(parent_dir, directory) 
  
# Create the directory 

os.mkdir(path) 
print("Directory '% s' created" % directory) 


# copyfile(src, dst) #example

copyfile('spel2.exe', 'backups-moudlunky-2/')

copyfile('savegame.sav', 'backups-modlunky2/')

print("done with back up")
