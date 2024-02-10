from datetime import datetime
from lib import SavingAccount



myTime = datetime.now()
flag = 0
ac1 = SavingAccount('ilya1', '123', 100)
while True:
    check = float(str(datetime.now() - myTime)[5:])
    if int(check) % 1 == 0 and flag != int(check):
        flag = int(check)
        ac1.chargePercent()
        print(ac1)
