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


grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]

# this is the heuristic function
heur_func = [[9, 8, 7, 6, 5, 4], 
             [8, 7, 6, 5, 4, 3], 
             [7, 6, 5, 4, 3, 2], 
             [6, 5, 4, 3, 2, 1], 
             [5, 4, 3, 2, 1, 0]]

expand_grid =  [[-1, -1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1, -1]]

init = [0,  0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

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
        open = [init]
        curr = init
        gvalue = 0
        fvalue = 0
        visited_cells = []
        gvalue_list = []
        fvalue_list = []    # f = g + h(x,y)

        _iter_exp = 0
        expand_grid[curr[0]][curr[1]] = _iter_exp

        gvalue_list.append([curr, gvalue])
        fvalue_list.append([curr, fvalue])
        while(curr != goal):
                neighbor_list = check_next(curr)

                # add the found neighbors to the open list if not alrady visited
                # also check that it is not already in the open list
                # also check that it is a valid neighbor
                for i in neighbor_list:
                        if (i not in visited_cells and i not in open and grid[i[0]][i[1]]==0):
                                open.append(i)
                                gvalue_list.append([i, gvalue+1])
                                temp_fvalue = (gvalue + heur_func[i[0]][i[1]])
                                fvalue_list.append([i, temp_fvalue])

                gvalue_list.remove([curr,gvalue])
                fvalue_list.remove([curr,fvalue])
                visited_cells.append(curr)
                
                gvalue += 1
                # get the lowest f-value in the list
                lowest_f = temp_fvalue
                for cell in fvalue_list:
                        if cell[1] <= lowest_f:
                                curr = cell[0]
                                lowest_f = cell[1]
                fvalue = lowest_f
                print(fvalue_list)
                _iter_exp += 1
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

search(grid, init, goal, cost)
for row in expand_grid:
    print(row)