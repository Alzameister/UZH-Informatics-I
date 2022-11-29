#!/usr/bin/env python3

class Fridge:
    def __init__(self) -> None:
        self.__items = []

    def __iter__(self):
        self.__items = sorted(self.__items)
        return self.__items.__iter__()

    #Add item to fridge
    def store(self, item):
        #Add item to list
        self.__items.append(item)

    #Remove item from fridge
    def take(self, item):
        if item in self.__items:
            print("hi")
            self.__items.remove(item)
            return item
        else: raise Warning("No matching Item found")

    #Find item in fridge
    def find(self, name):
        __sorted_by_date = sorted(self.__items)
        for item in __sorted_by_date:
            if name == item[1]:
                return item
        return None

    #Remove items from fridge that went bad
    def take_before(self, date):
        expired = []
        
        for item in self.__items:
            if item[0] < date:
                expired.append(item)
                self.__items.remove(item)
        return expired

    def get_Items(self):
        print("Items in the fridge:")
        for i in self.__items:
            print(f"- {i[1]} ({i[0]})")    

    def __len__(self):
        return len(self.__items)
    
    
f = Fridge()
f.store((201112, "Butter"))
f.store((191112, "Butter"))
print(f.find("Butter"))

