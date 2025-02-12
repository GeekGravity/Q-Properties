import tkinter as tk
import tkinter as ttk
from tkinter import ttk
import mysql.connector 
from PIL import Image, ImageTk 

root = tk.Tk()
root.state('zoomed')
root.title('Q-Properties')


mydb = mysql.connector.connect(
    host = '127.0.0.1',
    user = 'root',
    passwd = '2005',
    database ='project1')

trashcan=[]

back='#800000'
front='#F8F2ED'
textc2 = '#800000'
txtc = '#F8F2ED'

# ----SQL------------------------------------------------------------------------------------------
sqname=[]
sqadd=[]
sqroom=[]
sqfloor=[]
sqprice=[]
sqcontact=[]
sqpict = []


cur = mydb.cursor()
cur.execute('select nam from properties')
data = cur.fetchall()
for i in data:
    sqname.append(i[0])

cur.execute('select address from properties')
data = cur.fetchall()
for i in data:
    sqadd.append(i[0])

cur.execute('select area from properties')
data = cur.fetchall()
for i in data:
    sqroom.append(i[0])
cur.execute('select type0 from properties')
data = cur.fetchall()
for i in data:
    sqfloor.append(i[0])
cur.execute('select price from properties')
data = cur.fetchall()
for i in data:
    sqprice.append(i[0])
cur.execute('select contact from properties')
data = cur.fetchall()
for i in data:
    sqcontact.append(i[0])
cur.execute('select pict from properties')
data = cur.fetchall()
for i in data:
    sqpict.append(i[0])


    
# ----Pictures------------------------------------------------------------------------------------------





# ----Scrollbar & Frame 3------------------------------------------------------------------------------------------

frame3 = tk.Frame(root,bg=back)
frame3.place(relx=0,rely=0.35, relwidth=1, relheight=1, anchor='nw')

container = ttk.Frame(frame3)
canvas = tk.Canvas(container, bg='#800000', width=1900, height=655)
scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas)
scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

# ----Content page------------------------------------------------------------------------------------------  

x=len(sqname)





def listem(x):
    
    for i in range(x):
        
        listing = tk.Frame(scrollable_frame, bg=front, width=1900, height=200, relief='raised', bd=7)
        listing.pack(side='bottom')

        listname = ttk.Label(listing, text='Edens Villa', background=front, foreground=textc2, font=('Arial Bold', 18),wraplength=200,justify='center')
        listname.place(relx=0.1, rely=0.5, relwidth=0.13, height=70, anchor='center')

        lsep_frame = tk.Frame(listing, bg=back)
        lsep_frame.place(relx=0.1625, rely=0, relwidth=0.001, relheight=1, anchor='nw')

        listadd = ttk.Label(listing, text='1', background=front, foreground=textc2, font=('Arial', 16),wraplength=250, justify='center')
        listadd.place(relx=0.283, rely=0.5, width=300, height=100, anchor='center')

        lsep_frame2 = tk.Frame(listing, bg=back)
        lsep_frame2.place(relx=0.363, rely=0, relwidth=0.001, relheight=1, anchor='nw')

        listroom = ttk.Label(listing, text='1440 sq.ft  ', background=front, foreground=textc2, font=('Arial', 14),wraplength=300)
        listroom.place(relx=0.44, rely=0.5, relwidth=0.08, height=100, anchor='center')

        lsep_frame3 = tk.Frame(listing, bg=back)
        lsep_frame3.place(relx=0.475, rely=0, relwidth=0.001, relheight=1, anchor='nw')

        listfloor = ttk.Label(listing, text='2 Bed\n1 Bath', background=front, foreground=textc2, font=('Arial', 14),wraplength=300)
        listfloor.place(relx=0.5425 , rely=0.5, width = 200, height=100, anchor='center')

        lsep_frame4 = tk.Frame(listing, bg=back)
        lsep_frame4.place(relx=0.5632, rely=0, relwidth=0.001, relheight=1, anchor='nw')

        listprice = ttk.Label(listing, text='$2590/mo ', background=front, foreground=textc2, font=('Arial', 14),wraplength=250)
        listprice.place(relx=0.635, rely=0.5, width=200, height=100, anchor='center')

        lsep_frame5 = tk.Frame(listing, bg=back)
        lsep_frame5.place(relx=0.675, rely=0, relwidth=0.001, relheight=1, anchor='nw')

        listcontact = ttk.Label(listing, text='55479864 ', background=front, foreground=textc2, font=('Arial', 14),wraplength=250)
        listcontact.place(relx=0.76, rely=0.5, relwidth=0.1, height=100, anchor='center')
        
    
        lsep_frame6 = tk.Frame(listing, bg=back)
        lsep_frame6.place(relx=0.800, rely=0, relwidth=0.001, relheight=1, anchor='nw')

        
        
        listname.config(text=str(sqname[x-1]))
        listadd.config(text=str(sqadd[x-1]))
        listroom.config(text=str(sqroom[x-1]))
        listfloor.config(text=str(sqfloor[x-1]))
        listprice.config(text=str(sqprice[x-1]))
        listcontact.config(text=str(sqcontact[x-1]))

        img= (Image.open(sqpict[x-1]))
        resized_image= img.resize((300,205), Image.Resampling.LANCZOS)
        new_image= ImageTk.PhotoImage(resized_image)
        trashcan.append(new_image)
        label = tk.Label(listing, image = new_image)
        label.place(relx=0.808, rely=0.49,width=350,height=175, anchor='w')
    
        x-=1            

    
    
    container.pack()
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    




