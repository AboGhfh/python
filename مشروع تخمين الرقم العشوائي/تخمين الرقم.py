#اولاً عملت استدعاء للمكينة حق عمل رقم عشوائي
import random
#int ثانياً عملت متغير للمكينة منوع 
#وطلبت منه في المتغير ان يخمنلي رقم من اربع خانات
mak = random.randint(1000,9999)
#ثالثاً عملت متغير لكتابة الرقم الخاص بالمستخدم 
ui = int(input("Please write a number made up of four boxes \n"))
#رابعاً عملت الشروط بإستخدام الجملة الشرطية
#وقلت له في البداية اذا المستخدم كتب اكثر من اربع خانات يعطيه رسالة تعذر
#او اذا المستخدم كتب اقل من اربع خانات 
if len(str(ui)) != 4:
    print("error❌ | it seems you did not have four digits")
#ثم قلت له ثم اذا كتب المستخدم مثل ماكتب المكينة يعطي للمستخدم رسالة مبروك
elif ui == mak:
    print("Well done 😁 Looks like you beat your computer")
    print(f" {mak} | {ui}")
#ثم قلت له اذا كل هذا ماحصل يعطي للمستخدم رسالة خسارة
else:
    print("Looks like you could not beat the combuter 😭")
    print(f"yuo = {ui} cambuter= {mak}")
