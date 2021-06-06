from tkinter import *
from tkinter import messagebox
# create root window
root = Tk()
 

root.title("Travel app")
l = Label(root, text = "The information about the equipment for the travel")
l.pack(ipadx=10, ipady=50)
l.config(font =("Arial", 20))
root.geometry('600x600')
 

def frame_sentence():
    name = int(name_Tf.get())
    if (name=='' ) and (CheckVar1.get()==0) and (CheckVar2.get()==0) and  (CheckVar3.get()==0) and (CheckVar4.get()==0):
         return messagebox.showinfo('message',f'Please fullfill both inputs (kilometres and season type')
    elif (name ==100) and (CheckVar1.get()==1) and (CheckVar2.get()==0) and  (CheckVar3.get()==0) and (CheckVar4.get()==0):
        text.insert('1.0',f'You have to pick up 1 umbrella, 1 jacket, 1 boots, 1 autumn sweater, 1 autumn jeans, 1  autumn coat, 5 bottles of water, 1 tent, 2 packs of launches, 1 pack of snacks')
    elif (name ==100) and (CheckVar1.get()==0) and (CheckVar2.get()==1) and  (CheckVar3.get()==0) and (CheckVar4.get()==0):
        text.insert('1.0',f'You have to pick up 1 jacket, 1 hat, 1 jeans, 1 powerbank, 5 bottles of water, 1 medication box, ')
    elif (name  ==100) and (CheckVar1.get()==0) and (CheckVar2.get()==0) and  (CheckVar3.get()==1) and (CheckVar4.get()==0):
        text.insert('1.0',f'You have to pick up 2 down jackets, 1 hat, 2 scarf,  2 thermals, 2 scarves, 2 pairs of boots, 1 thermos flask, 1 portable humidifier, 6 bottles of water, 1 medication box, 1 pair of boots, 2 pairs of gloves, 1 tent, 2 packs of launches, 1 pack of snacks')
    elif (name ==100) and (CheckVar1.get()==0) and (CheckVar2.get()==0) and  (CheckVar3.get()==0) and (CheckVar4.get()==1):
        text.insert('1.0',f'You have to pick up 7 bottles of water, 2 shorts, 2 T-shirts,  1 powerbank, 1 headphones, 1 tent,  1 jeans, 1 bed-in-a-bag, 1 hat, 1 medication box, 1 back-pack, 2 packs of lunches, 1 pack of snacks, 1 pair sports shoes, 1 set of cards, 1 umbrella')
    elif (name <100) and (CheckVar1.get()==1) and (CheckVar2.get()==0) and  (CheckVar3.get()==0) and (CheckVar4.get()==0):
        text.insert('1.0',f'You have to pick up 1 umbrella, 1 jacket, 1 boots, 1 autumn sweater, 1 autumn jeans, 1  autumn coat, 4 bottles of water, 1 tent, 1 pack of launches, 1 pack of snacks')
    elif (name <100) and (CheckVar1.get()==0) and (CheckVar2.get()==1) and  (CheckVar3.get()==0) and (CheckVar4.get()==0):
        text.insert('1.0',f'You have to pick up 1 jacket, 1 hat, 1 jeans, 1 powerbank, 4 bottles of water, 1 medication box, 1 pack of snack, 1 pack of launches ')
    elif (name  <100) and (CheckVar1.get()==0) and (CheckVar2.get()==0) and  (CheckVar3.get()==1) and (CheckVar4.get()==0):
        text.insert('1.0',f'You have to pick up 1 down jackets, 1 hat, 1 scarf,  1 thermals, 1 scarves, 1 pairs of boots, 1 thermos flask, 1 portable humidifier, 4 bottles of water, 1 medication box, 1 pair of boots, 2 pairs of gloves, 1 tent, 1 pack of launches, 1 pack of snacks')
    elif (name <100) and (CheckVar1.get()==0) and (CheckVar2.get()==0) and  (CheckVar3.get()==0) and (CheckVar4.get()==1):
        text.insert('1.0',f'You have to pick up 6 bottles of water, 1 shorts, 1 T-shirts,  1 powerbank, 1 headphones, 1 tent,  1 jeans, 1 bed-in-a-bag, 1 hat, 1 medication box, 1 back-pack, 2 packs of lunches, 1 pack of snacks,  1 pair sports shoes, 1 set of cards, 1 umbrella')
    elif (name >100) and (CheckVar1.get()==1) and (CheckVar2.get()==0) and  (CheckVar3.get()==0) and (CheckVar4.get()==0):
        text.insert('1.0',f'You have to pick up 1 umbrella, 1 jacket, 1 boots, 1 autumn sweater, 1 autumn jeans, 1  autumn coat, 6 bottles of water, 1 tent, 1 passport, 3 packs of launches,   1 pack of snacks')
    elif (name >100) and (CheckVar1.get()==0) and (CheckVar2.get()==1) and  (CheckVar3.get()==0) and (CheckVar4.get()==0):
        text.insert('1.0',f'You have to pick up 1 jacket, 1 hat, 1 jeans, 1 powerbank, 6 bottles of water, 1 medication box, 1 passport, 4 packs of launches, 2 packs of snacks')
    elif (name >100) and (CheckVar1.get()==0) and (CheckVar2.get()==0) and  (CheckVar3.get()==1) and (CheckVar4.get()==0):
        text.insert('1.0',f'You have to pick up 1 down jackets, 1 hat, 1 scarf,  1 thermals, 1 scarves, 1 pairs of boots, 1 thermos flask, 1 portable humidifier, 6 bottles of water, 1 medication box, 1 pair of boots, 2 pairs of gloves, 1 tent, 1 passport, 4 packs of launches, 2 packs of snacks')
    elif (name > 100) and (CheckVar1.get()==0) and (CheckVar2.get()==0) and  (CheckVar3.get()==0) and (CheckVar4.get()==1):
        text.insert('1.0',f'You have to pick up 8 bottles of water, 1 shorts, 1 T-shirts,  1 powerbank, 1 headphones, 1 tent,  1 jeans, 1 bed-in-a-bag, 1 hat, 1 medication box, 1 back-pack, 2 packs of lunches, 1 pack of snacks, 1 pair sports shoes, 1 set of cards, 1 umbrella, 1 passport')
    else:
        text.insert('1.0',f'Undefined')

    
