#!/usr/bin/env python3
def valid_input(world, steps):
    valid_chars = ["-", " ", "|", "#"]
    len_of_lines = []

    #Check for field data type
    if type(world) != tuple:
        raise Warning

    #Check if world is empty
    if len(world) <= 0:
        raise Warning
    
    #Check if step is positive and integer
    if type(steps) is not int:
        raise Warning
    if steps <= 0 :
        raise Warning

    #Check for invalid chars, same length of lines and if field is big enough
    for string in world:
        if len(string) <= 2 and len(world) <= 2:
            raise Warning
        len_of_lines.append(len(string))
        for char in string:
            chars_valid = False
            for valids in valid_chars:
                if char == valids:
                    chars_valid = True
            if chars_valid == False:
                raise Warning

    if len(set(len_of_lines)) != 1:
        raise Warning

#Calculate a single step of evolution
def evolve_step(world):
    new_world = []
    populated_cells = 0

    for line_idx, line in enumerate(world):
        new_line = ""
        for cell_idx, cell in enumerate(line):
            populated = False
            neighbours = 0
            #Check for neighbours
            if cell == " ":
                neighbours = 0
                if world[line_idx][cell_idx-1] == "#":
                    neighbours += 1
                if world[line_idx][cell_idx+1] == "#":
                    neighbours += 1
                if world[line_idx-1][cell_idx] == "#":
                    neighbours += 1
                if world[line_idx+1][cell_idx] == "#":
                    neighbours += 1
                if world[line_idx+1][cell_idx+1] == "#":
                    neighbours += 1
                if world[line_idx+1][cell_idx-1] == "#":
                    neighbours += 1
                if world[line_idx-1][cell_idx+1] == "#":
                    neighbours += 1
                if world[line_idx-1][cell_idx-1] == "#":
                    neighbours += 1
            
            elif cell == "#":
                populated = True
                neighbours = 0
                if world[line_idx][cell_idx-1] == "#":
                    neighbours += 1
                if world[line_idx][cell_idx+1] == "#":
                    neighbours += 1
                if world[line_idx-1][cell_idx] == "#":
                    neighbours += 1
                if world[line_idx+1][cell_idx] == "#":
                    neighbours += 1
                if world[line_idx+1][cell_idx+1] == "#":
                    neighbours += 1
                if world[line_idx+1][cell_idx-1] == "#":
                    neighbours += 1
                if world[line_idx-1][cell_idx+1] == "#":
                    neighbours += 1
                if world[line_idx-1][cell_idx-1] == "#":
                    neighbours += 1

            #Calculate field of next generation
            if populated and 1 >= neighbours >= 0:
                new_line = new_line + " "
            elif populated and neighbours >= 4:
                new_line = new_line + " "
            elif populated and 2 <= neighbours <= 3:
                new_line = new_line + "#"
                populated_cells += 1
            elif not populated and neighbours == 3:
                new_line = new_line + "#"
                populated_cells += 1
            elif cell == " ":
                new_line = new_line + " "
            elif cell == "|":
                new_line = new_line + "|"
            elif cell == "-":
                new_line = new_line + "-"
        new_world.append(new_line)
    print(tuple(new_world))
    return tuple(new_world), populated_cells

def evolve(world, steps):
    valid_input(world, steps)

    while steps != 0:
        world, populated_cells = evolve_step(world)
        steps -= 1

    return world, populated_cells # placeholder

field = (
        "--------------",
        "|            |",
        "|  ###       |",
        "|  #         |",
        "|   #        |",
        "|            |",
        "--------------"
)
steps = 4

result, alive_cells = evolve(field, steps)

print(f"Game of Life after {steps} moves:")
for row in result:
    print(row)
print(f"{alive_cells} are alive.")

