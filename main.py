#Python Snake Classic Singeplayer/Multiplayer v0.1 Beta (By Ryhan.N)
#Pending:
#1) sound (high delay when experimenting)
version = "v0.1 Beta"

#import modules
import keyboard #keyboard input from user
import time #controls gamespeed and delays
import random #randomize food placements and dialogues
import os #scale the terminal
import hashlib #hash the highscores
from time import strftime, gmtime #get GM time with required formatting

#function for merging two strings alternatively
def merge(s1, s2): 
    result = "" 
    i = 0
    while (i < len(s1)) or (i < len(s2)):
        if (i < len(s1)):
            result += s1[i] 
        if (i < len(s2)):
            result += s2[i] 
        i += 1
    return result

#function for printing string in specific coordinates on screen
def cbstring(a="", x=1, y=1, z = False):
    '''
    Coordinate Based Printing Help (By Ryhan.N):
    Arg1 (string) = String to be printed
    Arg2 (+int) = X-Coordinate
    Arg3 (+int) = Y-Coordinate
    Arg4 (True/False) = Transparency (Can greatly reduce performance when turned On!) Default: False
    TIPS: 1) You can print strings in triple quotations!
    '''
    b = ""
    for j in a.split("\n"):
        c = x
        if z == True:
            for i in j.split(" "):
                if i != "":
                    b += f"\033[{y};{c}H" + i
                    c += len(i) + 1
                else:
                    c += 1
        else:
            b += f"\033[{y};{x}H" + j
        y += 1
    return b

#functions for changing directions
def up():
    global dir_snake_1
    global block_dir_snake_1
    if dir_snake_1 != "down" and block_dir_snake_1 == 0:
        dir_snake_1 = "up"
    block_dir_snake_1 = 1

def down():
    global dir_snake_1
    global block_dir_snake_1
    if dir_snake_1 != "up" and block_dir_snake_1 == 0:
        dir_snake_1 = "down"
    block_dir_snake_1 = 1
    
def right():
    global dir_snake_1
    global block_dir_snake_1
    if dir_snake_1 != "left" and block_dir_snake_1 == 0:
        dir_snake_1 = "right"
    block_dir_snake_1 = 1

def left():
    global dir_snake_1
    global block_dir_snake_1
    if dir_snake_1 != "right" and block_dir_snake_1 == 0:
        dir_snake_1 = "left"
    block_dir_snake_1 = 1
    
def up2():
    global dir_snake_2
    global block_dir_snake_2
    if dir_snake_2 != "down" and block_dir_snake_2 == 0:
        dir_snake_2 = "up"
    block_dir_snake_2 = 1

def down2():
    global dir_snake_2
    global block_dir_snake_2
    if dir_snake_2 != "up" and block_dir_snake_2 == 0:
        dir_snake_2 = "down"
    block_dir_snake_2 = 1
    
def right2():
    global dir_snake_2
    global block_dir_snake_2
    if dir_snake_2 != "left" and block_dir_snake_2 == 0:
        dir_snake_2 = "right"
    block_dir_snake_2 = 1

def left2():
    global dir_snake_2
    global block_dir_snake_2
    if dir_snake_2 != "right" and block_dir_snake_2 == 0:
        dir_snake_2 = "left"
    block_dir_snake_2 = 1

#gamemode selection (1-Singleplayer, 2-Multiplayer)
while(1):
    try:
        gamemode = int(input(f"Welcome to Python Snake Classic {version}! (By Ryhan.N)\n\nGAMEMODES:\n1 -> Singleplayer\n2 -> Multiplayer\n\nYour Choice: "))
        if gamemode == 1 or gamemode == 2:
            break
    except:
        pass
    print("Please enter either '1' or '2'!")
    time.sleep(2)
    print("\033[H\033[J", end='')

#intro
print("\033[H\033[J", end='')
if gamemode == 1:
    input(f"Welcome to Python Snake Classic Competetive {version}! (By Ryhan.N)\n\nCONTROLS:\nUP ARROW -> Turn up\nDOWN ARROW -> Turn down\nRIGHT ARROW -> Turn right\nLEFT ARROW -> Turn left\n\nRULES:\n1) Don't hit anything!\n2) Eat food to gain points, some give you double points!\n3) Try to score as much as possible!\n\nPRO TIP: You can't rapidly change directions!\n\nPress 'Enter' to continue...")
