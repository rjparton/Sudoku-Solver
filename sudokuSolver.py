from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = 'all'

import sys
import os
from pathlib import Path
from copy import deepcopy

def openfile(sudoku):
    
    # Pass through the name of the txt file as a string.
    
    import sys
    import os
    from pathlib import Path
    with open(Path(sudoku)) as file:
        L = file.readlines()

    
    grid = []
    for i in L:
        a = i.strip()
        if len(a) > 1:

            grid.append(a.replace(' ',''))
    gridder = [list(i) for i in grid]
    return gridder


# Innit Checks
# 0. Check 9 rows and columns
# 1. Check that each number is between 0-9 and not a string character
# 3. Check there are 9 values in each row. i.e no blanks or missing characters
def rowcol_lencheck(grid):
    if len(grid) != 9:
        return False #0 'Incorrect input.'
    if len(grid[0]) != 9:
        return False #0 'Incorrect input.'
    
    
    
def cellvaluechecker(grid):
    # make sure not a alpha char or a num >9
    
    
    # First, check the row numbers
    allowednumbers = ['0','1','2','3','4','5','6','7','8','9']
    for row in grid:
        numrowvalues = 0

        for column in row:

            # 1. Check all inputs are in allowednumbers
            if column in allowednumbers:
                numrowvalues += 1


            else:
                return False #'# 1. Incorrect input. Something not a 0-9'

        # 3.
        if numrowvalues != 9:
            return False # '# 3. not 9 row values somewhere', row

# Preassess() Checks:
# 2. Check the rows don't have dupe values
# 4. Check the columns don't have dupe vales
# 5. Check no dupes in each quadrant
def dupevaluechecker(grid):
    # Rows
    # Columns
    # Quads
    allowednumbers = ['0','1','2','3','4','5','6','7','8','9']

    # Do the Rows
    for row in grid:
        # 2. Create dict to track how many of each number in each row. If >1 then error
        uniquerownumbers = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}

        for column in row:

            # 2.
            if column in allowednumbers and column != '0':
                uniquerownumbers[column] += 1

        # 2.
        for k,v in uniquerownumbers.items():
            if v > 1:
                return False #'# 2. There is clearly no solution. A row has a dupe number',k,v

    
    # Columns
    # 4. Check no dupe values in each column
    # Transpose the columns to rows
    newgrid = [[grid[j][i] for j in range(len(grid))] for i in range(len(grid[0]))]

    for row in newgrid:
        uniquerownumbers = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}

        for column in row:
            if column in allowednumbers and column != '0':
                uniquerownumbers[column] += 1
        for k,v in uniquerownumbers.items():
            if v > 1:
                return False #'# 4. There is clearly no solution. A column has a dupe',k,v

                
    # Quads
    # 5. Check Each Quadrant doesn't have dupes

    # Quad 1
    uniquecellnumbers = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
    for row in range(0,3):
        for column in range(0,3):
            if grid[row][column] != '0':
                uniquecellnumbers[grid[row][column]] += 1

    for k,v in uniquecellnumbers.items():
            if v > 1:
                return False #'# 5. There is clearly no solution. A quad has a dupe',k,v

    # Quad 2
    uniquecellnumbers = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
    for row in range(0,3):
        for column in range(3,6):
            if grid[row][column] != '0':
                uniquecellnumbers[grid[row][column]] += 1

    for k,v in uniquecellnumbers.items():
            if v > 1:
                return False #'# 5. There is clearly no solution. A quad has a dupe',k,v

    # Quad 3
    uniquecellnumbers = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
    for row in range(0,3):
        for column in range(6,9):
            if grid[row][column] != '0':
                uniquecellnumbers[grid[row][column]] += 1

    for k,v in uniquecellnumbers.items():
            if v > 1:
                return False #'# 5. There is clearly no solution. A quad has a dupe',k,v


    # Quad 4
    uniquecellnumbers = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
    for row in range(3,6):
        for column in range(0,3):
            if grid[row][column] != '0':
                uniquecellnumbers[grid[row][column]] += 1

    for k,v in uniquecellnumbers.items():
            if v > 1:
                return False #'# 5. There is clearly no solution. A quad has a dupe',k,v

    # Quad 5
    uniquecellnumbers = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
    for row in range(3,6):
        for column in range(3,6):
            if grid[row][column] != '0':
                uniquecellnumbers[grid[row][column]] += 1

    for k,v in uniquecellnumbers.items():
            if v > 1:
                return False #'# 5. There is clearly no solution. A quad has a dupe',k,v

    # Quad 6
    uniquecellnumbers = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
    for row in range(3,6):
        for column in range(6,9):
            if grid[row][column] != '0':
                uniquecellnumbers[grid[row][column]] += 1

    for k,v in uniquecellnumbers.items():
            if v > 1:
                return False #'# 5. There is clearly no solution. A quad has a dupe',k,v


    # Quad 7
    uniquecellnumbers = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
    for row in range(6,9):
        for column in range(0,3):
            if grid[row][column] != '0':
                uniquecellnumbers[grid[row][column]] += 1

    for k,v in uniquecellnumbers.items():
            if v > 1:
                return False #'# 5. There is clearly no solution. A quad has a dupe',k,v

    # Quad 8
    uniquecellnumbers = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
    for row in range(6,9):
        for column in range(3,6):
            if grid[row][column] != '0':
                uniquecellnumbers[grid[row][column]] += 1

    for k,v in uniquecellnumbers.items():
            if v > 1:
                return False #'# 5. There is clearly no solution. A quad has a dupe',k,v

    # Quad 9
    uniquecellnumbers = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
    for row in range(6,9):
        for column in range(6,9):
            if grid[row][column] != '0':
                uniquecellnumbers[grid[row][column]] += 1

    for k,v in uniquecellnumbers.items():
            if v > 1:
                return False #'# 5. There is clearly no solution. A quad has a dupe',k,v