def clean():
      text.delete('1.0',"end")

btn = Button(
    root,
    text='Clean text area',
    relief=SOLID,
    command=clean
)
btn.pack(pady=10)

btn = Button(
    root,
    text='Generate the items list',
    relief=SOLID,
    command=frame_sentence
)
btn.pack(pady=10)


text = Text(root, height=8)
text.pack()


def welcomeMessage():
    name = int(name_Tf.get())
    return messagebox.showinfo('message',f'Hi, you have entered the number of kilometres which is {name}')
    
     
label = Label(root, text='The place for selecting years season')
label.pack(ipadx=10, ipady=3)


CheckVar1 = IntVar()
CheckVar2 = IntVar()
CheckVar3 = IntVar()
CheckVar4 = IntVar()
C1 = Checkbutton(root, text = "Autumn", variable = CheckVar1, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 50)
C2 = Checkbutton(root, text = "Spring", variable = CheckVar2, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 50)
C3 = Checkbutton(root, text = "Winter", variable = CheckVar3, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 50)
C4 = Checkbutton(root, text = "Summer", variable = CheckVar4, \
                 onvalue = 1, offvalue = 0, height=0, \
                 width = 50)
C1.pack()
C2.pack()
C3.pack()
C4.pack()


Label(root, text="Please enter the number of kilometres").pack()
name_Tf = Entry(root)
name_Tf.pack()

Button(root, text="Click Here", command=welcomeMessage).pack()


l.pack()
root.mainloop()