elif gamemode == 2:
    input(f"Welcome to Python Snake Classic Multiplayer {version}! (By Ryhan.N)\n\nCONTROLS PLAYER 1 (GREEN):\nUP ARROW -> Turn up\nDOWN ARROW -> Turn down\nRIGHT ARROW -> Turn right\nLEFT ARROW -> Turn left\n\nCONTROLS PLAYER 2 (YELLOW):\nW -> Turn up\nS -> Turn down\nD -> Turn right\nA -> Turn left\n\nRULES:\n1) Don't hit anything!\n2) Eat food to gain points, some give you double points!\n3) Snake with the highest point wins!\n\nPRO TIP: You can't rapidly change directions!\n\nPress 'Enter' to continue...")

#load and verify highscores in singleplayer
if gamemode == 1:
    salt = "BV[Gt(%RS:t:c8}7`dY`;fh9lAC:W'1;]cgNA:W6^myA>+_=`4wbOBp[9M6rZlG7y$wl^)7]E)MQ)vC#|zvOKAJ#<)ur?k_d2}vp"
    try:
        f = open('high_scores.txt','r')
        high_score_cache = f.readlines()
        high_score_0 = high_score_cache[0][:-1]
        high_score_1 = high_score_cache[1][:-1]
        high_score_2 = high_score_cache[2][:-1]
        high_score_3 = high_score_cache[3][:-1]
        high_score_4 = high_score_cache[4][:-1]
        high_score_5 = high_score_cache[5][:-1]
        check = high_score_cache[6]
        high_score_data = high_score_0 + "\n" + high_score_1 + "\n" + high_score_2 + "\n" + high_score_3 + "\n" + high_score_4 + "\n" + high_score_5
        f.close()
        check_original = hashlib.sha512(merge(salt, high_score_data).encode()).hexdigest()[:128]
        if check_original == check:
            pass
        else:
            print("\n\033[31mHigh Scores Compromised! Resetting Scores!\033[0m")
            time.sleep(2)
            raise Exception
    except:
        high_score_0 = "0 Saved Highscores"
        high_score_1 = "0 Saved Highscores"
        high_score_2 = "0 Saved Highscores"
        high_score_3 = "0 Saved Highscores"
        high_score_4 = "0 Saved Highscores"
        high_score_5 = "0 Saved Highscores"
        f = open('high_scores.txt', 'w')
        high_score_data = high_score_0 + "\n" + high_score_1 + "\n" + high_score_2 + "\n" + high_score_3 + "\n" + high_score_4 + "\n" + high_score_5
        f.write(high_score_data + "\n" + hashlib.sha512(merge(salt, high_score_data).encode()).hexdigest()[:128])
        f.close()
    
#resize terminal
print("\033[H\033[J", end='')
print("RESIZING...\n")
try:
    while ([os.get_terminal_size()[0],os.get_terminal_size()[1]] > [118, 28]):
        keyboard.send("Ctrl+plus")
        time.sleep(0.1)
    while ([os.get_terminal_size()[0],os.get_terminal_size()[1]] < [118, 28]):
        keyboard.send("Ctrl+-")
        time.sleep(0.1)
except:
    pass

#variables
snake_body_art = "#" #body of snakes
snake_head_art = "%" #head of snakes
food_art = "✪" #food of snakes
dir_snake_1 = "right" #direction of snake 1
dir_snake_2 = "right" #direction of snake 2
score_snake_1 = 0 #score of snake 1
score_snake_2 = 0 #score of snake 2
block_dir_snake_1 = 0 #flag for blocking direction change for snake 1
block_dir_snake_2 = 0 #flag for blocking direction change for snake 2
state_snake_1 = 1 #lifeline of snake 1
state_snake_2 = 1 #lifeline of snake 2
snake_1_head_coord = [10, 10] #coordinates of snake 1 head
snake_2_head_coord = [5, 5] #coordinates of snake 2 head
snake_1_body_coord = [(9, 10), (10, 10)] #coordinates of snake 1 bodies
snake_2_body_coord = [(4, 5), (5, 5)] #coordinates of snake 2 bodies
spawn_food_1_flag = 0 #flag to spawn food 1
spawn_food_2_flag = 0 #flag to spawn food 2
spawn_special_food_flag = 0 #flag to spawn special food
coord_food_1 = [] #coordinates of food 1
coord_food_2 = [] #coordinates of food 2
coord_special_food = [] #coordinates of special food
special_food_color_flag = 0 #special food color change flag
despawn_food_1 = 0 #despawn timer for food 1
despawn_food_2 = 0 #despawn timer for food 2
despawn_special_food = 0 #despawn timer for special food
all_food_coord = [] #list of all food spawn coordinates
possible_food_coord = all_food_coord #list of possible food spawn coordinates

