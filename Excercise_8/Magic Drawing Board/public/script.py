#!/usr/bin/env python3

class MagicDrawingBoard:
    #Constructor
    def __init__(self, x, y):
        self.__field = []
        self.__line_boundary = y
        self.__col_boundary = x

        #Initialize field
        if x < 1 or y < 1:
            raise Warning("Invalid Field size")

        for line in range(0,y):
            self.__field.append([])
            for col in range(0,x):
                self.__field[line].append(0)
        
        print(self.__field)

    #Print image
    def img(self):
        string = str(self.__field)
        string = string[1:-1]
        string = string.replace("[", "")
        string = string.replace(",", "")
        string = string.replace(" ", "")
        string = string.replace("]", "\n")
        string = string[:-1]
        return string

    #Draw a pixel
    def pixel(self, coord):
        x = coord[0]
        y = coord[1]

        if x < 0 or x >= self.__col_boundary:
            raise Warning("Invalid x Pixel")
        elif y < 0 or y >= self.__line_boundary:
            raise Warning("Invalid y Pixel")
        
        self.__field[x][y] = 1

    #Start = pixel, end = first pixel not painted
    def rect(self, start, end):
        start_x = start[0]
        start_y = start[1]
        end_x = end[0]
        end_y = end[1]

        if start_x < 0 or start_x >= self.__col_boundary or start_y < 0 or start_y >= self.__line_boundary or end_x < 0 or end_x > self.__col_boundary or end_y < 0 or end_y > self.__line_boundary:
            raise Warning("Invalid Pixel")
        if end_x < start_x or end_y < start_y:
            raise Warning("End smaller than Start")

        for line in range(start_y, end_y):
            for col in range(start_x, end_x):
                self.__field[line][col] = 1
    
    #Clear board
    def clear(self):
        for line in range(len(self.__field)):
            for col in range(len(self.__field[line])):
                if self.__field[line][col] == 1:
                    self.__field[line][col] = 0 

        return self.__field

        


# You can play around with your implementation in the body of the following 'if'.
# The contained statements will be ignored while evaluating your solution.
if __name__ == '__main__':
    db = MagicDrawingBoard(5,5)
    db.pixel((0,0))
    db.rect((3,3), (3,3))
    print(db.img())
    db.clear()
    print()
    db.rect((3,3), (4,5))
    print(db.img())

