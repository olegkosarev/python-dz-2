dictionary = {"зима": [12,1,2], "весна": [3,4,5], "лето": [6,7,8], "осень": [9,10,11]}
search_age = int(input("введите месяц "))


for key, value in dictionary.items():  
    if search_age in value:
        print(key)
