#اولاً عملت عنوان الشروع
print("ﻡﺎﻬﻤﻟﺍ ﺞﻣﺎﻧﺮﺑ ﻲﻓ ﻚﺑ ًﻼﻫﺍ📃📃📃","\n---------------")
#ثانياً عملت التغيرات
user = input("ﺖﺤﻤﺳﻮﻟ ﻚﻣﺎﻬﻣ ﺐﺘﻛﺍ\n").split(",")
list_Mission_yes = []
list_Mission_no = []
#ثالثاً عملت عملية التكرار

for x in user:
    print(f"\n{x}")
    user_p = input(f"?ﺔﻤﻬﻤﻟﺍ ﻩﺬﻫ ﺖﻠﻤﻛﺍ ﻞﻫ\n").lower()
    if user_p == "yes":
        print("ﺎﻬﻣﺎﻤﺗﺍ ﻰﻠﻋ ﻙﻭﺮﺒﻣ: 🎊","\n-----------")
        list_Mission_yes.append(x)
    elif user_p == "no":
        print("ﺎﻬﻤﺘﺗ ﻥﺍ ﻝﻭﺎﺣ","\n-----------")
        list_Mission_no.append(x)
    else:
        print("error")

    print("؟ﺲﻠﻔﻣ ﻚﻠﻜﺷ🙃")
hoh = input("؟ﻚﻣﺪﻘﺗ ﺔﻴﺋﻭﺭ ﺪﻳﺮﺗ ﻞﻫ \n").lower()
if hoh == "yes":
    print("\n     ********** ﺎﻬﺘﻠﻤﻛﺍ ﻱﺬﻟﺍ ﻡﺎﻬﻤﻟﺍ **********","\n",f"\n{list_Mission_yes}",
    "\n        ***** ﺎﻬﻠﻤﻜﺗ ﻢﻟ ﻱﺬﻟﺍ ﻡﺎﻬﻤﻟﺍ *****","\n",f"\n{list_Mission_no}")
    