def filterclick():
    global scrollable_frame,sqname,sqadd ,sqroom ,sqfloor,sqprice,sqcontact,sqpict

    a = option_var1.get()
    b = option_var2.get()
    c = option_var3.get()
    

    f1 = ''
    f2 = ''
    f3 = ''
    f4 = 0
    f5 = 0

    if a=='West Bay':
        f1=a
    elif a=='The Pearl':
        f1=a    
    elif a=='Al Sadd':
        f1=a
    elif a=='Al Waab':
        f1=a
    elif a=='Lusail':
        f1=a

    if b=='Any':
        f2 = 0
        f3 = 999999
    elif b=='QR.0-QR.19999':
        f2=0
        f3=19999
    elif b=='QR.20000-QR.39999':
        f2=20000
        f3=39999    
    elif b=='QR.40000-QR.59999':
        f2=40000
        f3=59999
    elif b=='QR.60000-QR.79999':
        f2=60000
        f3=79999
    elif b=='QR.80000+':
        f2=80000
        f3=999999

    if c=='Any':
        f4 = 0
        f5= 99999
    elif c=='0-999 sq.ft':
        f4=0
        f5=999
    elif c=='1000-2999 sq.ft':
        f4=1000
        f5=2999   
    elif c=='3000-4999 sq.ft':
        f4=3000
        f5=4999
    elif c=='5000+ sq.ft':
        f4=5000
        f5=99999
   


    # print(a,b,c)
    # print(f1,f2,f3,f4,f5)
    print("Button works")

    sqname=[]
    sqadd=[]
    sqroom=[]
    sqfloor=[]
    sqprice=[]
    sqcontact=[]
    sqpict = []


    cur = mydb.cursor()
    cur.execute('select x.nam,address,area,type0,price,contact,pict from properties x, properties1 y where x.nam=y.nam and address1 =(%s) and price1>(%s) and price1<(%s) and area1>(%s) and area1<(%s)',(f1,f2,f3,f4,f5,))
    data = cur.fetchall()
    for i in data:
        sqname.append(i[0])
        sqadd.append(i[1])
        sqroom.append(i[2])
        sqfloor.append(i[3])
        sqprice.append(i[4])
        sqcontact.append(i[5])
        sqpict.append(i[6])
        

    
    x=len(sqname)    

    scrollable_frame.destroy()
    
    scrollable_frame = tk.Frame(canvas)
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    canvas.configure(yscrollcommand=scrollbar.set)


    listem(x)
    
    
    





# ----Listings--------------------------------------------------------------------------------------------------------




listem(x)



# ----Title Frame------------------------------------------------------------------------------------------------------
frame1 = tk.Frame(root, background=back)
frame1.place(relx=0, rely=0, relwidth=1, relheight=0.15, anchor='nw')

