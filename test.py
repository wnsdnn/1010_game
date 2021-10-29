FILED = [
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0]
]


FILED_HEIGHT = 8
FILED_WIDTH = 8



for y in range(FILED_HEIGHT):
    xx = 0
    for x in range(FILED_WIDTH):
        if FILED[x][y] == 1:
            xx += 1
        if xx >= FILED_WIDTH:
            for x in range(FILED_WIDTH):
                print(FILED[x][y])
                FILED[x][y] = 0

print(FILED)