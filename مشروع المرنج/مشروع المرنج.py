#اولاً قلت له يطبع اسم البرنامج
print("Program to konw tha meter and price$ 😎😎😎")
#ثانياً عملت متغيرات الأسئلة
width = input("Please write the width 📏 \n")
length = input("Please write the length 📏 \n")
price = input("Please write the price per square meter 💰 \n")
#  هو  نص input لأن الذي يتخزن في  float ثالثاً حولت المتغيرات الى 
w_f = float(width)
h_f = float(length)
s_f = float(price)
#رابعاً عملت العمليات الحسابية
w_h = w_f * h_f
s_s = s_f * w_h
#خامساً طبعت الناتج الاخير من العمليات الحسابية
#علشان  تنسق المتغيرات  f واستخدمت 
#لا تطبع الا النصوص print الأن 
print(f" room area = {w_h}📏 price ={s_s}$💰")
