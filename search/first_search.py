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


grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
init = [0, 0]
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
        visited_cells = []
        #gvalue_list = [[init], gvalue]
        gvalue_list = []

        gvalue_list.append([curr, gvalue])
        while(curr != goal):
                neighbor_list = check_next(curr)

                # add the found neighbors to the open list if not alrady visited
                for i in neighbor_list:
                        if (i not in visited_cells and i not in open and grid[i[0]][i[1]]==0):
                                open.append(i)
                                gvalue_list.append([i, gvalue+1])

                #open.remove([curr,gvalue])
                gvalue_list.remove([curr,gvalue])
                visited_cells.append(curr)
                
                gvalue += 1
                # get the lowest g-value in the list
                lowest_g = gvalue
                for cell in gvalue_list:
                        if cell[1] <= lowest_g:
                                curr = cell[0]
                                lowest_g = cell[1]
                gvalue = lowest_g
                print(gvalue_list)

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