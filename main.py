import turtle
from time import sleep
from random import randint
from pyautogui import alert, prompt, password
im = password('Game Code', 'GAME CODE', mask='*')
while im != 'UCC238':
    alert('WRONG', 'CORRECT/WRONG', 'OK')
    im = password('Game Code', 'GAME CODE', mask='*')
else:
    alert('CORRECT', 'CORRECT/WRONG', 'OK')
    pass
t = turtle.Turtle()
s = turtle.Screen()
turtle.setundobuffer(0)
s.bgcolor('black')
s.title('Ultimate Coin Collector')
s.setup(680, 680)
score = 0
lives = 10
level = 1
start = prompt("Let's Play(Play or Help): ", 'Ultimate Coin Collector(Start)', 'Your Opinion').upper()
if start == 'PLAY':
    sleep(1)
    pass
elif start == 'HELP':
    alert('''   Welcome To Ultimate Coin Collector.
            The Instructions Are Given Below.
            Left Arrow Key For Turning 45 Degrees To The Left.
            Right Arrow Key For Turning 45 Degrees To The Right.
            Up Arrow Key For Acceleration.
            Down Arrow Key For Deceleration.
            R Key For Reset Position.
            The Goal Is To Get The Coin.
            Once You Have Got 10 Score You Have Won.
            Click Ok To Continue.
            Then Enter Your Preferred Speed.
            Then You Have 2 Secs To Put Your Fingers On The Arrow Keys.
            After That Game Starts.''', 'Ultimate Coin Collector Instructions')
    sleep(2)
    pass
speed = int(prompt('Please Enter Your Preferred Speed', 'Your Preferred Speed', 'Speed'))


class Sprite(turtle.Turtle):
    def __init__(self, shape, color, start_x, start_y, shapesize=1):
        super().__init__(shape)
        self.speed = speed
        self.up()
        self.shapesize(shapesize)
        self.shape(shape)
        self.color(color)
        self.goto(start_x, start_y)

    def move(self):
        self.up()
        self.fd(self.speed)
        if self.xcor() >= 270 or self.ycor() >= 270 or self.xcor() <= -270 or self.ycor() <= -270:
            self.lt(180)

    def is_collided(self, other):
        if self.distance(other.xcor(), other.ycor()) <= 20:
            return True
        else:
            return False


class Player(Sprite):
    def __init__(self, shape, color, start_x, start_y):
        Sprite.__init__(self, shape, color, start_x, start_y)

    def accelerate(self):
        self.speed += 1

    def decelerate(self):
        self.speed -= 1

    def turn_right(self):
        self.rt(45)

    def turn_left(self):
        self.lt(45)

    def reset_pos(self):
        self.goto(0, 0)


class Game(turtle.Turtle):
    def __init__(self):
        self.goal = 0
        super().__init__()

    def draw_border(self):
        self.speed(0)
        self.ht()
        self.color('white')
        self.up()
        self.goto(280, -280)
        self.down()
        for i in range(4):
            self.lt(90)
            self.fd(570)

    def write_all(self):
        global level
        self.undo()
        self.up()
        self.goto(-300, 300)
        self.down()
        if level == 1:
            self.goal = 10
        elif level == 2:
            self.goal = 15
        else:
            self.goal = 20
        if score == self.goal:
            level += 1
        self.write(f'SCORE: {score} LIVES: {lives} LEVEL: {level} GOAL: {self.goal}', font=('New Times Roman', 20, 'bold'))


class Coin(Sprite):
    def __init__(self, shape):
        Sprite.__init__(self, shape, 'gold', randint(-260, 260), randint(-260, 260))


class Enemy(Player):
    def __init__(self):
        Player.__init__(self, 'circle', 'red', randint(-260, 260), randint(-260, 260))
        self.rt(randint(45, 180))


p1 = Player('triangle', 'white', 0, 0)
c = Coin('circle')
p1.shapesize(stretch_wid=0.5, stretch_len=1.3)
e0 = Enemy()
e1 = Enemy()
e2 = Enemy()
g = Game()
g.draw_border()
g.write_all()
s.onkey(p1.accelerate, 'Up')
s.onkey(p1.decelerate, 'Down')
s.onkey(p1.turn_right, 'Right')
s.onkey(p1.turn_left, 'Left')
s.listen()
while True:
    p1.move()
    e0.move()
    e1.move()
    e2.move()
    if p1.is_collided(c) and c.is_collided(p1):
        score += 1
        g.write_all()
        x = randint(-260, 260)
        y = randint(-260, 260)
        c.goto(x, y)
    if p1.is_collided(e0) and e0.is_collided(p1) or p1.is_collided(e1) and \
            e1.is_collided(p1) or p1.is_collided(e2) and e2.is_collided(p1):
        lives -= 1
        x = randint(-260, 260)
        y = randint(-260, 260)
        e0.goto(x, y)
        e1.goto(x, y)
        e2.goto(x, y)
        g.write_all()
    if lives == 0:
        alert('You Died', 'END OUTCOME', button='OK')
        break
    elif score == 20:
        alert('You Won!', 'END OUTCOME', button='OK')
        break
    elif score == 20 and lives == 10:
        alert('WOW!! You Made It To The End Without Losing Even 1 Life!!', 'END OUTCOME', button='OK')
