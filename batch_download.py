import requests
from pathlib import Path

dl_data = 'HMI_SHARP'

if dl_data == 'HMI_SHARP': # download HMI SHARP '.fits' data
    save_dir = Path('E:/Research/Data/HMI/SHARP/') # save directory
    # iterate for time range and parameters
    for date in ['0429', '0430', '0501', '0502', '0503', '0504', '0505', '0506', '0507', \
                 '0508', '0509', '0510', '0511', '0512', '0513', '0514', '0515']:
        for hour in ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', \
                     '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23']:
            for minute in ['00', '12', '24', '36', '48']:
                for param in ['Br', 'Bt', 'Bp', 'magnetogram']:
                    # get time record
                    time_record = '2024' + date + '_' + hour + minute + '00'
                    print('downloading ' + time_record + ' ' + param + ' with requests')
                    # set downloading url (submitted request on JSOC first)
                    url = 'https://jsoc1.stanford.edu/SUM39/D1774177699/S00000/hmi.sharp_cea_720s.11149.' \
                        + time_record + '_TAI.' + param + '.fits'
                    # begin download
                    r = requests.get(url)
                    file_name = url.split('/')[-1]
                    file_path = save_dir / file_name
                    with open(file_path, 'wb') as file:
                        file.write(r.content)
                    # check download    
                    print('saved ' + time_record + ' ' + param)

elif dl_data == 'WSO_synoptic': # download WSO synoptic '.txt' data
    # iterate for Carrington Rotation
    for i_cr in range(2261,2273):
        print('downloading CR' + str(i_cr) + ' with requests')
        # set downloading url
        url = 'http://wso.stanford.edu/synoptic/WSO.' + str(i_cr) + '.F.txt'
        # begin download
        r = requests.get(url)
        with open('E:/Research/Data/WSO/download/txt/CR' + str(i_cr) + '.txt', 'wb') as code:
            code.write(r.content)
        # check download
        print('saved CR' + str(i_cr) + '.txt')