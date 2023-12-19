from tkinter import *
import math
from pygame import mixer
import speech_recognition

mixer.init()

def click(value):
    ex = entryField.get()
    ans = ''
    try:
        if value == 'C':
            ex = ex[0:len(ex) - 2]  # start from 0 index
            entryField.delete(0, END)
            entryField.insert(0, ex)
            return

        elif value == 'CE':
            entryField.delete(0, END)

        elif value == '√':
            ans = math.sqrt(eval(ex))

        elif value == 'π':
            ans = math.pi

        elif value == 'cosθ':
            ans = math.cos(math.radians(eval(ex)))

        elif value == 'tanθ':
            ans = math.cos(math.radians(eval(ex)))

        elif value == 'sinθ':
            ans = math.cos(math.radians(eval(ex)))

        elif value == '2π':
            ans = 2 * math.pi

        elif value == 'cosh':
            ans = math.cosh(eval(ex))

        elif value == 'tanh':
            ans = math.cosh(eval(ex))

        elif value == 'sinh':
            ans = math.cosh(eval(ex))

        elif value == chr(8731):
            ans = eval(ex) ** (1 / 3)

        elif value == 'x\u02b8':
            entryField.insert(END, '**')
            return

        elif value == 'x\u00B3':
            ans = eval(ex) ** 3

        elif value == 'x\u00B2':
            ans = eval(ex) ** 2

        elif value == 'log2':
            ans = math.log2(eval(ex))

        elif value == 'deg':
            ans = math.radians(eval(ex))

        elif value == 'e':
            ans = math.e

        elif value == 'log10':
            ans = math.log10(eval(ex))

        elif value == 'x!':
            ans = math.factorial(eval(ex))

        elif value == '÷':
            entryField.insert(END, "/")
            return
        elif value == '+':
            entryField.insert(END, "+")
            return

        elif value == '-':
            entryField.insert(END, "-")
            return

        elif value == '*':
            entryField.insert(END, "*")
            return

        elif value == '=':
            ans = eval(ex)

        else:
            entryField.insert(END, value)
            return

        entryField.delete(0, END)
        entryField.insert(0, ans)

    except SyntaxError:
        pass


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mult(a, b):
    return a * b


def div(a, b):
    return a / b


def mod(a, b):
    return a % b


def lcm(a, b):
    l = math.lcm(a, b)
    return l


def hcf(a, b):
    h = math.gcd(a, b)
    return h


def tan(a):
    t = math.tan(math.radians(a))
    return t


def sin(a):
    s = math.sin(math.radians(a))
    return s


def cos(a):
    c = math.cos(math.radians(a))
    return c


def cosh(a):
    c = math.cosh(a)
    return c


def sinh(a):
    c = math.sinh(a)
    return c


def tanh(a):
    c = math.tanh(a)
    return c


def rootthree(a):
    c = a ** (1 / 3)
    return c


def power(a, b):
    c = a ** b
    return c


def square(a):
    c = a ** 2
    return c


def cube(a):
    c = a ** 3
    return c


def log2(a):
    c = math.log2(a)
    return c


def radian(a):
    c = math.radians(a)
    return c


def degree(a):
    c = math.radians(a)
    return c


def root(a):
    c = math.sqrt(a)
    return c


def log10(a):
    c = math.log10(a)
    return c


def factorial(a):
    a = int(a)
    c = math.factorial(a)
    return c


def pi(a):
    p = a * math.pi
    return p


def e(a):
    p = a * math.e
    return p


