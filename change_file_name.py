import os

dir = 'E:/Research/Work/magnetic_multipole/WSO_map/' # directory of files to rename are
files = os.listdir('E:/Research/Work/magnetic_multipole/WSO_map/') # list filenames 
for file_name in files:
    if file_name[0:2] != 'CR': # identify specific file
        continue
    new_name = 'WSO_map_' + file_name[2:6] + '.png'
    old_dir = os.path.join(dir,file_name)
    new_dir = os.path.join(dir,new_name)
    if os.path.exists(new_dir):
        os.remove(old_dir) # delete namesake file
    else:
        os.rename(old_dir, new_dir)
        print(new_name)