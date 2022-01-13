#Gagan Namburi, AA502, Python Assignment 2

#Original positions on board.
pos = {"A1":"A1", "A2":"A2", "A3":"A3", "B1":"B1", "B2":"B2", "B3":"B3", "C1":"C1", "C2":"C2", "C3":"C3"}

#Indicator for the end of the game.
end = False

#Indicator for X or O.
x = True

#Tic tac toe loop as long as end indicator is not true.
while end is False:
	
	#Print board.
	print(pos["A1"], pos["B1"], pos["C1"])
	print(pos["A2"], pos["B2"], pos["C2"])
	print(pos["A3"], pos["B3"], pos["C3"])

	#Ask user for input.
	position = input("Choose a position: ")
	
	#Checks if user inputted valid space.
	if position.upper() not in pos.keys():
		print("Invalid input")
		continue
	#Checks if space was already taken.
	elif pos[position.upper()] == "X" or pos[position.upper()] == "O":
		print("Space already taken")
		continue
	#Alternates through X and Os for each turn.
	else:
		if x:
			pos[position.upper()] = "X"
			x = False
		else:
			pos[position.upper()] = "O"
			x = True

	#Checks for every possible way to win and outputs message if condition is met. (Vertical, horizontal, and diagonal)
	if pos["A1"]==pos["A2"]==pos["A3"] or pos["B1"]==pos["B2"]==pos["B3"] or pos["C1"]==pos["C2"]==pos["C3"] or pos["A1"]==pos["B1"]==pos["C1"] or pos["A2"]==pos["B2"]==pos["C2"] or pos["A3"]==pos["B3"]==pos["C3"] or pos["A1"]==pos["B2"]==pos["C3"] or pos["A3"]==pos["B2"]==pos["C1"]:
		end = True
		message = pos[position.upper()] + "'s have won!"
	#Checks if all values in pos are X or O in order to determine tie game if no matches were made.
	elif all(v=="X" or v=="O" for v in pos.values()):
		end = True
		message = "Tied game!"

#Prints final board and final game message.
print(pos["A1"], pos["B1"], pos["C1"])
print(pos["A2"], pos["B2"], pos["C2"])
print(pos["A3"], pos["B3"], pos["C3"])
print(message)