def otherrowcolumnvalues(x,y,grid):
    # Returns the numbers in the coordinate's row and column
    itsrow = []
    itscolumn = []
    for i in range(9):
        itsrow.append(grid[x][i])
#     itsrow
    for i in range(9):
        itscolumn.append(grid[i][y])
#     itscolumn
    incolandrow = itsrow + itscolumn
    incolandrow = list(set(incolandrow))
    return incolandrow

def coordinate_location(x,y):
    # Returns the position of a cell in a quad and what quad it's in
    rowdict = {0:'top',3:'top',6:'top',1:'middle',4:'middle',7:'middle',2:'bottom',5:'bottom',8:'bottom',}
    coldict = {0:'left',3:'left',6:'left',1:'middle',4:'middle',7:'middle',2:'right',5:'right',8:'right',}
    rowpos = rowdict[x]
    colpos = coldict[y]
    
    #output quadrant position
    # x = rows, y = columns
    # First row quadrants (first line)
    if x < 3 and y < 3:
        quadpos = 0
    elif x < 3 and y > 2 and y < 6:
        quadpos = 1
    elif x < 3 and y > 5:
        quadpos = 2
    # Second row quadrants (second line)    
    elif x >2 and x < 6 and y < 3:
        quadpos = 3
    elif x >2 and x < 6 and y > 2 and y < 6:
        quadpos = 4
    elif x >2 and x < 6 and y > 5:
        quadpos = 5
    # Third row quadrants (third line) 
    elif x >4 and y < 3:
        quadpos = 6
    elif x >4 and y > 2 and y < 6:
        quadpos = 7
    elif x >4 and y > 5:
        quadpos = 8
        
    return rowpos,colpos,quadpos
            
def otherquadvalues(x,y,poscoordinate,grid):
    # Returns the other values in a coordinate's quad. Uses coordinatelocation()
        # First we must find the other values in the cell's quad:
