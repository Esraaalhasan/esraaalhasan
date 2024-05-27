def bin2dec(binary_number):
    decimal = 0
    power = 0
    for digit in binary_number[::-1]:
        if digit not in '01' :
            return "خطأ,قم بإدخال رقم ثنائي من فضلك :"
        decimal += int(digit)*2**power
        power += 1
    return decimal
binary_input = input("ادخل رقما ثنائيا ليتم تحويله لرقم عشري :")
decimal_output = bin2dec(binary_input)
print("الرقم العشري : ", decimal_output)
