
def check_lang(sent):
    t = 0
    s= 0
    for letter in sent:
        if letter.lower() == "t":
            t += 1
        elif letter.lower() == "s":
            s += 1
    if t > s:
        print ("English")
    elif s >= t: 
        print ("French")
check_lang("sssstt")