# x = 0
# y = 0
# poscoordinate = coordinate_location(x,y)
    # Top left:
    if poscoordinate[0] == 'top' and poscoordinate[1] == 'left':
        quadvalues = [ grid[x][y+1], grid[x][y+2],
                      grid[x+1][y], grid[x+1][y+1], grid[x+1][y+2],
                      grid[x+2][y], grid[x+2][y+1], grid[x+2][y+2],
                     ]
        quadvalues = list(set(quadvalues))
        if '0' in quadvalues:
            quadvalues.remove('0')
    # Top middle:
    elif poscoordinate[0] == 'top' and poscoordinate[1] == 'middle':
        quadvalues = [ grid[x][y-1], grid[x][y+1],
                      grid[x+1][y-1], grid[x+1][y], grid[x+1][y+1],
                      grid[x+2][y-1], grid[x+2][y], grid[x+2][y+1],
                     ]
        quadvalues = list(set(quadvalues))
        if '0' in quadvalues:
            quadvalues.remove('0')
    # Top right:
    elif poscoordinate[0] == 'top' and poscoordinate[1] == 'right':
        quadvalues = [ grid[x][y-2], grid[x][y-1],
                      grid[x+1][y-2], grid[x+1][y-1], grid[x+1][y],
                      grid[x+2][y-2], grid[x+2][y-1], grid[x+2][y],
                     ]
        quadvalues = list(set(quadvalues))
        if '0' in quadvalues:
            quadvalues.remove('0')
    # Middle left:
    elif poscoordinate[0] == 'middle' and poscoordinate[1] == 'left':
        quadvalues = [ grid[x-1][y], grid[x-1][y+1], grid[x-1][y+2],
                      grid[x][y+1], grid[x][y+2],
                      grid[x+1][y], grid[x+1][y+1], grid[x+1][y+2],
                     ]
        quadvalues = list(set(quadvalues))
        if '0' in quadvalues:
            quadvalues.remove('0')
    # Middle middle:
    elif poscoordinate[0] == 'middle' and poscoordinate[1] == 'middle':
        quadvalues = [ grid[x-1][y-1], grid[x-1][y], grid[x-1][y+1],
                      grid[x][y-1], grid[x][y+1],
                      grid[x+1][y-1], grid[x+1][y], grid[x+1][y+1],
                     ]
        quadvalues = list(set(quadvalues))
        if '0' in quadvalues:
            quadvalues.remove('0')
    # Middle right:
    elif poscoordinate[0] == 'middle' and poscoordinate[1] == 'right':
        quadvalues = [ grid[x-1][y-2], grid[x-1][y-1], grid[x-1][y],
                      grid[x][y-2], grid[x][y-1],
                      grid[x+1][y-2], grid[x+1][y-1], grid[x+1][y],
                     ]
        quadvalues = list(set(quadvalues))
        if '0' in quadvalues:
            quadvalues.remove('0')
    # Bottom left:
    elif poscoordinate[0] == 'bottom' and poscoordinate[1] == 'left':
        quadvalues = [ grid[x-2][y], grid[x-2][y+1], grid[x-2][y+2],
                      grid[x-1][y], grid[x-1][y+1], grid[x-1][y+2],
                      grid[x][y+1], grid[x][y+2],
                     ]
        quadvalues = list(set(quadvalues))
        if '0' in quadvalues:
            quadvalues.remove('0')
    # Bottom middle:
    elif poscoordinate[0] == 'bottom' and poscoordinate[1] == 'middle':
        quadvalues = [ grid[x-2][y-1], grid[x-2][y], grid[x-2][y+1],
                      grid[x-1][y-1], grid[x-1][y], grid[x-1][y+1],
                      grid[x][y-1], grid[x][y+1],
                     ]
        quadvalues = list(set(quadvalues))
        if '0' in quadvalues:
            quadvalues.remove('0')
    # Bottom right:
    elif poscoordinate[0] == 'bottom' and poscoordinate[1] == 'right':
        quadvalues = [ grid[x-2][y-2], grid[x-2][y-1], grid[x-2][y],
                      grid[x-1][y-2], grid[x-1][y-1], grid[x-1][y],
                      grid[x][y-2], grid[x][y-1],
                     ]
        quadvalues = list(set(quadvalues))
        if '0' in quadvalues:
            quadvalues.remove('0')
    return quadvalues
            
