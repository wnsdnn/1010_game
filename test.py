import math

FILED_PIECE_SIZE = 35

def cordinates(num):
    n =  num % FILED_PIECE_SIZE
    result = num / FILED_PIECE_SIZE
    if n > FILED_PIECE_SIZE / 2:
        return math.ceil(result)
    else:
        return math.floor(result)

aa = 236
print(cordinates(aa), aa / 35)
