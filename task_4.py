stroka = input("введите строку ")


list_word = stroka.split()

i = 1

for el in list_word:	
	print(str(i)+" строка: "+el[:10])
	i +=1
