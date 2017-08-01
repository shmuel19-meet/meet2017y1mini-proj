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
UP_EDGE=250
DOWN_EDGE=-250
RIGHT_EDGE=400
LEFT_EDGE=-400
def up():
    global direction 
    direction=UP  
    print("You pressed the up key!")
def down():
    global direction 
    direction=DOWN  
    print("You pressed the down key!")
def left():
    global direction 
    direction=LEFT  
    print("You pressed the left key!")
def right():
    global direction 
    direction=RIGHT 
    print("You pressed the right key!")
turtle.onkeypress(up, UP_ARROW)
turtle.onkeypress(down, DOWN_ARROW)
turtle.onkeypress(left, LEFT_ARROW)
turtle.onkeypress(right, RIGHT_ARROW)
turtle.listen()
#def_makefood









def move_snake():
    my_pos=snake.pos
    x_pos=my_pos()[0]
    y_pos=my_pos()[1]
    #grab position of snake
    new_pos=snake.pos()
    new_x_pos=new_pos[0]
    new_y_pos=new_pos[1]
    #the next 3 lines check if the snake is hitting the right edge
    if new_x_pos>=RIGHT_EDGE:
        print("you hit the right edge! game over")
        quit()
    elif new_x_pos<=LEFT_EDGE:
            print("you hit the left edge game over")
            quit()
    elif new_y_pos>=UP_EDGE:
            print("you hit the up edge")
            quit()
    elif new_y_pos<=DOWN_EDGE:
            print("you hit the down edge")
            quit()
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
    global food_stamps,food_pos
    if snake.pos() in food_pos:
        food_ind=food_pos.index(snake.pos())
        food.clearstamp(food_stamps[food_ind])
        food_pos.pop(food_ind)
        food_stamps.pop(food_ind)
        print("you have eaten the food")
        #this if statment might be useful in part 8
    old_stamp=stamp_list.pop(0)
    snake.clearstamp(old_stamp)
    pos_list.pop(0)

    turtle.ontimer(move_snake,TIME_STEP)
move_snake()

turtle.register_shape("trash.gif")
food=turtle.clone()
food.shape("trash.gif")
food.hideturtle()
food_pos=[(100,100), (-100,100), (-100,-100), (100,-100)]
food_stamps=[]
for this_food_pos in food_pos:
    food.goto(this_food_pos)
    food_ID=food.stamp()
    food_stamps.append(food_ID)
