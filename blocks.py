from classes import *
import time
import winsound
import threading
import numpy as np

# Sets the objects
window = Window("Block Breaker", "black")
paddle = Paddle()
ball = Ball()
score = Score()
life = Life()

block_list = np.array([])
temp_array = [[]]



# 
def onmove(self, fun, add=None):

    if fun is None:
        self.cv.unbind('<Motion>')
    else:
        def eventfun(event):
            fun(self.cv.canvasx(event.x) / self.xscale, -self.cv.canvasy(event.y) / self.yscale)
        self.cv.bind('<Motion>', eventfun, add)

# paddle mouse control
def goto_handler(x, y):

    # avoid overlapping events
    onmove(turtle.Screen(), None)
    turtle.setheading(turtle.towards(x, y))

    # sets the height
    paddle.turtle.goto(x, -230)

    # move by mouse position
    onmove(turtle.Screen(), goto_handler)


# sets the blocks by given number of row, columns, the gaps, colors and block life
def make_blocks(rows, columns, x_gap, y_gap, frame_color, fill_color, life):

    # start position
    y = 200
    x = -250

    # set the block objects and insert to the list
    for row in range(rows):
        for col in range (columns):
            temp_array.append([x-30,y+10,x+30,y-10,\
            Block([x, y], "square", [3,1], frame_color, fill_color, life)])
            x += x_gap
        y -= y_gap
        x = -250

# create the blocks
make_blocks(5, 9, 63, 25, "red", "blue", 2)

# copy to numpy list to efficiency
block_list = np.append(block_list,temp_array,0)

# top corners life
life.turtle.write("Life: " + str(life.turtle.life), font=("Courier", 12, "normal"))

# when the ball is falled
fall = Score()
fall.turtle.goto(0,0)
fall.turtle.color("red")

# paddle move left keyboard
def left():
    x = paddle.turtle.xcor()
    x -= 50
    paddle.turtle.setx(x)

# paddle move right keyboard
def right():
    x = paddle.turtle.xcor()
    x += 50
    paddle.turtle.setx(x)

# exit the program
def out():
    window.turtle.bye()
    exit()

# delete blocks
def roy():
    block_list[-1][2].turtle.reset()
    block_list.remove(block_list[-1])



window.turtle.listen()

# The possible keys
window.turtle.onkeypress(right, "Right")
window.turtle.onkeypress(left, "Left")
window.turtle.onkeypress(out, "Escape")
window.turtle.onkeypress(roy,"space")

