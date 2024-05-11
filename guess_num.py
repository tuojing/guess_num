import random
num = random.randint(1,100)
while True:
	guess = int(input('請從1到100中輸入一個數字: '))
	if guess == num:
		print('終於猜對了!')
		break
	else:
		if 	guess > num:
			print('比答案大')
		else: 
			print('比答案小')	