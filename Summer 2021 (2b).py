result_list = []
for num in range(20, 61):
    if num % 2 == 0 or num % 5 == 0:
        if num % 2 == 0:
            num += 5
        elif num % 5 == 0:
            num += 2
        result_list.append(num)
print(result_list)