titlehead=ttk.Label(frame1,text='Q-PROPERTIES',background=back,foreground=txtc,font=('Bauhaus 93',35))
titlehead.place(relx=0.4, rely=0.5, anchor='w' )

# ----Filter Frame------------------------------------------------------------------------------------------------------
frame2 = tk.Frame(root, background=back)
frame2.place(relx=0, rely=0.15, relwidth=1, relheight=0.1, anchor='nw')

fsep_frame2 = tk.Frame(frame2, bg=front)
fsep_frame2.place(relx=0, rely=0, relwidth=1, relheight=0.02, anchor='nw')

label1 = tk.Label(frame2, text='Filters:', font=('Berlin Sans FB', 30),background=back,foreground=txtc)
label1.place(rely=0.475, relx=0.02, anchor='w')

label1 = tk.Label(frame2, text='Location:', font=('Berlin Sans FB', 15),background=back,foreground=txtc)
label1.place(rely=0.5, relx=0.115, anchor='w')

locations = ('West Bay', 'The Pearl', 'Al Sadd','Lusail', 'Al Waab')

option_var1 = tk.StringVar()

def option_changed( *args):
    pass

option_menu1 = ttk.OptionMenu(frame2,option_var1,locations[0],*locations,command=option_changed, )
option_menu1.place(rely=0.5, relx=0.16, anchor='w', width=100, height =30)

label1 = tk.Label(frame2, text='Price:', font=('Berlin Sans FB', 15),background=back,foreground=txtc)
label1.place(rely=0.5, relx=0.27, anchor='w')


price = ('Any','QR.0-QR.19999', 'QR.20000-QR.39999','QR.40000-QR.59999','QR.60000-QR.79999','QR.80000+')

option_var2 = tk.StringVar()

def option2_changed( *args):
    pass

option_menu2 = ttk.OptionMenu(frame2,option_var2,price[0],*price,command=option2_changed)
option_menu2.place(rely=0.5, relx=0.3, anchor='w',width=140, height =30)

label1 = tk.Label(frame2, text='Area:', font=('Berlin Sans FB', 15),background=back,foreground=txtc)
label1.place(rely=0.5, relx=0.422, anchor='w')

bed = ('Any','0-999 sq.ft','1000-2999 sq.ft', '3000-4999 sq.ft','5000+ sq.ft')

option_var3 = tk.StringVar()

def option3_changed( *args):
    pass

option_menu3 = ttk.OptionMenu(frame2,option_var3,bed[0],*bed,command=option3_changed)
option_menu3.place(rely=0.5, relx=0.45, anchor='w',width=120, height =30)

searchbtn=ttk.Button(frame2,text='Search', command= filterclick)
searchbtn.place(rely=0.5, relx=0.85, anchor='w', width=130, height=35)


# ----ColumnFrame-------------------------------------------------------------------------------------------------------
frame4 = tk.Frame(root, background=back)
frame4.place(relx=0, rely=0.25,width=1900, relheight=0.1, anchor='nw')

fillframe = tk.Frame(root, background=back)
fillframe.place(relx=0.95, rely=0.252,width=100, relheight=0.098, anchor='nw')

sep_frame=tk.Frame(frame4, bg=front)
sep_frame.place(relx=0, rely=0, relwidth=1, relheight=0.02, anchor='nw')

sep_frame2=tk.Frame(frame4, bg=front)
sep_frame2.place(relx=0.166, rely=0, relwidth=0.001, relheight=1, anchor='nw')

c_name=ttk.Label(frame4,text='Name',background=back,foreground=txtc,font=('Arial Bold',17))
c_name.place(relx=0.06, rely=0.5,relwidth=0.08,relheight=0.5, anchor='w' )

sep_frame3=tk.Frame(frame4, bg=front)
sep_frame3.place(relx=0.3649, rely=0, relwidth=0.001, relheight=1, anchor='nw')

c_address=ttk.Label(frame4,text='Address',background=back,foreground=txtc,font=('Arial Bold',17))
c_address.place(relx=0.24, rely=0.5,relwidth=0.11,height=50, anchor='w' )

