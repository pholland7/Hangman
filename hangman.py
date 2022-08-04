import turtle
import requests
import random

website = "https://www.mit.edu/~ecprice/wordlist.10000"
r = requests.get(website)

WORDS = r.content.splitlines()
WIDTH = 800
HEIGHT = 800
DELAY = 2500


def bindKeys():
    screen.onkey(lambda: guess("a"), "a")
    screen.onkey(lambda: guess("b"), "b")
    screen.onkey(lambda: guess("c"), "c")
    screen.onkey(lambda: guess("d"), "d")
    screen.onkey(lambda: guess("e"), "e")
    screen.onkey(lambda: guess("f"), "f")
    screen.onkey(lambda: guess("g"), "g")
    screen.onkey(lambda: guess("h"), "h")
    screen.onkey(lambda: guess("i"), "i")
    screen.onkey(lambda: guess("j"), "j")
    screen.onkey(lambda: guess("k"), "k")
    screen.onkey(lambda: guess("l"), "l")
    screen.onkey(lambda: guess("m"), "m")
    screen.onkey(lambda: guess("n"), "n")
    screen.onkey(lambda: guess("o"), "o")
    screen.onkey(lambda: guess("p"), "p")
    screen.onkey(lambda: guess("q"), "q")
    screen.onkey(lambda: guess("r"), "r")
    screen.onkey(lambda: guess("s"), "s")
    screen.onkey(lambda: guess("t"), "t")
    screen.onkey(lambda: guess("u"), "u")
    screen.onkey(lambda: guess("v"), "v")
    screen.onkey(lambda: guess("w"), "w")
    screen.onkey(lambda: guess("x"), "x")
    screen.onkey(lambda: guess("y"), "y")
    screen.onkey(lambda: guess("z"), "z")
    screen.onkey(lambda: guess("a"), "A")
    screen.onkey(lambda: guess("b"), "B")
    screen.onkey(lambda: guess("c"), "C")
    screen.onkey(lambda: guess("d"), "D")
    screen.onkey(lambda: guess("e"), "E")
    screen.onkey(lambda: guess("f"), "F")
    screen.onkey(lambda: guess("g"), "G")
    screen.onkey(lambda: guess("h"), "H")
    screen.onkey(lambda: guess("i"), "I")
    screen.onkey(lambda: guess("j"), "J")
    screen.onkey(lambda: guess("k"), "K")
    screen.onkey(lambda: guess("l"), "L")
    screen.onkey(lambda: guess("m"), "M")
    screen.onkey(lambda: guess("n"), "N")
    screen.onkey(lambda: guess("o"), "O")
    screen.onkey(lambda: guess("p"), "P")
    screen.onkey(lambda: guess("q"), "Q")
    screen.onkey(lambda: guess("r"), "R")
    screen.onkey(lambda: guess("s"), "S")
    screen.onkey(lambda: guess("t"), "T")
    screen.onkey(lambda: guess("u"), "U")
    screen.onkey(lambda: guess("v"), "V")
    screen.onkey(lambda: guess("w"), "W")
    screen.onkey(lambda: guess("x"), "X")
    screen.onkey(lambda: guess("y"), "Y")
    screen.onkey(lambda: guess("z"), "Z")


def unbindKeys():
    screen.onkey(None, "a")
    screen.onkey(None, "b")
    screen.onkey(None, "c")
    screen.onkey(None, "d")
    screen.onkey(None, "e")
    screen.onkey(None, "f")
    screen.onkey(None, "g")
    screen.onkey(None, "h")
    screen.onkey(None, "i")
    screen.onkey(None, "j")
    screen.onkey(None, "k")
    screen.onkey(None, "l")
    screen.onkey(None, "m")
    screen.onkey(None, "n")
    screen.onkey(None, "o")
    screen.onkey(None, "p")
    screen.onkey(None, "q")
    screen.onkey(None, "r")
    screen.onkey(None, "s")
    screen.onkey(None, "t")
    screen.onkey(None, "u")
    screen.onkey(None, "v")
    screen.onkey(None, "w")
    screen.onkey(None, "x")
    screen.onkey(None, "y")
    screen.onkey(None, "z")
    screen.onkey(None, "A")
    screen.onkey(None, "B")
    screen.onkey(None, "C")
    screen.onkey(None, "D")
    screen.onkey(None, "E")
    screen.onkey(None, "F")
    screen.onkey(None, "G")
    screen.onkey(None, "H")
    screen.onkey(None, "I")
    screen.onkey(None, "J")
    screen.onkey(None, "K")
    screen.onkey(None, "L")
    screen.onkey(None, "M")
    screen.onkey(None, "N")
    screen.onkey(None, "O")
    screen.onkey(None, "P")
    screen.onkey(None, "Q")
    screen.onkey(None, "R")
    screen.onkey(None, "S")
    screen.onkey(None, "T")
    screen.onkey(None, "U")
    screen.onkey(None, "V")
    screen.onkey(None, "W")
    screen.onkey(None, "X")
    screen.onkey(None, "Y")
    screen.onkey(None, "Z")