operations = {'ADD': add, 'ADDITION': add, 'SUM': add, 'PLUS': add, '+': add,
              'SUBTRACTION': sub, 'MINUS': sub, 'SUBTRACT': sub, '-': sub,
              'PRODUCT': mult, 'MULTIPLICATION': mult, 'INTO': mult,
              'DIVISION': div, 'DIV': div, 'DIVIDE': div,
              'LCM': lcm, 'HCF': hcf,
              'MOD': mod, 'REMAINDER': mod, 'MODULUS': mod,
              'COSS': cos, 'COS': cos, 'CAUSE': cos, 'COSE': cos, 'Cos': cos,
              'SIN': sin, 'SINE': sin, 'SIGN': sin, 'SINN': sin,
              'TAN THETA': tan, 'TAN': tan, 'TANE': tan, 'TEN': tan, '': tan,
              'HYPERBOLA': cosh, 'COS AGE': cosh, 'CAUSE HYPERBOLA': cosh, 'COSS H': cosh, 'HYPERBOLA COS': cosh,
              'SIN H': sin, 'SINE H': sin, 'SIGN AICH': sin, 'SINH': sin,
              'TAN H': tan, 'TANN H': tan, 'TAN AICH': tan,
              'SHIFT ROUTE': rootthree, 'THREE ROUTE': rootthree, 'SHIFT ROOT': rootthree, 'THREE ROOT': rootthree,
              'TOTHEPOWER': power, 'TO THE POWER': power, 'POWER': power,
              'SQUARE': square, 'POWER 2': square, 'POWER TWO': square,
              'CUBE': cube, 'POWER 3': cube, 'POWER THREE': cube,
              'LOG': log2,
              'RADIAN': radian,
              'ROOT': root, 'ROUT': root, '√': root,
              '10 LOG': log10, "LOGTEN": log10, 'TEN LOG': log10, 'TOKTAN': log10,  # hoina
              'FACTORIAL': factorial,
              'DEGREE': degree,
              'PI': pi, 'PIE': pi,
              'E': e,

              }

def findNumbers(t):
    l = []
    for num in t:
        try:
            l.append(float(num))  # detect value and convert into float
        except ValueError:
            pass

    return l


def audio():
    mixer.music.load('Tudo.mp3')
    mixer.music.play()
    sr = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as m:
        try:
            sr.adjust_for_ambient_noise(m, duration=0.2)
            voice = sr.listen(m)  # listening voice
            text = sr.recognize_google(voice)  # coverting voice to text
            temp = text
            if (text.__contains__('into')) == True:
                temp = text.replace("into", "x")
            elif (text.__contains__('division')) == True:
                temp = text.replace("division", "÷")
            print(text)
            mixer.music.load('Tudo2.mp3')
            mixer.music.play()
            text_list = text.split(' ')
            #print(text_list)    #() spliting sentence in words
            for word in text_list:
                if word.upper() in operations.keys():
                    l = findNumbers(text_list)
                    #print(l)   #() display number in float
                    size = len(l)
                    print(size)
                    if size == 2:
                        result = operations[word.upper()](l[0], l[1])  #25=l[0], 5 =l[1]
                        entryField.delete(0, END)
                        entryField.insert(0, temp + "=")
                        entryField.insert(END, result)
                    elif size == 1:
                        print(l)
                        result = operations[word.upper()](l[0])  #
                        entryField.delete(0, END)
                        entryField.insert(0, temp + " = ")
                        entryField.insert(END, result)

                else:
                    pass
        except:
            pass

root = Tk()  # object of the tk() class
root.title('CASIO fx-991ES PLUS')
root.config(bg='dodgerblue3')
root.geometry('680x495+400+200')

entryField = Entry(root, font=('arial', 20, 'bold'), bg='SlateGray1', fg='black', bd=10, width=30)
entryField.grid(row=0, column=0, columnspan=8, rowspan=1)

# Logo Image
logoImage = PhotoImage(file='colorful.png')
logoLabel = Label(root, image=logoImage, bg='dodgerblue3')
logoLabel.grid(row=0, column=0)

# Mic Image
micImage = PhotoImage(file='micro.png')
micButton = Button(root, image=micImage, bd=0, bg='dodgerblue3', activebackground='dodgerblue3', command=audio)
micButton.grid(row=0, column=7)

# Button Work
button_text_list = ["C", "CE", "√", "+", "π", "cosθ", "tanθ", "sinθ", "1", "2", "3", "-",
                    "2π", "cosh", "tanh", "sinh", "4", "5", "6", "*", chr(8731), "x\u02b8",
                    "x\u00B3", "x\u00B2", "7", "8", "9", "÷", "log2", "deg",
                    "rad", "e", "0", ".", "%", "=", "log10", "(", ")", "x!"]
rowvalue = 1
columnvalue = 0
for i in button_text_list:
    button = Button(root, width=5, height=2, bd=2, relief=GROOVE, text=i, bg='dodgerblue3', fg='white',
                    # relief=GROOVE / RAISED / RIDGE /SUNKEN
                    font=('arial', 18, 'bold'), activebackground='snow', command=lambda button=i: click(button))
    button.grid(row=rowvalue, column=columnvalue, pady=1)
    columnvalue = columnvalue + 1
    if columnvalue > 7:
        rowvalue = rowvalue + 1
        columnvalue = 0

root.mainloop()  # Continuos loop
