import Tkinter as tk
from PIL import ImageTk, Image
window = tk.Tk()
window.title('Metaimage')
window.geometry('1000x700')

var = tk.StringVar()
var2 = tk.StringVar()

frm = tk.Frame(window)
frm.pack()
frm_l = tk.Frame(frm,)
frm_r = tk.Frame(frm)
frm_l.pack(side = 'left')
frm_r.pack(side='right')
l = tk.Label(frm_l,textvariable = var,bg='green',
	font=('Arial',12),width=15,height=2)
l.pack()

on_hit = False

def hit_me():
	global on_hit
	if on_hit==False:
		on_hit = True
		var.set('Metaimage')
	else:
		on_hit = False
		var.set('')

b = tk.Button(frm_l,text='hit me',width=15,
	height=2, command=hit_me)
b.pack()

ll = tk.Label(frm_l,text='', bg='yellow',
	font=('Arial',12),width=15,height=2)
ll.pack()

counter = 0

def do_job():
	global counter
	ll.config(text='do '+str(counter))
	counter +=1

e = tk.Entry(frm_l,show='*')
e.pack()

def insert_point():
	var1 = e.get()
	t.insert('insert',var1)
def insert_end():
	var1 = e.get()
	t.insert('end',var1)

b1 = tk.Button(frm_l,text='insert point',width = 15,
	height = 2, command=insert_point)
b1.pack()

b2 = tk.Button(frm_l,text='insert end',width = 15,
	height = 2, command=insert_end)
b2.pack()

t = tk.Text(frm_l,height = 2)
t.pack()

def print_selection():
	value=lb.get(lb.curselection())
	var2.set(value)


l1 = tk.Label(frm_l,bg='red',width = 4,textvariable = var2)
l1.pack()

b3 = tk.Button(frm_l,text='Print Selection',width = 15,
	height = 2, command=print_selection)
b3.pack()

var3 = tk.StringVar()
var3.set((11,22,33,44))
lb = tk.Listbox(frm_l,listvariable=var3)
list_items=[1,2,3,4]
for item in list_items:
	lb.insert('end',item)
lb.insert(1,'Hao')

lb.pack()

canvas = tk.Canvas(frm_r,bg='blue',height=600,width=500)
image_file = tk.PhotoImage(file='C:/Users/Hao Zou/Documents/vipearthquake/static/images/b.gif')
image = canvas.create_image(0,0,anchor='nw',image=image_file)
canvas.pack()

def moveit():
	canvas.move(image,0,2)
	
b4 = tk.Button(frm_r,text='move',width = 15,
	height = 2, command=moveit)
b4.pack()

path = "C:/Users/Hao Zou/Documents/vipearthquake/static/images/A.jpg"

#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img = ImageTk.PhotoImage(Image.open(path))

#The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = tk.Label(frm_l, image = img)

#The Pack geometry manager packs widgets in rows or columns.
panel.pack(side = "left", fill = "both", expand = "no")



menubar = tk.Menu(window)
filemenu = tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label='File',menu=filemenu)
filemenu.add_command(label='New',command=do_job)
filemenu.add_command(label='Open',command=do_job)
filemenu.add_command(label='Save',command=do_job)
filemenu.add_separator()
filemenu.add_command(label='Exit',command=window.quit)


editmenu = tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label='Edit',menu=editmenu)
editmenu.add_command(label='Cut',command=do_job)
editmenu.add_command(label='Copy',command=do_job)
editmenu.add_command(label='Paste',command=do_job)

submenu = tk.Menu(filemenu)
filemenu.add_cascade(label='Import',menu=submenu,underline=0)
submenu.add_command(label='submenu1',command=do_job)

window.config(menu=menubar)

window.mainloop()


#import os 
#filename = input("Please enter your filename: ").strip()

#for root,dirs,files in os.walk(filename): 

 #   for filespath in files: 

      #print(os.path.join(root,filespath))
