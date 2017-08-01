import turtle
import random #We'll need this later in the lab
turtle.tracer(1,0) #This helps the turtle move more smoothly
SIZE_X=800
SIZE_Y=500
turtle.penup()
SQUARE_SIZE = 20
START_LENGTH = 6
#Initialize lists
pos_list = []
stamp_list = []
food_pos = []
food_stamps = []
#Set up positions (x,y) of boxes that make up the snake
snake = turtle.clone()
snake.shape("square")
turtle.setup(SIZE_X, SIZE_Y) #Curious? It's the turtle window
for i in range(START_LENGTH):
    x_pos=snake.pos()[0] #Get x-position with snake.pos()[0]
    y_pos=snake.pos()[1]
    x_pos+=SQUARE_SIZE
    my_pos=(x_pos,y_pos)
    snake.goto(x_pos,y_pos)
    pos_list.append(my_pos)
    stampID=snake.stamp()
    stamp_list.append(stampID)
    
#Hide the turtle object (it's an arrow - we don't need to see it)
turtle.hideturtle()
UP_ARROW = "Up" #Make sure you pay attention to upper and lower
LEFT_ARROW = "Left" #Pay attention to upper and lower case
DOWN_ARROW = "Down" #Pay attention to upper and lower case
RIGHT_ARROW = "Right" #Pay attention to upper and lower case
TIME_STEP = 100 #Update snake position after this many

#milliseconds

spacebar = "space" # Careful, it's not supposed to be
#capitalized!
UP = 0
DOWN=1
LEFT=2
RIGHT=3
direction = UP
def up():
    global direction 
    direction=UP 
    move_snake() 
    print("You pressed the up key!")
def down():
    global direction 
    direction=DOWN 
    move_snake() 
    print("You pressed the down key!")
def left():
    global direction 
    direction=LEFT 
    move_snake() 
    print("You pressed the left key!")
def right():
    global direction 
    direction=RIGHT 
    move_snake() 
    print("You pressed the right key!")
turtle.onkeypress(up, UP_ARROW)
turtle.onkeypress(down, DOWN_ARROW)
turtle.onkeypress(left, LEFT_ARROW)
turtle.onkeypress(right, RIGHT_ARROW)
turtle.listen()
def move_snake():
    my_pos=snake.pos
    x_pos=my_pos()[0]
    y_pos=my_pos()[1]

    if direction==RIGHT:
        snake.goto(x_pos+SQUARE_SIZE, y_pos)
        print("you moved right!")
    elif direction==LEFT:
        snake.goto(x_pos-SQUARE_SIZE, y_pos)
        print("you moved left!")
    if direction==UP:
        snake.goto(x_pos, y_pos+SQUARE_SIZE)
        print("you moved up!")
    elif direction==DOWN:
          snake.goto(x_pos,y_pos-SQUARE_SIZE)
          print("you moved down!")
    stampID2=snake.stamp()
    stamp_list.append(stampID2)
    my_pos=snake.pos()
    pos_list.append(my_pos)
    new_stamp=snake.stamp()
    stamp_list.append(new_stamp)

    old_stamp=stamp_list.pop(0)
    snake.clearstamp(old_stamp)
    pos_list.pop(0)
          
