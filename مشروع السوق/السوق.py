#اولاً عملت عنوان البرنامج 
print("ﻕﻮﺴﻟﺍ ﺞﻣﺎﻧﺮﺑ🛒🛒🛒","\n------------------")
#ثانياً عملت متغير يتخزن فيه الذي كتبة المستخدم كم عدد مشترياتك
USER = int(input("ﻚﺗﺎﻳﺮﺘﺸﻣ ﺩﺪﻋ ﻢﻛ 🗑   \n"))
list_m = []
list_d = []
if USER > 0:
    for x in range(0,USER):
        user_m = input(f"({x+1}) ﻢﻗﺭ ﻪﺘﻳﺮﺘﺷ ﻱﺬﻟﺍ ﺀﻲﺸﻟﺍ ﻢﺳﺃ ﺎﻣ\n")
        list_m.append(user_m)
        user_d = float(input(" ﻩﺮﻌﺳ ﻢﻛ 🤑   \n"))
        list_d.append(user_d)
    user_m_input = input("ﻚﺘﻳﺮﺘﺸﻣ ﻊﻴﻤﺟ ﺔﻳﺅﺭ ﺪﻳﺮﺗ ﻞﻫ\n").lower()
    if user_m_input == "yes":
        print("""
        **********     ﺕﺎﻳﺮﺘﺸﻤﻟﺍ ﺔﻤﺋﺎﻗ     **********
        """)
        print(list_m)
    user_d_input = input(" ﻲﻟﺎﻤﺟﻷﺍ ﺮﻌﺴﻟﺍ ﺔﻳﺅﺭ ﺪﻳﺮﺗ ﻞﻫ \n").lower()
    if user_d_input == "yes":
        print("""
        **********     ﻲﻟﺎﻤﺟﻷﺍ ﺮﻌﺴﻟﺍ     **********
        """)
        print(f"{sum(list_d)}$")
else:
    print("ﺲﻠﻔﻣ ﻚﻠﻜﺷ 😅😅😅")