# winsound.PlaySound('sounds/xxx.mp3', winsound.SND_ASYNC | winsound.SND_ALIAS )
while True:
    onmove(turtle.Screen(), goto_handler)
    # Speed up ball movement
    # if ball.turtle.dx >= 0:
    #     ball.turtle.dx += 0.002
    # else:
    #     ball.turtle.dx -= 0.002
    
    # if ball.turtle.dy >= 0:
    #     ball.turtle.dy += 0.002
    # else:
    #     ball.turtle.dy -= 0.002

    # update the score
    score.turtle.clear()
    score.turtle.write("Score: " + str(score.turtle.sc), font=("Courier", 12, "normal"))

    # ball movement
    ball.turtle.setx(ball.turtle.xcor() + ball.turtle.dx)
    ball.turtle.sety(ball.turtle.ycor() + ball.turtle.dy)
    window.turtle.update()


    # When the ball touchs blocks
    for i in range(1,len(block_list)):
        # blocks cordinates from the list of blocks
        if (ball.turtle.xcor() >= block_list[i][0] and ball.turtle.xcor() <= block_list[i][2]) \
        and (ball.turtle.ycor() <= block_list[i][1] and ball.turtle.ycor() >= block_list[i][3]):

            # The block hit sound
            winsound.PlaySound("sounds/Xploshor.wav", winsound.SND_ASYNC | winsound.SND_ALIAS ) 

            # Earse block increase score and dealete the cordinates of block from list
            block_list[i][4].turtle.reset()

            # to fix the block is hiding in the middle
            block_list[i][4].turtle.hideturtle()

            # score up
            score.increase_score(score)

            # delete the hitted block
            block_list = np.delete(block_list,i)

            # change the ball movement
            ball.turtle.dx *= -1
            ball.turtle.dy *= -1
            break

    # Ceiling border
    if ball.turtle.ycor() > 290:
        ball.turtle.sety(290)
        ball.turtle.dy *= -1

    # Right wall border
    if ball.turtle.xcor() > 290:
        ball.turtle.setx(290)
        ball.turtle.dx *= -1

    # Left wall border
    if ball.turtle.xcor() < -290:
        ball.turtle.setx(-290)
        ball.turtle.dx *= -1
    
    # Floor border , Fail
    if ball.turtle.ycor() < -290:
        winsound.PlaySound("sounds/Padexplo.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
        ball.turtle.dx *= -1
        ball.turtle.dy *= -1
        ball.turtle.goto(0,0) # reset the ball
        ball.turtle.clear()
        i = 3 # number of lifes

        # Count down
        while i >= 0:
            fall.turtle.write(str(i),align="center", font=("Courier", 20, "bold"))
            fall.turtle.clear()
            if life.turtle.life > 1:
                time.sleep(1)
                paddle.turtle.goto(0, -230)
            i -= 1
            TODO # reset ball speed when ball fall
        
        # Update the life count
        life.turtle.clear()
        if life.turtle.life == 2: # red when last life left
            life.turtle.color("red")
        life.turtle.life -= 1
        life.turtle.write("Life: " + str(life.turtle.life), font=("Courier", 12, "normal"))
        continue
    
    # Tuch the paddle, have to fix(TODO add vectors)
    if (ball.turtle.ycor() < paddle.turtle.ycor() + 20) and (ball.turtle.xcor() > paddle.turtle.xcor() - 60)\
        and (ball.turtle.xcor() < paddle.turtle.xcor() + 60):
        winsound.PlaySound("sounds/Wowpulse.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
        ball.turtle.dy *= -1
        # ---~-
        if ball.turtle.xcor() > paddle.turtle.xcor() + 8 and ball.turtle.xcor() <= paddle.turtle.xcor() + 16: # right first pad
            if ball.turtle.dx > 0: # fly right
                ball.turtle.dx *= 2
            elif ball.turtle.dx < 0: # fly left
                ball.turtle.dx *= 0.5
            else:
                ball.turtle.dx = 1
        # -~---
        elif ball.turtle.xcor() < paddle.turtle.xcor() - 8 and ball.turtle.xcor() >= paddle.turtle.xcor() - 16: # right first pad
            if ball.turtle.dx > 0: # fly right
                ball.turtle.dx *= 0.5
            elif ball.turtle.dx < 0: # fly left
                ball.turtle.dx *= 2
            else:
                ball.turtle.dx = -1
        # ~----
        elif ball.turtle.xcor() < paddle.turtle.xcor() - 16 and ball.turtle.xcor() >= paddle.turtle.xcor() - 40: # right second pad
            if ball.turtle.dx > 0: # fly right
                ball.turtle.dx *= -0.2
            elif ball.turtle.dx < 0: # fly left
                ball.turtle.dx *= 5
            else:
                ball.turtle.dx = -2
        # ----~
        elif ball.turtle.xcor() > paddle.turtle.xcor() + 16 and ball.turtle.xcor() <= paddle.turtle.xcor() + 40: # right second pad
            if ball.turtle.dx > 0: # fly right
                ball.turtle.dx *= 5
            elif ball.turtle.dx < 0: # fly left
                ball.turtle.dx *= -0.2
            else:
                ball.turtle.dx = 2
    # Tuch the paddle
    # if (ball.turtle.ycor() < paddle.turtle.ycor() + 20) and (ball.turtle.xcor() > paddle.turtle.xcor() - 40)\
    #     and (ball.turtle.xcor() < paddle.turtle.xcor() + 40):
    #         winsound.PlaySound("sounds/Wowpulse.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
    #         ball.turtle.dy *= -1
    
    # Lose the game
    if life.turtle.life == 0:
        ball.turtle.clear()
        life.turtle.goto(0,0)
        life.turtle.color("red")
        life.turtle.write("Game Over",font=("Courier", 40, "normal"), align="center")
        winsound.PlaySound("sounds/Padexplo.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
        time.sleep(2)
        break
    
    if len(block_list) == 0:
        life.turtle.goto(0,0)
        life.turtle.write("You win",font=("Courier", 40, "normal"), align="center")
        time.sleep(2)
        break
