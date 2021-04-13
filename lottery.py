import numpy as np

lotteryTeams = []
x = 14

#Prompt user to enter the 6 lottery teams
for _ in range(6):
	team = input('Enter the owner of the ' + str(x) + 'th place seed: ')
	x = x-1
	lotteryTeams.append(team)

#Select a winner based on the probabilities specified
Winner = np.random.choice(lotteryTeams, 1, p=[0.35, 0.25, 0.15, 0.10, 0.085, 0.065])

#print(Winner)

#Remove the winner from the draft order and re-insert them in the #1 position
lotteryTeams.remove(Winner)
lotteryTeams.insert(0, Winner)

#Print our draft order in reverse order requiring user input with each pick for added dramatic effect
x = 6
for team in reversed(lotteryTeams):
	if x==1 :
		input('The team with the first overall pick and the winner of the 2021 YOFHL draft lottery is ' + str(Winner) + '! Congratulations!')
	else:
		input('The team with pick #' + str(x) + ' is ' + str(team))
		x = x-1