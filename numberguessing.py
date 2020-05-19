import random
while True:
	
	print("Welcome to the number guess game")
	print("Enter any number from 1 to 10")
	a = random.randint(1,10)
	count = 1
	while count <= 5:
		count += 1
		user = int(input("Enter your guessed number: "))
		if user == a:
			print("You've Guessed correct")
			print(a,"is the number")
			break
		elif user == -1:
			print("The hidden number is:",a)
			count = 1
			a = random.randint(1,10)
			continue
		elif user < a and count <= 5 and user<10:
			print("Lower number")
		elif user > a and count !=5 and user<10:
			print("Higher number")
		elif user > 10:
			print("Invalid Entry")
		elif count > 5:
			print("You've lost")
	f = input("Do you want to play again? \n Type 'Yes' or 'No' \n:")
	if f == 'No' or f == 'no':
		break
#	if f == 'Yes' or f == 'yes':
#		a = random.randint(1,10)