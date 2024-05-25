#اولاً عملت عنوان المشروع
print("👨")
print("randm")
print("randint")
#ثانياً عملت متغير يتخزن فيه الذي كتبة المستخدم
user = input("1 or 2 \n")
#ثالثاً استدعيت المكينة بتاعة التخمين 
import random
#خامساً اشترط له 
if user == "1":
    r = random.randint(0,1)
    if r == 0:
        cam = "h"
    else:
        cam = "$"
elif user == "2":
    r = random.random()
    if r >=0.5:
        cam = "h"
    else:
        cam = "$"
else:
    print("error")
#سادساً اشترط له بتاع المستخدم
userp = input(" h😎 or $🤑 \n")
#بعدها عملت الاكواد النهائية بالتاعة الطباعة
if userp.lower() == "h":
    if userp == cam:
        print(f"yes 😎 {userp} = 😎 {cam}")
    else:
        print(f"no 😭 😎 {userp} = 🤑 {cam}")
elif userp == "$":
    if userp == cam:
        print(f"yes 🤑 {userp} = 🤑 {cam}")
    else:
        print(f"no 😭 🤑 {userp} = 😎 {cam}")
else:
    print("error")