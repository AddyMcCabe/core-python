"""Restaurant rating lister."""


# put your code here
file = open("./scores.txt","r")
restaurant_dict = {}
for line in file:
    x = line.split(":")
    restaurant = x[0]
    rating = x[1]
    c = len(rating)-1
    rating = rating[0:c]
    restaurant_dict[restaurant] = rating
    
sortedByKey = {k: v for k, v in sorted((restaurant_dict.items()))}
list = list(sortedByKey)
print(list)


