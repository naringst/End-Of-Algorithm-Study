keyinput, board = ["down", "down", "down", "down", "down"], [7, 9]

x = int(board[0]/2)
y = int(board[1]/2)
now_x = 0
now_y = 0
for move in keyinput:
    if move == "left":
        now_x -= 1
        if now_x < -x:
            now_x = -x
    if move == "right":
        now_x += 1
        if now_x > x:
            now_x = x
    if move == "up":
        now_y += 1
        if now_y > y:
            now_y = y
    if move == "down":
        now_y -= 1
        if now_y < -y:
            now_y = -y

print(now_x, now_y)