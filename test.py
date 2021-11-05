# import math

# FILED_PIECE_SIZE = 35

# def cordinates(num):
#     n =  num % FILED_PIECE_SIZE
#     result = num / FILED_PIECE_SIZE
#     if n > FILED_PIECE_SIZE / 2:
#         return math.ceil(result)
#     else:
#         return math.floor(result)

# aa = 236
# print(cordinates(aa), aa / 35)



# option = []

# op = True
# for i in range(3):
#     option.append(op)

# print(option)


import json

with open("C:/Users/User/Desktop/1010_game/js/record.json") as json_file:
    json_data = json.load(json_file)

    score_obj = json_data["score_object"]["score"]
    print(score_obj)