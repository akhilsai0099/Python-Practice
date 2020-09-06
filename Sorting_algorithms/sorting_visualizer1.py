import pygame
import random

pygame.font.init()
screen = pygame.display.set_mode((900,650))
pygame.display.set_caption("Sorting Visualisation")

run = True

width = 900
height = 600
array = [0]*151
arr_clr = [(0, 204, 102)]*151
clr_ind = 0
clr = [(0, 204, 102), (255, 0, 0),
(0, 0, 153), (255, 102, 0)]
TIME = 20

fnt = pygame.font.SysFont("comicsans", 30)
fnt1 = pygame.font.SysFont("comicsans", 20)
fnt2 = pygame.font.SysFont("comicsans", 25)

def refill():
    screen.fill((255,255,255))
    draw()
    pygame.display.update()
    pygame.time.delay(TIME)

for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_i:
            value = "Insertion Sort"
            refill()


def mergesort(array, l, r):
    mid =(l + r)//2
    if l<r:
        mergesort(array, l, mid)
        mergesort(array, mid + 1, r)
        merge(array, l, mid,
            mid + 1, r)

def merge(array, x1, y1, x2, y2):
    i = x1
    j = x2
    temp =[]
    pygame.event.pump()
    while i<= y1 and j<= y2:
        for event in pygame.event.get():
        # If we click Close button in window
            if event.type == pygame.QUIT:
                pygame.quit()
        arr_clr[i]= clr[1]
        arr_clr[j]= clr[1]
        refill()
        arr_clr[i]= clr[0]
        arr_clr[j]= clr[0]
        if array[i]<array[j]:
                temp.append(array[i])
                i+= 1
        else:
                temp.append(array[j])
                j+= 1
    while i<= y1:
        for event in pygame.event.get():
        # If we click Close button in window
            if event.type == pygame.QUIT:
                pygame.quit()
        arr_clr[i]= clr[1]
        refill()
        arr_clr[i]= clr[0]
        temp.append(array[i])
        i+= 1
    while j<= y2:
        for event in pygame.event.get():
        # If we click Close button in window
            if event.type == pygame.QUIT:
                pygame.quit()
        arr_clr[j]= clr[1]
        refill()
        arr_clr[j]= clr[0]
        temp.append(array[j])
        j+= 1
    j = 0
    for i in range(x1, y2 + 1):
        pygame.event.pump()
        array[i]= temp[j]
        j+= 1
        arr_clr[i]= clr[2]
        refill()
        if y2-x1 == len(array)-2:
            arr_clr[i]= clr[3]
        else:
            arr_clr[i]= clr[0]




def insertionSort(array):
    for i in range(1, len(array)):
        for event in pygame.event.get():
        # If we click Close button in window
            if event.type == pygame.QUIT:
                pygame.quit()
        pygame.event.pump()
        refill()
        key = array[i]
        arr_clr[i] = clr[2]
        j = i - 1
        while j >= 0 and key < array[j]:

            array[j + 1] = array[j]
            arr_clr[j] = clr[1]
            refill()
            arr_clr[j] = clr[3]
            j = j - 1
        array[j + 1] = key
        refill()
        arr_clr[i] = clr[3]


def selection_sort(list):
    for i in range(0,len(list)-1):
        for event in pygame.event.get():
            # If we click Close button in window
            if event.type == pygame.QUIT:
                pygame.quit()
        pygame.event.pump()
        refill()
        min_position = i
        arr_clr[i] =clr[2]

        for j in range(i+1, len(list)):
            if  list[j] < list[min_position]:

                arr_clr[j] = clr[1]
                refill()
                min_position = j
                arr_clr[j] = clr[0]
        if min_position != i:

            list[i], list[min_position] = list[min_position], list[i]

        arr_clr[i] = clr[3]

    refill()

def Bubble_sort(list):
    for i in range(len(list)-1,0,-1):
        for event in pygame.event.get():
            # If we click Close button in window
            if event.type == pygame.QUIT:
                pygame.quit()
        pygame.event.pump()
        refill()

        for j in range(i):
            if list[j] > list[j+1]:
                temp = list[j]
                arr_clr[j] = clr[1]
                refill()
                list[j] = list[j+1]
                arr_clr[j] = clr[2]
                refill()
                list[j+1] = temp
                arr_clr[j] = clr[0]
        arr_clr[i] = clr[3]
        refill()

def generate_arr():
    for i in range(1 ,151):
        arr_clr[i] = clr[0]
        array[i] = random.randrange(1,100)

generate_arr()



def draw():
    txt = fnt.render("PRESS INITIAL LETTER OF THE ALGORITHM BELOW TO START SORTING" ,1,(0,0,0))
    screen.blit(txt,(20,20))

    txt1 = fnt.render("PRESS 'R' FOR NEW ARRAY",1,(0,0,0))
    screen.blit(txt1,(20,60))

    txt2 = fnt1.render("Selection sort , Merge sort , Insertion sort , Bubble sort",3,(0,0,0))
    screen.blit(txt2,(20,40))

    txt2 = fnt2.render("Press Up or Down arrows to increase or decrease the speed respectively",2,(0,0,0))
    screen.blit(txt2,(310,60))


    element_width = width //151
    boundry_arr = 900 / 150
    boundry_grp = 550 / 100

    pygame.draw.line(screen, (0,0,0),(0,95),(900,95) , 6)

    for i in range(1,100):
        pygame.draw.line(screen,(224,224,224),(0,boundry_grp*i+100),(900 , boundry_grp*i+100),1)

    for i in range(1,151):
        pygame.draw.line(screen,arr_clr[i],(boundry_arr*i-3, 100),(boundry_arr * i-3, array[i]*boundry_grp + 100),element_width)

while run:
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_i:
                pygame.display.set_caption("Sorting Algorithm : Insertion sort")
                insertionSort(array)

            if event.key == pygame.K_s:
                pygame.display.set_caption("Sorting Algorithm : Selection sort")
                selection_sort(array)

            if event.key == pygame.K_r:
                pygame.display.set_caption("Generated New array")
                generate_arr()

            if event.key == pygame.K_m:
                pygame.display.set_caption("Sorting Algorithm : Merge sort")
                mergesort(array,1,len(array)-1)
                
            if event.key == pygame.K_b:
                pygame.display.set_caption("Sorting Algorithm : Bubble sort")
                Bubble_sort(array)

            if event.key == pygame.K_UP:
                pygame.display.set_caption(f"speed : {TIME}")
                TIME -= 5
            
            if event.key == pygame.K_DOWN:
                pygame.display.set_caption(f"speed : {TIME}")
                TIME += 10
                

    draw()
    pygame.display.update()

pygame.quit()
