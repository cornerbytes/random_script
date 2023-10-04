"""
Extract public data from mpr.go.id.
"""

import requests
from bs4 import BeautifulSoup
import csv

def scrap_page(url: str):
    data = requests.get(url).text
    soup = BeautifulSoup(data, 'html.parser')
    table = soup.find_all('table')[0]

    for row in table.find_all('tr'):
        DATA.append([i.string for i in row.find_all('td')])


def write_csv():
    with open('anggota_mpr.csv','w') as f:
        write = csv.writer(f)
        write.writerow(["NOMOR ANGGOTA", "NAMA ANGGOTA", "FRAKSI"])
        write.writerows(DATA)


if __name__ == "__main__":
    DATA = []
    BASE_URL = "https://www.mpr.go.id/keanggotaan/anggota-mpr-ri?page="
    for i in range(1, 36):
        target_url = f"{BASE_URL}{i}"
        scrap_page(target_url)
        print(f"scrap page : {i}")
    print(f'Total Row : {len(DATA)}')
    print('Write result into csv file...')
    write_csv()
