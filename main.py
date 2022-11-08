import os
import time

from study import study


def getAccounts():
    result = []

    accountsRaw = os.getenv("ACCOUNTS")
    if accountsRaw is None:
        accountsRaw = open("accounts.txt").read()
    for account in accountsRaw.split("\n"):
        account = account.strip()
        if account == "":
            continue
        username, password = account.split()
        result.append((username, password))
    return result


ua = os.getenv('UA',
               'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.42')

accounts = getAccounts()
print(f'账号数量：{len(accounts)}')
successful = 0
count = 0
for username, password in accounts:
    count += 1
    print(f'--User {count}--')
    if study(username, password, ua):
        successful += 1

failed = count - successful
print('--Summary--')
print(f'成功：{successful}，失败：{failed}')
if failed != 0:
    raise Exception(f'有{failed}个失败！')