#200 snake dialogues by CHATGPT
load_diag = open("dialogues.txt", 'r').readlines() #load dialogues file
diag_snake_1 = load_diag[random.randrange(200)] #random dialogue for snake 1
if gamemode == 2:
    diag_snake_2 = load_diag[random.randrange(200)] #random dialogue for snake 2

#loading screen (doesn't load anything! just for aesthetics)
print("\033[H\033[J", end='')
print("LOADING...\n")
bar_head = snake_head_art
bar_extend = snake_body_art
for i in range(59):
    bar_head = bar_extend + " " + bar_head
    print("                                                                                                                      \033[31m"+food_art+"\033[0m", end='\r')
    print("\033[32m"+bar_head+"\033[0m", end='\r')
    time.sleep(0.05)

#create 'all_food_coord'
for i in range(1, 30):
    for j in range(2, 26):
        all_food_coord.append([i,j])

#keyboard hotkeys for changing directions
keyboard.on_press_key("up", lambda _: up())
keyboard.on_press_key("down", lambda _: down())
keyboard.on_press_key("right", lambda _: right())
keyboard.on_press_key("left", lambda _: left())
if gamemode == 2:
    keyboard.on_press_key("w", lambda _: up2())
    keyboard.on_press_key("s", lambda _: down2())
    keyboard.on_press_key("d", lambda _: right2())
    keyboard.on_press_key("a", lambda _: left2())
