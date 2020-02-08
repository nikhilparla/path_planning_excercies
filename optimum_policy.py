# ----------
# User Instructions:
#
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

import sys
from copy import deepcopy


grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

expand_grid =  [[-1, -1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1, -1]]

delta = [[-1, 0],  # go up
         [0, -1],  # go left
         [1, 0],  # go down
         [0, 1]]  # go right

delta_name = ['^', '<', 'v', '>']
res_list = [init[i] + delta[1][i] for i in range(len(init))]
#print(res_list)
#search(grid, init, goal, cost)


def search(grid, init, goal, cost):
    # ----------------------------------------
    # insert code here
        open = [goal]
        curr = goal
        gvalue = 0
        prev_gvalue = gvalue #storing the prev gavlue so that we dont always keep increasing _iter value
        visited_cells = []
        #gvalue_list = [[init], gvalue]
        gvalue_list = []

        _iter_exp = 0
        expand_grid[curr[0]][curr[1]] = _iter_exp

        gvalue_list.append([goal, gvalue])

        # not an elegant while expression. Since we are not adding the blocked cells,
        # I know that the number will be less than total cells and just break when gvalue list is 0
        while(not(len(visited_cells) == (len(grid) * len(grid[0])))):
                neighbor_list = check_next(curr)

                # add the found neighbors to the open list if not alrady visited
                for i in neighbor_list:
                        if (i not in visited_cells and i not in open and grid[i[0]][i[1]] == 0):
                                open.append(i)
                                gvalue_list.append([i, gvalue+1])

                #open.remove([curr,gvalue])
                gvalue_list.remove([curr,gvalue])
                visited_cells.append(curr)
                if(len(gvalue_list) == 0):
                        break
                
                gvalue += 1
                # get the lowest g-value in the list
                lowest_g = gvalue
                for cell in gvalue_list:
                        if cell[1] <= lowest_g:
                                curr = cell[0]
                                lowest_g = cell[1]
                gvalue = lowest_g
                print(gvalue_list)

                # For all same g-valued cells, their neighbors also will also have similar g-values (+1)
                # compare with expansion search here how they are different
                if(not(prev_gvalue == gvalue)):
                        _iter_exp += 1
                        prev_gvalue = gvalue                        
                
                expand_grid[curr[0]][curr[1]] = _iter_exp

    # ----------------------------------------

        return [gvalue,curr[0], curr[1]]

def check_next(curr):
        neighbor_list = []
        # if there is a position to the left
        if(not((curr[1]-1) < 0)):
                # append the left element to neighbor list. row remains same
                neighbor_list.append([(curr[0]),curr[1]-1])
        # if there is a position to the right
        if(not((curr[1]+1) > len(grid[0]) - 1 )):
                # append the right element to neighbor list. row remains same
                neighbor_list.append([( curr[0]), curr[1]+1])
        # if there is a position to the top
        if(not((curr[0]-1) < 0)):
                # append the top element to neighbor list. col remains same
                neighbor_list.append([(curr[0]-1),curr[1]])
        # if there is a position to the bottom                
        if(not((curr[0]+1) > len(grid)-1 )):
                # append the bottom element to neighbor list. row remains same
                neighbor_list.append([(curr[0]+1) , curr[1]])
        
        return neighbor_list                

print(search(grid, init, goal, cost))
print("---------------------------")
for row in expand_grid:
    print(row)

optimum_list = deepcopy(expand_grid)
def find_least_neighnor(x_pos, y_pos):
    least_value = sys.maxsize
    value = 0
    # if there is a position to the left
    if(not((y_pos-1) < 0)):
        # append the left element to neighbor list. row remains same
        # neighbor_list.append([(x_pos),y_pos-1])
        # print(type((expand_grid[x_pos][y_pos-1])))
        # print(expand_grid[x_pos][y_pos-1])
        if((expand_grid[x_pos][y_pos-1]) < least_value and not(expand_grid[x_pos][y_pos-1] == -1)):
            least_value = expand_grid[x_pos][y_pos-1]
            value = '<'
    # if there is a position to the right
    if(not((y_pos+1) > len(grid[0]) - 1 )):
            # append the right element to neighbor list. row remains same
            # neighbor_list.append([( x_pos), y_pos+1])
        if(expand_grid[x_pos][y_pos+1] < least_value and not(expand_grid[x_pos][y_pos+1] == -1)):
            least_value = expand_grid[x_pos][y_pos+1]
            value = '>'
    # if there is a position to the top
    if(not((x_pos-1) < 0)):
        # append the top element to neighbor list. col remains same
        # neighbor_list.append([(x_pos-1),y_pos])
        if(expand_grid[x_pos-1][y_pos] < least_value and not(expand_grid[x_pos-1][y_pos] == -1)):
            least_value = expand_grid[x_pos-1][y_pos]
            value = '^'
    # if there is a position to the bottom                
    if(not((x_pos+1) > len(grid)-1 )):
        # append the bottom element to neighbor list. row remains same
        # neighbor_list.append([(x_pos+1) , y_pos])
        if(expand_grid[x_pos+1][y_pos] < least_value and not(expand_grid[x_pos+1][y_pos] == -1)):
            least_value = expand_grid[x_pos+1][y_pos]       
            value = 'v'
    
    # update with the least value
    optimum_list[x_pos][y_pos] = value

# For every element in expansion grid, check the neighbor element with the least value and 
# change the direction accordingly
for x in range(len(optimum_list)):
    for y in range(len(optimum_list[0])):
        if(not(optimum_list[x][y] == -1)):
            # print(type(optimum_list[x][y]))
            find_least_neighnor(x,y)

print("---------------------------")
for row in optimum_list:
    print(row)