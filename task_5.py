my_list = [7, 5, 3, 3, 2]

n = int(input("введите новый элемент рейтинга "))

for el in my_list:
	if n >= el:
		my_list.insert(my_list.index(el),n)
		break

	if n < my_list[-1]:
		my_list.append(n)
		break


print(my_list)