def drawInitializer(initial):
    initial.shape("square")
    initial.color(0, 0, 0)
    initial.pensize(10)
    initial.penup()


def guess(char):
    if char in mysteryWord and char not in guessedLetters:
        addLetter(char)
    elif char not in guessedLetters:
        addBodyPart(char)


def addLetter(char):
    global notGuessed
    guessedLetters.append(char)
    x = -len(unguessedList) * 20
    guessDrawer.goto(x, -200)
    for ch in mysteryWord:
        guessDrawer.goto(x, -190)
        if ch == char:
            guessDrawer.pendown()
            guessDrawer.write(ch, font=("Comic Sans MS", 16, "normal"))
            guessDrawer.penup()
            notGuessed += char
        x += 40
    if len(notGuessed) == len(mysteryWord):
        letterGuessDrawer.goto(0, 200)
        letterGuessDrawer.pendown()
        letterGuessDrawer.write("You won!", align="center", font=("Comic Sans MS", 16, "normal"))
        letterGuessDrawer.penup()
        unbindKeys()
        turtle.ontimer(newGame, DELAY)


def addBodyPart(char):
    global guessX
    guessedLetters.append(char)
    incorrectGuess.append(char)
    letterGuessDrawer.pendown()
    letterGuessDrawer.write(char, font=("Comic Sans MS", 16, "normal"))
    letterGuessDrawer.penup()
    guessX += 15
    letterGuessDrawer.goto(guessX, 100)
    if len(incorrectGuess) == 1:
        drawer.goto(-50, 90)
        drawer.pendown()
        drawer.circle(15)
        drawer.penup()
    elif len(incorrectGuess) == 2:
        drawer.goto(-50, 85)
        drawer.pendown()
        drawer.goto(-50, 20)
        drawer.penup()
    elif len(incorrectGuess) == 3:
        drawer.goto(-50, 60)
        drawer.pendown()
        drawer.goto(-70, 70)
        drawer.penup()
    elif len(incorrectGuess) == 4:
        drawer.goto(-50, 60)
        drawer.pendown()
        drawer.goto(-30, 70)
        drawer.penup()
    elif len(incorrectGuess) == 5:
        drawer.goto(-50, 20)
        drawer.pendown()
        drawer.goto(-70, -20)
        drawer.penup()
    elif len(incorrectGuess) == 6:
        drawer.goto(-50, 20)
        drawer.pendown()
        drawer.goto(-30, -20)
        drawer.penup()
    if guessX >= 115:
        letterGuessDrawer.goto(0, 200)
        letterGuessDrawer.pendown()
        letterGuessDrawer.write(f"You lost! The word was {mysteryWord}.", align="center",
                                font=("Comic Sans MS", 16, "normal"))
        letterGuessDrawer.penup()
        unbindKeys()
        turtle.ontimer(newGame, DELAY)


def getNewWord():
    global mysteryWord, notGuessed, guessedLetters, unguessedList, incorrectGuess
    guessedLetters = []
    mysteryWord = WORDS[random.randint(0, 10000)].decode('utf-8')
    unguessedList = []
    incorrectGuess = []
    notGuessed = ""
    for ch in mysteryWord:
        unguessedList.append("")


def newGame():
    global guessX
    bindKeys()
    getNewWord()
    letterGuessDrawer.clear()
    guessDrawer.clear()
    drawer.clear()
    drawer.goto(-200, -50)
    drawer.pendown()
    drawer.goto(-100, -50)
    drawer.penup()
    drawer.goto(-150, -50)
    drawer.pendown()
    drawer.goto(-150, 150)
    drawer.goto(-50, 150)
    drawer.goto(-50, 120)
    drawer.penup()

    x = -len(unguessedList) * 20
    guessDrawer.goto(x, -200)
    for ch in unguessedList:
        guessDrawer.goto(x, -200)
        guessDrawer.pendown()
        guessDrawer.write("_", font=("Comic Sans MS", 16, "normal"))
        guessDrawer.penup()
        x += 40
    guessDrawer.goto(0, -300)
    guessDrawer.write("Enter a letter to guess!", align="center", font=("Comic Sans MS", 16, "normal"))
    guessDrawer.penup()

    letterGuessDrawer.goto(25, 120)
    letterGuessDrawer.pendown()
    letterGuessDrawer.write("Incorrect Guesses: ", font=("Comic Sans MS", 16, "normal"))
    letterGuessDrawer.penup()
    letterGuessDrawer.goto(25, 100)
    guessX = 25


screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("Hangman")
turtle.colormode(255)
screen.bgcolor(112, 158, 230)
screen.tracer(0)

screen.listen()

drawer = turtle.Turtle()
drawInitializer(drawer)

guessDrawer = turtle.Turtle()
drawInitializer(guessDrawer)

letterGuessDrawer = turtle.Turtle()
drawInitializer(letterGuessDrawer)

newGame()

turtle.done()
