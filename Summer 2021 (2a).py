lst = ['Shikha','Haua','Muzam','01971700130']
vowel = 0
character = 0
for i in lst:
    i.lower()
    for j in i:
        character += 1
        if j == 'a' or j == 'e' or j == 'i' or j=='o' or j == 'u':
            vowel += 1


print("Number of Character:",character)
print("Number of Vowel:", vowel)