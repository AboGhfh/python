#اولاً عملت عنوان البرانامج
print("Welcome to Lotf Library: 📚")
print("---------------------------")
#ثانياً عملت مكتبتان مكتبتي ومكتبة التمني 
Library = []
Wishing_Library = []
#ثالثاً عملت المتغرات الخاصة بالمكتبة الخاصة بي
#وعملت الشروط اذا كتب المستخدم اسم الكتاب راح ينضاف في المكتبة
add_Library = input("Add a book to your library or press a Enter to skip:📘 \n")
if add_Library:
    Library.append(add_Library)
    add2_Library = input("Add a second book to your library or press a Enter to skip:📙 \n")
    if add2_Library: 
        Library.append(add2_Library)
#وبعدها عملت امر الطباعة 
print("---------------------------------------")
print(f"Your Library {Library}:📚")
print("---------------------------------------")
#وبعدها عد نفس الخطوات بس في المكتبة الخاصة بالتمني 
add_Wishing_Library = input("Add a book to Wishing Library or press a Enter to skip:📘 \n")
if add_Wishing_Library:
    Wishing_Library.append(add_Wishing_Library)
    add2_Wishing_Library = input("Add a sencond book to Wishing Library or press :a Enter to skip:📙 \n")
    if add2_Wishing_Library:
        Wishing_Library.append(add2_Wishing_Library)
print("----------------------------------------")
print(f"Your Library {Library}:📚")
print("-----------------------------------------")
print(f"Wishing Library {Wishing_Library}:📚")
print("------------------------------------------")
#عملت هنا سؤال هل من احدى كتب التمني حصل عليه
removel_Wishing_Library = input("Did you get a wish book?:a Enter to skip:📕 \n")
if removel_Wishing_Library in Wishing_Library:
    Wishing_Library.remove(removel_Wishing_Library)
    Library.append(removel_Wishing_Library)
removel_Library = input("Did you donate a book from a libary?a Enter to skip:📗 \n:")
if removel_Library in Library:
    Library.remove(removel_Library)
#وبالنهاية عملت امر الطباعة الاخير
print("----------------------------------------")
print(f"Your Library {Library}:📚")
print("-----------------------------------------")
print(f"Wishing Library {Wishing_Library}:📚")
print("------------------------------------------")