from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES
from gtts import gTTS
import os 
def change(text="type", src="english", dest="hindi"):
trans=Translator(service_urls=['translate.googleapis.com'])
trans1=trans.translate(text,dest,src)
return trans1.text
def data():
s=combo_sor.get()
d=combo_dest.get()
msg=sor_txt.get(1.0,END)
text_get=change(text=msg,src=s,dest=d)
dest_txt.delete(1.0,END)
dest_txt.insert(END,text_get)
def speak():
txt = dest_txt.get(1.0,END)
myobj = gTTS(text=txt,slow=FALSE)
myobj.save("text.mp3")
os.system("start text.mp3")
root =Tk()
root.title("Translator")
root.geometry("500x700")
lab_text = Label(root, text="Translator",font=("times new roman",40,"bold"))
lab_text.pack()
lab_sor = Label(root,text="Source Text",font=("times new roman",20,"bold"))
lab_sor.pack()
frame = Frame(root).pack(side=BOTTOM)
sor_txt = Text(frame, font=("times new roman",20),wrap=WORD)
sor_txt.place(x=10,y=130,height=200,width=480)
lang_list = list(LANGUAGES.values())
combo_sor = ttk.Combobox(frame,value=lang_list)
combo_sor.place(x=10,y=350,height=20,width=153)
combo_sor.set("English")
button = Button(frame,text="Translate",relief=RAISED,command=data)
button.place(x=173,y=350,height=20,width=153)
combo_dest = ttk.Combobox(frame,value=lang_list)
combo_dest.place(x=336,y=350,height=20,width=153)
combo_dest.set("Hindi")
lab_dest = Label(frame,text="Translated Text",font=("times new roman",20,"bold"))
lab_dest.place(x=100,y=390,height=40,width=300)
speakButton = Button(frame,text=" ",relief=RAISED,command=speak) 🔊
speakButton.place(x=10,y=420,height=20,width=20)
dest_txt = Text(frame,font=("times new roman",20),wrap=WORD)
dest_txt.place(x=10,y=450,height=200,width=480)
root.mainloop()
