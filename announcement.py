#!/usr/bin/python3
import re 
import requests

"""
    Buat orang yang males buka website if polibatam.
    Note: hasil yang ditampilkan kemungkinan tidak akurat.
"""

if __name__ == '__main__' : 
    URL = "https://if.polibatam.ac.id/Page/Pengumuman/pengumuman.php"
    content = requests.get(URL).text
    pattern = re.compile(
        r'<h3><a href="([^"]+)">(.+?)</a></h3>\s*<p>Posted on (.+?)</p>.*?<p><a href="([^"]+)">',
        re.DOTALL
    )
    matches = pattern.findall(content)
    for match in matches:
        detail_link, title, date, attachment_link = match
        print(f"Title: {title}")
        print(f"Date: {date}")
        print(f"Detail Link: https://if.polibatam.ac.id/Page/Pengumuman/{detail_link}")
        print(f"Attachment Link: {attachment_link}")
        print("-" * 50)
