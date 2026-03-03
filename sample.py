
x = "the red cat sat on the mat"
t = 0
s= 0
for letter in x:
    if letter.lower == t:
        t += 1
    elif letter.lower == s:
        s += 1
if t >= s:
    print ("English")
if s >= t: 
    print ("French")