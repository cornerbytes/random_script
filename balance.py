import datetime
from calendar import monthrange

BALANCE = 400_000

def calc_balance(now, x: int)->int:
    return BALANCE - (round(BALANCE/x) * now.day)

if __name__ == "__main__":
    now = datetime.datetime.now()
    x = monthrange(now.year, now.month)[1]
    daily_spend = round(BALANCE/x)

    while True:
        data = input('1. Check Balance\n2. Daily\n3. Exit\n>>> ')
        if data == '1': print(calc_balance(now, x))
        elif data == '2': print(daily_spend)
        elif data == '3': exit()
        else: print('error')
    
    


