from random import randint
t = ["Rock", "Paper", "Scissors"]
computer = t[randint(0,2)]
player = False 
while player == False:
	player = input("Rock, Paper, Scissors?")
	if player == computer :
		print ("Tie")
	elif player=="Rock":
		if computer =="Paper":
			print("You lose because of ", computer , "covers",player)
		else:
			print("You win because of", player , "smashes" , computer)
	elif player=="Paper":
		if computer=="Scissors":
			print("You lose because of", computer , "cut", player)
		else:
			print("You win because of", player , "covers" , computer)
	elif player=="Scissors":
		if computer== "Rock":
			print("You lose because of" , computer , "broke" , player)
		else:
			print("You win because of" , player , "cut" , computer)
	else:
		print("That's not a valid play. Check your spelling!")
	player = False
	computer = t[randint(0,2)]