print("Project while")
pc = 8
user = int(input(" "))
if user > pc:
    print("top")
elif user < pc:
    print("buttom")
while user != pc:
    user = int(input(" "))
    if user > pc:
        print("top")
    elif user < pc:
        print("buttom")

print("yes")