def NameScore(name):
    score = 0
    for char in name:
        score += ord(char) - ord('A') + 1
    return score


file = open("p022_names.txt", "r")
data = file.read()
name_list = data.split(",")
name_list = [name.replace('"', '') for name in name_list]
name_list.sort()
scoreTotal = 0
for i in range(len(name_list)):
    scoreTotal += (i + 1) * NameScore(name_list[i])

print(scoreTotal)
