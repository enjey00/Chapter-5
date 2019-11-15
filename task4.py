size_of_fishes = [5, 3, 4, 2, 1]
direction_of_fishes = [0, 1, 0, 0, 1]

sorted_fishes = {0:[],1:[]}

for index in range(len(size_of_fishes)):
    if direction_of_fishes[index] == 0:
        sorted_fishes[0].append(size_of_fishes[index])
    elif direction_of_fishes[index] == 1:
        sorted_fishes[1].append(size_of_fishes[index])

print(sorted_fishes, '\n')

sorted_fishes[0].sort(reverse=True)
sorted_fishes[1].sort()

print(sorted_fishes, '\n')

while True:
    try:
        if sorted_fishes[0][-1] < sorted_fishes[1][0]:
            sorted_fishes[0].remove(sorted_fishes[0][-1])
        if sorted_fishes[0][-1] > sorted_fishes[1][0]:
            sorted_fishes[1].remove(sorted_fishes[1][0])
    except IndexError:
        break

if sorted_fishes[0] == []:
    pass
elif sorted_fishes[0] != []:
    print(len(sorted_fishes[0]))

if sorted_fishes[1] == []:
    pass
elif sorted_fishes[1] != []:
    print(len(sorted_fishes[1]))