import pygame
import math
from queue import PriorityQueue

WIDTH = 800  # assigning the width of the window
WIN = pygame.display.set_mode((WIDTH,WIDTH)) # creating the windows with the assigned width
pygame.display.set_caption("A* Path finding algorithm")# setting the caption for the window


# colors for the visualiser
YELLOW = (245, 239, 66)
GERY = (128,128,128)
WHITE = (255 , 255,255)
GREEEN = (81, 245, 66)
BLACK = (0,0,0)
ORANGE = (179,66,66)
TURQUOISE = (64,224,208)
BLUE = (66, 206, 245)
RED = (245, 129, 66)
PURPLE = (90, 66, 245)


class Spot:
    def __init__(self, row , col, width ,total_rows,): # creating the spot class intialising variables
        self.row = row
        self.col = col
        self.x = row*width
        self.y = col * width 
        self.color = WHITE
        self.neighbors = []
        self.width = width 
        self.total_rows = total_rows

    def get_pos(self): # for getting the position of the spot
        return self.row , self.col
    
    def is_closed(self):
        return self.color == RED

    def is_open(self):
        return self.color == GREEEN
    
    def is_barrier(self):
        return self.color == BLACK

    def is_start(self):
        return self.color == PURPLE

    def is_end(self):
        return self.color == TURQUOISE

    def reset(self):
        self.color = WHITE

    def make_start(self):
        self.color = ORANGE

    def make_closed(self):
        self.color = RED

    def make_open(self):
        self.color = GREEEN

    def make_barrier(self):
        self.color = BLACK

    def make_end(self):
        self.color = TURQUOISE

    def make_path(self):
        self.color = PURPLE

    def draw(self , win): # drawing the small cubes which gives the visual effect
        pygame.draw.rect(win , self.color ,(self.x , self.y , self.width ,self.width))

    def update_neighbors(self , grid): # checking if there are any barriers in the way of the node to reach the end point
        self.neighbors = []
        if self.row < self.total_rows -1 and not grid[self.row + 1][self.col].is_barrier(): # DOWN
            self.neighbors.append(grid[self.row + 1][self.col])
        
        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier(): # UP
            self.neighbors.append(grid[self.row - 1][self.col])
        
        if self.col < self.total_rows -1 and not grid[self.row ][self.col + 1].is_barrier():  # RIGHT
            self.neighbors.append(grid[self.row ][self.col + 1])
        
        if self.col > 0 and not grid[self.row ][self.col - 1].is_barrier(): # LEFT
            self.neighbors.append(grid[self.row ][self.col- 1])


    # def __lt__(self , other): # checking if the 
    #     return False


def h(p1 ,p2): # checking the heristic distance between the two nodes 
    x1, y1 = p1
    x2 , y2 = p2
    return abs(x1 - x2) +abs(y1 - y2)

def reconstruct_path(came_from , current , draw): # Drawing the final path 
    while current in came_from:
        current = came_from[current]
        current.make_path()
        draw()

def algorithm(draw , grid , start , end): # A* algorithm 
    count = 0
    open_set = PriorityQueue()
    open_set.put((0 , count, start)) # ((f_score , count , node))
    came_from = {}
    g_score = {spot : float("inf") for row in grid for spot in row} # setting the initial g_score of the spots to infinity except for the start node as it is 0
    g_score[start] = 0

    f_score = {spot : float("inf") for row in grid for spot in row}
    f_score[start] = h(start.get_pos() , end.get_pos()) # setting the f_score of the start node to heristic distance from start to end node

    open_set_hash = {start} # creating an open_set_hash with start initially

    while not open_set.empty(): # looping till the open_set gets empty
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = open_set.get()[2] # taking the node from the open_set which is at index 2 after f_score and count
        open_set_hash.remove(current)

        if current == end: # checking if we found the path and reconstucting the path
            reconstruct_path(came_from , end , draw)
            end.make_end()
            start.make_start()
            return True

        for neighbor in current.neighbors: # checking the neighbores of the current node
            temp_g_score = g_score[current] + 1 
            
            if temp_g_score < g_score[neighbor]: # checking if the neighbors have less g_score
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + h(neighbor.get_pos(), end.get_pos())
                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbor], count , neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.make_open()

        draw()
        if current != start:
            current.make_closed()

    return False


def make_grid(rows , width): # making the small cubical grids in the window
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            spot = Spot(i , j , gap , rows) # assing the spot variable to Spot object
            grid[i].append(spot)

    return grid

def draw_grid(win , rows , width): # for drawing the grid lines
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win , GERY,(0,i*gap) , (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win , GERY,(j*gap, 0) , (j * gap , width ))

def draw(win , grid, rows , width): # draw function which uses all the draw functions and updates the screen 
    win.fill(WHITE)

    for row in grid:
        for spot in row:
            spot.draw(win)
    draw_grid(win, rows , width)
    pygame.display.update()

def get_clicked_pos(pos , rows , width ): # to get the position where the mouse is clicked
    gap = width // rows
    y , x = pos

    row = y // gap
    col = x // gap  
    return row , col

def main(win , width):
    ROWS = 50
    grid = make_grid(ROWS , width)

    start = None
    end = None

    run = True

    while run:
        draw(win , grid ,ROWS , width) # using draw function to display all the grids
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


            if pygame.mouse.get_pressed()[0]: # LEFT mouse button
                pos = pygame.mouse.get_pos()
                row , col = get_clicked_pos(pos , ROWS , width)
                spot = grid[row][col] # assigning the spot position
                if not start and spot != end:
                    start = spot
                    start.make_start()

                elif not end and spot != start:
                    end = spot
                    end.make_end()

                elif spot != end and spot != start:
                    spot.make_barrier()

            elif pygame.mouse.get_pressed()[2]: # RIGHT
                pos = pygame.mouse.get_pos()
                row , col = get_clicked_pos(pos , ROWS , width)
                spot = grid[row][col]
                spot.reset()
                if spot == start:
                    start =None
                elif spot == end:
                    end = None
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start and end:
                    for row in grid:
                        for spot in row:
                            spot.update_neighbors(grid)
                    
                    algorithm(lambda : draw(win , grid , ROWS,width ) , grid , start , end) # calling the algorithm

                if event.key == pygame.K_c:
                    start = None
                    end = None
                    grid = make_grid(ROWS , width)




    pygame.quit()

main(WIN ,WIDTH)