sep_frame4=tk.Frame(frame4, bg=front)
sep_frame4.place(relx=0.476, rely=0, relwidth=0.001, relheight=1, anchor='nw')

c_rooms=ttk.Label(frame4,text='Area',background=back,foreground=txtc,font=('Arial Bold',17))
c_rooms.place(relx=0.407, rely=0.5,relwidth=0.04,height=50, anchor='w' )

sep_frame5=tk.Frame(frame4, bg=front)
sep_frame5.place(relx=0.5632, rely=0, relwidth=0.001, relheight=1, anchor='nw')

c_floor=ttk.Label(frame4,text='Type',background=back,foreground=txtc,font=('Arial Bold',17))
c_floor.place(relx=0.505, rely=0.5,relwidth=0.05,height=50, anchor='w' )

sep_frame6=tk.Frame(frame4, bg=front)
sep_frame6.place(relx=0.674, rely=0, relwidth=0.001, relheight=1, anchor='nw')

c_price=ttk.Label(frame4,text='Price',background=back,foreground=txtc,font=('Arial Bold',17))
c_price.place(relx=0.6, rely=0.5,relwidth=0.05,height=50, anchor='w' )


sep_frame7=tk.Frame(frame4, bg=front)
sep_frame7.place(relx=0.799, rely=0, relwidth=0.001, relheight=1, anchor='nw')

c_contact=ttk.Label(frame4,text='Contact',background=back,foreground=txtc,font=('Arial Bold',17))
c_contact.place(relx=0.71, rely=0.5,relwidth=0.08,height=50, anchor='w' )

c_picture=ttk.Label(frame4,text='Picture',background=back,foreground=txtc,font=('Arial Bold',17))
c_picture.place(relx=0.865, rely=0.5,relwidth=0.18,height=50, anchor='w' )

'''
# ----Create Account Frame-----------------------------------------------------------------------------------------

seller_frame=tk.Frame(root,bg=back)
seller_frame.place(relx=0,rely=0,relwidth=1, relheight=1)

f6title=tk.Label(seller_frame,text="CREATE LISTING",font=("Arial Bold",60),fg=front,bg=back)
f6title.place(relx=0.295, rely=0.1,)

#listname
f6name=tk.Label(seller_frame,text="Listing Name:",font=("",18),fg=front,bg=back)
f6name.place(relx=0.3,rely=0.3)

f6namentry=tk.Entry(seller_frame,bg='#ac8279',fg=front,width=35,font='Arial 14')
f6namentry.place(relx=0.3,rely=0.35,relwidth=0.15,relheight=0.045)

#location
f6location=tk.Label(seller_frame,text="Location:",font=("",18),fg=front,bg=back)
f6location.place(relx=0.5,rely=0.3)

locations = ('West Bay', 'The Pearl', 'Al Sadd','Lusail', 'Al Waab')
option_var1 = tk.StringVar()
def option_changed( *args):
    pass
option_menu1 = ttk.OptionMenu(seller_frame,option_var1,locations[0],*locations,command=option_changed, )
option_menu1.place(rely=0.375, relx=0.5, anchor='w', width=150, height =40)

#address
f6add=tk.Label(seller_frame,text="Address:",font=("wdwdwq",18),fg=front,bg=back)
f6add.place(relx=0.3,rely=0.45)

f6addentry=tk.Entry(seller_frame,bg='#ac8279',fg=front,font='Arial 14',width=35)
f6addentry.place(relx=0.3,rely=0.5,relwidth=0.35,relheight=0.045)

f6bed=tk.Label(seller_frame,text="Bed/Bath:",font=("wdwdwq",18),fg=front,bg=back)
f6bed.place(relx=0.3,rely=0.6)

f6bedentry=tk.Entry(seller_frame,bg='#ac8279',fg=front,font='Arial 14',width=35)
f6bedentry.place(relx=0.3,rely=0.65,relwidth=0.15,relheight=0.045)

f6area=tk.Label(seller_frame,text="Area:",font=("wdwdwq",18),fg=front,bg=back)
f6area.place(relx=0.5,rely=0.6)

f6areaentry=tk.Entry(seller_frame,bg='#ac8279',fg=front,font='Arial 14',width=35)
f6areaentry.place(relx=0.5,rely=0.65,relwidth=0.15,relheight=0.045)

f6num=tk.Label(seller_frame,text="Mobile no:",font=("wdwdwq",18),fg=front,bg=back)
f6num.place(relx=0.3,rely=0.75)

f6numentry=tk.Entry(seller_frame,bg='#ac8279',fg=front,font='Arial 14',width=35)
f6numentry.place(relx=0.3,rely=0.8,relwidth=0.35,relheight=0.045)

def lmao(event):
    u= f2usentry.get()
    v= f2pswdentry.get()
    h = f2repswdentry.get()
    if u =='' or v=='':
        f2error=ttk.Label(create_frame,text='Enter Valid username or password!',background=front,foreground=back,font=('',14))
        f2error.place(relx=0.38,rely=0.7,relwidth=0.38,relheight=0.045)
    else:
        if u in squser:
            f2error=ttk.Label(create_frame,text='Username already taken. Please try again',background=front,foreground=back,font=('',14))
            f2error.place(relx=0.38,rely=0.64,relwidth=0.38,relheight=0.045)
            
        elif v != h:
            f2error=ttk.Label(create_frame,text='Incorrect password. Please try again',background=front,foreground=back,font=('',14))
            f2error.place(relx=0.38,rely=0.7,relwidth=0.38,relheight=0.045)
            
        else:
            cur.execute('insert into accounts values((%s),(%s))',(u,v,))
            mydb.commit()
            f2error=ttk.Label(create_frame,text='Account created!',background=front,foreground=back,font=('',14))
            f2error.place(relx=0.45,rely=0.7,relwidth=0.38,relheight=0.045)


create=tk.Button(create_frame,text='CREATE',fg=front,bg=back,font=('Arial Bold',18),command=lambda : lmao('sddsd'))
create.place(relx=0.42,rely=0.75, relwidth=0.15,relheight=0.05 )

#Gobackbutton
lgtacc=tk.Label(create_frame,text="Already have an account?",font=('',13),fg=back,bg=front)
lgtacc.place(relx=0.029, rely=0.89)

lgtbtn=tk.Button(create_frame, text='Login', font=('',11),fg=front,bg=back,width=18,command=lambda: raise_frame(login_frame))
lgtbtn.place(relx=0.015, rely=0.93, relwidth=0.12)



'''

