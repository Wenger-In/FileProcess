import requests

for i_cr in range(1642,2258):
    print('downloading CR'+str(i_cr)+' with requests')
    url = 'http://wso.stanford.edu/synoptic/WSO.'+str(i_cr)+'.F.txt'
    r = requests.get(url)
    with open('E:/Research/Data/WSO/download/txt/CR'+str(i_cr)+'.txt', 'wb') as code:
        code.write(r.content)
    print('saving CR'+str(i_cr)+'.txt')