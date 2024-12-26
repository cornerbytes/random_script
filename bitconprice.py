#!/usr/bin/python3

import requests

if __name__ == "__main__":
    try: 
        req = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json').json()
        price = int(req['bpi']['USD']['rate_float'])
        print(f"Bitcoin price today : $ {price}")
    except:
        print("something error") 
