items = [
 {"name": "1. Froot Loops", "price": 7.99, "department": "Food", "Description": "Colored rings of cereal for breakfast"},
 {"name": "2. Apple", "price": 1.99, "department": "Food", "Description": "A healthy crunchy red fruit"},
 {"name": "3. Orange", "price": 2.49, "department": "Food", "Description": "A juicy round orange healthy fruit"},
 {"name": "4. Grapes", "price": 3.49, "department": "Food", "Description": "Colorful juicy red or purple fruit"},
 {"name": "5. Watermelon", "price": 8.99, "department": "Food", "Description": "A summer seasonal fruit that is juicy when cut into"},
 {"name": "6. Sharpie Permanent Markers", "price": 6.99, "department": "School Supplies", "Description": "Permanent marker which is hard to get off"},
 {"name": "7. Crayola Colored Pencils", "price": 4.99, "department": "School Supplies", "Description": "Colored pencils for drawing or coloring"},
 {"name": "8. Nike Backpack", "price": 94.99, "department": "School Supplies", "Description": "A sports bag which can also be used for school"},
 {"name": "9. Muji pens", "price": 14.49, "department": "School Supplies", "Description": "Premium styled pens designed to not smudge"},
 {"name": "10. Number two pencils", "price": 7.99, "department": "School Supplies", "Description": "Pencils used for everything you can imagine"},
 {"name": "11. Nintendo Switch", "price": 129.99, "department": "Electronics", "Description": "A console for games enabled through game cards or online purchases"},
 {"name": "12. AirPods 4th Generation", "price": 168.49, "department": "Electronics", "Description": "Mini headphones used for music or calls"},
 {"name": "13. IPhone 17 Pro Max", "price": 879.99, "department": "Electronics", "Description": "A handheld device used for calls or messages"},
 {"name": "14. Samsung Desktop PC", "price": 2499.99, "department": "Electronics", "Description": "A desktop computer without a monitor"},
 {"name": "15. iPad 8th Generation", "price": 435.99, "department": "Electronics", "Description" : "A handheld device that can be used for school among other things"},
 {"name": "16. Kitchen Appliances", "price": 14.49, "department": "Utilities", "Description": "A bundle of knives, spoons, and forks"}, 
 {"name": "17. Latex gloves", "price": 8.99, "department": "Utilities", "Description": "Gloves used for cleaning or to keep your hands dry"},
 {"name": "18. Bounty paper towels", "price": 17.99, "department": "Utilities", "Description": "Used for soaking up liquid messes"},
 {"name": "19. Scott Toilet paper", "price": 14.99, "department": "Utilities", "Description": "Pack of toilet paper used for cleanliness"},
 {"name": "20. leenex tissue paper", "price": 18.99, "department": "Utilities", "Description": "A 12 pack of tissues to be discarded after use"}
]
a=input("Would you like to shop")

for letter in a:
    if letter == "y":
        shopping = True
<<<<<<< HEAD
    elif letter == "n":
        shopping = False
        print ("Goodbye")
        
if shopping == True:
    for item in items:
         print(item["name"])
    x = input("This is our shopping menu, select the number of the item you would like to purchase")
cart = []
cart.append(x)
for item in items:
    print(items[x]["name"])
print (cart)
while shopping == True:
    y=input("Would you like to continue?")
    
for letter in y:
    if letter == "y":
=======
cart1 = []
z=0
y = int(input("Put the item number of what you would like to buy"))
shopping = True
cart1.append(y)
for number in cart1:
    print (number, ":", items[number])
    z+=items[number]["price"]
while shopping == True:
    
    shopping = False
    x = int(input("Type 1 if you want to continue shopping. Otherwise, type any other number"))
    if x == 1:
        y = int(input("Put the item number of what you would like to buy"))
        cart1.append(y)
        for character in cart1:
            print (character, ":", items[character])
        z+=items[character]["price"]
>>>>>>> 0b673a7663cd3c78bac8329c19141b0938550cf5
        shopping = True
    elif x != 1:
        shopping = False
        for character in cart1:
            print (character, ":", items[character])
        print (z)

    
