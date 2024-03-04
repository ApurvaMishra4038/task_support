noTestcases = int(input().strip())

if not 1 <= noTestcases <= 10 ** 5:
    print("Number of test cases must be between 1 and 10^5")
    exit()

testcases = []

for _ in range(noTestcases):
    case_info = list(map(int, input().strip().split()))

    players = case_info[0]
    main_height = case_info[1]

    if not (1 <= players <= 10 ** 5 and 1 <= main_height <= 10 ** 6):
        print("Number of players must be between 1 and 10^5, main height must be between 1 and 10^6")
        exit()

    players_height = list(map(int, input().strip().split()))

    if len(players_height) != players:
        print("Number of player's heights must match the number of players specified")
        exit()

    if not all(1 <= height <= 10 ** 6 for height in players_height):
        print("Player's height must be between 1 and 10^6")
        exit()

    testcases.append((players, main_height, players_height))

results = []

for i in range(noTestcases):
    count = 0
    for j in range(testcases[i][0]):
        if testcases[i][2][j] > testcases[i][1]:
            count += 1
    results.append(count)

for result in results:
    print(result)