#main loop
while(1):
    #move snake head based on current direction
    if dir_snake_1 == "up":
        snake_1_head_coord[1] -= 1
    elif dir_snake_1 == "down":
        snake_1_head_coord[1] += 1
    elif dir_snake_1 == "right":
        snake_1_head_coord[0] += 1
    elif dir_snake_1 == "left":
        snake_1_head_coord[0] -= 1
    if gamemode == 2:
        if dir_snake_2 == "up":
            snake_2_head_coord[1] -= 1
        elif dir_snake_2 == "down":
            snake_2_head_coord[1] += 1
        elif dir_snake_2 == "right":
            snake_2_head_coord[0] += 1
        elif dir_snake_2 == "left":
            snake_2_head_coord[0] -= 1
    #unblock direction hotkeys
    block_dir_snake_1 = 0
    block_dir_snake_2 = 0
    #snake collisions
    if snake_1_head_coord[0] == 0 or snake_1_head_coord[1] == 1 or snake_1_head_coord[0] > 29 or snake_1_head_coord[1] > 25:
        state_snake_1 = 0
        diag_snake_1 = "*DEAD* "
    if snake_2_head_coord[0] == 0 or snake_2_head_coord[1] == 1 or snake_2_head_coord[0] > 29 or snake_2_head_coord[1] > 25 and gamemode == 2:
        state_snake_2 = 0
        diag_snake_2 = "*DEAD* "
    if snake_1_head_coord == snake_2_head_coord and gamemode == 2:
        break
    if tuple(snake_1_head_coord) in snake_1_body_coord[:-1]:
        state_snake_1 = 0
        diag_snake_1 = "*DEAD* "
    if tuple(snake_2_head_coord) in snake_2_body_coord[:-1] and gamemode == 2:
        state_snake_2 = 0
        diag_snake_2 = "*DEAD* "
    if gamemode == 2:
        if tuple(snake_1_head_coord) in snake_2_body_coord[:-1] and state_snake_2 == 1:
            state_snake_1 = 0
            diag_snake_1 = "*DEAD* "
        if tuple(snake_2_head_coord) in snake_1_body_coord[:-1] and state_snake_1 == 1:
            state_snake_2 = 0
            diag_snake_2 = "*DEAD* "
    #move snake(s)' bodies
    snake_1_body_coord.append(tuple(snake_1_head_coord))
    if gamemode == 2:
        snake_2_body_coord.append(tuple(snake_2_head_coord))
    #create 'possible_food_coord'
    possible_food_coord = all_food_coord
    if gamemode == 2:
        for i in snake_1_body_coord + snake_2_body_coord:
            try:
                possible_food_coord.remove(i)
            except:
                pass
    else:
        for i in snake_1_body_coord:
            try:
                possible_food_coord.remove(i)
            except:
                pass
    #spawn/despawn normal food
    if spawn_food_1_flag == 0:
        try:
            coord_food_1 = random.choice(possible_food_coord)
        except:
            break
        spawn_food_1_flag = 1
    else:
        despawn_food_1 += 1
    if despawn_food_1 == 60:
        despawn_food_1 = 0
        spawn_food_1_flag = 0
    if spawn_food_2_flag == 0:
        try:
            coord_food_2 = random.choice(possible_food_coord)
        except:
            break
        spawn_food_2_flag = 1
    else:
        despawn_food_2 += 1
    if despawn_food_2 == 60:
        despawn_food_2 = 0
        spawn_food_2_flag = 0
    #spawn/despawn special food
    if random.randrange(50) == 25 and spawn_special_food_flag == 0:
        try:
            coord_special_food = random.choice(possible_food_coord)
        except:
            break
        spawn_special_food_flag = 1
        despawn_special_food = 0
    else:
        despawn_special_food += 1
    if despawn_special_food == 30:
        spawn_special_food_flag = 0
        despawn_special_food = 0
    #main display
    print("\033[H\033[J", end='')
    if gamemode == 2:
        print(f"""._________________________________________________________.
|                                                         | Greenie: {diag_snake_1[:-1]}
|                                                         | SCORE: {score_snake_1}
|                                                         |
|                                                         | Yelowie: {diag_snake_2[:-1]}
|                                                         | SCORE: {score_snake_2}
|                                                         |
|                                                         |
|                                                         |
|                                                         |
|                                                         |
|                                                         |
|                                                         |
|                                                         |
|                                                         |
|                                                         |
|                                                         |
|                                                         |
|                                                         |
|                                                         |
|                                                         |
|                                                         |
|                                                         |
|                                                         |
|                                                         |          
'---------------------------------------------------------'""")
    else:
        print(f"""._________________________________________________________.
|                                                         | Greenie: {diag_snake_1[:-1]}
|                                                         | SCORE: {score_snake_1}
|                                                         | HIGH SCORE: {high_score_0[0]}
|                                                         |
|                                                         |
|                                                         |
|                                                         |
|                                                         |
|                                                         |
|                                                         |
|                                                         |
|                                                         |
|                                                         |
|                                                         |
|                                                         |
|                                                         |
|                                                         |
|                                                         |
|                                                         |
|                                                         |
|                                                         |
|                                                         |
|                                                         |
|                                                         |          
'---------------------------------------------------------'""")
    if spawn_food_1_flag == 1:
        print("\033[31m"+cbstring(food_art,coord_food_1[0]*2,coord_food_1[1])+"\033[0m")
    if spawn_food_2_flag == 1:
        print("\033[31m"+cbstring(food_art,coord_food_2[0]*2,coord_food_2[1])+"\033[0m")
    if special_food_color_flag == 0 and spawn_special_food_flag == 1:
        special_food_color_flag = 1
        print("\033[95m"+cbstring(food_art,coord_special_food[0]*2,coord_special_food[1])+"\033[0m")
    elif special_food_color_flag == 1 and spawn_special_food_flag == 1:
        special_food_color_flag = 0
        print("\033[96m"+cbstring(food_art,coord_special_food[0]*2,coord_special_food[1])+"\033[0m")
    for i in range(len(snake_1_body_coord)-1):
        if state_snake_1 == 1:    
            print("\033[32m"+cbstring(snake_body_art,snake_1_body_coord[i][0]*2,snake_1_body_coord[i][1])+"\033[0m")
    if gamemode == 2:
        for i in range(len(snake_2_body_coord)-1):
            if state_snake_2 == 1:    
                print("\033[33m"+cbstring(snake_body_art,snake_2_body_coord[i][0]*2,snake_2_body_coord[i][1])+"\033[0m")
    if state_snake_1 == 1:
        print("\033[32m"+cbstring(snake_head_art,(snake_1_head_coord[0]*2),snake_1_head_coord[1])+"\033[0m")
    if state_snake_2 == 1 and gamemode == 2:
        print("\033[33m"+cbstring(snake_head_art,(snake_2_head_coord[0]*2),snake_2_head_coord[1])+"\033[0m")
    #snake(s) eating food
    if snake_1_head_coord == coord_food_1:
        spawn_food_1_flag = 0
        score_snake_1 += 1
        snake_1_body_coord.append(tuple(snake_1_head_coord))
        diag_snake_1 = load_diag[random.randrange(200)]
        despawn_food_1 = 0
    if snake_1_head_coord == coord_food_2:
        spawn_food_2_flag = 0
        score_snake_1 += 1
        snake_1_body_coord.append(tuple(snake_1_head_coord))
        diag_snake_1 = load_diag[random.randrange(200)]
        despawn_food_2 = 0
    if snake_1_head_coord == coord_special_food and spawn_special_food_flag == 1:
        spawn_special_food_flag = 0
        score_snake_1 += 2
        snake_1_body_coord.append(tuple(snake_1_head_coord))
        snake_1_body_coord.append(tuple(snake_1_head_coord))
        diag_snake_1 = load_diag[random.randrange(200)]
    if gamemode == 2:
        if snake_2_head_coord == coord_food_1:
            spawn_food_1_flag = 0
            score_snake_2 += 1
            snake_2_body_coord.append(tuple(snake_2_head_coord))
            diag_snake_2 = load_diag[random.randrange(200)]
            despawn_food_1 = 0
        if snake_2_head_coord == coord_food_2:
            spawn_food_2_flag = 0
            score_snake_2 += 1
            snake_2_body_coord.append(tuple(snake_2_head_coord))
            diag_snake_2 = load_diag[random.randrange(200)]
            despawn_food_2 = 0
        if snake_2_head_coord == coord_special_food and spawn_special_food_flag == 1:
            spawn_special_food_flag = 0
            score_snake_2 += 2
            snake_2_body_coord.append(tuple(snake_2_head_coord))
            snake_2_body_coord.append(tuple(snake_2_head_coord))
            diag_snake_2 = load_diag[random.randrange(200)]
    #remove snake(s)' tail
    del (snake_1_body_coord[0])
    if gamemode == 2:
        del (snake_2_body_coord[0])
    #end game if snake(s) die
    if state_snake_1 == 0 and state_snake_2 == 0 and gamemode == 2:
        break
    elif state_snake_1 == 0 and gamemode == 1:
        break
    if gamemode == 2:
        if score_snake_1 > score_snake_2 and state_snake_2 == 0:
            break
        elif score_snake_1 < score_snake_2 and state_snake_1 == 0:
            break
    #game speed
    time.sleep(0.3)

