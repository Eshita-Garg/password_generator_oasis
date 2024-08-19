import random

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
digits = "0123456789"
symbols = "!@#$%^&*(){}[].,-_=?/+~"

upper, lower, syms, nums = True, True, True, True

all = ""

if upper:
    all += uppercase_letters
if lower:
    all += lowercase_letters
if syms:
    all += symbols
if nums:
    all += digits

length = 20
amount = 50

for x in range(amount):
    password = "".join(random.sample(all, length))
    print(password)