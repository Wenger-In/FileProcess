#!/bin/python3
# get the rbsp data
# writen by Liangjin Song on 20191219
import sys
import requests
from pathlib import Path

# the url containing the cdf files
url = 'https://cdaweb.gsfc.nasa.gov/pub/data/psp/sweap/spc/l3/l3i/2022/'
# local path to save the cdf file
path = 'E:/Research/Data/PSP/spc/2022/'

def main():
    re=requests.get(url)
    html=re.text
    cdfs=resolve_cdf(html)

    ncdf=len(cdfs)
    if ncdf == 0:
        return

    print(str(ncdf) + " cdf files are detected.")

    i=1
    # download 
    for f in cdfs:
        rcdf=url+f
        lcdf=path+f
        print(str(i)+ "   Downloading " + rcdf)
        download_cdf(rcdf,lcdf)
        i+=1
    return

# resolve the file name of cdf
def resolve_cdf(html):
    cdfs=list()
    head=html.find("href=")
    
    if head == -1:
        print("The cdf files not found!")
        return cdfs

    leng=len(html)

    while head != -1:
        tail=html.find(">",head,leng)
        # Extract the cdf file name
        cdf=html[head+6:tail-1]
        head=html.find("href=",tail,leng)
        if cdf.find('cdf') == -1:
            continue
        cdfs.append(cdf)
    return cdfs

def download_cdf(rcdf,lcdf):
    rfile=requests.get(rcdf)
    with open(lcdf,"wb") as f:
        f.write(rfile.content)
    f.close()
    return

if __name__ == "__main__":
    lpath=Path(path)
    if not lpath.is_dir():
        print("Path not found: " + path)
        sys.exit(0)
    sys.exit(main())