def highfreqgenerator(grid):
    dict_1 = {str(i):0 for i in range(0,10)}
    for i in grid:
        for j in i:
            dict_1[j] += 1
    dict_2 = {}
    for k,v in dict_1.items():
        if k != '0':
            if v not in dict_2:
                dict_2[v] = [k] 
            else:
                dict_2[v].append(k)
    return dict_2

quad_0 = [(0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)]
quad_1 = [(i[0],i[1]+3)  for i in quad_0]
quad_2 = [(i[0],i[1]+3)  for i in quad_1]

quad_3 = [(i[0]+3,i[1])  for i in quad_0]
quad_4 = [(i[0],i[1]+3)  for i in quad_3]
quad_5 = [(i[0],i[1]+3)  for i in quad_4]

quad_6 = [(i[0]+3,i[1])  for i in quad_3]
quad_7 = [(i[0],i[1]+3)  for i in quad_6]
quad_8 = [(i[0],i[1]+3)  for i in quad_7]
quadlist = [quad_0, quad_1, quad_2, quad_3, quad_4, quad_5, quad_6, quad_7, quad_8]

def fillnumber(number,grid,quad_list = quadlist):
    for quad in quad_list:
        possible = 0
        for coord in quad:
            gridder_3 = deepcopy(grid)
            if gridder_3[coord[0]][coord[1]] == '0':
                gridder_3[coord[0]][coord[1]] = number
                if dupevaluechecker(gridder_3) == False:
                    grid[coord[0]][coord[1]] = '0'
                else:
                    possible += 1
                    poss_cord = coord
        if possible == 1:
            grid[poss_cord[0]][poss_cord[1]] = number
    return grid


def forced(grid):
    maxfreqlist = highfreqgenerator(grid) #func to find highfreq num
    gridchanged = 1
    while gridchanged:
        maxfrequency = max(maxfreqlist.keys())
        grid2 = deepcopy(grid)
        for j in maxfreqlist[maxfrequency]:
            nomoreplacementsavailable = 1
            while nomoreplacementsavailable:
                grid3 = deepcopy(grid2)
                grid3 = fillnumber(j,grid3) #make it return the grid
                if grid3 != grid2:
                    grid2 = deepcopy(grid3)
                else:
                    nomoreplacementsavailable = 0
        # was anything changed?
        if grid2 != grid:
            grid = deepcopy(grid2)
            maxfreqlist = highfreqgenerator(grid2)
            # ADD FUNCTION: update dicter to be the new version of high freq numbers
        else:
            if maxfreqlist != {}:
                _ = maxfreqlist[maxfrequency].pop()
                if maxfreqlist[maxfrequency] == []:
                    _ = maxfreqlist.pop(maxfrequency)
                    #remove dicter[maxfrequency] from the dictionary
            if maxfreqlist == {}:
                gridchanged = 0
    return grid    
            
def forcedandbaretexoutput(grid):
    sudoku_template_part1 = '\\documentclass[10pt]{article}\n\\usepackage[left=0pt,right=0pt]{geometry}\n\\usepackage{tikz}\n\\usetikzlibrary{positioning}\n\\usepackage{cancel}\n\\pagestyle{empty}\n\n\\newcommand{\\N}[5]{\\tikz{\\node[label=above left:{\\tiny #1},\n                               label=above right:{\\tiny #2},\n                               label=below left:{\\tiny #3},\n                               label=below right:{\\tiny #4}]{#5};}}\n\n\\begin{document}\n\n\\tikzset{every node/.style={minimum size=.5cm}}\n\n\\begin{center}\n\\begin{tabular}{||@{}c@{}|@{}c@{}|@{}c@{}||@{}c@{}|@{}c@{}|@{}c@{}||@{}c@{}|@{}c@{}|@{}c@{}||}\\hline\\hline\n'
    sudoku_template_part2 = '% Line 1\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} \\\\ \\hline\n\n% Line 2\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} \\\\ \\hline\n\n% Line 3\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} \\\\ \\hline\\hline\n\n% Line 4\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} \\\\ \\hline\n\n% Line 5\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} \\\\ \\hline\n\n% Line 6\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} \\\\ \\hline\\hline\n\n% Line 7\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} \\\\ \\hline\n\n% Line 8\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} \\\\ \\hline\n\n% Line 9\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} \\\\ \\hline\\hline\n'
    sudoku_template_part3 = '\\end{tabular}\n\\end{center}\n\n\\end{document}\n'

    linestring = "% "
    for lineno in range(len(grid)):
        final = ""
        line = grid[lineno]
        for i in range(len(grid[lineno])):
            if line[i] != "0":
                final += "\\N{}{}{}{}{" + line[i] +"} & "
    #             final += "\\N{}{}{}{}{} & "
            else:
                final += "\\N{}{}{}{}{} & "
            if (i+1)%3 == 0 and i + 1 != 9:
                final = final[:-1]
                final += "\n"
        if (lineno + 1) % 3 == 0:
            final  = final[:-2] + "\\\\ \\hline\\hline\n\n% "
        else:
            final  = final[:-2] + "\\\\ \\hline\n\n% "
        final = "Line " + str(lineno + 1) + "\n" + final
    #     print(final)
        linestring += final
    linestring = linestring[:-3]
    output = sudoku_template_part1 + linestring + sudoku_template_part3
    return output


