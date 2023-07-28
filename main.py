import turtle
import time
import random

screen_game = turtle.Screen()
screen_game.bgcolor("light blue")
screen_game.title("CatchTheTurtle")
TYPE = "Ariel" , 20 , "normal"

score = 0
turtle_list=[]

countdown_turtle = turtle.Turtle()
score_turtle = turtle.Turtle()
def setup_score_turtle():
    score_turtle.color("dark blue")
    score_turtle.hideturtle()
    score_turtle.penup()

    top_height = screen_game.window_height() / 2
    y = top_height * 0.9
    score_turtle.goto(0,y)
    score_turtle.write(arg="Score: 0",move=False,align="center",font=TYPE)


grid_size = 10
def make_turtle(x,y):
    drawing_board = turtle.Turtle()

    def handle_click(x, y):
        #print(x,y)
        global score
        score += 1
        score_turtle.clear()
        score_turtle.write(arg="Score: {}".format(score), move=False, align="center", font=TYPE)

    drawing_board.onclick(handle_click)
    drawing_board.penup()
    drawing_board.shape("turtle")
    drawing_board.color("green")
    drawing_board.shapesize(2,2)
    drawing_board.goto(x*grid_size,y*grid_size)
    turtle_list.append(drawing_board)

x_coordinates = [-20,-10,0,10,20]
y_coordinates = [20,10,0,-10,-20]


def setup_turtles_cor():
    for x in x_coordinates:
        for y in y_coordinates:
            make_turtle(x,y)


def hide_turtles():
    for t in turtle_list:
        t.hideturtle()

def show_turtles_random():
    hide_turtles()
    random.choice(turtle_list).showturtle()
    screen_game.ontimer(show_turtles_random,500)


def countdown(time):
    countdown_turtle.hideturtle()
    countdown_turtle.color("black")
    countdown_turtle.penup()

    top_height = screen_game.window_height() / 2
    y = top_height * 0.9
    countdown_turtle.goto(0, y - 30)
    countdown_turtle.clear()

    if time > 0:
        countdown_turtle.clear()
        countdown_turtle.write(arg="Time: {}".format(time), move=False, align="center", font=TYPE)
        screen_game.ontimer(lambda: countdown(time-1),1000)

    else:
        countdown_turtle.clear()
        hide_turtles()
        countdown_turtle.write(arg="Game Over!", move=False, align="center", font=TYPE)







turtle.tracer(0)



setup_score_turtle()
setup_turtles_cor()
hide_turtles()
show_turtles_random()
countdown(10)



turtle.tracer(1)






turtle.mainloop()
