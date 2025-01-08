from time import process_time


def pawn(x1, y1, x2, y2):
    return y2 - y1 == 1 and abs(x2 - x1) == 1

def damka(x1, y1, x2, y2):
    ox = abs(x1 - x2)
    oy = abs(y1 - y2)

    return ox == oy

print(damka(5, 1, 5, 2))

# git add .
# git commit -m "message"
# git push origin main/master
