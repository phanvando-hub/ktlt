print("Ho va ten: Phan Van Do")
print("MSSV: 205752020710012")

impor= tkinter
Import= random
colours ('Red', 'Blue', 'Green', 'Pink', 'Black',
         'Yellow', "Orange", "White", "Purple", "Brown")
score =0
timeleft=30
def startGame (event):
    if timeleft== 30:
        countdown()
    nextColour()
def nextColour():
    global score
    global timeleft
    if timeleft > 0:
        e.focus_set()
    if.e.get().lower()== colours[1].lower():
        acore+= 1
    e.delete(0, tkinter. END)
    random.shuffle (colours)
    label.config(fg =str(colours[1]), text= str (colours[0]))
    scoreLabel.config(text= "Score: "+ str(score))
def countdown():
    global timeleft
    if timeleft> 0:
        timeleft-=1
        timeLabel.config(text "Time left:" + str(timeleft))
        timeLabel.after(1000, countdown)
root= tkinter.Tk()
root.title("COLORGAME")
root.geometry("375x200")
instructions tkinter. Label (root, text = "Type in the colour of the )
                            "and not the word text", font('Helvet)
instructions.pack()
scoreLabel tkinter.Label (root, text "Fress enter to start"
                        ,font= ('Helvetica', 12))
scoreLabel.pack()
                                                          
timeLabel tkinter. Label (root, text "Time left: "
                        +str(timeleft), font (Helvetica', 12))
timeLabel.pack()
label tkinter.Label (root, font('Helvetica', 60))
label.pack()
eckinter. Entry (root)
root.bind('<Return>', startGame)
e.pack()
e.focus set()
root.mainloop()

