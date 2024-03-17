semister_fee = int(input())
result = float(input())

if result > 3.50:
    waiver_ammount = semister_fee * (20 / 100)

elif result >= 3.00 and result <= 3.50:
    waiver_ammount = semister_fee * (10 / 100)

elif result < 3.00:
    waiver_ammount = semister_fee * (5 / 100)

print(waiver_ammount)