# ----Login--------------------------------------------------------------------------------------------------------


def raise_frame(frame):
    frame.tkraise()

login_frame=tk.Frame(root,bg=front)
login_frame.place(relx=0,rely=0,relwidth=1, relheight=1)

create_frame=tk.Frame(root, bg=front)
create_frame.place(relx=0, rely=0, relwidth=1,relheight=1)

#Title
f1title=ttk.Label(login_frame,text="WELCOME!",font=("Arial Bold",60),foreground=back,background=front)
f1title.place(relx=0.38, rely=0.1,)

#Username
usname=ttk.Label(login_frame,text="Username:",font=("",18),foreground=back,background=front)
usname.place(relx=0.3,rely=0.35)

usentry=tk.Entry(login_frame,background='#ac8279',foreground=front,width=35,font='Arial 14')
usentry.place(relx=0.3,rely=0.4,relwidth=0.38,relheight=0.045)

#password
pswd=ttk.Label(login_frame,text="Password:",font=("",18),foreground=back,background=front)
pswd.place(relx=0.3,rely=0.5)

pswdentry=tk.Entry(login_frame, show='*', background='#ac8279',foreground=front,font='Arial 14',width=35)
pswdentry.place(relx=0.3,rely=0.55,relwidth=0.38,relheight=0.045)

#Loginbutton
squser={}
sqpass={}


def lol(event):
    cur.execute('select * from accounts')
    data = cur.fetchall()
    for (i,j) in data:
        squser[i]=j

    if usentry.get() in squser:
        if pswdentry.get()== squser[usentry.get()]:
            raise_frame(frame1)
            raise_frame(frame2)
            raise_frame(frame4)
            raise_frame(frame3)
    else:
        error=ttk.Label(login_frame,text='Wrong email id or password. Please try again',background=front,foreground=back,font=('',14))
        error.place(relx=0.38,rely=0.64,relwidth=0.38,relheight=0.045)
