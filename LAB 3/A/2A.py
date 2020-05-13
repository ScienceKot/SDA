n = int(input('Enter the number of layers:'))
game_story = []
players_info = {}
# Entering the data
for i in range(n):
    print("Enter the information about player number {}:".format(i+1))
    name = input("Enter the name of the player:")
    point = int(input("Enter the number of player's point:"))
    # If the player name is not in the dictionary the it is added, else the points are added to this players point
    if name in players_info:
        players_info[name] +=point
    else:
        players_info[name] = point
    game_story.append({name:point})
# Searching for the maximal points that were get during the game
maxi = 0
for name in players_info:
    if maxi < players_info[name]:
        maxi = players_info[name]
# Searching the winners
winners = []
for name in players_info:
    if players_info[name] == maxi:
        winners.append(name)
# Searching for the winner
if len(winners) == 1:
    print("The winner is {}".format(winners[0]))
else:
    stop = False
    point_story = {name : 0 for name in winners}
    for round in game_story:
        if list(round.keys())[0] in winners:
            point_story[list(round.keys())[0]] += list(round.values())[0]
        for name in point_story:
            if point_story[name] == maxi:
                print("The winner is {}".format(name))
                stop = True
        if stop:
            break