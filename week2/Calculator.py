num_1 = int(input("Введите первое число\n"))

znak = input("Введите знак\n")

num_2 = int(input("Введите второе число\n"))

# +-*/					int()

if znak == "+":
	result = num_1 + num_2
	print("Ответ: " + str(result))
elif znak == "-":
	result = num_1 - num_2
	print("Ответ: " + str(result))
elif znak == "*":
	result = num_1 * num_2
	print("Ответ: " + str(result))
elif znak == "/":
	try:
		result = num_1 / num_2
		print("Ответ: " + str(result))
	except ZeroDivisionError:
		print("Деление на 0!")
else:
	print("nothing")


 