login=tk.Button(login_frame,text='LOGIN',bg=back, fg=front,font=('Arial Bold',18),command=lambda : lol('sddsd'))
login.bind('<Return>',lol)
login.place(relx=0.41, rely= 0.7, relwidth=0.15,relheight=0.05 )

#create button text
crtacc=tk.Label(login_frame,text="Don't have an account?",font=('Arial',13),fg=back,bg=front)
crtacc.place(relx=0.032, rely=0.89)

crtbtn=tk.Button(login_frame, text='Create account', font=('',11),fg=front,bg=back, command= lambda :raise_frame(create_frame))
crtbtn.place(relx=0.015, rely=0.93, relwidth=0.12)



# ----Create Account Frame------------------------------------------------------------------------------------------

f2title=tk.Label(create_frame,text="CREATE ACCOUNT",font=("Arial Bold",60),fg=back,bg=front)
f2title.place(relx=0.295, rely=0.1,)

#username
f2usname=tk.Label(create_frame,text="New Username:",font=("",18),fg=back,bg=front)
f2usname.place(relx=0.3,rely=0.3)

f2usentry=tk.Entry(create_frame,bg='#ac8279',fg=front,width=35,font='Arial 14')
f2usentry.place(relx=0.3,rely=0.35,relwidth=0.38,relheight=0.045)

#password
f2pswd=tk.Label(create_frame,text="Password:",font=("wdwdwq",18),fg=back,bg=front)
f2pswd.place(relx=0.3,rely=0.45)

f2pswdentry=tk.Entry(create_frame,bg='#ac8279',fg=front,font='Arial 14',width=35)
f2pswdentry.place(relx=0.3,rely=0.5,relwidth=0.38,relheight=0.045)

f2repswd=tk.Label(create_frame,text="Re-enter Password:",font=("wdwdwq",18),fg=back,bg=front)
f2repswd.place(relx=0.3,rely=0.6)

f2repswdentry=tk.Entry(create_frame,bg='#ac8279',fg=front,font='Arial 14',width=35)
f2repswdentry.place(relx=0.3,rely=0.65,relwidth=0.38,relheight=0.045)

def lmao(event):
    u= f2usentry.get()
    v= f2pswdentry.get()
    h = f2repswdentry.get()
    if u =='' or v=='':
        f2error=ttk.Label(create_frame,text='Enter Valid username or password!',background=front,foreground=back,font=('',14))
        f2error.place(relx=0.38,rely=0.7,relwidth=0.38,relheight=0.045)
    else:
        if u in squser:
            f2error=ttk.Label(create_frame,text='Username already taken. Please try again',background=front,foreground=back,font=('',14))
            f2error.place(relx=0.38,rely=0.64,relwidth=0.38,relheight=0.045)
            
        elif v != h:
            f2error=ttk.Label(create_frame,text='Incorrect password. Please try again',background=front,foreground=back,font=('',14))
            f2error.place(relx=0.38,rely=0.7,relwidth=0.38,relheight=0.045)
            
        else:
            cur.execute('insert into accounts values((%s),(%s))',(u,v,))
            mydb.commit()
            f2error=ttk.Label(create_frame,text='Account created!',background=front,foreground=back,font=('',14))
            f2error.place(relx=0.45,rely=0.7,relwidth=0.38,relheight=0.045)


create=tk.Button(create_frame,text='CREATE',fg=front,bg=back,font=('Arial Bold',18),command=lambda : lmao('sddsd'))
create.place(relx=0.42,rely=0.75, relwidth=0.15,relheight=0.05 )

#Gobackbutton
lgtacc=tk.Label(create_frame,text="Already have an account?",font=('',13),fg=back,bg=front)
lgtacc.place(relx=0.029, rely=0.89)

lgtbtn=tk.Button(create_frame, text='Login', font=('',11),fg=front,bg=back,width=18,command=lambda: raise_frame(login_frame))
lgtbtn.place(relx=0.015, rely=0.93, relwidth=0.12)


raise_frame(login_frame)


# ----Login Logic------------------------------------------------------------------------------------------

   


root.mainloop()
