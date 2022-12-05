import tkinter
from tkinter import *
import random
from tkinter import messagebox
import pyttsx3
import speech_recognition as sr
from PIL import Image,ImageTk
import win32gui, win32con
import ctypes

#This line of code hides the command prompt upon launch
ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 6 )

#You can add more words as per your requirement
#These are the lists of words, pictures, coordinates for the pictures, and clues. Their indicies correspond with each other

answers = [
    "basement",
    "restaurant",
    "school",
    "garden",
    "car",
    "gym",
    "bathroom",
    "living room",
    "kitchen",
    "bedroom",
    "home"
]

photos = [
    "Pictures/basement.jpg",
    "Pictures/restaurant.jpg",
    "Pictures/school.jpg",
    "Pictures/garden.jpg",
    "Pictures/car.jpg",
    "Pictures/gym.jpg",
    "Pictures/bathroom.jpg",
    "Pictures/livingroom.jpg",
    "Pictures/kitchen.jpg",
    "Pictures/bedroom.jpg",
    "Pictures/home.jpg"
]


pos = [
    [475,114.5],
    [250,144],
    [314,144],
    [601,172],
    [569,200.75],
    [411,229.5],
    [536.5,229.5],
    [94,258.25],
    [411,314],
    [411,371.5],
    [475,429]
]

words = [
    "Lower floor of a house",
    "A place to go to eat outside",
    "A place for learning",
    "Where flowers grow outside the house",
    "Something you use to travel",
    "A place to workout",
    "The room with a shower",
    "A room that can be used to relax",
    "The room for cooking",
    "The room for sleeping",
    "Where you live"    
]

#This generates a random clue to start off with
num =  random.randrange(0, len(words), 1)

points = 0

#The default function prints out that random clue
def default():
    global words,answers,num
    lbl.config(text = words[num])
    
#Resets the Crossword Puzzle Worksheet and the points variable
def res():
    global words,answers,num, points
    points = 0
    e1.delete(0, END)
    my_image = Image.open('Pictures/Crossword Puzzle Worksheet.jpg')
    my_imager = ImageTk.PhotoImage(my_image)
    my_image_label = Label(image=my_imager)
    my_image_label.image = my_imager
    my_image_label.place(x=0, y=0)

#The down and across functions print out a specific clue from the words list, and that clue corresponds to the num integer.
def down1():
    global words,answers,num
    num = 0
    lbl.config(text = words[num])
    e1.delete(0, END)

def cross2():
    global words,answers,num
    num = 1
    lbl.config(text = words[num])
    e1.delete(0, END)

def down3():
    global words,answers,num
    num = 2
    lbl.config(text = words[num])
    e1.delete(0, END)

def down4():
    global words,answers,num
    num = 3
    lbl.config(text = words[num])
    e1.delete(0, END)

def cross5():
    global words,answers,num
    num = 4
    lbl.config(text = words[num])
    e1.delete(0, END)

def cross6():
    global words,answers,num
    num = 5
    lbl.config(text = words[num])
    e1.delete(0, END)

def down7():
    global words,answers,num
    num = 6
    lbl.config(text = words[num])
    e1.delete(0, END)

def cross8():
    global words,answers,num
    num = 7
    lbl.config(text = words[num])
    e1.delete(0, END)

def cross9():
    global words,answers,num
    num = 8
    lbl.config(text = words[num])
    e1.delete(0, END)

def cross10():
    global words,answers,num
    num = 9
    lbl.config(text = words[num])
    e1.delete(0, END)

def cross11():
    global words,answers,num
    num = 10
    lbl.config(text = words[num])
    e1.delete(0, END)

#This function checks if the inputed word is correct and prints out a statement corresponding to if the answer is correct or not.
#It converts the text into speech.
#It also adds 1 to the points variable and if the points variable reaches 11 it prints out a statement.
def checkans():
    global words,answers,num, points
    var = e1.get()
    audio = pyttsx3.init()
    audio.setProperty('rate', 125)
    audio.say(var)
    audio.runAndWait()
    if var == answers[num]:
        points += 1
        messagebox.showinfo("Success", "This is a correct answer")
        correct = Image.open(photos[num])
        correctk = ImageTk.PhotoImage(correct)
        correct_label = Label(image=correctk)
        correct_label.image = correctk
        correct_label.place(x = pos[num][0], y = pos[num][1])
        relief = FLAT
        if points == len(answers):
            messagebox.showinfo("Congratulations!", "You've completed the cross word.")            
    else:
        messagebox.showerror("Incorrect Answer", "Please try again")
        e1.delete(0, END)

#Converts speech to text, and inserts what you said into the textbox.
def audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("say something!")
        speech = r.listen(source)

    try:
        text = r.recognize_google(speech)
        lower = text.lower()
        e1.insert(END, lower)
    except:
        print("Try again")

#This replaces the original tkinter icon with an icon of your choice, and also created a window for the crossword puzzle worksheet
window = Tk()
window.geometry("750x850+400+300")
window.iconbitmap('Pictures/Crossword Puzzle Icon.ico')
window.title("Crossword Puzzle")

#This inserts the crossword puzzle board into the crossword puzzle window
my_image = Image.open('Pictures/Crossword Puzzle Worksheet.jpg')
my_imager = ImageTk.PhotoImage(my_image)
my_image_label = Label(image=my_imager)
my_image_label.image = my_imager
my_image_label.place(x=0, y=0)

#This generates the main window
root = tkinter.Toplevel()
root.geometry("550x650+400+300")
root.title("Crosspeech")
root.configure(background = "orange")
root.iconbitmap('Pictures/Crossword Puzzle Icon.ico')


