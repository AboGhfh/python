#ستدعيت ادات النصوص واداة التخمين
import string
import random
#عملت عنوان المشروع
print(" !ﺔﻳﻮﻗ ﺮﺳ ﺕﺎﻤﻠﻛ ﺊﺸﻨﻣ ﺞﻣﺎﻧﺮﺑ ﻲﻓ ﻚﺑ ًﻼﻫ 🤖🤖🤖")
#عملت امتعيرات حق سؤال المستخدم
USER_ = int(input(" ﺮﺴﻟﺍ ﺔﻤﻠﻛ ﻝﻮﻃ ﺪﻳﺮﺗ ﻢﻛ  "))
print("----------------------------------")
UESR_str = int(input("ﻑﺮﺣﺍ ﺪﻳﺮﺗ ﻢﻛ "))
USER_up = int(input("ﺯﻮﻣﺭ ﺪﻳﺮﺗ ﻢﻛ "))
USER_nump = int(input("ﻡﺎﻗﺭﺍ ﺪﻳﺮﺗ ﻢﻛ "))
#عملت عملية اتكرار علشان كل حرف يكون لوحده
if  UESR_str + USER_nump + USER_up == USER_ and USER_ >0:
    #عملت المتغيرات
    str_ = string.ascii_letters
    str_nump = string.digits
    str_up = string.punctuation
    posswerd = (random.choices(str_,k=UESR_str)+ random.choices(str_nump,k=USER_nump) + random.choices(str_up,k=USER_up))
    random.shuffle(posswerd)
    tot = "".join(posswerd)
    print(f"{tot} : ﺓﺰﻫﺎﺟ ﺮﺳ ﺔﻤﻠﻛ ﻩﺬﻫ")
else:
    print("ﺰﻣﺮﻟﺍ ﻝﻮﻃ ﻊﻣ ﻖﻓﺍﻮﺘﻳﻻ ﻪﺘﻠﺧﺩﺍ ﻱﺬﻟﺍ ﺩﺪﻌﻟﺍ ❌") 