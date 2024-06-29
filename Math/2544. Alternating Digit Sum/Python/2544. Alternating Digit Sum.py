def alternateDigitSum(num):
    #Make an Integer List
    str_num = str(num)
    int_list = []
    for char in str_num:
        int_list.append(int(char))
        out = 0
    for i in range(len(int_list)):
        if i % 2 == 0:
            out += int_list[i]
        else:
            out -= int_list[i]
    return out

print(alternateDigitSum(521))
print(alternateDigitSum(111))
print(alternateDigitSum(886996))
    
    
