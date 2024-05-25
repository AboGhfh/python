print("📠📠📟")
# user = input(' ')
# user_2 = int(user[2])
# user_1 = int(user[0])
# if user[1] == "+":
#     print(user_1 + user_2)
# elif user[1] == "-":
#     print(user_1 - user_2)
# elif user[1] == "x":
#     print(user_1 * user_2)
# elif user[1] == "÷":
#     print(user_1 / user_2)
import string
user = input("").lower().split()
pc_1 = int(user[0])
pc = user[1]
pc_2 = int(user[2])
if pc == "+":
    print(pc_1 + pc_2)
elif pc == "÷" or pc == "/":
    print(pc_1 / pc_2)
elif pc == "-":
    print(pc_1 - pc_2)
elif pc == "x":
    print(pc_1 * pc_2)
else:
    print('❌❌❌')