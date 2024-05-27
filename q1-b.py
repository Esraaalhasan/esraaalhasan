num = int(input("ادخل رقم صحيح ليتم حساب العدد العاملة له: "))
factorial = 1
if num == 0:
    factorial = 1
else :
    if num>0 :
        for i in range(1,num+1):
            factorial*=i
        print("العاملة للعدد :",num,"هو : ",factorial)
    else :
        print("خطأ : ادخل عدد موجب")
