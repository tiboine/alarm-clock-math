# show 4 sets of equations. 
#guess the right equation for the answer



def main():
	import random
	x = 0
	random_int = list(range(1,99))
	symbols = ['+', '-', '/', '*']
	answers = [0,0,0,0]
	for num in range(4):
		
		first = random.choice(random_int) # first number
		symbol = random.choice(symbols) # arithmetic 
		last = random.choice(random_int) # last number
		
		
		print(f'{x+1} {first} {symbol} {last}')
		
		if symbol == '+':
			answers[x] = first + last
			x += 1
		if symbol == '-':
			answers[x] = first - last
			x += 1
		if symbol == '/':
			answers[x] = round(first / last,2)
			x += 1
		if symbol == '*':
			answers[x] = first * last
			x += 1

		
	answer_random = random.randint(0,3)
	print('')
	print(str(answers[answer_random]) + ' is the answer to? ') # print answer to the equation to guess

	user = input('Guess 1-4 : ')
	if user == str(answer_random+1):
		print('Good boy. Alarm off')
		print('Will you try again?')
		cont = input('y/n ')
		if cont =='y':
			main()
		else:
			exit()

	else:
		print('Nope. try again')
		main()

while True:
    main()
   


# TODO: 
# repeat app when wrong answer given
# add timer (!) 