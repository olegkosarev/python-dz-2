my_list = list()

while True:
	el = input("введите новый элемент для списка ")
	if el == "break":
		break
	else:
		my_list.append(el)


i=0

while i < len(my_list):
	move_element = my_list[i]
	my_list.pop(i)
	my_list.insert(i+1,move_element)
	i += 2
	

print(my_list)
