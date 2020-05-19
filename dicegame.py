import random as rm
min_val = 1
max_val = 6

roll_again = 'y'

while roll_again == 'y':
	print("Rolling dice")
	print("The values are........")
	dice1 = rm.randint(min_val,max_val)
	print(dice1)
	dice2 = rm.randint(min_val,max_val)
	print(dice2)
	roll_again = input("You want to roll the dice again? \n y/n \n :")
	