def commaCode(spam):
    count = 0
    string_value = ''
    while count < len(spam)-1:
        string_value = string_value + spam[count] + ', '
        count +=1
    return string_value + 'and ' + spam[count]

spam_value = ['cat','rat','tofu','dev']
print(commaCode(spam_value))

#Alternate method

def commaCode2(spam1):
    string_list = [str(i) for i in spam1]

    endpart = ", and ".join(spam1[-2:])
    firstpart = string_list[:-2]

    formatted_string = ", ".join(firstpart + [endpart])
    return formatted_string

spam_value1 = [1,'rat','tofu','pooja']
print(commaCode2(spam_value1))


