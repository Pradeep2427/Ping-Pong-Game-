
import turtle
import time

print("WELCOME TO PINGP-PONG GAME")
player1name = input ("  Enter First Player Name : ")
player2name = input ("  Enter Second Player Name : ")
print(player1name , "vs" , player2name)
print('Control')
print(player1name," up = w,down = s")
print(player2name," up = up arrow, down = down arrow")
print('winning point is 7')
time.sleep(5)

#screen setup

wn=turtle.Screen()

wn.title("pradeep's ping-pong")
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer(0)

#paddle1

paddle1 = turtle.Turtle()
paddle1.speed(0)
paddle1.shape("square")
paddle1.color("red")
paddle1.penup()
paddle1.shapesize(stretch_wid=5,stretch_len=1)
paddle1.goto(-350,0)

#paddle2

paddle2=turtle.Turtle()
paddle2.speed(0)
paddle2.shape("square")
paddle2.color("blue")
paddle2.penup()
paddle2.shapesize(stretch_wid=5,stretch_len=1)
paddle2.goto(350,0)

#ball

ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("green")
ball.penup()
ball.goto (0,0)
ballx = 2 
bally = 2

def paddle1_up():
    y=paddle1.ycor()
    y=y+20
    if(paddle1.ycor()>300):
        y=y-20
    paddle1.sety(y)
    
def paddle1_down():
    y=paddle1.ycor()
    y=y-20
    if(paddle1.ycor()==-300):
        y=y+20
    paddle1.sety(y)
    
def paddle2_up():
    y=paddle2.ycor()
    y=y+20
    if(paddle2.ycor()>300):
        y=y-20
    paddle2.sety(y)
    
def paddle2_down():
    y=paddle2.ycor()
    y=y-20
    if(paddle2.ycor()==-300):
        y=y+20
    paddle2.sety(y)    

wn.listen()
wn.onkeypress(paddle1_up,'w')
wn.onkeypress(paddle1_down,'s')
wn.onkeypress(paddle2_up,'Up')
wn.onkeypress(paddle2_down,'Down')


score1=0
score2=0


# score card

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.goto(0,260)
pen.hideturtle()
pen.write("{}    ||  {}  ".format(player1name,player2name) ,  align="center", font =("italic",20))
#pen.write("Player 1 :         ||         Player 2 :    " , align="center" , font =("italic",20))

def scoreupdate():
     score.clear()
     score.write("{}                  {}".format(score1,score2) , align="center", font =("italic",20))

score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0,220)

win = turtle.Turtle()
win.speed(0)
win.color("white")
win.penup()
win.hideturtle()
win.goto(0,50)

while (True and ( score1<7 and score2<7 )) :
    wn.update()
    ball.setx(ball.xcor()+ballx)
    ball.sety(ball.ycor()+bally)
    time.sleep(0.01)
    #scoreupdate()
    
    
   
# ball bouncing four sides

    if(ball.ycor() > 290):
        ball.sety(290)
        bally=bally *-1
       
    if(ball.xcor() > 380):
        ball.setx(380)
        ballx= ballx * -1
        score1 = score1 + 1
        scoreupdate()
        time.sleep(3)
        ball.goto(0,0)
        
      
       
    if(ball.ycor() < -290):
        ball.sety(-290)
        bally= bally * -1
       
    if(ball.xcor() < -380):
        ball.setx(-380)
        ballx= ballx * -1
        score2 = score2 + 1
        scoreupdate()
        time.sleep(1)
        ball.goto(0,0)

# ball hitting the paddle

    if( ball.xcor()==330) and (ball.ycor() < paddle2.ycor() +50 and ball.ycor() > paddle2.ycor() -50) :
        ballx = ballx * -1

    
    if( ball.xcor()==-330) and (ball.ycor() < paddle1.ycor() +50 and ball.ycor()  > paddle1.ycor() -50) :
        ballx = ballx * -1


while True:
    wn.update()
    if (score1==7):
        win.write("{} won".format(player1name),align="center",font=("italic,100"))
       
    if (score2==7):
        win.write("{} won".format(player2name),align="center",font=("italic,100"))
        
   







    

   






    
