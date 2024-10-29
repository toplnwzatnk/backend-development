a = int(input("กรุณากรอกคะแนน"))
if a <0 or a > 100 :
    print("ใส่เลข 0-100")
elif a >=80:
    print("เกรด4")
elif a >=75:
    print("เกรด3.5")
elif a >=70:
    print("เกรด3")
elif a >65:
    print("เกรด2.5")
elif a >=60:
    print("เกรด2")    
elif a >=55:
    print("เกรด1.5")
elif a >=50:
    print("เกรด1")   
elif a <=50:
    print("เกรด0")    