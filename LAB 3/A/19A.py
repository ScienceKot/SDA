n = int(input("Enter the number of teams participating:"))
teams_scores = {}
games = []
for i in range(n):
    print("Enter the name of team number {}:".format(i+1), end='')
    name = input()
    teams_scores[name] = 0
teams_list = list(teams_scores.keys())
for team in teams_list:
    for contra in teams_list:
        if team != contra:
            games.append((team, contra))
print("Enter the scores for the following games [score1 : score2] :")
for g in games:
    print("{} : {}:".format(g[0], g[1]), end='')
    score = input()
    if score == ' ':
        continue
    s1, s2 = tuple(score.split(':'))
    s1, s2 = int(s1), int(s2)
    if s1 == s2:
        teams_scores[g[0]]+=1
        teams_scores[g[1]]+=1
    elif s1 > s2:
        teams_scores[g[0]] += 3
    else:
        teams_scores[g[1]] += 3
greatest_scores = list(teams_scores.values()).sort()[:n//2]
for team in teams_scores:
    if teams_scores[team] in greatest_scores:
        print(team)