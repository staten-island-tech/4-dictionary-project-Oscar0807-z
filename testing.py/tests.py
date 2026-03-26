weight = [2,3,4,4,5,6,1,2,2,2,1,8,2]
deals = [] 
y=0
for character in weight:
    if character % 2 == 0:
        y += character
    if character % 2 == 1:
        deals.append(y)
        y=0
    deals.append(y)
print (max(deals))
