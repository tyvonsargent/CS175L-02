#tyvon ali sargent
#cs 175L
#restaurant.py


vegan=False
gluten_free=False
vegetarian=False
keep_going = 'yes'

while keep_going == 'yes':
    response = input('is anyone in your party vegan?:')
    if response == 'yes':
        vegan = True
    response = input('is anyone in your party gluten_free?:')
    if response == 'yes':
        gluten_free = True
    response = input('is anyone in your party vegetarian?:')
    if response == 'yes':
        vegetarian = True
    print('Here are your restaurant choices')
    if not vegetarian and not vegan and not gluten_free: print("Joe's Gorumet Burgers")
    if not vegan and not gluten_free: print("Mama's fine Italian")
    if not vegan: print ('Main Street Pizza')
    print("corner cafe")
    print ("Chef's Kitchen")
    keep_going = input("Enter 'yes' to continue or 'no' to end: ")
