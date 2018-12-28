# show 4 sets of equations. 
#guess the right equation for the answer

import random
import time
score = 0
score_time = 5
score_times = 0

def main():
	
	x = 0
	global score_time
	global score_times
	global score
	random_int = list(range(1,99))
	symbols = ['+', '-', '/', '*']
	random.shuffle(symbols)
	answers = [0,0,0,0]
	print('')
	print('***********')
	start = time.time()
	for num in range(4):
		
		first = random.choice(random_int) # first number
		symbol = symbols.pop(0) # arithmetic symbol
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
	print('***********')
	print('')
	
	print(str(answers[answer_random]) + ' is the answer to? ') # print answer to the equation to guess

	user = input('Guess 1-4: ')
	if user == str(answer_random + 1):
		end = time.time()
		time_used = round(end-start)
		score += 1		
		score_times = max(0, score_times + (score_time - time_used))
		print('your timed score is ' + str(score_times))
		#print('Your score is ' + str(score))
		print('Good boy. Alarm off')
		print('Want to try again?')
		
		cont = input('y/n ')
		if cont =='y' or cont == '1':
			main()
		else:
			exit()
	if user == 'n':
		exit()

	else:
		print('Nope. try again')
		score -= 1
		print('Your score is: ' + str(score))
		main()

while True:
    main()
   


# TODO: 
# repeat app when wrong answer given /done
# add scoreboard /done
# only one type of aritmethic symbol at once /done
# add timer (!) 