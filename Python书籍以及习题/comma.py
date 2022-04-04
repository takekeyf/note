def comma(list):
    word = "'"
    for w in range(len(list)-1):
        word += str(list[w])+","
    word += "and "+ str(list[-1]) + "'"
    return word
spam = ['apples','bananas','tofu','cats',]
print(comma(spam))