#Generates a square at the very top which allows the clue text to be visible, and also creates a border behind the clue text.
lbl = Label(
    root,
    text = "Your Here",
    font = ("Verdana", 18),
    bg = "orange",
    fg = "#000000",
)
lbl.pack(pady = 30,ipady=10,ipadx=10)

#This creates a box where you can insert text through typing or through speech to text
ans1 = StringVar()

e1 = Entry(
    root,
    font = ("Verdana", 16),
    textvariable = ans1,
)
e1.pack(ipady=5,ipadx=5)

#This generates a button that you can click to command the checkans function to run.
btncheck = Button(
    root,
    text = "Check",
    font = ("Comic sans ms", 16),
    width = 16,
    bg = "#4c4b4b",
    fg = "#6ab04c",
    relief = GROOVE,
    command = checkans,
)
btncheck.pack(pady = 20)


#This generates a button that you can click to record input from a microphone and convert it into text (Speech to text)
btnaudio = Button(root, text = 'Record', command =lambda:audio(), font = ("Comic sans ms", 16),
    width = 16, height=1,
    bg = "#4c4b4b",
    fg = "#ADD8E6",
    relief = GROOVE
    )
btnaudio.pack()

#btn1 to btn11 generate buttons that you can click, and each button number corresponds to across#, or down# functions.
#If the button is clicked it commands its corresponding function to run
btn1 = Button(
    root,
    text = "Down 1",
    font = ("Comic sans ms", 10),
    width = 8,
    height=1,
    bg = "#4c4b4b",
    fg = "#EA425C",
    relief = GROOVE,
    command = down1
    )
btn1.pack(pady = 20)
btn1.place(x = 165, y = 310)


btn2 = Button(
    root,
    text = "Across 2",
    font = ("Comic sans ms", 10),
    width = 8,
    height=1,
    bg = "#4c4b4b",
    fg = "#EA425C",
    relief = GROOVE,
    command = cross2
    )
btn2.pack(pady = 20)
btn2.place(x = 310, y = 310)

btn3 = Button(
    root,
    text = "Down 3",
    font = ("Comic sans ms", 10),
    width = 8,
    height=1,
    bg = "#4c4b4b",
    fg = "#EA425C",
    relief = GROOVE,
    command = down3
    )
btn3.pack(pady = 20)
btn3.place(x = 165, y = 355)

btn4 = Button(
    root,
    text = "Down 4",
    font = ("Comic sans ms", 10),
    width = 8,
    height=1,
    bg = "#4c4b4b",
    fg = "#EA425C",
    relief = GROOVE,
    command = down4
    )
btn4.pack(pady = 20)
btn4.place(x = 165, y = 400)

btn5 = Button(
    root,
    text = "Across 5",
    font = ("Comic sans ms", 10),
    width = 8,
    height=1,
    bg = "#4c4b4b",
    fg = "#EA425C",
    relief = GROOVE,
    command = cross5
    )
btn5.pack(pady = 20)
btn5.place(x = 310, y = 355)

btn6 = Button(
    root,
    text = "Across 6",
    font = ("Comic sans ms", 10),
    width = 8,
    height=1,
    bg = "#4c4b4b",
    fg = "#EA425C",
    relief = GROOVE,
    command = cross6
    )
btn6.pack(pady = 20)
btn6.place(x = 310, y = 400)

btn7 = Button(
    root,
    text = "Down 7",
    font = ("Comic sans ms", 10),
    width = 8,
    height=1,
    bg = "#4c4b4b",
    fg = "#EA425C",
    relief = GROOVE,
    command = down7
    )
btn7.pack(pady = 20)
btn7.place(x = 165, y = 445)

btn8 = Button(
    root,
    text = "Across 8",
    font = ("Comic sans ms", 10),
    width = 8,
    height=1,
    bg = "#4c4b4b",
    fg = "#EA425C",
    relief = GROOVE,
    command = cross8
    )
btn8.pack(pady = 20)
btn8.place(x = 310, y = 445)

btn9 = Button(
    root,
    text = "Across 9",
    font = ("Comic sans ms", 10),
    width = 8,
    height=1,
    bg = "#4c4b4b",
    fg = "#EA425C",
    relief = GROOVE,
    command = cross9
    )
btn9.pack(pady = 20)
btn9.place(x = 310, y = 490)

btn10 = Button(
    root,
    text = "Across 10",
    font = ("Comic sans ms", 10),
    width = 8,
    height=1,
    bg = "#4c4b4b",
    fg = "#EA425C",
    relief = GROOVE,
    command = cross10
    )
btn10.pack(pady = 20)
btn10.place(x = 310, y = 535)

btn11 = Button(
    root,
    text = "Across 11",
    font = ("Comic sans ms", 10),
    width = 8,
    height=1,
    bg = "#4c4b4b",
    fg = "#EA425C",
    relief = GROOVE,
    command = cross11
    )
btn11.pack(pady = 20)
btn11.place(x = 310, y = 580)

btnreset = Button(
    root,
    text = "Play Again",
    font = ("Comic sans ms", 16),
    width = 16,
    height=1,
    bg = "#4c4b4b",
    fg = "cyan",
    relief = GROOVE,
    command = res
)
btnreset.pack(pady = 20)
btnreset.place(x = 5, y = 595)

btnreset = Button(
    root,
    text = "Play Again",
    font = ("Comic sans ms", 16),
    width = 16,
    height=1,
    bg = "#4c4b4b",
    fg = "cyan",
    relief = GROOVE,
    command = res
)
btnreset.pack(pady = 20)
btnreset.place(x = 5, y = 595)

#This calls the default function and prints out the desired clue
default()


#This runs our code in an infite loop until you close the window by pressing x. Needed for tkinter to work properly.
root.mainloop()
