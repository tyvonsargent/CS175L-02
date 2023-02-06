#Tyvon Ali Sargent
#Proffesor Eckert
#CS175L-02
#Februaey 5th, 2021
RestaurauntOptions_ = {
"The Chef's kitchen" : {"vegetarian": True, "vegan": False, "gluten_free": True},
"Corner Cafe" : {"vegetarian": True, "vegan": True, "gluten_free": True},
"Main Street Pizza Company" : {"vegetarian": True, "vegan": False, "gluten_free": True},
"Mama's Fine Italian" : {"vegetarian": True, "vegan": False, "gluten_free": False}
}

def chooseRestaurants(vegatarian, vegan, gluten_free):
    suitable_restaurants = []
    for restaurant, restrictions in restaurant_option.items():
        if restrictions["vegetarian"] >= vegatarian and restrictions ['vegan'] >= vegan and restrict:
            suitable_restaurants.append(restaurant)
    return suitable_restaurants

def main():
    is_vegetarian = input("is anyone in your group a vegetarian") == "yes"
    is_vegan = input('is anyone in your group a vegan') == 'yes'
    is_glutenFree = input('is anyone in your group-gluten') == 'yes'

    suitable_restaurants = chooseRestaurants(is_vegetarian, is_vegan, is_glutenFree)

    if suitable_restaurants:
        print("here are your restaurant choices:")
        for restaurant in suitable_restaurants:
            print(f"  {restaurants}")
    else:
        print('Sorry, there are no restaurants that fits your criteria')
if __name__=="_main_":
    main()






