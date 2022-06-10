"""Restaurant rating lister."""


# put your code here
restaurant_dict = {}

def get_restaurants():
    file = open("./scores.txt","r")
    for line in file:
        x = line.split(":")
        restaurant = x[0]
        rating = x[1]
        c = len(rating)-1
        rating = rating[0:c]
        restaurant_dict[restaurant] = rating
get_restaurants()

def print_restaurants():
    res_items = restaurant_dict.items()
    res_items_sorted = sorted(res_items)

    for key, val in res_items_sorted:
        print(f"{key} is rated at a {val}")
print_restaurants()

def add_restaurant():
    new_restaurant = input("enter a restaurant\n")
    new_rating = int(input("add a rating 1 through 5\n"))

    if new_rating > 5:
        print("Rating bust be between 1 and 5")
        add_restaurant()
    elif new_rating < 1:
        print("Rating bust be between 1 and 5")
        add_restaurant()
    else:
        restaurant_dict.update({new_restaurant:new_rating})
        print_restaurants()
add_restaurant()





    





