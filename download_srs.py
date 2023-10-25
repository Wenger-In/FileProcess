from sunpy.net import Fido, attrs as a

import tensorflow as tf

# results = Fido.search(a.Time('1976/01/01','1996/01/01'), 
#                     a.Instrument.srs_table)
# data_dir = 'E:/Research/Data/NOAA/SRS/'
# dld_file = Fido.fetch(results,path=data_dir+'{file}',overwrite=False)