#game over
if gamemode == 1:
    if score_snake_1 > int(high_score_0.split(" ")[0]):
        print("\033[H\033[J", end='')
        print(f"GAME OVER!\n\nCongratulations! You set the new high score ({score_snake_1})!\n\nPress 'Enter' to save...")
        input()
        high_score_5 = high_score_4
        high_score_4 = high_score_3
        high_score_3 = high_score_2
        high_score_2 = high_score_1
        high_score_1 = high_score_0
        high_score_0_name = input(f"Enter your username to save it (Avoid Spaces and limit to 15 characters): ").replace(" ", "")[:16]
        high_score_0 = str(score_snake_1) + " Points By: " + high_score_0_name + " @" + strftime("%Y-%m-%d %H.%M.%S", gmtime())
    f = open('high_scores.txt', 'w')
    high_score_data = high_score_0 + "\n" + high_score_1 + "\n" + high_score_2 + "\n" + high_score_3 + "\n" + high_score_4 + "\n" + high_score_5
    f.write(high_score_data + "\n" + hashlib.sha512(merge(salt, high_score_data).encode()).hexdigest()[:128])
    f.close()
    print("\033[H\033[J", end='')
    print("GAME OVER!")
    print("\nSCORE:", score_snake_1)
    print(f"\nHIGH SCORES:\n{high_score_0}\n{high_score_1}\n{high_score_2}\n{high_score_3}\n{high_score_4}\n{high_score_5}\n")
elif gamemode == 2:
    print("\033[H\033[J", end='')
    print("GAME OVER!")
    print("\nGreenie SCORE:", score_snake_1)
    print("\nYelowie SCORE:", score_snake_2)
    if score_snake_1 > score_snake_2:
        print("\nGreenie has won!\n")
    elif score_snake_2 > score_snake_1:
        print("\nYelowie has won!\n")
    elif score_snake_1 == 0 and score_snake_2 == 0:
        print("\nThis is why both of you are still single!\n")
    else:
        print("\nDraw between Greenie and Yelowie\n")
        
keyboard.wait()
#THE END