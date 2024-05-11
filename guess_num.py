import random
num = random.randint(1,100)
count = 0
while True:
	count = count + 1
	guess = int(input('請從1到100中輸入一個數字: '))
	if guess == num:
		print('終於猜對了!這是你猜的第', count, '次')
		break
	elif guess > num:
		print('比答案大')
	elif guess < num: 
		print('比答案小')
	print('這是你猜的第', count, '次')		