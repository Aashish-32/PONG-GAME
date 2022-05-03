

import turtle



wn = turtle.Screen()
wn.title("game")
wn.setup(width=800,height=600)
wn.bgcolor("black")
wn.tracer(0)

#Initial score
x=0
y=0

#Paddle A

paddle_A=turtle.Turtle()
paddle_A.shape("square")
paddle_A.penup()
paddle_A.color("white")
paddle_A.shapesize(stretch_len=1,stretch_wid=6)
paddle_A.goto(-350,0)
paddle_A.speed(0)

#Paddle B

paddle_B=turtle.Turtle()
paddle_B.speed(1)
paddle_B.shape("square")
paddle_B.color("white")
paddle_B.penup()
paddle_B.goto(350,0)
paddle_B.shapesize(stretch_wid=6,stretch_len=1)

#Ball

ball=turtle.Turtle()
ball.shape("square")
ball.color("white")
ball.speed(0)
ball.penup()
ball.goto(0,0)
ball.dx=0.2
ball.dy=-0.2

#pen
pen=turtle.Turtle()
pen.color("white")
pen.penup()
pen.speed(0)
pen.hideturtle()
pen.goto(0,250)
pen.write("Player A: 0   Player B: 0" , align="center",font=("Courier",24,"normal"))

#To move paddle A upward

def padA_up():
    y=paddle_A.ycor()
    y+=40
    paddle_A.sety(y)

#To move paddle A downward

def padA_down():
    y=paddle_A.ycor()
    y-=40
    paddle_A.sety(y)

##To move paddle B upward

def padB_up():
    y=paddle_B.ycor()
    y+=40
    paddle_B.sety(y)

 #To move paddle B downward

def padB_down():
    y=paddle_B.ycor()
    y-=40
    paddle_B.sety(y)

#keyboardbindings

wn.listen()
wn.onkeypress(padB_down,"Down")
wn.onkeypress(padB_up,"Up")
wn.onkeypress(padA_down,"s")
wn.onkeypress(padA_up,"w")

#moving the ball
def mv_ball():
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)


#paddle and ball collision#
#Right side collision:
def collide():
    if ball.xcor()>340 and ball.xcor()<350 and ball.ycor()<paddle_B.ycor()+50 and ball.ycor()>paddle_B.ycor()-50:
        ball.dx *= -1

#Left side collision:
    if ball.xcor()<-340 and ball.xcor()>-350 and ball.ycor()<paddle_A.ycor()+50 and ball.ycor()>paddle_A.ycor()-50:
        ball.dx *= -1


while True:
#Border checking

    if ball.ycor() > 285:
        ball.sety(285)
        ball.dy *= -1

    if  ball.ycor() < -285:
        ball.sety(-285)
        ball.dy *= -1

    if  ball.xcor() > 390:
        x += 1
        ball.setx(0)
        ball.sety(0)
        ball.dx *= -1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(x,y) , align="center",font=("Courier",24,"normal"))

    if ball.xcor()< -390:
        y +=1
        ball.setpos(0,0)
        ball.dx *= -1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(x,y) , align="center",font=("Courier",24,"normal"))

    wn.update()
    mv_ball()
    collide()