def markupgenerator(grid):
    # Pass this output into markedtextoutput()
    coordmarkups = {}
    for row in range(9):
        for col in range(9):
            if grid[row][col] == '0':
                possiblenumbers = ['1','2','3','4','5','6','7','8','9']
                rcvalues = otherrowcolumnvalues(row,col,grid)
                cooordetails = coordinate_location(row,col)
                quadvalues = otherquadvalues(row,col,cooordetails,grid)
                rcqvalues = rcvalues + quadvalues
                if '0' in rcqvalues:
                    rcqvalues.remove('0')
                markupnumbers = []
                for i in possiblenumbers:
                    if i not in rcqvalues:
                        markupnumbers.append(i)
                coordmarkups[(row,col)] = markupnumbers
            else:
                markupnumbers = []
                coordmarkups[(row,col)] = markupnumbers
    return coordmarkups

def markupstringgenerator(lister): 
    # This function gets called by markedtextoutput() below.
    ##  lister = [1,2,3,4] -> "\\N{1}{2}{3}{4}{} & "
    final_str = ""
    top_left = ""
    if "1" in lister:
        top_left += "1"
    if "2" in lister: 
        if top_left == "":
            top_left = "2"
        else:
            top_left += " 2"

    top_right = ""
    if "3" in lister :
        top_right += "3"
    if "4" in lister: 
        if top_right == "":
            top_right = "4"
        else:
            top_right += " 4"
    
    bottom_left = ""
    if "5" in lister :
        bottom_left += "5"
    if "6" in lister: 
        if bottom_left == "":
            bottom_left = "6"
        else:
            bottom_left += " 6"
            
    bottom_right = ""
    if "7" in lister :
        bottom_right += "7"
    if "8" in lister: 
        if bottom_right == "":
            bottom_right = "8"
        else:
            bottom_right += " 8"
    if "9" in lister: 
        if bottom_right == "":
            bottom_right = "9"
        else:
            bottom_right += " 9"
            
    final_str += "\\N{"+ top_left +"}{"+ top_right +"}{" + bottom_left + "}{" + bottom_right + "}{"
    return final_str

