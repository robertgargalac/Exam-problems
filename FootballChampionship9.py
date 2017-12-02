# win -3p
# draw - 1p
# lose - 0p

k = int(raw_input())
n = int(raw_input())
counter = n

data_in = []
while counter != 0:
    data_in.append(raw_input())
    counter -= 1

teams = []
for j in range(n):
    teams.append(data_in[j].split(" ")[0])
    teams.append(data_in[j].split(" ")[4])

teams_final = set(teams)

team_l = []
team_r = []
score_l = []
score_r = []
for i in data_in:
    team_l.append(i.split(" ")[0])
    team_r.append(i.split(" ")[4])
    score_l.append(int(i.split(" ")[1]))
    score_r.append(int(i.split(" ")[3]))

scores = []
for team in teams_final:
    pr = 0
    ins = 0
    p = 0
    for i in range(n):
        if team == team_l[i] and score_l[i] > score_r[i]:
            p += 3
        if team == team_l[i] and score_l[i] == score_r[i]:
            p += 1
        if team == team_r[i] and score_r[i] > score_l[i]:
            p += 3
        if team == team_r[i] and score_r[i] == score_l[i]:
            p += 1
        if team == team_l[i]:
            ins += score_l[i]
            pr += score_r[i]
        if team == team_r[i]:
            ins += score_r[i]
            pr += score_l[i]
    scores.append(team + " " + str(p) + " " + str(ins) + " " + str(pr))

for i in range(k):
    for j in range(k):
        if int(scores[i].split(" ")[1]) > int(scores[j].split(" ")[1]):
            aux = scores[j]
            scores[j] = scores[i]
            scores[i] = aux
for score in scores:
    print(score)


