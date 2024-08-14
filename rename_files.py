import os

# Setting the directory of files to rename
data_dir = 'E:/Research/Work/magnetic_multipole/WSO_map/'

# Listing filenames
files = os.listdir(data_dir)

# Iterating through filenames
for old_name in files:
    # Identifying specific files
    if old_name[0:2] != 'CR': 
        continue
    new_name = 'WSO_map_' + old_name[2:6] + '.png'
    # Renaming
    old_dir = os.path.join(data_dir, old_name)
    new_dir = os.path.join(data_dir, new_name)
    # Deleting old files
    if os.path.exists(new_dir):
        os.remove(old_dir) 
    else:
        os.rename(old_dir, new_dir)
        print(new_name)