def markedtexoutput(grid,coordmarkups):
    sudoku_template_part1 = '\\documentclass[10pt]{article}\n\\usepackage[left=0pt,right=0pt]{geometry}\n\\usepackage{tikz}\n\\usetikzlibrary{positioning}\n\\usepackage{cancel}\n\\pagestyle{empty}\n\n\\newcommand{\\N}[5]{\\tikz{\\node[label=above left:{\\tiny #1},\n                               label=above right:{\\tiny #2},\n                               label=below left:{\\tiny #3},\n                               label=below right:{\\tiny #4}]{#5};}}\n\n\\begin{document}\n\n\\tikzset{every node/.style={minimum size=.5cm}}\n\n\\begin{center}\n\\begin{tabular}{||@{}c@{}|@{}c@{}|@{}c@{}||@{}c@{}|@{}c@{}|@{}c@{}||@{}c@{}|@{}c@{}|@{}c@{}||}\\hline\\hline\n'
    sudoku_template_part2 = '% Line 1\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} \\\\ \\hline\n\n% Line 2\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} \\\\ \\hline\n\n% Line 3\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} \\\\ \\hline\\hline\n\n% Line 4\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} \\\\ \\hline\n\n% Line 5\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} \\\\ \\hline\n\n% Line 6\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} \\\\ \\hline\\hline\n\n% Line 7\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} \\\\ \\hline\n\n% Line 8\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} \\\\ \\hline\n\n% Line 9\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} &\n\\N{}{}{}{}{} & \\N{}{}{}{}{} & \\N{}{}{}{}{} \\\\ \\hline\\hline\n'
    sudoku_template_part3 = '\\end{tabular}\n\\end{center}\n\n\\end{document}\n'

    linestring = "% "
    for lineno in range(len(grid)):
        final = ""
        line = grid[lineno]
        for i in range(len(grid[lineno])):
            if line[i] != "0":
                # Calculate the markupvalues for a coord and input them in the str. gen.
                final += "\\N{}{}{}{}{" + line[i] +"} & "
    #             final += "\\N{}{}{}{}{} & "
            else:
                final += markupstringgenerator(coordmarkups[(lineno,i)])+ "} & "
#                 final += "\\N{}{}{}{}{} & "
            if (i+1)%3 == 0 and i + 1 != 9:
                final = final[:-1]
                final += "\n"
        if (lineno + 1) % 3 == 0:
            final  = final[:-2] + "\\\\ \\hline\\hline\n\n% "
        else:
            final  = final[:-2] + "\\\\ \\hline\n\n% "
        final = "Line " + str(lineno + 1) + "\n" + final
    #     print(final)
        linestring += final
    linestring = linestring[:-3]
    output = sudoku_template_part1 + linestring + sudoku_template_part3
    return output




class SudokuError(Exception):
    pass

class Sudoku:
    
    def __init__(self,sudoku):
        self.sudokustring = sudoku
        self.sudokustring2 = self.sudokustring[:-4]
        self.grid = openfile(sudoku)
        self.forcedrun = False
        if rowcol_lencheck(self.grid) == False or cellvaluechecker(self.grid) == False:
            raise SudokuError('Incorrect input')
    
    def preassess(self):
        if dupevaluechecker(self.grid) == False:
            print('There is clearly no solution.')
        else:
            print('There might be a solution.')
    
    def bare_tex_output(self):
        baresudokustring = forcedandbaretexoutput(self.grid)
        file = open(str(self.sudokustring2) + '_bare.tex','w')
        file.write(baresudokustring)
    
    def forced_tex_output(self):
        global forced_sudoku_grid
        forced_sudoku_grid = forced(self.grid)
        forcedsudokustring = forcedandbaretexoutput(forced_sudoku_grid)
        self.grid = forced_sudoku_grid
        file = open(str(self.sudokustring2) + '_forced.tex','w')
        file.write(forcedsudokustring)
        self.forcedrun = True
        
    def marked_tex_output(self):
        if self.forcedrun == True:
            coordmarkups = markupgenerator(self.grid)
            markedupstring = markedtexoutput(self.grid,coordmarkups)
            file = open(str(self.sudokustring2) + '_marked.tex','w')
            file.write(markedupstring)
        else:
            #Need to do the forced_tex first then mark up
            forced_sudoku_grid = forced(self.grid)
            forcedsudokustring = forcedandbaretexoutput(forced_sudoku_grid)
            self.grid = forced_sudoku_grid
            file = open(str(self.sudokustring2) + '_forced.tex','w')
            file.write(forcedsudokustring)
            self.forcedrun = True
            
            coordmarkups = markupgenerator(self.grid)
            markedupstring = markedtexoutput(self.grid,coordmarkups)
            file = open(str(self.sudokustring2) + '_marked.tex','w')
            file.write(markedupstring)
        
        
        