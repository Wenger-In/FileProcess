import requests
from pathlib import Path
from sunpy.net import Fido
from sunpy.net import attrs as a

## Selecting data type to download
dl_data = 'WSO_synoptic'

## Downloading HMI-SHARP '.fits' data
if dl_data == 'HMI_SHARP':
    # Setting save directory
    save_dir = Path('E:/Research/Data/HMI/SHARP/') 
    # Iterating for time range and parameters
    for date in ['0429', '0430', '0501', '0502', '0503', '0504', '0505', '0506', '0507', \
                 '0508', '0509', '0510', '0511', '0512', '0513', '0514', '0515']:
        for hour in ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', \
                     '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23']:
            for minute in ['00', '12', '24', '36', '48']:
                for param in ['Br', 'Bt', 'Bp', 'magnetogram']:
                    # Getting time record
                    time_record = '2024' + date + '_' + hour + minute + '00'
                    print('downloading ' + time_record + ' ' + param + ' with requests')
                    # Setting download url (submitted request on JSOC first)
                    url = 'https://jsoc1.stanford.edu/SUM39/D1774177699/S00000/hmi.sharp_cea_720s.11149.' \
                        + time_record + '_TAI.' + param + '.fits'
                    # Downloading
                    r = requests.get(url)
                    file_name = url.split('/')[-1]
                    file_path = save_dir / file_name
                    with open(file_path, 'wb') as file:
                        file.write(r.content)
                    # Checking download    
                    print('saved ' + time_record + ' ' + param)

## Downloading WSO synoptic map '.txt' data
elif dl_data == 'WSO_synoptic': 
    # Setting save directory
    save_dir = 'E:/Research/Data/WSO/download/txt/'
    # Iterate for Carrington Rotation index
    for i_cr in range(2273,2289):
        print('downloading CR' + str(i_cr) + ' with requests')
        # Setting download url
        url = 'http://wso.stanford.edu/synoptic/WSO.' + str(i_cr) + '.F.txt'
        # Downloading
        r = requests.get(url)
        with open(save_dir + 'CR' + str(i_cr) + '.txt', 'wb') as code:
            code.write(r.content)
        # Checking download
        print('saved CR' + str(i_cr) + '.txt')

## Download NOAA SRS table '.txt' data
elif dl_data == 'NOAA_SRS': 
    # Setting save directory
    save_dir = 'E:/Research/Data/NOAA/SRS/'
    # Selecting time range
    results = Fido.search(a.Time('1996/01/01','1996/01/03'), 
                        a.Instrument.srs_table)
    # Downloading
    dl_file = Fido.fetch(results, path = save_dir + '{file}', overwrite=False)