
import tkinter


root = tkinter.Tk()
root.title("SINAV")
root.geometry('700x900')
c = 0
label_t = tkinter.Label(root, text="SINAV", font=("arial", 50))
label_t.place(x=600, y=50)

label_u = tkinter.Label(root, text="KULLANICI ADI", font=("arial", 23))
label_u.place(x=250, y=250)

entry = tkinter.Entry(root, font=("arial", 30))
entry.place(x=500, y=250)


def increase():
    global c
    c += 1


def info1():
    global c
    name = entry.get()
    label_q1 = tkinter.Label(root, text="SORU 1", font=("Arial", 35))
    label_q1.place(x=550, y=50)
    label1 = tkinter.Label(root, text="Hangisi Pythonda anahtar kelimedir?", font=("Arial", 30))
    label1.place(x=300, y=100)

    op1 = tkinter.Button(root, text="range", font=("Arial", 20), command=info2)
    op1.place(x=400, y=200)
    op2 = tkinter.Button(root, text="def", font=("Arial", 20), command=lambda: [info2(), increase()])
    op2.place(x=800, y=200)
    op3 = tkinter.Button(root, text="val", font=("Arial", 20), command=info2)
    op3.place(x=400, y=300)
    op4 = tkinter.Button(root, text="to", font=("Arial", 20), command=info2)
    op4.place(x=800, y=300)

    label_t.destroy()
    label_u.destroy()
    entry.destroy()
    button.destroy()


def info2():
    global c, label_q1, label1, op1, op2, op3, op4
    c += 1
    label_q2 = tkinter.Label(root, text="SORU 2", font=("Arial", 35))
    label_q2.place(x=550, y=50)
    label2 = tkinter.Label(root, text="Ekrana yazdırılmasını sağlayan komut hangisidir?", font=("Arial", 30))
    label2.place(x=300, y=100)

    opp1 = tkinter.Button(root, text="factorial()", font=("Arial", 20), command=info3)
    opp1.place(x=400, y=200)
    opp2 = tkinter.Button(root, text="print()", font=("Arial", 20), command=lambda: [info3(), increase()])
    opp2.place(x=800, y=200)
    opp3 = tkinter.Button(root, text="seed()", font=("Arial", 20), command=info3)
    opp3.place(x=400, y=300)
    opp4 = tkinter.Button(root, text="sqrt()", font=("Arial", 20), command=info3)
    opp4.place(x=800, y=300)

    label_q1.destroy()
    label1.destroy()
    op1.destroy()
    op2.destroy()
    op3.destroy()
    op4.destroy()


def info3():
    global c, opp1, opp2, opp3, opp4, label_q2, label2
    c += 1
    label_q3 = tkinter.Label(root, text="SORU 3", font=("Arial", 35))
    label_q3.place(x=550, y=50)
    label3 = tkinter.Label(root, text="hangisi Python'daki temel veri türü değildir?",
                           font=("Arial", 37))
    label3.place(x=200, y=100)

    oppp1 = tkinter.Button(root, text="Tuple", font=("Arial", 20), width=8, command=info4)
    oppp1.place(x=400, y=200)
    oppp2 = tkinter.Button(root, text="Dictionary", font=("Arial", 20), width=7, command=info4)
    oppp2.place(x=800, y=200)
    oppp3 = tkinter.Button(root, text="Lists", font=("Arial", 20), width=7, command=info4)
    oppp3.place(x=400, y=300)
    oppp4 = tkinter.Button(root, text="Class", font=("Arial", 20), command=lambda: [info4(), increase()])
    oppp4.place(x=800, y=300)
    opp1.destroy()
    opp2.destroy()
    opp3.destroy()
    opp4.destroy()
    label_q2.destroy()
    label2.destroy()



def info4():
    global c, oppp1, oppp2, oppp3, oppp4, label_q3, label3
    c += 1
    label_q4 = tkinter.Label(root, text="SORU 4", font=("Arial", 38))
    label_q4.place(x=550, y=50)
    label4 = tkinter.Label(root, text="Python programlama dilini kim geliştirdi?", font=("Arial", 40))
    label4.place(x=200, y=100)
   
    opppp1 = tkinter.Button(root, text="Wick Van Rossum", font=("Arial", 20), command=info5)
    opppp1.place(x=400, y=200)
    opppp2 = tkinter.Button(root, text="Rasmus Lerdorf", font=("Arial", 20), command=info5)
    opppp2.place(x=800, y=200)
    opppp3 = tkinter.Button(root, text="Guido Van Rossum", font=("Arial", 20), command=lambda: [info5(), increase()])
    opppp3.place(x=400, y=300)
    opppp4 = tkinter.Button(root, text="Niene Stom", font=("Arial", 20), command=info5)
    opppp4.place(x=800, y=300)

    label_q3.destroy()
    label3.destroy()
    oppp1.destroy()
    oppp2.destroy()
    oppp3.destroy()
    oppp4.destroy()


def info5():
    global c, opppp1, opppp2, opppp3, opppp4, label_q4, label4
    c += 1
    label_q5 = tkinter.Label(root, text="SORU 5", font=("Arial", 38))
    label_q5.place(x=550, y=50)
    label5 = tkinter.Label(root, text="     hangisi Python dosyasının uzantısıdır?",
                           font=("Arial", 41))
    label5.place(x=150, y=100)

    oppppp1 = tkinter.Button(root, text=".python", font=("Arial", 20), width=15, command=info6)
    oppppp1.place(x=400, y=200)
    oppppp2 = tkinter.Button(root, text=".p", font=("Arial", 20), width=13, command=info6)
    oppppp2.place(x=800, y=200)
    oppppp3 = tkinter.Button(root, text=".pl", font=("Arial", 20), width=16, command=info6)
    oppppp3.place(x=400, y=300)
    oppppp4 = tkinter.Button(root, text=".py", font=("Arial", 20), width=10, command=lambda: [info6(), increase()])
    oppppp4.place(x=800, y=300)

    label_q4.destroy()
    label4.destroy()
    opppp1.destroy()
    opppp2.destroy()
    opppp3.destroy()
    opppp4.destroy()


def info6():
    global c, name, label_q6, label6, labell6, oppppp1, oppppp2, oppppp3, oppppp4, label_q5, label5
    label_q6 = tkinter.Label(root, text="SCORE", font=("Arial", 38), width=10)
    label_q6.place(x=550, y=50)
    label6 = tkinter.Label(root, text=name, font=("Arial", 35))
    label6.place(x=150, y=200)
    labell6 = tkinter.Label(root, text=f"Score: {c}", font=("Arial", 30))
    labell6.place(x=400, y=450)  

    
    label_q5.destroy()
    label5.destroy()


button = tkinter.Button(root, text="ENTER", font=("arial", 30), command=info1)
button.place(x=600, y=350)
root.mainloop()