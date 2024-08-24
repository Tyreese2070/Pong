class PongGame():
    import turtle
    import winsound
    import random

    global paddle_b
    global paddle_a

    wn = turtle.Screen()
    wn.title("Pong Game")
    wn.bgcolor("black")
    wn.setup(width=800, height=600)
    wn.tracer(0)

    #scores
    score_a = 0
    score_b = 0


    #Paddle A
    paddle_a=turtle.Turtle()
    paddle_a.speed(0)
    paddle_a.shape("square")
    paddle_a.color("white")
    paddle_a.shapesize(stretch_wid=5, stretch_len=1)
    paddle_a.penup()
    paddle_a.goto(-350, 0)


    #Paddle B
    paddle_b=turtle.Turtle()
    paddle_b.speed(0)
    paddle_b.shape("square")
    paddle_b.color("white")
    paddle_b.shapesize(stretch_wid=5, stretch_len=1)
    paddle_b.penup()
    paddle_b.goto(350, 0)


    #Ball
    ball=turtle.Turtle()
    ball.speed(0)
    ball.shape("circle")
    ball.color("white")
    ball.penup()
    ball.goto(0, 0)
    #ball speed**not really / direction
    ball.dx = 0.3
    ball.dy = 0.3

    #pen for score text
    pen = turtle.Turtle()
    pen.speed(0)
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 260)
    pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))


    #functions
    def paddle_a_up():
        y = paddle_a.ycor()
        y += 30 #size of each press going up for left paddle
        paddle_a.sety(y)

    def paddle_a_down():
        y = paddle_a.ycor()
        y -= 30 #size of each press going down for left paddle
        paddle_a.sety(y)

    def paddle_b_up():
        y = paddle_b.ycor()
        y += 30 #size of each press going up for right paddle
        paddle_b.sety(y)

    def paddle_b_down():
        y = paddle_b.ycor()
        y -= 30 #size of each press going down for right paddle
        paddle_b.sety(y)

    #Key Binding
    wn.listen()
    wn.onkey(paddle_a_up, "w")
    wn.onkey(paddle_a_down, "s")
    wn.onkey(paddle_b_up, "Up")
    wn.onkey(paddle_b_down, "Down")



    #main game loop
    while True:
        wn.update()

        #move the ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        #border check
        #top border
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1
        
        #bottom border
        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1
        
        #right border
        if ball.xcor() > 390:
            ball.goto(0, 0)
            ball.dx *= -1
            score_a += 1
            pen.clear()
            pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
            winsound.PlaySound("pointsound.wav", winsound.SND_ASYNC)
        
        #left border
        if ball.xcor() < -390:
            ball.goto(0, 0)
            ball.dx *= -1
            score_b += 1
            pen.clear()
            pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
            winsound.PlaySound("pointsound.wav", winsound.SND_ASYNC)

        #collisions
        #right paddle collide
        if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 50):
            ball.setx(340)
            ball.dx *= -1
            winsound.PlaySound("bounce1.wav", winsound.SND_ASYNC)

        #left paddle collide
        if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 50):
            ball.setx(-340)
            ball.dx *= -1
            winsound.PlaySound("bounce1.wav", winsound.SND_ASYNC)
            
        #left paddle collides with borders
        if paddle_a.ycor() > 290: #top border
            paddle_a.sety(-290)
        if paddle_a.ycor() < -290: #bottom border
            paddle_a.sety(290) 
        #right paddle collides with borders
        if paddle_b.ycor() > 290: #top border
            paddle_b.sety(-290)
        if paddle_b.ycor() < -290: #bottom border
            paddle_b.sety(290)
            
