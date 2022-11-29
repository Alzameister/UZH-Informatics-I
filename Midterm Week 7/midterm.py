milton_hotel = {
    "standard":  120.00,
    "executive": 160.00,
    "suite":     320.00,
    "breakfast": 25.00,
    "parking":   30.00,
}
def booking(pricing, products):
    cost_no_discount = 0
    discount = 0
    cost_with_discount = 0
    room_types = []
    room_count = 0

    #Calculate cost without discounts
    for product in products:
        cost_no_discount += pricing[product]
    #print(cost_no_discount)

    #Check for discounts
    if "executive" in products and "parking" in products:
        discount += pricing["parking"]
        products.remove("parking")

    if "suite" in products and "parking" in products:
        discount += pricing["parking"]
        products.remove("parking")

    if "suite" in products and "breakfast" in products:
        discount += pricing["breakfast"]
        products.remove("breakfast")

    for product in products:
        if product == "suite" or product == "executive" or product == "standard":
            room_count += 1
            room_types.append(product)

    if room_count >= 3:
        for rooms in room_types:
            #temp = pricing[rooms]
            discount += pricing[rooms] * 0.1

    #Calculate price with discounts
    cost_with_discount = cost_no_discount - discount

    return cost_no_discount, discount, cost_with_discount


print( booking(milton_hotel, [ # no discounts
    "executive", "breakfast"
]))
print( booking(milton_hotel, [ # one free parking
    "standard", "executive", "breakfast", "breakfast", "parking"
]))
print( booking(milton_hotel, [ # two free parking (one applied) and one free breakfast plus 10% off all rooms
    "standard", "executive", "suite", "parking",
    "breakfast", "breakfast", "breakfast"
]))













def add(n):
    return lambda x: n + x
    pass # implement here

#print( add(3.5)(10) )
#print( add(-5)(15) )









def sort_dict_values(d):
    for keys, values in d.items():
        values.sort()
        
        d[keys] = values
    return d
    pass # implement here


#print( sort_dict_values({"a": [3, 1, 2]}) )
#print( sort_dict_values({1: ["z", "az"], 2: [1]}) )










def multiply(n, factor=1):
    return n * factor

#print( multiply(2, 2) )
#print( multiply(2) )



















def print_range(start, stop, step):
    number = start

    while number < stop:
        print(number)
        number += step
    
    pass # implement here

#print( print_range(0, 1, 1) )
#print( print_range(5, 20, 3) )



















def length(iterable):
    index = 0
    
    for element in iterable:
        index += 1
    
    if index == 0:
        return 0
    if index == 1:
        return 1
    else:
        return 1 + length(iterable[:-1])
    
    
    pass # implement here

#print( length([1, 2, [3, 4]]) )
#print( length(("a", 1, 2, None)) )
#print( length("") )

#3
#4
#7










def normalize(number, lower, upper):
    if number < lower:
        return lower
    elif number > upper:
        return upper
    else:
        return number
    
#print( normalize(1, 0, 1) )
#print( normalize(15, 10, 20) )



