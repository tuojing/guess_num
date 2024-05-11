import random
start = int(input('請決定隨機變數範圍的初始值: '))
end = int(input('請決定隨機變數範圍的結束值: '))
num = random.randint(start,end)
count = 0
while True:
	count = count + 1
	guess = int(input('請猜數字: '))
	if guess == num:
		print('終於猜對了!這是你猜的第', count, '次')
		break
	elif guess > num:
		print('比答案大')
	elif guess < num: 
		print('比答案小')
	print('這是你猜的第', count, '次')		