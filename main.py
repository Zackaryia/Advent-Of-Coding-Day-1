with open('input.txt', 'r') as input_data:
	numbers = input_data.read().split('\n')
print(list(numbers[0]))

new_num = []
for number in numbers:
	new_num.append(int(number))

for number1 in new_num:
	for number2 in new_num:
		if int(number1)+int(number2) == 2020:
			print(int(number1)*int(number2))

#Part 2
for number1 in new_num:
	for number2 in new_num:
		for number3 in new_num:
			if int(number1)+int(number2)+int(number3) == 2020:
				print(int(number1)*int(number2)*int(number3))



