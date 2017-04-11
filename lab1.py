import requests, os, time
import pandas as pd
from time import strftime, gmtime
from bs4 import BeautifulSoup

if not os.path.isdir("data"):
    os.makedirs("data")


def get_file(index):
    vhi_url = requests.get('https://members.123helpme.com/document/280372')
    soup = BeautifulSoup(vhi_url.text)
    #text = soup.body.tt.pre.getText().replace('year,week,, provinceID, SMN,SMT,VCI,TCI,VHI', 'year,week,SMN,SMT,VCI,TCI,VHI').replace(',', ' ').replace('   ', ' ').replace('  ', ' ').replace(' ',',')
    filename = 'provience-{0}-{1}.txt'
    output = open(filename, 'w')
    output.write(soup)
    output.close()


def create_data_frame(filedir):
    frame_dict = {}
    for filename in os.listdir(filedir):
        if filename.endswith('.csv'):
            frame_dict[filename] = pd.read_csv(filename, index_col=False, header=0)
    return frame_dict


def main():
    for index in range(1, 28):
        get_file(index)

if __name__ == "__main__":
    main()
