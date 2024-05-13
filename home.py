import tkinter
from PIL import Image,ImageTk   #pip pillow install 
from tkinter import messagebox
import pymysql
import webbrowser
root=tkinter.Tk()
root.title("JPS koderma jharkhand")
root.config(bg="#212529")
root.geometry("1920x1080")

def p_msg():
    messagebox.showinfo('Error','work in progress')
def calendar():
    messagebox.showinfo('Error','work in progress')
    
def holiday():
    messagebox.showinfo('Error','work in progress')
    
def event():
    messagebox.showinfo('Error','work in progress')
    
def report1():
    messagebox.showinfo('Error','work in progress')
    
def report2():
    messagebox.showinfo('Error','work in progress')


def library():
    messagebox.showinfo('Error','work in progress')
    
def hostel():
    messagebox.showinfo('Error','work in progress')
    
def canteen():
    messagebox.showinfo('Error','work in progress')
    
def medical():
    messagebox.showinfo('Error','work in progress')
    
def health_club():
    messagebox.showinfo('Error','work in progress')
    
def wifi():
    messagebox.showinfo('Error','work in progress')


def img_gallery():
    root=tkinter.Toplevel()
    root.geometry("1920x1080")
    #frame
    f=tkinter.Frame(root,bg="blue")
    f.place(x=0,y=0,height=30,width=1920)
    a1=tkinter.Label(f,text="JPS: Jharkhand Public School (official website)",fg="white",bg="blue",font="arial 12 bold")
    a1.place(x=0,y=5)
    #png icon helpdesk
    i=tkinter.Label(f,image=img9,fg="black",bg="white",font="arial 14 bold")
    i.place(x=1360,y=5)
    a2=tkinter.Button(f,text="Helpdesk",fg="white",bg="blue",font="arial 12 bold",bd=0,cursor='hand2',command=help_desk)
    a2.place(x=1400,y=5)
    #frame
    f1=tkinter.Frame(root,bg="white")
    f1.place(x=0,y=30,height=105,width=1920)
    #logo frame
    flogo=tkinter.Frame(f1,bg="white",highlightthickness=2)
    flogo.place(x=0,y=0,height=105,width=180)
    #logo png
    school_img=tkinter.PhotoImage(name="school_1",file="jplogo.png") 
    i=tkinter.Label(flogo,image=school_img,fg="black",bg="white",font="arial 12 bold")
    i.place(x=30,y=0)
    
    b1=tkinter.Label(f1,text="झारखंड पब्लिक स्कूल",fg="black",bg="white")
    b1.place(x=200,y=5)
    b2=tkinter.Label(f1,text="झारखंड शासन",fg="black",bg="white")
    b2.place(x=220,y=20)
    b3=tkinter.Label(f1,text="____________________________",fg="black",bg="white")
    b3.place(x=200,y=35)
    b4=tkinter.Label(f1,text="Jharkhand Public School",fg="black",bg="white",font="arial 12 bold")
    b4.place(x=200,y=55)
    b4=tkinter.Label(f1,text="Government of Jharkhand",fg="black",bg="white",font="arial 12 bold")
    b4.place(x=200,y=75)
    b5=tkinter.Label(f1,text="Email Us:",fg="black",bg="white",font="arial 12")
    b5.place(x=1100,y=30)
    #png icon emailbox
    i=tkinter.Label(f1,image=img10,fg="black",bg="white",font="arial 14 bold")
    i.place(x=1070,y=30)
    b6=tkinter.Label(f1,text="jps123@gmail.com",fg="black",bg="white",font="arial 12 bold")
    b6.place(x=1100,y=50)
    
    #ashok icon frame
    ashk_f=tkinter.Frame(f1,bg="white",highlightthickness=1)
    ashk_f.place(x=1370,y=0,height=105,width=210)
    #png icon ashok
    i=tkinter.Label(ashk_f,image=ashk,fg="black",bg="white",font="arial 14 bold")
    i.place(x=0,y=5)

    #frame menu 
    f2=tkinter.Frame(root,bg="blue")
    f2.place(x=0,y=135,height=60,width=1920)
    #menu button
    c1=tkinter.Button(f2,text="Home",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="blue",command=home,cursor='hand2')
    c1.place(x=130,y=15)

    # menubutton
    menubutton=tkinter.Menubutton(f2,text="About us",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",cursor='hand2')
    menu=tkinter.Menu(menubutton,tearoff=False)
    menubutton["menu"]=menu
    menu.add_command(label="principle message",command=p_msg)
    menubutton.place(x=210,y=15) 

    menubutton=tkinter.Menubutton(f2,text="Academic",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",cursor='hand2')
    menu=tkinter.Menu(menubutton,tearoff=False)
    menubutton["menu"]=menu
    menu.add_command(label="Academic Calendar",command=library)
    menu.add_command(label="List Of Holidays",command=holiday)
    menu.add_command(label="Event at a Schedule",command=event)
    menu.add_command(label="Annual Report 2021-2022",command=report1)   
    menu.add_command(label="Annual Report 2022-2023",command=report2)
    menubutton.place(x=320,y=15) 


    menubutton=tkinter.Menubutton(f2,text="Facilities",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",cursor='hand2')
    menu=tkinter.Menu(menubutton,tearoff=False)
    menubutton["menu"]=menu
    menu.add_command(label="E-Library",command=library)
    menu.add_command(label="Hostels",command=hostel)
    menu.add_command(label="Canteen",command=canteen)
    menu.add_command(label="Medical Clinic",command=medical)
    menu.add_command(label="Health Club",command=health_club)
    menu.add_command(label="Wi-Fi Campus",command=wifi)
    menubutton.place(x=435,y=15) 

       
    menubutton=tkinter.Menubutton(f2,text="Gallery",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",cursor='hand2')
    menu=tkinter.Menu(menubutton,tearoff=False)
    menubutton["menu"]=menu
    menu.add_command(label="Image Gallery",command=img_gallery)
    menu.add_command(label="Video Gallery",command=video_gallery)
    menubutton.place(x=545,y=15) 

    c1=tkinter.Button(f2,text="Key Persons",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",command=key_person,cursor='hand2')
    c1.place(x=650,y=15)
    c1=tkinter.Button(f2,text="Web Information Manager",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",command=web_desiner,cursor='hand2')
    c1.place(x=775,y=15)
    c1=tkinter.Button(f2,text="Contact",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",cursor='hand2',command=contact)
    c1.place(x=980,y=15)
    
    
    f3=tkinter.Frame(root,bg="#e6e6e6")
    f3.place(x=0,y=195,height=600,width=1920)
    image1=Image.open("C:\\Users\\ASUS\\onedrive\\Desktop\\school1\\ind.jpg")
    photo1=ImageTk.PhotoImage(image1)
    l1=tkinter.Button(f3,image=photo1,bd=0)
    l1.place(x=30,y=30)
    
    image2=Image.open("C:\\Users\\ASUS\\onedrive\\Desktop\\school1\\teacherday.jpg")
    photo2=ImageTk.PhotoImage(image2)
    l1=tkinter.Button(f3,image=photo2,bd=0)
    l1.place(x=450,y=10)
    
    image3=Image.open("C:\\Users\\ASUS\\onedrive\\Desktop\\school1\\holii.jpg")
    photo3=ImageTk.PhotoImage(image3)
    l1=tkinter.Button(f3,image=photo3,bd=0)
    l1.place(x=870,y=30)
    
    image4=Image.open("C:\\Users\\ASUS\\onedrive\\Desktop\\school1\\asd.jpg")
    photo4=ImageTk.PhotoImage(image4)
    l1=tkinter.Button(f3,image=photo4,bd=0)
    l1.place(x=450,y=250)
    
    
    
    f9=tkinter.Frame(root,bg="navy blue")
    f9.place(x=00,y=680,height=150,width=1920)
    bttm=tkinter.Label(f9,text="© हे शालेय शिक्षण व क्रीडा विभागाचे अधिकृत संकेतस्थळ आहे. सर्व हक्क सुरक्षित.",fg="white",bg="navy blue")
    bttm.place(x=550,y=20)
    bttm=tkinter.Label(f9,text="© 2024 This is the official website of School Education and Sports Department, Govt of Jharkhand.All Rights Reserved.",fg="white",bg="navy blue",font="arial 12 bold")
    bttm.place(x=350,y=50)  
    
    root.mainloop()
    
    
def video_gallery():
    messagebox.showinfo('Error','work in progress')   
    
    

 
 

def help_desk():
     help_f=tkinter.Frame(f1,bg="white")
     help_f.place(x=1300,y=0,height=20,width=180)
     msg=tkinter.Label(help_f,text="jps123@gmail.com",bg="#E3E3E3",fg="black",font="arial 10 bold")
     msg.place(x=5,y=0)  
             


def contact():
    root=tkinter.Toplevel()
    root.geometry("1920x1080")
    #frame
    f=tkinter.Frame(root,bg="blue")
    f.place(x=0,y=0,height=30,width=1920)
    a1=tkinter.Label(f,text="JPS: Jharkhand Public School (official website)",fg="white",bg="blue",font="arial 12 bold")
    a1.place(x=0,y=5)
    #png icon helpdesk
    i=tkinter.Label(f,image=img9,fg="black",bg="white",font="arial 14 bold")
    i.place(x=1360,y=5)
    a2=tkinter.Button(f,text="Helpdesk",fg="white",bg="blue",font="arial 12 bold",bd=0,cursor='hand2',command=help_desk)
    a2.place(x=1400,y=5)
    #frame
    f1=tkinter.Frame(root,bg="white")
    f1.place(x=0,y=30,height=105,width=1920)
    #logo frame
    flogo=tkinter.Frame(f1,bg="white",highlightthickness=2)
    flogo.place(x=0,y=0,height=105,width=180)
    #logo png
    school_img=tkinter.PhotoImage(name="school_1",file="jplogo.png") 
    i=tkinter.Label(flogo,image=school_img,fg="black",bg="white",font="arial 12 bold")
    i.place(x=30,y=0)
    
    b1=tkinter.Label(f1,text="झारखंड पब्लिक स्कूल",fg="black",bg="white")
    b1.place(x=200,y=5)
    b2=tkinter.Label(f1,text="झारखंड शासन",fg="black",bg="white")
    b2.place(x=220,y=20)
    b3=tkinter.Label(f1,text="____________________________",fg="black",bg="white")
    b3.place(x=200,y=35)
    b4=tkinter.Label(f1,text="Jharkhand Public School",fg="black",bg="white",font="arial 12 bold")
    b4.place(x=200,y=55)
    b4=tkinter.Label(f1,text="Government of Jharkhand",fg="black",bg="white",font="arial 12 bold")
    b4.place(x=200,y=75)
    b5=tkinter.Label(f1,text="Email Us:",fg="black",bg="white",font="arial 12")
    b5.place(x=1100,y=30)
    #png icon emailbox
    i=tkinter.Label(f1,image=img10,fg="black",bg="white",font="arial 14 bold")
    i.place(x=1070,y=30)
    b6=tkinter.Label(f1,text="jps123@gmail.com",fg="black",bg="white",font="arial 12 bold")
    b6.place(x=1100,y=50)
    
    #ashok icon frame
    ashk_f=tkinter.Frame(f1,bg="white",highlightthickness=1)
    ashk_f.place(x=1370,y=0,height=105,width=210)
    #png icon ashok
    i=tkinter.Label(ashk_f,image=ashk,fg="black",bg="white",font="arial 14 bold")
    i.place(x=0,y=5)

    #frame menu 
    f2=tkinter.Frame(root,bg="blue")
    f2.place(x=0,y=135,height=60,width=1920)
    #menu button
    c1=tkinter.Button(f2,text="Home",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="blue",command=home,cursor='hand2')
    c1.place(x=130,y=15)

    # menubutton
    menubutton=tkinter.Menubutton(f2,text="About us",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",cursor='hand2')
    menu=tkinter.Menu(menubutton,tearoff=False)
    menubutton["menu"]=menu
    menu.add_command(label="principle message",command=p_msg)
    menubutton.place(x=210,y=15) 

    menubutton=tkinter.Menubutton(f2,text="Academic",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",cursor='hand2')
    menu=tkinter.Menu(menubutton,tearoff=False)
    menubutton["menu"]=menu
    menu.add_command(label="Academic Calendar",command=calendar)
    menu.add_command(label="List Of Holidays",command=holiday)
    menu.add_command(label="Event at a Schedule",command=event)
    menu.add_command(label="Annual Report 2021-2022",command=report1)   
    menu.add_command(label="Annual Report 2022-2023",command=report2)
    menubutton.place(x=320,y=15) 


    menubutton=tkinter.Menubutton(f2,text="Facilities",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",cursor='hand2')
    menu=tkinter.Menu(menubutton,tearoff=False)
    menubutton["menu"]=menu
    menu.add_command(label="E-Library",command=library)
    menu.add_command(label="Hostels",command=hostel)
    menu.add_command(label="Canteen",command=canteen)
    menu.add_command(label="Medical Clinic",command=medical)
    menu.add_command(label="Health Club",command=health_club)
    menu.add_command(label="Wi-Fi Campus",command=wifi)
    menubutton.place(x=435,y=15) 

       
    menubutton=tkinter.Menubutton(f2,text="Gallery",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",cursor='hand2')
    menu=tkinter.Menu(menubutton,tearoff=False)
    menubutton["menu"]=menu
    menu.add_command(label="Image Gallery",command=img_gallery)
    menu.add_command(label="Video Gallery",command=video_gallery)
    menubutton.place(x=545,y=15) 

    c1=tkinter.Button(f2,text="Key Persons",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",command=key_person,cursor='hand2')
    c1.place(x=650,y=15)
    c1=tkinter.Button(f2,text="Web Information Manager",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",command=web_desiner,cursor='hand2')
    c1.place(x=775,y=15)
    c1=tkinter.Button(f2,text="Contact",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",cursor='hand2',command=contact)
    c1.place(x=980,y=15)   
    
    
    f2=tkinter.Frame(root,bg="white")
    f2.place(x=130,y=230,height=200,width=550)
    # png icon loction
    location_icon=tkinter.PhotoImage(name="location",file="location.png")
    i=tkinter.Label(f2,image=location_icon,fg="black",bg="white",font="arial 14 bold")
    i.place(x=250,y=40)
    
    l1=tkinter.Label(f2,text="Our Location",fg="black",bg="white",font="arial 16 bold")
    l1.place(x=210,y=90)
    l1=tkinter.Label(f2,text="Jharkhand Public School Giridih Road Salaidih (Inderwa) Dist - Koderma PIN-825410",fg="black",bg="white",font="arial 11")
    l1.place(x=0,y=120)
    l1=tkinter.Label(f2,text=" Dist - Koderma PIN-825410",fg="black",bg="white",font="arial 12")
    l1.place(x=210,y=140)

    f3=tkinter.Frame(root,bg="white")
    f3.place(x=130,y=470,height=180,width=250)
    # png icon email
    i=tkinter.Label(f3,image=img10,fg="black",bg="white",font="arial 14 bold")
    i.place(x=120,y=60)
    l2=tkinter.Label(f3,text="Email Us",fg="black",bg="white",font="arial 14 bold")
    l2.place(x=90,y=90)
    l2=tkinter.Label(f3,text="jps123@gmail.com",fg="black",bg="white",font="arial 12")
    l2.place(x=80,y=120)


    f4=tkinter.Frame(root,bg="white")
    f4.place(x=430,y=470,height=180,width=250) 
    # png icon call
    call_icon=tkinter.PhotoImage(name="call",file="phonecall.png")
    i=tkinter.Label(f4,image=call_icon,fg="black",bg="white",font="arial 14 bold")
    i.place(x=100,y=50)
    
    l3=tkinter.Label(f4,text="Contact Us",fg="black",bg="white",font="arial 14 bold")
    l3.place(x=70,y=90)
    l3=tkinter.Label(f4,text="6200072389",fg="black",bg="white",font="arial 12")
    l3.place(x=75,y=120)

    def live_location():
        webbrowser.open('https://maps.app.goo.gl/KYF79pCUfGHf35T1A')

    img_f=tkinter.Frame(root,bg="white")
    img_f.place(x=900,y=280,height=225,width=500)
    image1=Image.open("C:\\Users\\ASUS\\onedrive\\Desktop\\school1\\maplocation.png")
    photo1=ImageTk.PhotoImage(image1)
    l1=tkinter.Button(img_f,image=photo1,bd=0,command=live_location)
    l1.place(x=0,y=0)
    
    
    #
    f9=tkinter.Frame(root,bg="navy blue")
    f9.place(x=00,y=680,height=150,width=1920)
    bttm=tkinter.Label(f9,text="© हे शालेय शिक्षण व क्रीडा विभागाचे अधिकृत संकेतस्थळ आहे. सर्व हक्क सुरक्षित.",fg="white",bg="navy blue")
    bttm.place(x=550,y=20)
    bttm=tkinter.Label(f9,text="© 2024 This is the official website of School Education and Sports Department, Govt of Jharkhand.All Rights Reserved.",fg="white",bg="navy blue",font="arial 12 bold")
    bttm.place(x=350,y=50)    
    
    root.mainloop()


def key_person():
    root=tkinter.Toplevel()
    root.geometry("1920x1080")
    #frame
    f=tkinter.Frame(root,bg="blue")
    f.place(x=0,y=0,height=30,width=1920)
    a1=tkinter.Label(f,text="JPS: Jharkhand Public School (official website)",fg="white",bg="blue",font="arial 12 bold")
    a1.place(x=0,y=5)
    #png icon helpdesk
    i=tkinter.Label(f,image=img9,fg="black",bg="white",font="arial 14 bold")
    i.place(x=1360,y=5)
    a2=tkinter.Label(f,text="Helpdesk",fg="white",bg="blue",font="arial 12 bold")
    a2.place(x=1400,y=5)
    #frame
    f1=tkinter.Frame(root,bg="white")
    f1.place(x=0,y=30,height=105,width=1920)
    #logo frame
    flogo=tkinter.Frame(f1,bg="white",highlightthickness=2)
    flogo.place(x=0,y=0,height=105,width=180)
    #logo png
    school_img=tkinter.PhotoImage(name="school_1",file="jplogo.png") 
    i=tkinter.Label(flogo,image=school_img,fg="black",bg="white",font="arial 12 bold")
    i.place(x=30,y=0)
    
    b1=tkinter.Label(f1,text="झारखंड पब्लिक स्कूल",fg="black",bg="white")
    b1.place(x=200,y=5)
    b2=tkinter.Label(f1,text="झारखंड शासन",fg="black",bg="white")
    b2.place(x=220,y=20)
    b3=tkinter.Label(f1,text="____________________________",fg="black",bg="white")
    b3.place(x=200,y=35)
    b4=tkinter.Label(f1,text="Jharkhand Public School",fg="black",bg="white",font="arial 12 bold")
    b4.place(x=200,y=55)
    b4=tkinter.Label(f1,text="Government of Jharkhand",fg="black",bg="white",font="arial 12 bold")
    b4.place(x=200,y=75)
    b5=tkinter.Label(f1,text="Email Us:",fg="black",bg="white",font="arial 12")
    b5.place(x=1100,y=30)
    #png icon emailbox
    i=tkinter.Label(f1,image=img10,fg="black",bg="white",font="arial 14 bold")
    i.place(x=1070,y=30)
    
    b6=tkinter.Label(f1,text="jps123@gmail.com",fg="black",bg="white",font="arial 12 bold")
    b6.place(x=1100,y=50)
    
    #ashok icon frame
    ashk_f=tkinter.Frame(f1,bg="white",highlightthickness=1)
    ashk_f.place(x=1370,y=0,height=105,width=210)
    #png icon ashok
    i=tkinter.Label(ashk_f,image=ashk,fg="black",bg="white",font="arial 14 bold")
    i.place(x=0,y=5)

    #frame menu 
    f2=tkinter.Frame(root,bg="blue")
    f2.place(x=0,y=135,height=60,width=1920)
    # menu button
    c1=tkinter.Button(f2,text="Home",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="blue",command=home,cursor='hand2')
    c1.place(x=130,y=15)
    # menubutton
    menubutton=tkinter.Menubutton(f2,text="About us",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",cursor='hand2')
    menu=tkinter.Menu(menubutton,tearoff=False)
    menubutton["menu"]=menu
    menu.add_command(label="principle message",command=p_msg)
    menubutton.place(x=210,y=15) 

    menubutton=tkinter.Menubutton(f2,text="Academic",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",cursor='hand2')
    menu=tkinter.Menu(menubutton,tearoff=False)
    menubutton["menu"]=menu
    menu.add_command(label="Academic Calendar",command=calendar)
    menu.add_command(label="List Of Holidays",command=holiday)
    menu.add_command(label="Event at a Schedule",command=event)
    menu.add_command(label="Annual Report 2021-2022",command=report1)   
    menu.add_command(label="Annual Report 2022-2023",command=report2)
    menubutton.place(x=320,y=15) 


    menubutton=tkinter.Menubutton(f2,text="Facilities",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",cursor='hand2')
    menu=tkinter.Menu(menubutton,tearoff=False)
    menubutton["menu"]=menu
    menu.add_command(label="E-Library",command=library)
    menu.add_command(label="Hostels",command=hostel)
    menu.add_command(label="Canteen",command=canteen)
    menu.add_command(label="Medical Clinic",command=medical)
    menu.add_command(label="Health Club",command=health_club)
    menu.add_command(label="Wi-Fi Campus",command=wifi)
    menubutton.place(x=435,y=15) 

       
    menubutton=tkinter.Menubutton(f2,text="Gallery",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",cursor='hand2')
    menu=tkinter.Menu(menubutton,tearoff=False)
    menubutton["menu"]=menu
    menu.add_command(label="Image Gallery",command=img_gallery)
    menu.add_command(label="Video Gallery",command=video_gallery)
    menubutton.place(x=545,y=15) 
    
    
    
    c1=tkinter.Button(f2,text="Key Persons",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",command=key_person,cursor='hand2')
    c1.place(x=650,y=15)
    c1=tkinter.Button(f2,text="Web Information Manager",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",command=web_desiner,cursor='hand2')
    c1.place(x=775,y=15)
    c1=tkinter.Button(f2,text="Contact",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",cursor='hand2',command=contact)
    c1.place(x=980,y=15)


    #image frame
    f3=tkinter.Frame(root,bg="white")
    f3.place(x=0,y=190,height=600,width=1920)
    #image
    image=Image.open("C:\\Users\\ASUS\\onedrive\\Desktop\\school1\\lifetechguru.jpg")
    photo=ImageTk.PhotoImage(image)
    l1=tkinter.Button(f3,image=photo)
    l1.place(x=50,y=20)
    name=tkinter.Label(f3,text="Raju Manjhi Sir",fg="black",bg="white",font="arial 20 bold")
    name.place(x=80,y=280)
    name1=tkinter.Label(f3,text="(professeor's of Ranchi University)",fg="black",bg="white",font="arial 14 ")
    name1.place(x=50,y=315)
  
    #
    f9=tkinter.Frame(root,bg="navy blue")
    f9.place(x=00,y=680,height=150,width=1920)
    bttm=tkinter.Label(f9,text="© हे शालेय शिक्षण व क्रीडा विभागाचे अधिकृत संकेतस्थळ आहे. सर्व हक्क सुरक्षित.",fg="white",bg="navy blue")
    bttm.place(x=550,y=20)
    bttm=tkinter.Label(f9,text="© 2024 This is the official website of School Education and Sports Department, Govt of Jharkhand.All Rights Reserved.",fg="white",bg="navy blue",font="arial 12 bold")
    bttm.place(x=350,y=50)
    
    
    root.mainloop()



def web_desiner():
    root=tkinter.Toplevel()
    root.geometry("1920x1080")
    f=tkinter.Frame(root,bg="blue")
    f.place(x=0,y=0,height=30,width=1920)
    a1=tkinter.Label(f,text="JPS: Jharkhand Public School (official website)",fg="white",bg="blue",font="arial 12 bold")
    a1.place(x=0,y=5)
    i=tkinter.Label(f,image=img9,fg="black",bg="white",font="arial 14 bold")
    i.place(x=1360,y=5)
    a2=tkinter.Label(f,text="Helpdesk",fg="white",bg="blue",font="arial 12 bold")
    a2.place(x=1400,y=5)

    #frame
    f1=tkinter.Frame(root,bg="white")
    f1.place(x=0,y=30,height=105,width=1920)
    #logo frame
    flogo=tkinter.Frame(f1,bg="white",highlightthickness=2)
    flogo.place(x=0,y=0,height=105,width=180)
    #png icon logo
    school_img=tkinter.PhotoImage(name="school_1",file="jplogo.png") 
    i=tkinter.Label(flogo,image=school_img,fg="black",bg="white",font="arial 12 bold")
    i.place(x=30,y=0)   
     
    b1=tkinter.Label(f1,text="झारखंड पब्लिक स्कूल",fg="black",bg="white")
    b1.place(x=200,y=5)
    b2=tkinter.Label(f1,text="झारखंड शासन",fg="black",bg="white")
    b2.place(x=220,y=20)
    b3=tkinter.Label(f1,text="____________________________",fg="black",bg="white")
    b3.place(x=200,y=35)
    b4=tkinter.Label(f1,text="Jharkhand Public School",fg="black",bg="white",font="arial 12 bold")
    b4.place(x=200,y=55)
    b4=tkinter.Label(f1,text="Government of Jharkhand",fg="black",bg="white",font="arial 12 bold")
    b4.place(x=200,y=75)
    b5=tkinter.Label(f1,text="Email Us:",fg="black",bg="white",font="arial 12")
    b5.place(x=1100,y=30)
    #email png icon
    i=tkinter.Label(f1,image=img10,fg="black",bg="white",font="arial 14 bold")
    i.place(x=1070,y=30)
    
    b6=tkinter.Label(f1,text="jps123@gmail.com",fg="black",bg="white",font="arial 12 bold")
    b6.place(x=1100,y=50)
    #ashoka frame
    ashk_f=tkinter.Frame(f1,bg="white",highlightthickness=1)
    ashk_f.place(x=1370,y=0,height=105,width=210) 
    #ashoka logo png icon
    i=tkinter.Label(ashk_f,image=ashk,fg="black",bg="white",font="arial 14 bold")
    i.place(x=0,y=5)

    #frame menu button
    f2=tkinter.Frame(root,bg="blue")
    f2.place(x=0,y=135,height=60,width=1920)
    c1=tkinter.Button(f2,text="Home",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="blue",command=home,cursor='hand2')
    c1.place(x=130,y=15)

    # menubutton
    menubutton=tkinter.Menubutton(f2,text="About us",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",cursor='hand2')
    menu=tkinter.Menu(menubutton,tearoff=False)
    menubutton["menu"]=menu
    menu.add_command(label="principle message",command=p_msg)
    menubutton.place(x=210,y=15) 

    menubutton=tkinter.Menubutton(f2,text="Academic",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",cursor='hand2')
    menu=tkinter.Menu(menubutton,tearoff=False)
    menubutton["menu"]=menu
    menu.add_command(label="Academic Calendar",command=calendar)
    menu.add_command(label="List Of Holidays",command=holiday)
    menu.add_command(label="Event at a Schedule",command=event)
    menu.add_command(label="Annual Report 2021-2022",command=report1)   
    menu.add_command(label="Annual Report 2022-2023",command=report2)
    menubutton.place(x=320,y=15) 


    menubutton=tkinter.Menubutton(f2,text="Facilities",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",cursor='hand2')
    menu=tkinter.Menu(menubutton,tearoff=False)
    menubutton["menu"]=menu
    menu.add_command(label="E-Library",command=library)
    menu.add_command(label="Hostels",command=hostel)
    menu.add_command(label="Canteen",command=canteen)
    menu.add_command(label="Medical Clinic",command=medical)
    menu.add_command(label="Health Club",command=health_club)
    menu.add_command(label="Wi-Fi Campus",command=wifi)
    menubutton.place(x=435,y=15) 

       
    menubutton=tkinter.Menubutton(f2,text="Gallery",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",cursor='hand2')
    menu=tkinter.Menu(menubutton,tearoff=False)
    menubutton["menu"]=menu
    menu.add_command(label="Image Gallery",command=img_gallery)
    menu.add_command(label="Video Gallery",command=video_gallery)
    menubutton.place(x=545,y=15) 

    c1=tkinter.Button(f2,text="Key Persons",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",command=key_person,cursor='hand2')
    c1.place(x=650,y=15)
    c1=tkinter.Button(f2,text="Web Information Manager",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",command=web_desiner,cursor='hand2')
    c1.place(x=775,y=15)
    c1=tkinter.Button(f2,text="Contact",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",cursor='hand2',command=contact)
    c1.place(x=980,y=15)


    #image frame
    f3=tkinter.Frame(root,bg="white")
    f3.place(x=0,y=190,height=600,width=1920)
    #image
    # image=Image.open("")
    # photo=ImageTk.PhotoImage(image)
    # l1=tkinter.Button(f3,image=photo)
    # l1.place(x=50,y=10) 
    # name=tkinter.Label(f3,text="SHWEETA MA'AM",fg="black",bg="white",font="arial 16 bold")
    # name.place(x=50,y=250)
    # edu=tkinter.Label(f3,text="(Asst. Profesor of Ranchi college)",fg="black",bg="white",font="arial 14 bold")
    # edu.place(x=50,y=285)
    # edu=tkinter.Label(f3,text="Department on Computer Application",fg="black",bg="white",font="arial 12 bold")
    # edu.place(x=50,y=310)
    
    # image
    image1=Image.open("C:\\Users\\ASUS\\onedrive\\desktop\\school1\\spiku.jpg")
    photo1=ImageTk.PhotoImage(image1)
    l1=tkinter.Button(f3,image=photo1)
    l1.place(x=50,y=10)
    name=tkinter.Label(f3,text="Sourabh Kumar",fg="black",bg="white",font="arial 16 bold")
    name.place(x=50,y=250)
    edu=tkinter.Label(f3,text="Bachelor of Science(Information Technology)",fg="black",bg="white",font="arial 12 bold")
    edu.place(x=50,y=285)
    
    
    f9=tkinter.Frame(root,bg="navy blue")
    f9.place(x=00,y=680,height=150,width=1920)
    bttm=tkinter.Label(f9,text="© हे शालेय शिक्षण व क्रीडा विभागाचे अधिकृत संकेतस्थळ आहे. सर्व हक्क सुरक्षित.",fg="white",bg="navy blue")
    bttm.place(x=550,y=20)
    bttm=tkinter.Label(f9,text="© 2024 This is the official website of School Education and Sports Department, Govt of Jharkhand.All Rights Reserved.",fg="white",bg="navy blue",font="arial 12 bold")
    bttm.place(x=350,y=50) 
    
    root.mainloop()


def forget():
    Top=tkinter.Toplevel(root)
    Top.geometry("800x600")
    Top.maxsize(800,600)
    Top.minsize(800,600)
    f=tkinter.Frame(Top,bg="blue")
    f.place(x=0,y=0,height=30,width=1920)
    a1=tkinter.Label(f,text="JPS: Jharkhand Public School (official website)",fg="white",bg="blue",font="arial 8 bold")
    a1.place(x=0,y=5)
    i=tkinter.Label(f,image=img9,fg="black",bg="white",font="arial 8 bold")
    i.place(x=670,y=5)
    a2=tkinter.Label(f,text="Helpdesk",fg="white",bg="blue",font="arial 10 bold")
    a2.place(x=700,y=5)
    
    f1=tkinter.Frame(Top,bg="white")
    f1.place(x=0,y=30,height=100,width=1920)
    flogo=tkinter.Frame(f1,bg="white",highlightthickness=2)
    flogo.place(x=0,y=0,height=80,width=80)
    # school_img=tkinter.PhotoImage(name="school_1",file="jplogo.png") 
    i=tkinter.Label(flogo,image=school_img,fg="black",bg="white",font="arial 12 bold")
    i.place(x=0,y=0)
    b1=tkinter.Label(f1,text="झारखंड पब्लिक स्कूल",fg="navy blue",bg="white",font="arial 8 bold")
    b1.place(x=100,y=5)
    b2=tkinter.Label(f1,text="झारखंड शासन",fg="black",bg="white")
    b2.place(x=100,y=20)
    b3=tkinter.Label(f1,text="____________________________",fg="black",bg="white")
    b3.place(x=100,y=35)
    b4=tkinter.Label(f1,text="Jharkhand Public School",fg="black",bg="white",font="arial 8 bold")
    b4.place(x=100,y=55)    
    b4=tkinter.Label(f1,text="Government of Jharkhand",fg="black",bg="white",font="arial 8 bold")
    b4.place(x=100,y=75)
    b5=tkinter.Label(f1,text="Email Us:",fg="black",bg="white",font="arial 10")
    b5.place(x=630,y=30)
    i=tkinter.Label(f1,image=img10,fg="black",bg="white",font="arial 14 bold")
    i.place(x=600,y=30)
    b6=tkinter.Label(f1,text="jps123@gmail.com",fg="black",bg="white",font="arial 12 bold")
    b6.place(x=630,y=50)
    ashk_f=tkinter.Frame(f1,bg="white",highlightthickness=1)
    ashk_f.place(x=1370,y=0,height=105,width=210)
    i=tkinter.Label(ashk_f,image=ashk,fg="black",bg="white",font="arial 14 bold")
    i.place(x=0,y=5)
    
    
    def send_link():
        if email1.get()=="" :
            messagebox.showinfo('error','all filed required')
        else:
            mycon = pymysql.connect(host="localhost",user="root",password="",db="data_login")
            mycur = mycon.cursor()
            mycur.execute("select * from studentdata where email=%s ",(email1.get()))
            row=mycur.fetchone()
            if(row==None):
                messagebox.showinfo('Envaild','invaild username ')
            else:
                messagebox.showinfo('Sucessfully','send your email change your password visit link')
                
            mycon.commit()
            mycon.close()
    
    
    f2=tkinter.Frame(Top,bg="navy blue")
    f2.place(x=0,y=130,height=60,width=1920)
    sch_portal=tkinter.Label(f2,text="Reset Forget Passward",fg="white",bg="navy blue",font="arial 20 bold")
    sch_portal.place(x=60,y=10)
    

    f5=tkinter.Frame(Top,bg="#33adff")
    f5.place(x=0,y=190,height=310,width=1920)
    f6=tkinter.Frame(f5,bg="#e6e6e6")
    f6.place(x=240,y=30,height=220,width=300)
    fgt=tkinter.Label(f6,text="Forget Passward",fg="#33adff",bg="#e6e6e6",font="arial 18 bold")
    fgt.place(x=60,y=0)
    em=tkinter.Label(f6,text="enter you e-mail adress and well ",fg="black",bg="#e6e6e6",font="arial 8 ")
    em.place(x=45,y=35)
    em=tkinter.Label(f6,text="send a link you to reset your passward",fg="black",bg="#e6e6e6",font="arial 8")
    em.place(x=45,y=50)
    email1=tkinter.Entry(f6)
    email1.place(x=20,y=80,height=40,width=260)
    f7=tkinter.Frame(f6,bg="#33ff33")
    f7.place(x=20,y=130,width=260,height=40)
    se_link=tkinter.Button(f7,text="Send Link",fg="white",bg="#33ff33",font="arial 16 bold",bd=0,activebackground="#33ff33",activeforeground="white",cursor='hand2',command=send_link)
    se_link.place(x=70,y=5)
    l1=tkinter.Label(f6,text="Not a memeber?",fg="black",bg="#e6e6e6",font="arial 10")
    l1.place(x=70,y=190)    
    sin_in=tkinter.Button(f6,text="Signup",fg="blue",bg="#e6e6e6",font="arial 10 bold",bd=0,activebackground="#e6e6e6",activeforeground="blue",command=sign,cursor='hand2')
    sin_in.place(x=170,y=190)
      
    f9=tkinter.Frame(Top,bg="navy blue")
    f9.place(x=0,y=500,height=100,width=1920)
    bttm=tkinter.Label(f9,text="© हे शालेय शिक्षण व क्रीडा विभागाचे अधिकृत संकेतस्थळ आहे. सर्व हक्क सुरक्षित.",fg="white",bg="navy blue")
    bttm.place(x=250,y=20)
    bttm=tkinter.Label(f9,text="© 2024 This is the official website of School Education and Sports Department, Govt of Jharkhand.All Rights Reserved.",fg="white",bg="navy blue",font="arial 8 bold")
    bttm.place(x=80,y=50)
    Top.mainloop()
    

def sign():
  
    root=tkinter.Toplevel()
    from tkinter import messagebox
    root.geometry("1920x1080")
    f=tkinter.Frame(root,bg="blue")
    f.place(x=0,y=0,height=30,width=1920)
    a1=tkinter.Label(f,text="JPS: Jharkhand Public School (official website)",fg="white",bg="blue",font="arial 12 bold")
    a1.place(x=0,y=5)
    # png icon helpdesk
    i=tkinter.Label(f,image=img9,fg="black",bg="white",font="arial 14 bold")
    i.place(x=1360,y=5)
    a2=tkinter.Label(f,text="Helpdesk",fg="white",bg="blue",font="arial 12 bold")
    a2.place(x=1400,y=5)
    #frame
    f1=tkinter.Frame(root,bg="white")
    f1.place(x=0,y=30,height=105,width=1920)
    # logo frame
    flogo=tkinter.Frame(f1,bg="white",highlightthickness=2)
    flogo.place(x=0,y=0,height=105,width=180)
    # png logo
    school_img=tkinter.PhotoImage(name="school_1",file="jplogo.png") 
    i=tkinter.Label(flogo,image=school_img,fg="black",bg="white",font="arial 12 bold")
    i.place(x=30,y=0)
    
    b1=tkinter.Label(f1,text="झारखंड पब्लिक स्कूल",fg="black",bg="white")
    b1.place(x=200,y=5)
    b2=tkinter.Label(f1,text="झारखंड शासन",fg="black",bg="white")
    b2.place(x=220,y=20)
    b3=tkinter.Label(f1,text="____________________________",fg="black",bg="white")
    b3.place(x=200,y=35)
    b4=tkinter.Label(f1,text="Jharkhand Public School",fg="black",bg="white",font="arial 12 bold")
    b4.place(x=200,y=55)    
    b4=tkinter.Label(f1,text="Government of Jharkhand",fg="black",bg="white",font="arial 12 bold")
    b4.place(x=200,y=75)
    b5=tkinter.Label(f1,text="Email Us:",fg="black",bg="white",font="arial 12")
    b5.place(x=1100,y=30)
    # png icon email
    i=tkinter.Label(f1,image=img10,fg="black",bg="white",font="arial 14 bold")
    i.place(x=1070,y=30)
    b6=tkinter.Label(f1,text="jps123@gmail.com",fg="black",bg="white",font="arial 12 bold")
    b6.place(x=1100,y=50)
    # ashoka frame
    ashk_f=tkinter.Frame(f1,bg="white",highlightthickness=1)
    ashk_f.place(x=1370,y=0,height=105,width=210)
    #ashoka icon png
    i=tkinter.Label(ashk_f,image=ashk,fg="black",bg="white",font="arial 14 bold")
    i.place(x=0,y=5)
    
    f2=tkinter.Frame(root,bg="navy blue")
    f2.place(x=0,y=135,height=60,width=1920)
    sch_portal=tkinter.Label(f2,text="Student Register Now",fg="white",bg="navy blue",font="arial 20 bold")
    sch_portal.place(x=80,y=10)
    # png icon home
    home_img=tkinter.PhotoImage(name="himage_5",file="home1.png")
    i=tkinter.Button(f2,image=home_img,fg="black",bg="white",font="arial 14 bold",bd=0,cursor='hand2',command=home)
    i.place(x=1370,y=20)
    signup=tkinter.Button(f2,text="Home",fg="white",bg="navy blue",font="arial 14 bold",bd=0,activebackground="navy blue",activeforeground="white",command=home,cursor='hand2')
    signup.place(x=1400,y=15)
    
    
    def submit():
        
        if u.get()=='' or p.get()=='' or s.get()=='':
            messagebox.showinfo('error',"all fields are required")
        elif p.get() != s.get():
            messagebox.showinfo('error','Please enter correct your confirm password')
        else:
            messagebox.showinfo('sucessfully')
            email=u.get()
            pswd=p.get()
            c_pswd=s.get()
            mycon = pymysql.connect(host="localhost",user="root",password="",db="data_login")
            mycur = mycon.cursor()
            mycur.execute("INSERT INTO studentdata (email,pswd,c_pswd) VALUES (\'"+email+"\', \'"+pswd+"\',\'"+c_pswd+"\');")
            mycon.commit()
            mycon.close()
        #print(mycon)

            if(mycon):
                messagebox.showinfo('connection sucessfullly')
            else:
                messagebox.error('faield')


    u=tkinter.StringVar()
    p=tkinter.StringVar()
    s=tkinter.StringVar()
    
    f3=tkinter.Frame(root,bg="#cccccc")
    f3.place(x=0,y=190,height=600,width=1920)
    f4=tkinter.Frame(f3,bg="#e6e6e6")
    f4.place(x=570,y=20,height=530,width=450)
    sign_icon=tkinter.PhotoImage(name="signup",file="signupicon.png")
    i=tkinter.Label(f4,image=sign_icon,fg="black",bg="#e6e6e6",font="arial 14 bold")
    i.place(x=120,y=10)
    sig=tkinter.Label(f4,text="Sign Up",fg="black",bg="#e6e6e6",font="arial 22 bold")
    sig.place(x=170,y=10)
    user_icon=tkinter.PhotoImage(name="name",file="user12.png")
    i=tkinter.Label(f4,image=user_icon,fg="black",bg="#e6e6e6",font="arial 14 bold")
    i.place(x=10,y=60)
    name=tkinter.Label(f4,text="FULL NAME",fg="black",bg="#e6e6e6",font="arial 12 bold")
    name.place(x=50,y=70)
    box=tkinter.Entry(f4)
    box.place(x=20,y=95,width=410,height=30)
    i=tkinter.Label(f4,image=img10,fg="black",bg="white",font="arial 14 bold")
    i.place(x=10,y=130)
    mail=tkinter.Label(f4,text="EMAIL",fg="black",bg="#e6e6e6",font="arial 12 bold")
    mail.place(x=40,y=130)
    box2=tkinter.Entry(f4,textvariable=u)
    box2.place(x=20,y=155,height=30,width=410)
    psswd_icon=tkinter.PhotoImage(name="passward",file="psswd.png")
    i=tkinter.Label(f4,image=psswd_icon,fg="black",bg="#e6e6e6",font="arial 14 bold")
    i.place(x=10,y=190)
    pswd=tkinter.Label(f4,text="PASSWARD",fg="black",bg="#e6e6e6",font="arial 12 bold")
    pswd.place(x=40,y=190)
    box3=tkinter.Entry(f4,show="*",textvariable=p)
    box3.place(x=20,y=215,height=30,width=410)
    i=tkinter.Label(f4,image=psswd_icon,fg="black",bg="#e6e6e6",font="arial 14 bold")
    i.place(x=10,y=250)
    c_pswd=tkinter.Label(f4,text="CONFIRM PASSWARD",fg="black",bg="#e6e6e6",font="arial 12 bold")
    c_pswd.place(x=40,y=250)
    box4=tkinter.Entry(f4,show="*",textvariable=s)
    box4.place(x=20,y=275,height=30,width=410)
    sign_btn=tkinter.Button(f4,text="Sign up with your organization",fg="blue",bg="#e6e6e6",font="arial 12",bd=0,activebackground="#e6e6e6",activeforeground="blue",command=submit)
    sign_btn.place(x=120,y=340)
    l=tkinter.Label(f4,text="Already have on account?",fg="black",bg="#e6e6e6",font="arial 8 ")
    l.place(x=130,y=370)
    log_in=tkinter.Button(f4,text="Login",fg="red",bg="#e6e6e6",font="arial 10",bd=0,activebackground="#e6e6e6",activeforeground="red",command=student,cursor='hand2')
    log_in.place(x=260,y=365)
    l=tkinter.Label(f4,text="---------------------------------------OR--------------------------------------",bg="#e6e6e6",fg="black",font="arial 12 bold")
    l.place(x=15,y=390)
    def google():
     webbrowser.open("https://account.google.com/")
    g_f=tkinter.Frame(f4,bg="white")
    g_f.place(x=15,y=425,height=40,width=420)
    g_img=tkinter.PhotoImage(name="gimage_5",file="google.png")
    i=tkinter.Label(g_f,image=g_img,fg="black",bg="white",font="arial 14 bold",cursor='hand2')
    i.place(x=20,y=2)
    g_bttn=tkinter.Button(g_f,text="Continue with Google",fg="black",bg="white",font="arial 14 bold",bd=0,activebackground="white",activeforeground="black",command=google,cursor='hand2')
    g_bttn.place(x=100,y=5)
    def facebook():
        webbrowser.open("https://www.facebook.com/login.php/")
    face_f=tkinter.Frame(f4,bg="white")
    face_f.place(x=15,y=475,height=40,width=420)
    face_img=tkinter.PhotoImage(name="fimage_5",file="facebook.png")
    i=tkinter.Label(face_f,image=face_img,fg="black",bg="white",font="arial 14 bold",cursor='hand2')
    i.place(x=20,y=2)
    face_bttn=tkinter.Button(face_f,text="Continue with Facebook",fg="black",bg="white",font="arial 14 bold",bd=0,activebackground="white",activeforeground="black",command=facebook,cursor='hand2')
    face_bttn.place(x=100,y=5)
    
    root.mainloop()
    



def student():
    def login():
        if e1.get()=="" or e2.get()=="":
            messagebox.showinfo('error','all filed required')
        else:
            mycon = pymysql.connect(host="localhost",user="root",password="",db="data_login")
            mycur = mycon.cursor()
            mycur.execute("select * from studentdata where email=%s and pswd=%s",(e1.get(),e2.get()))
            row=mycur.fetchone()
            if(row==None):
                messagebox.showinfo('Envaild','invaild username or password')
            else:
                messagebox.showinfo('Sucessfully','your data is process on work')
                
            mycon.commit()
            mycon.close()
    
        
        
    root=tkinter.Toplevel()
    root.geometry("1920x1080")
    f=tkinter.Frame(root,bg="blue")
    f.place(x=0,y=0,height=30,width=1920)
    a1=tkinter.Label(f,text="JPS: Jharkhand Public School (official website)",fg="white",bg="blue",font="arial 12 bold")
    a1.place(x=0,y=5)
    i=tkinter.Label(f,image=img9,fg="black",bg="white",font="arial 14 bold")
    i.place(x=1360,y=5)
    a2=tkinter.Label(f,text="Helpdesk",fg="white",bg="blue",font="arial 12 bold")
    a2.place(x=1400,y=5)
    
    f1=tkinter.Frame(root,bg="white")
    f1.place(x=0,y=30,height=105,width=1920)
    flogo=tkinter.Frame(f1,bg="white",highlightthickness=2)
    flogo.place(x=0,y=0,height=105,width=180)
    # school_img=tkinter.PhotoImage(name="school_1",file="jplogo.png") 
    i=tkinter.Label(flogo,image=school_img,fg="black",bg="white",font="arial 12 bold")
    i.place(x=30,y=0)
    b1=tkinter.Label(f1,text="झारखंड पब्लिक स्कूल",fg="black",bg="white")
    b1.place(x=200,y=5)
    b2=tkinter.Label(f1,text="झारखंड शासन",fg="black",bg="white")
    b2.place(x=220,y=20)
    b3=tkinter.Label(f1,text="____________________________",fg="black",bg="white")
    b3.place(x=200,y=35)
    b4=tkinter.Label(f1,text="Jharkhand Public School",fg="black",bg="white",font="arial 12 bold")
    b4.place(x=200,y=55)    
    b4=tkinter.Label(f1,text="Government of Jharkhand",fg="black",bg="white",font="arial 12 bold")
    b4.place(x=200,y=75)
    b5=tkinter.Label(f1,text="Email Us:",fg="black",bg="white",font="arial 12")
    b5.place(x=1100,y=30)
    i=tkinter.Label(f1,image=img10,fg="black",bg="white",font="arial 14 bold")
    i.place(x=1070,y=30)
    b6=tkinter.Label(f1,text="jps123@gmail.com",fg="black",bg="white",font="arial 12 bold")
    b6.place(x=1100,y=50)
    ashk_f=tkinter.Frame(f1,bg="white",highlightthickness=1)
    ashk_f.place(x=1370,y=0,height=105,width=210)
    i=tkinter.Label(ashk_f,image=ashk,fg="black",bg="white",font="arial 14 bold")
    i.place(x=0,y=5)
    
    f2=tkinter.Frame(root,bg="navy blue")
    f2.place(x=0,y=135,height=60,width=1920)
    sch_portal=tkinter.Label(f2,text="Student Portal",fg="white",bg="navy blue",font="arial 20 bold",cursor='hand2')
    sch_portal.place(x=80,y=10)
    # png icon signup
    sign_img=tkinter.PhotoImage(name="simage_5",file="signicon.png")
    i=tkinter.Button(f2,image=sign_img,fg="black",bg="white",font="arial 14 bold",cursor='hand2',bd=0,command=sign)
    i.place(x=1220,y=20)
    signup=tkinter.Button(f2,text="Signup",fg="white",bg="navy blue",font="arial 14 bold",bd=0,activebackground="navy blue",activeforeground="white",command=sign,cursor='hand2')
    signup.place(x=1250,y=15)
    # png icon home
    home_img=tkinter.PhotoImage(name="himage_5",file="home1.png")
    i=tkinter.Button(f2,image=home_img,fg="black",bg="white",font="arial 14 bold",bd=0,cursor='hand2',command=home)
    i.place(x=1370,y=20)
    h1=tkinter.Button(f2,text="Home",fg="white",bg="navy blue",font="arial 14 bold",bd=0,activebackground="navy blue",activeforeground="white",command=home,cursor='hand2')
    h1.place(x=1400,y=15)
    
    f3=tkinter.Frame(root,bg="#d9d9d9")
    f3.place(x=0,y=190,height=600,width=1920)                   
    image1=Image.open("C:\\Users\\ASUS\\onedrive\\Desktop\\school1\\h.jpg")
    photo1=ImageTk.PhotoImage(image1)
    l1=tkinter.Button(f3,image=photo1)
    l1.place(x=0,y=0)

    f4=tkinter.Frame(f3,bg="#EBEBEB")
    f4.place(x=1050,y=130,height=430,width=350)
    st_icon=tkinter.PhotoImage(name="profile",file="login.png") 
    user=tkinter.Label(f4,text="USER LOGIN HERE",fg="black",bg="#EBEBEB",font="ariall 16 bold")
    user.place(x=90,y=10)
    i=tkinter.Label(f4,image=st_icon,fg="black",bg="white",font="arial 14 bold")
    i.place(x=40,y=10)
    user_icon=tkinter.PhotoImage(name="username",file="user1.png")
    l1=tkinter.Label(f4,text="User Name",fg="black",bg="#EBEBEB",font="arial 14")
    l1.place(x=35,y=70)
    i=tkinter.Label(f4,image=user_icon,fg="black",bg="white",font="arial 14 bold")
    i.place(x=5,y=75)
    e1=tkinter.Entry(f4)
    e1.place(x=10,y=110,width=330,height=30)
    psswd_icon=tkinter.PhotoImage(name="passward",file="psswd.png")
    l2=tkinter.Label(f4,text="Passward",fg="black",bg="#EBEBEB",font="arial 16")
    l2.place(x=35,y=150)
    i=tkinter.Label(f4,image=psswd_icon,fg="black",bg="white",font="arial 14 bold")
    i.place(x=5,y=155)
    e2=tkinter.Entry(f4,show="*")
    e2.place(x=10,y=190,width=330,height=30)
    
    f5=tkinter.Frame(f4,bg="#e6e6e6")
    f5.place(x=100,y=220,height=50,width=100)
    image2=Image.open("C:\\Users\\ASUS\\onedrive\\Desktop\\school1\\captcha1.jpg")
    photo2=ImageTk.PhotoImage(image2)
    l1=tkinter.Button(f5,image=photo2)
    l1.place(x=10,y=5)
    
    e3=tkinter.Entry(f4) 
    e3.place(x=10,y=280,width=330,height=30)
    b=tkinter.Button(f4,text="Login",fg="white",bg="blue",font="arial 16 bold",bd=0,activebackground="#EBEBEB",activeforeground="black",cursor='hand2',command=login)
    b.place(x=70,y=330)
    b1=tkinter.Button(f4,text="Cancel",fg="white",bg="red",font="arial 16 bold",bd=0,activebackground="#EBEBEB",activeforeground="black",command=quit,cursor='hand2')
    b1.place(x=200,y=330)
    b2=tkinter.Button(f4,text="forget passward....?",fg="blue",bg="#EBEBEB",bd=0,activebackground="#EBEBEB",activeforeground="blue",command=forget,cursor='hand2')
    b2.place(x=120,y=380)
    frgt=tkinter.Label(f4,text="Support: jharkhandsarkar@gmail.com",fg="black",bg="#EBEBEB",font="arial 12")
    frgt.place(x=40,y=405)
    root.mainloop()
    
    
def school_portal():
    root=tkinter.Toplevel()
    root.geometry("1920x1080")
    
    
            
    f=tkinter.Frame(root,bg="blue")
    f.place(x=0,y=0,height=30,width=1920)
    a1=tkinter.Label(f,text="JPS: Jharkhand Public School (official website)",fg="white",bg="blue",font="arial 12 bold")
    a1.place(x=0,y=5)
    i=tkinter.Label(f,image=img9,fg="black",bg="white",font="arial 14 bold")
    i.place(x=1360,y=5)
    a2=tkinter.Label(f,text="Helpdesk",fg="white",bg="blue",font="arial 12 bold")
    a2.place(x=1400,y=5)
    
    f1=tkinter.Frame(root,bg="white")
    f1.place(x=0,y=30,height=105,width=1920)
    flogo=tkinter.Frame(f1,bg="white",highlightthickness=2)
    flogo.place(x=0,y=0,height=105,width=180)
    # school_img=tkinter.PhotoImage(name="school_1",file="jplogo.png") 
    i=tkinter.Label(flogo,image=school_img,fg="black",bg="white",font="arial 12 bold")
    i.place(x=30,y=0)
    b1=tkinter.Label(f1,text="झारखंड पब्लिक स्कूल",fg="black",bg="white")
    b1.place(x=200,y=5)
    b2=tkinter.Label(f1,text="झारखंड शासन",fg="black",bg="white")
    b2.place(x=220,y=20)
    b3=tkinter.Label(f1,text="____________________________",fg="black",bg="white")
    b3.place(x=200,y=35)
    b4=tkinter.Label(f1,text="Jharkhand Public School",fg="black",bg="white",font="arial 12 bold")
    b4.place(x=200,y=55)    
    b4=tkinter.Label(f1,text="Government of Jharkhand",fg="black",bg="white",font="arial 12 bold")
    b4.place(x=200,y=75)
    b5=tkinter.Label(f1,text="Email Us:",fg="black",bg="white",font="arial 12")
    b5.place(x=1100,y=30)
    i=tkinter.Label(f1,image=img10,fg="black",bg="white",font="arial 14 bold")
    i.place(x=1070,y=30)
    b6=tkinter.Label(f1,text="jps123@gmail.com",fg="black",bg="white",font="arial 12 bold")
    b6.place(x=1100,y=50)
    ashk_f=tkinter.Frame(f1,bg="white",highlightthickness=1)
    ashk_f.place(x=1370,y=0,height=105,width=210)
    i=tkinter.Label(ashk_f,image=ashk,fg="black",bg="white",font="arial 14 bold")
    i.place(x=0,y=5)
    

    # frame
    f2=tkinter.Frame(root,bg="#e6e6e6")
    f2.place(x=0,y=135,height=40,width=1920)
    #png icon home
    home_img=tkinter.PhotoImage(name="himage_5",file="home1.png")
    i=tkinter.Button(f2,image=home_img,fg="black",bg="white",font="arial 14 bold",bd=0,cursor='hand2',command=home)
    i.place(x=90,y=10)
    
    h1=tkinter.Button(f2,text="Home",fg="black",bg="#e6e6e6",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",command=home,cursor='hand2')
    h1.place(x=120,y=10)
    # menubutton
    menubutton=tkinter.Menubutton(f2,text="About us",fg="black",bg="#e6e6e6",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",cursor='hand2')
    menu=tkinter.Menu(menubutton,tearoff=False)
    menubutton["menu"]=menu
    menu.add_command(label="principle message",command=p_msg)
    menubutton.place(x=210,y=10) 

    menubutton=tkinter.Menubutton(f2,text="Academic",fg="black",bg="#e6e6e6",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",cursor='hand2')
    menu=tkinter.Menu(menubutton,tearoff=False)
    menubutton["menu"]=menu
    menu.add_command(label="Academic Calendar",command=calendar)
    menu.add_command(label="List Of Holidays",command=holiday)
    menu.add_command(label="Event at a Schedule",command=event)
    menu.add_command(label="Annual Report 2021-2022",command=report1)   
    menu.add_command(label="Annual Report 2022-2023",command=report2)
    menubutton.place(x=320,y=10) 


    menubutton=tkinter.Menubutton(f2,text="Facilities",fg="black",bg="#e6e6e6",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",cursor='hand2')
    menu=tkinter.Menu(menubutton,tearoff=False)
    menubutton["menu"]=menu
    menu.add_command(label="E-Library",command=library)
    menu.add_command(label="Hostels",command=hostel)
    menu.add_command(label="Canteen",command=canteen)
    menu.add_command(label="Medical Clinic",command=medical)
    menu.add_command(label="Health Club",command=health_club)
    menu.add_command(label="Wi-Fi Campus",command=wifi)
    menubutton.place(x=435,y=10) 

       
    menubutton=tkinter.Menubutton(f2,text="Gallery",fg="black",bg="#e6e6e6",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",cursor='hand2')
    menu=tkinter.Menu(menubutton,tearoff=False)
    menubutton["menu"]=menu
    menu.add_command(label="Image Gallery",command=img_gallery)
    menu.add_command(label="Video Gallery",command=video_gallery)
    menubutton.place(x=545,y=10) 

    c1=tkinter.Button(f2,text="Key Persons",fg="black",bg="#e6e6e6",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",command=key_person,cursor='hand2')
    c1.place(x=650,y=10)
    c1=tkinter.Button(f2,text="Web Information Manager",fg="black",bg="#e6e6e6",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",command=web_desiner,cursor='hand2')
    c1.place(x=775,y=10)
    c1=tkinter.Button(f2,text="Contact",fg="black",bg="#e6e6e6",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",cursor='hand2',command=contact)
    c1.place(x=980,y=10)

    
    f3=tkinter.Frame(root,bg="#e6e6e6")
    f3.place(x=0,y=175,height=600,width=1920)       
    f4=tkinter.Frame(f3,bg="#e6e6e6")
    f4.place(x=0,y=0,height=450,width=1920)
    image1=Image.open("C:\\Users\\ASUS\\onedrive\\Desktop\\jps.jpg")
    photo1=ImageTk.PhotoImage(image1)
    l1=tkinter.Button(f4,image=photo1,bd=0)
    l1.place(x=0,y=0,height=450,width=1920)
    
    
    wel_co=tkinter.Label(f3,text="Welcome To Jharkhand Public School",font="arial 16 bold",fg="black",bg="#e6e6e6",bd=0,activebackground="#e6e6e6",activeforeground="black")
    wel_co.place(x=500,y=470)
   

    root.mainloop()
    

    
def admission():
    root=tkinter.Toplevel()
    root.geometry("1920x1080")
    
    f=tkinter.Frame(root,bg="blue")
    f.place(x=0,y=0,height=30,width=1920)
    a1=tkinter.Label(f,text="JPS: Jharkhand Public School (official website)",fg="white",bg="blue",font="arial 12 bold")
    a1.place(x=0,y=5)
    i=tkinter.Label(f,image=img9,fg="black",bg="white",font="arial 14 bold")
    i.place(x=1360,y=5)
    a2=tkinter.Label(f,text="Helpdesk",fg="white",bg="blue",font="arial 12 bold")
    a2.place(x=1400,y=5)
    
    f1=tkinter.Frame(root,bg="white")
    f1.place(x=0,y=30,height=105,width=1920)
    flogo=tkinter.Frame(f1,bg="white",highlightthickness=2)
    flogo.place(x=0,y=0,height=105,width=180)
    # school_img=tkinter.PhotoImage(name="school_1",file="jplogo.png") 
    i=tkinter.Label(flogo,image=school_img,fg="black",bg="white",font="arial 12 bold")
    i.place(x=30,y=0)
    b1=tkinter.Label(f1,text="झारखंड पब्लिक स्कूल",fg="black",bg="white")
    b1.place(x=200,y=5)
    b2=tkinter.Label(f1,text="झारखंड शासन",fg="black",bg="white")
    b2.place(x=220,y=20)
    b3=tkinter.Label(f1,text="____________________________",fg="black",bg="white")
    b3.place(x=200,y=35)
    b4=tkinter.Label(f1,text="Jharkhand Public School",fg="black",bg="white",font="arial 12 bold")
    b4.place(x=200,y=55)    
    b4=tkinter.Label(f1,text="Government of Jharkhand",fg="black",bg="white",font="arial 12 bold")
    b4.place(x=200,y=75)
    b5=tkinter.Label(f1,text="Email Us:",fg="black",bg="white",font="arial 12")
    b5.place(x=1100,y=30)
    i=tkinter.Label(f1,image=img10,fg="black",bg="white",font="arial 14 bold")
    i.place(x=1070,y=30)
    b6=tkinter.Label(f1,text="jps123@gmail.com",fg="black",bg="white",font="arial 12 bold")
    b6.place(x=1100,y=50)
    ashk_f=tkinter.Frame(f1,bg="white",highlightthickness=1)
    ashk_f.place(x=1370,y=0,height=105,width=210)
    i=tkinter.Label(ashk_f,image=ashk,fg="black",bg="white",font="arial 14 bold")
    i.place(x=0,y=5)
    
    f2=tkinter.Frame(root,bg="#e6e6e6")
    f2.place(x=0,y=135,height=60,width=1920)
    # menu
    c1=tkinter.Button(f2,text="Home",fg="black",bg="#e6e6e6",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",command=home,cursor='hand2')
    c1.place(x=130,y=10)
    
     # menubutton
    menubutton=tkinter.Menubutton(f2,text="About us",fg="black",bg="#e6e6e6",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",cursor='hand2')
    menu=tkinter.Menu(menubutton,tearoff=False)
    menubutton["menu"]=menu
    menu.add_command(label="principle message",command=p_msg)
    menubutton.place(x=210,y=10) 

    menubutton=tkinter.Menubutton(f2,text="Academic",fg="black",bg="#e6e6e6",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",cursor='hand2')
    menu=tkinter.Menu(menubutton,tearoff=False)
    menubutton["menu"]=menu
    menu.add_command(label="Academic Calendar",command=calendar)
    menu.add_command(label="List Of Holidays",command=holiday)
    menu.add_command(label="Event at a Schedule",command=event)
    menu.add_command(label="Annual Report 2021-2022",command=report1)   
    menu.add_command(label="Annual Report 2022-2023",command=report2)
    menubutton.place(x=320,y=10) 


    menubutton=tkinter.Menubutton(f2,text="Facilities",fg="black",bg="#e6e6e6",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",cursor='hand2')
    menu=tkinter.Menu(menubutton,tearoff=False)
    menubutton["menu"]=menu
    menu.add_command(label="E-Library",command=library)
    menu.add_command(label="Hostels",command=hostel)
    menu.add_command(label="Canteen",command=canteen)
    menu.add_command(label="Medical Clinic",command=medical)
    menu.add_command(label="Health Club",command=health_club)
    menu.add_command(label="Wi-Fi Campus",command=wifi)
    menubutton.place(x=435,y=10) 

       
    menubutton=tkinter.Menubutton(f2,text="Gallery",fg="black",bg="#e6e6e6",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",cursor='hand2')
    menu=tkinter.Menu(menubutton,tearoff=False)
    menubutton["menu"]=menu
    menu.add_command(label="Image Gallery",command=img_gallery)
    menu.add_command(label="Video Gallery",command=video_gallery)
    menubutton.place(x=545,y=10) 
     

    c1=tkinter.Button(f2,text="Key Persons",fg="black",bg="#e6e6e6",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",command=key_person,cursor='hand2')
    c1.place(x=650,y=15)
    c1=tkinter.Button(f2,text="Web Information Manager",fg="black",bg="#e6e6e6",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",command=web_desiner,cursor='hand2')
    c1.place(x=775,y=15)
    c1=tkinter.Button(f2,text="Contact",fg="black",bg="#e6e6e6",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",cursor='hand2',command=contact)
    c1.place(x=980,y=15)
    
    
    f3=tkinter.Frame(root,bg="#4d4dff")
    f3.place(x=0,y=190,height=60,width=1920)
    addm=tkinter.Label(f3,text="ADMISSION OF STUDENTS TO A SCHOOL, TRANSFER/MIGRATION OF STUDENTS",fg="white",bg="#4d4dff",font="arial 14 bold",cursor='hand2')
    addm.place(x=335,y=15)
    
    f4=tkinter.Frame(root,bg="#e6e6e6")
    f4.place(x=0,y=250,height=600,width=1920)
    
    f5=tkinter.Frame(f4,bg="#6666ff")
    f5.place(x=400,y=50,height=60,width=700)
    adm1=tkinter.Button(f5,text="Admission: General Condition",fg="white",bg="#6666ff",font="arial  18 bold",bd=0,activebackground="#6666ff",activeforeground="white",cursor='hand2')
    adm1.place(x=170,y=10)
    
    f6=tkinter.Frame(f4,bg="#6666ff")
    f6.place(x=400,y=130,height=60,width=700)
    adm2=tkinter.Button(f6,text="Admission: Specific Recuirements",fg="white",bg="#6666ff",font="arial  18 bold",bd=0,activebackground="#6666ff",activeforeground="white",cursor='hand2')
    adm2.place(x=170,y=10)
    
    f7=tkinter.Frame(f4,bg="#6666ff")
    f7.place(x=400,y=210,height=60,width=700)
    adm3=tkinter.Button(f7,text="Admission Procdure",fg="white",bg="#6666ff",font="arial  18 bold",bd=0,activebackground="#6666ff",activeforeground="white",cursor='hand2')
    adm3.place(x=240,y=10)
    
    f8=tkinter.Frame(f4,bg="#6666ff")
    f8.place(x=400,y=290,height=60,width=700)
    adm4=tkinter.Button(f8,text="Admission To Class I to XI On Account Of Change Of School",fg="white",bg="#6666ff",font="arial  16 bold",bd=0,activebackground="#6666ff",activeforeground="white",cursor='hand2')
    adm4.place(x=40,y=10)
    

    f9=tkinter.Frame(root,bg="navy blue")
    f9.place(x=00,y=680,height=150,width=1920)
    bttm=tkinter.Label(f9,text="© हे शालेय शिक्षण व क्रीडा विभागाचे अधिकृत संकेतस्थळ आहे. सर्व हक्क सुरक्षित.",fg="white",bg="navy blue")
    bttm.place(x=550,y=20)
    bttm=tkinter.Label(f9,text="© 2023 This is the official website of School Education and Sports Department, Govt of Maharashtra.All Rights Reserved.",fg="white",bg="navy blue",font="arial 12 bold")
    bttm.place(x=350,y=50)

  
    root.mainloop()


def examation():
    root=tkinter.Toplevel()
    root.geometry("1920x1080")

    f=tkinter.Frame(root,bg="blue")
    f.place(x=0,y=0,height=30,width=1920)
    a1=tkinter.Label(f,text="JPS: Jharkhand Public School (official website)",fg="white",bg="blue",font="arial 12 bold")
    a1.place(x=0,y=5)
    # png icon helpdesk
    img9=tkinter.PhotoImage(name="image_10",file="helpdesk.png")
    i=tkinter.Label(f,image=img9,fg="black",bg="white",font="arial 14 bold")
    i.place(x=1360,y=5)
    a2=tkinter.Label(f,text="Helpdesk",fg="white",bg="blue",font="arial 12 bold")
    a2.place(x=1400,y=5)


    f1=tkinter.Frame(root,bg="white")
    f1.place(x=0,y=30,height=105,width=1920)
    # logo frame
    flogo=tkinter.Frame(f1,bg="white",highlightthickness=2)
    flogo.place(x=0,y=0,height=105,width=180)
    # png icon school logo
    school_img=tkinter.PhotoImage(name="school_1",file="jplogo.png") 
    i=tkinter.Label(flogo,image=school_img,fg="black",bg="white",font="arial 12 bold")
    i.place(x=30,y=0)

    b1=tkinter.Label(f1,text="झारखंड पब्लिक स्कूल",fg="black",bg="white")
    b1.place(x=200,y=5)
    b2=tkinter.Label(f1,text="झारखंड शासन",fg="black",bg="white")
    b2.place(x=220,y=20)
    b3=tkinter.Label(f1,text="____________________________",fg="black",bg="white")
    b3.place(x=200,y=35)
    b4=tkinter.Label(f1,text="Jharkhand Public School",fg="black",bg="white",font="arial 12 bold")
    b4.place(x=200,y=55)
    b4=tkinter.Label(f1,text="Government of Jharkhand",fg="black",bg="white",font="arial 12 bold")
    b4.place(x=200,y=75)
    b5=tkinter.Label(f1,text="Email Us:",fg="black",bg="white",font="arial 12")
    b5.place(x=1100,y=30)
    # png icon email
    img10=tkinter.PhotoImage(name="image_11",file="email.png")
    i=tkinter.Label(f1,image=img10,fg="black",bg="white",font="arial 14 bold")
    i.place(x=1070,y=30)
    b6=tkinter.Label(f1,text="jps123@gmail.com",fg="black",bg="white",font="arial 12 bold")
    b6.place(x=1100,y=50)
    # ashoka frame
    ashk_f=tkinter.Frame(f1,bg="white",highlightthickness=1)
    ashk_f.place(x=1370,y=0,height=105,width=210)
    # png icon ashoka
    ashk=tkinter.PhotoImage(name="ashokstambh",file="ashk3.png") 
    i=tkinter.Label(ashk_f,image=ashk,fg="black",bg="white",font="arial 14 bold")
    i.place(x=0,y=5)

    # menu frame
    f2=tkinter.Frame(root,bg="blue")
    f2.place(x=0,y=135,height=60,width=1920)
    # menu
    c1=tkinter.Button(f2,text="Home",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="blue",command=home,cursor='hand2')
    c1.place(x=130,y=15)
    # menubutton
    menubutton=tkinter.Menubutton(f2,text="About us",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",cursor='hand2')
    menu=tkinter.Menu(menubutton,tearoff=False)
    menubutton["menu"]=menu
    menu.add_command(label="principle message")
    menubutton.place(x=210,y=15) 

    menubutton=tkinter.Menubutton(f2,text="Academic",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",cursor='hand2')
    menu=tkinter.Menu(menubutton,tearoff=False)
    menubutton["menu"]=menu
    menu.add_command(label="Academic Calendar",command=calendar)
    menu.add_command(label="List Of Holidays",command=holiday)
    menu.add_command(label="Event at a Schedule",command=event)
    menu.add_command(label="Annual Report 2021-2022",command=report1)   
    menu.add_command(label="Annual Report 2022-2023",command=report2)
    menubutton.place(x=320,y=15) 


    menubutton=tkinter.Menubutton(f2,text="Facilities",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",cursor='hand2')
    menu=tkinter.Menu(menubutton,tearoff=False)
    menubutton["menu"]=menu
    menu.add_command(label="E-Library",command=library)
    menu.add_command(label="Hostels",command=hostel)
    menu.add_command(label="Canteen",command=canteen)
    menu.add_command(label="Medical Clinic",command=medical)
    menu.add_command(label="Health Club",command=health_club)
    menu.add_command(label="Wi-Fi Campus",command=wifi)
    menubutton.place(x=435,y=15) 

       
    menubutton=tkinter.Menubutton(f2,text="Gallery",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",cursor='hand2')
    menu=tkinter.Menu(menubutton,tearoff=False)
    menubutton["menu"]=menu
    menu.add_command(label="Image Gallery",command=img_gallery)
    menu.add_command(label="Video Gallery",command=video_gallery)
    menubutton.place(x=545,y=15) 

    c1=tkinter.Button(f2,text="Key Persons",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",command=key_person,cursor='hand2')
    c1.place(x=650,y=15)
    c1=tkinter.Button(f2,text="Web Information Manager",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",command=web_desiner,cursor='hand2')
    c1.place(x=775,y=15)
    c1=tkinter.Button(f2,text="Contact",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",cursor='hand2',command=contact)
    c1.place(x=980,y=15)

    
    f3=tkinter.Frame(root,bg="white")
    f3.place(x=0,y=190,height=600,width=1920)
    l=tkinter.Label(f3,text="Jharkhand Education Portal",fg="red",bg="white",font="arial 16 bold")
    l.place(x=50,y=30)
    l1=tkinter.Label(f3,text="Examation:- Not a Declare Date.",fg="black",bg="white",font="arial 12")
    l1.place(x=55,y=60)

    f4=tkinter.Frame(root,bg="navy blue")
    f4.place(x=00,y=680,height=150,width=1920)
    bttm=tkinter.Label(f4,text="© हे शालेय शिक्षण व क्रीडा विभागाचे अधिकृत संकेतस्थळ आहे. सर्व हक्क सुरक्षित.",fg="white",bg="navy blue")
    bttm.place(x=550,y=20)
    bttm=tkinter.Label(f4,text="© 2024 This is the official website of School Education and Sports Department, Govt of Jharkhand.All Rights Reserved.",fg="white",bg="navy blue",font="arial 12 bold")
    bttm.place(x=350,y=50)
  
    root.mainloop()   



def stf_portal():
    root=tkinter.Toplevel()
    root.geometry("1920x1080")

    f=tkinter.Frame(root,bg="blue")
    f.place(x=0,y=0,height=30,width=1920)
    a1=tkinter.Label(f,text="JPS: Jharkhand Public School (official website)",fg="white",bg="blue",font="arial 12 bold")
    a1.place(x=0,y=5)
    # png icon helpdesk
    img9=tkinter.PhotoImage(name="image_10",file="helpdesk.png")
    i=tkinter.Label(f,image=img9,fg="black",bg="white",font="arial 14 bold")
    i.place(x=1360,y=5)
    a2=tkinter.Label(f,text="Helpdesk",fg="white",bg="blue",font="arial 12 bold")
    a2.place(x=1400,y=5)


    f1=tkinter.Frame(root,bg="white")
    f1.place(x=0,y=30,height=105,width=1920)
    # logo frame
    flogo=tkinter.Frame(f1,bg="white",highlightthickness=2)
    flogo.place(x=0,y=0,height=105,width=180)
    # png icon school logo
    school_img=tkinter.PhotoImage(name="school_1",file="jplogo.png") 
    i=tkinter.Label(flogo,image=school_img,fg="black",bg="white",font="arial 12 bold")
    i.place(x=30,y=0)

    b1=tkinter.Label(f1,text="झारखंड पब्लिक स्कूल",fg="black",bg="white")
    b1.place(x=200,y=5)
    b2=tkinter.Label(f1,text="झारखंड शासन",fg="black",bg="white")
    b2.place(x=220,y=20)
    b3=tkinter.Label(f1,text="____________________________",fg="black",bg="white")
    b3.place(x=200,y=35)
    b4=tkinter.Label(f1,text="Jharkhand Public School",fg="black",bg="white",font="arial 12 bold")
    b4.place(x=200,y=55)
    b4=tkinter.Label(f1,text="Government of Jharkhand",fg="black",bg="white",font="arial 12 bold")
    b4.place(x=200,y=75)
    b5=tkinter.Label(f1,text="Email Us:",fg="black",bg="white",font="arial 12")
    b5.place(x=1100,y=30)
    # png icon email
    img10=tkinter.PhotoImage(name="image_11",file="email.png")
    i=tkinter.Label(f1,image=img10,fg="black",bg="white",font="arial 14 bold")
    i.place(x=1070,y=30)
    b6=tkinter.Label(f1,text="jps123@gmail.com",fg="black",bg="white",font="arial 12 bold")
    b6.place(x=1100,y=50)
    # ashoka frame
    ashk_f=tkinter.Frame(f1,bg="white",highlightthickness=1)
    ashk_f.place(x=1370,y=0,height=105,width=210)
    # png icon ashoka
    ashk=tkinter.PhotoImage(name="ashokstambh",file="ashk3.png") 
    i=tkinter.Label(ashk_f,image=ashk,fg="black",bg="white",font="arial 14 bold")
    i.place(x=0,y=5)

    # menu frame
    f2=tkinter.Frame(root,bg="blue")
    f2.place(x=0,y=135,height=60,width=1920)
    # menu
    c1=tkinter.Button(f2,text="Home",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="blue",command=home,cursor='hand2')
    c1.place(x=130,y=15)
    # menubutton
    menubutton=tkinter.Menubutton(f2,text="About us",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",cursor='hand2')
    menu=tkinter.Menu(menubutton,tearoff=False)
    menubutton["menu"]=menu
    menu.add_command(label="principle message",command=p_msg)
    menubutton.place(x=210,y=15) 

    menubutton=tkinter.Menubutton(f2,text="Academic",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",cursor='hand2')
    menu=tkinter.Menu(menubutton,tearoff=False)
    menubutton["menu"]=menu
    menu.add_command(label="Academic Calendar",command=calendar)
    menu.add_command(label="List Of Holidays",command=holiday)
    menu.add_command(label="Event at a Schedule",command=event)
    menu.add_command(label="Annual Report 2021-2022",command=report1)   
    menu.add_command(label="Annual Report 2022-2023",command=report2)
    menubutton.place(x=320,y=15) 


    menubutton=tkinter.Menubutton(f2,text="Facilities",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",cursor='hand2')
    menu=tkinter.Menu(menubutton,tearoff=False)
    menubutton["menu"]=menu
    menu.add_command(label="E-Library",command=library)
    menu.add_command(label="Hostels",command=hostel)
    menu.add_command(label="Canteen",command=canteen)
    menu.add_command(label="Medical Clinic",command=medical)
    menu.add_command(label="Health Club",command=health_club)
    menu.add_command(label="Wi-Fi Campus",command=wifi)
    menubutton.place(x=435,y=15) 

       
    menubutton=tkinter.Menubutton(f2,text="Gallery",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",cursor='hand2')
    menu=tkinter.Menu(menubutton,tearoff=False)
    menubutton["menu"]=menu
    menu.add_command(label="Image Gallery",command=img_gallery)
    menu.add_command(label="Video Gallery",command=video_gallery)
    menubutton.place(x=545,y=15) 

    c1=tkinter.Button(f2,text="Key Persons",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",command=key_person,cursor='hand2')
    c1.place(x=650,y=15)
    c1=tkinter.Button(f2,text="Web Information Manager",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",command=web_desiner,cursor='hand2')
    c1.place(x=775,y=15)
    c1=tkinter.Button(f2,text="Contact",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",cursor='hand2')
    c1.place(x=980,y=15)

    
    f3=tkinter.Frame(root,bg="white")
    f3.place(x=0,y=190,height=700,width=1920)
    heading=tkinter.Label(f3,text="JHARKHAND PUBLIC SCHOOL, kODERMA, JHARKHAD",fg="black",bg="white",font="arial 24 bold")
    heading.place(x=370,y=10)
    heading1=tkinter.Label(f3,text="STAFF DETALS FOR SESION 2024-2025",fg="black",bg="white",font="arial 18 bold")
    heading1.place(x=550,y=50)
    image=Image.open("C:\\Users\\ASUS\\onedrive\\Desktop\\school1\\stafimg1.png")
    photo=ImageTk.PhotoImage(image)
    l1=tkinter.Label(f3,image=photo,bd=0)
    l1.place(x=300,y=100)

    
    f4=tkinter.Frame(root,bg="navy blue")
    f4.place(x=00,y=700,height=150,width=1920)
    bttm=tkinter.Label(f4,text="© हे शालेय शिक्षण व क्रीडा विभागाचे अधिकृत संकेतस्थळ आहे. सर्व हक्क सुरक्षित.",fg="white",bg="navy blue")
    bttm.place(x=550,y=20)
    bttm=tkinter.Label(f4,text="© 2024 This is the official website of School Education and Sports Department, Govt of Jharkhand.All Rights Reserved.",fg="white",bg="navy blue",font="arial 12 bold")
    bttm.place(x=350,y=50)
    

  
    root.mainloop()

def admin_forget():
    def admin_update():
        pswd = e1.get()
        pswd =e2.get()
        c_pswd=e3.get()
        if e1.get()=='' or e2.get()=='' or e3.get()=='':
            messagebox.showinfo('ALERT','Please enter fiels you want to update!')
        elif e2.get() != e3.get():
            messagebox.showinfo('error','Please enter correct your confirm password')
        else:
            con = pymysql.connect(host="localhost", user="root", password="", database="admin_login")
            cursor = con.cursor()
            cursor.execute("update admin_data set e2 = '"+ pswd +"', e2='"+ c_pswd +"', where  e1='"+ pswd +"'")
            cursor.execute("commit")
            messagebox.showinfo("Status", "Successfully Updated") 
        
            con.close()
        
    root=tkinter.Toplevel()
    root.geometry("1920x1080")
    
    f=tkinter.Frame(root,bg="blue")
    f.place(x=0,y=0,height=30,width=1920)
    a1=tkinter.Label(f,text="JPS: Jharkhand Public School (official website)",fg="white",bg="blue",font="arial 12 bold")
    a1.place(x=0,y=5)
    # png icon helpdesk
    img9=tkinter.PhotoImage(name="image_10",file="helpdesk.png")
    i=tkinter.Label(f,image=img9,fg="black",bg="white",font="arial 14 bold")
    i.place(x=1360,y=5)
    a2=tkinter.Label(f,text="Helpdesk",fg="white",bg="blue",font="arial 12 bold")
    a2.place(x=1400,y=5)


    f1=tkinter.Frame(root,bg="white")
    f1.place(x=0,y=30,height=105,width=1920)
    # logo frame
    flogo=tkinter.Frame(f1,bg="white",highlightthickness=2)
    flogo.place(x=0,y=0,height=105,width=180)
    # png icon school logo
    school_img=tkinter.PhotoImage(name="school_1",file="jplogo.png") 
    i=tkinter.Label(flogo,image=school_img,fg="black",bg="white",font="arial 12 bold")
    i.place(x=30,y=0)

    b1=tkinter.Label(f1,text="झारखंड पब्लिक स्कूल",fg="black",bg="white")
    b1.place(x=200,y=5)
    b2=tkinter.Label(f1,text="झारखंड शासन",fg="black",bg="white")
    b2.place(x=220,y=20)
    b3=tkinter.Label(f1,text="____________________________",fg="black",bg="white")
    b3.place(x=200,y=35)
    b4=tkinter.Label(f1,text="Jharkhand Public School",fg="black",bg="white",font="arial 12 bold")
    b4.place(x=200,y=55)
    b4=tkinter.Label(f1,text="Government of Jharkhand",fg="black",bg="white",font="arial 12 bold")
    b4.place(x=200,y=75)
    b5=tkinter.Label(f1,text="Email Us:",fg="black",bg="white",font="arial 12")
    b5.place(x=1100,y=30)
    # png icon email
    img10=tkinter.PhotoImage(name="image_11",file="email.png")
    i=tkinter.Label(f1,image=img10,fg="black",bg="white",font="arial 14 bold")
    i.place(x=1070,y=30)
    b6=tkinter.Label(f1,text="jps123@gmail.com",fg="black",bg="white",font="arial 12 bold")
    b6.place(x=1100,y=50)
    # ashoka frame
    ashk_f=tkinter.Frame(f1,bg="white",highlightthickness=1)
    ashk_f.place(x=1370,y=0,height=105,width=210)
    # png icon ashoka
    ashk=tkinter.PhotoImage(name="ashokstambh",file="ashk3.png") 
    i=tkinter.Label(ashk_f,image=ashk,fg="black",bg="white",font="arial 14 bold")
    i.place(x=0,y=5)

    # menu frame
    f2=tkinter.Frame(root,bg="blue")
    f2.place(x=0,y=135,height=60,width=1920)
    # menu
    c1=tkinter.Button(f2,text="Home",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="blue",command=home,cursor='hand2')
    c1.place(x=130,y=15)
    # menubutton
    menubutton=tkinter.Menubutton(f2,text="About us",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",cursor='hand2')
    menu=tkinter.Menu(menubutton,tearoff=False)
    menubutton["menu"]=menu
    menu.add_command(label="principle message",command=p_msg)
    menubutton.place(x=210,y=15) 

    menubutton=tkinter.Menubutton(f2,text="Academic",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",cursor='hand2')
    menu=tkinter.Menu(menubutton,tearoff=False)
    menubutton["menu"]=menu
    menu.add_command(label="Academic Calendar",command=calendar)
    menu.add_command(label="List Of Holidays",command=holiday)
    menu.add_command(label="Event at a Schedule",command=event)
    menu.add_command(label="Annual Report 2021-2022",command=report1)   
    menu.add_command(label="Annual Report 2022-2023",command=report2)
    menubutton.place(x=320,y=15) 


    menubutton=tkinter.Menubutton(f2,text="Facilities",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",cursor='hand2')
    menu=tkinter.Menu(menubutton,tearoff=False)
    menubutton["menu"]=menu
    menu.add_command(label="E-Library",command=library)
    menu.add_command(label="Hostels",command=hostel)
    menu.add_command(label="Canteen",command=canteen)
    menu.add_command(label="Medical Clinic",command=medical)
    menu.add_command(label="Health Club",command=health_club)
    menu.add_command(label="Wi-Fi Campus",command=wifi)
    menubutton.place(x=435,y=15) 

       
    menubutton=tkinter.Menubutton(f2,text="Gallery",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",cursor='hand2')
    menu=tkinter.Menu(menubutton,tearoff=False)
    menubutton["menu"]=menu
    menu.add_command(label="Image Gallery",command=img_gallery)
    menu.add_command(label="Video Gallery",command=video_gallery)
    menubutton.place(x=545,y=15) 
    c1=tkinter.Button(f2,text="Key Persons",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",command=key_person,cursor='hand2')
    c1.place(x=650,y=15)
    c1=tkinter.Button(f2,text="Web Information Manager",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",command=web_desiner,cursor='hand2')
    c1.place(x=775,y=15)
    c1=tkinter.Button(f2,text="Contact",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",cursor='hand2',command=contact)
    c1.place(x=980,y=15)

    
    f3=tkinter.Frame(root,bg="white")
    f3.place(x=0,y=190,height=600,width=1920)
    l=tkinter.Label(f3,text="Jharkhand Education Portal",fg="red",bg="white",font="arial 16 bold")
    l.place(x=50,y=30)
    l1=tkinter.Label(f3,text="Teacher's Information details will be availble soon.",fg="black",bg="white",font="arial 12")
    l1.place(x=55,y=60)
    
    f4=tkinter.Frame(root,bg="white")
    f4.place(x=0,y=190,height=500,width=1920)
    image=Image.open("C:\\Users\\ASUS\\onedrive\\Desktop\\school1\\admin1.webp")
    photo=ImageTk.PhotoImage(image)
    l1=tkinter.Button(f4,image=photo,bd=0)
    l1.place(x=0,y=0,height=500,width=1920)
    f6=tkinter.Frame(f4,bg="navy blue")
    f6.place(x=550,y=80,height=300,width=490)
    f7=tkinter.Frame(f6,bg="white")
    f7.place(x=10,y=10,height=280,width=470)
    adm=tkinter.Label(f7,text="Reset your password",fg="sky blue",bg="white",font="arial 18 bold")
    adm.place(x=120,y=10)
    l1=tkinter.Label(f7,text="Username",fg="black",bg="white",font="arial 12 bold")
    l1.place(x=30,y=50)
    # png icon username
    user_icon=tkinter.PhotoImage(name="username",file="user1.png")
    i=tkinter.Label(f7,image=user_icon,fg="black",bg="white",font="arial 14 bold")
    i.place(x=5,y=50)
    e1=tkinter.Entry(f7,bg="white")
    e1.place(x=20,y=80,width=400,height=30)
    
    l2=tkinter.Label(f7,text="New password",fg="black",bg="white",font="arial 12 bold")
    l2.place(x=30,y=110)
    # png icon psswd
    psswd_icon=tkinter.PhotoImage(name="passward",file="psswd.png")
    i=tkinter.Label(f7,image=psswd_icon,fg="black",bg="white",font="arial 14 bold")
    i.place(x=5,y=115)
    e2=tkinter.Entry(f7,bg="white")
    e2.place(x=20,y=140,width=400,height=30)
    
    l3=tkinter.Label(f7,text="Confirm password",fg="black",bg="white",font="arial 12 bold")
    l3.place(x=30,y=170)
    # png icon pswd 
    psswd1_icon=tkinter.PhotoImage(name="passward1",file="psswd.png")
    i=tkinter.Label(f7,image=psswd1_icon,fg="black",bg="white",font="arial 14 bold")
    i.place(x=5,y=175)
    e3=tkinter.Entry(f7,bg="white")
    e3.place(x=20,y=200,width=400,height=30)
    
    l4=tkinter.Button(f7,text="Submit",bg="white",fg="black",font="arial 16 bold",bd=0,command=admin_update)
    l4.place(x=190,y=240)
    
    f11=tkinter.Frame(root,bg="navy blue")
    f11.place(x=00,y=680,height=150,width=1920)
    bttm=tkinter.Label(f11,text="© हे शालेय शिक्षण व क्रीडा विभागाचे अधिकृत संकेतस्थळ आहे. सर्व हक्क सुरक्षित.",fg="white",bg="navy blue",font="arial 12 bold")
    bttm.place(x=550,y=20)
    bttm=tkinter.Label(f11,text="© 2024 This is the official website of School Education and Sports Department, Govt of Jharkhand.All Rights Reserved.",fg="white",bg="navy blue",font="arial 12 bold")
    bttm.place(x=350,y=50)
    
    root.mainloop()
    

     

 
def admin_sign():
    root=tkinter.Toplevel()
    root.geometry("1920x1080")
    
    f=tkinter.Frame(root,bg="blue")
    f.place(x=0,y=0,height=30,width=1920)
    a1=tkinter.Label(f,text="JPS: Jharkhand Public School (official website)",fg="white",bg="blue",font="arial 12 bold")
    a1.place(x=0,y=5)
    # png icon helpdesk
    img9=tkinter.PhotoImage(name="image_10",file="helpdesk.png")
    i=tkinter.Label(f,image=img9,fg="black",bg="white",font="arial 14 bold")
    i.place(x=1360,y=5)
    a2=tkinter.Label(f,text="Helpdesk",fg="white",bg="blue",font="arial 12 bold")
    a2.place(x=1400,y=5)


    f1=tkinter.Frame(root,bg="white")
    f1.place(x=0,y=30,height=105,width=1920)
    # logo frame
    flogo=tkinter.Frame(f1,bg="white",highlightthickness=2)
    flogo.place(x=0,y=0,height=105,width=180)
    # png icon school logo
    school_img=tkinter.PhotoImage(name="school_1",file="jplogo.png") 
    i=tkinter.Label(flogo,image=school_img,fg="black",bg="white",font="arial 12 bold")
    i.place(x=30,y=0)

    b1=tkinter.Label(f1,text="झारखंड पब्लिक स्कूल",fg="black",bg="white")
    b1.place(x=200,y=5)
    b2=tkinter.Label(f1,text="झारखंड शासन",fg="black",bg="white")
    b2.place(x=220,y=20)
    b3=tkinter.Label(f1,text="____________________________",fg="black",bg="white")
    b3.place(x=200,y=35)
    b4=tkinter.Label(f1,text="Jharkhand Public School",fg="black",bg="white",font="arial 12 bold")
    b4.place(x=200,y=55)
    b4=tkinter.Label(f1,text="Government of Jharkhand",fg="black",bg="white",font="arial 12 bold")
    b4.place(x=200,y=75)
    b5=tkinter.Label(f1,text="Email Us:",fg="black",bg="white",font="arial 12")
    b5.place(x=1100,y=30)
    # png icon email
    img10=tkinter.PhotoImage(name="image_11",file="email.png")
    i=tkinter.Label(f1,image=img10,fg="black",bg="white",font="arial 14 bold")
    i.place(x=1070,y=30)
    b6=tkinter.Label(f1,text="jps123@gmail.com",fg="black",bg="white",font="arial 12 bold")
    b6.place(x=1100,y=50)
    # ashoka frame
    ashk_f=tkinter.Frame(f1,bg="white",highlightthickness=1)
    ashk_f.place(x=1370,y=0,height=105,width=210)
    # png icon ashoka
    ashk=tkinter.PhotoImage(name="ashokstambh",file="ashk3.png") 
    i=tkinter.Label(ashk_f,image=ashk,fg="black",bg="white",font="arial 14 bold")
    i.place(x=0,y=5)

    # menu frame
    f2=tkinter.Frame(root,bg="blue")
    f2.place(x=0,y=135,height=60,width=1920)
    # menu
    c1=tkinter.Button(f2,text="Home",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="blue",command=home,cursor='hand2')
    c1.place(x=130,y=15)
    # menubutton
    menubutton=tkinter.Menubutton(f2,text="About us",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",cursor='hand2')
    menu=tkinter.Menu(menubutton,tearoff=False)
    menubutton["menu"]=menu
    menu.add_command(label="principle message",command=p_msg)
    menubutton.place(x=210,y=15) 

    menubutton=tkinter.Menubutton(f2,text="Academic",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",cursor='hand2')
    menu=tkinter.Menu(menubutton,tearoff=False)
    menubutton["menu"]=menu
    menu.add_command(label="Academic Calendar",command=calendar)
    menu.add_command(label="List Of Holidays",command=holiday)
    menu.add_command(label="Event at a Schedule",command=event)
    menu.add_command(label="Annual Report 2021-2022",command=report1)   
    menu.add_command(label="Annual Report 2022-2023",command=report2)
    menubutton.place(x=320,y=15) 


    menubutton=tkinter.Menubutton(f2,text="Facilities",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",cursor='hand2')
    menu=tkinter.Menu(menubutton,tearoff=False)
    menubutton["menu"]=menu
    menu.add_command(label="E-Library",command=library)
    menu.add_command(label="Hostels",command=hostel)
    menu.add_command(label="Canteen",command=canteen)
    menu.add_command(label="Medical Clinic",command=medical)
    menu.add_command(label="Health Club",command=health_club)
    menu.add_command(label="Wi-Fi Campus",command=wifi)
    menubutton.place(x=435,y=15) 

       
    menubutton=tkinter.Menubutton(f2,text="Gallery",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",cursor='hand2')
    menu=tkinter.Menu(menubutton,tearoff=False)
    menubutton["menu"]=menu
    menu.add_command(label="Image Gallery",command=img_gallery)
    menu.add_command(label="Video Gallery",command=video_gallery)
    menubutton.place(x=545,y=15) 

    c1=tkinter.Button(f2,text="Key Persons",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",command=key_person,cursor='hand2')
    c1.place(x=650,y=15)
    c1=tkinter.Button(f2,text="Web Information Manager",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",command=web_desiner,cursor='hand2')
    c1.place(x=775,y=15)
    c1=tkinter.Button(f2,text="Contact",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",cursor='hand2',command=contact)
    c1.place(x=980,y=15)

    
    f3=tkinter.Frame(root,bg="white")
    f3.place(x=0,y=190,height=600,width=1920)
    l=tkinter.Label(f3,text="Jharkhand Education Portal",fg="red",bg="white",font="arial 16 bold")
    l.place(x=50,y=30)
    l1=tkinter.Label(f3,text="Teacher's Information details will be availble soon.",fg="black",bg="white",font="arial 12")
    l1.place(x=55,y=60)
    
    f4=tkinter.Frame(root,bg="white")
    f4.place(x=0,y=190,height=730,width=1920)
    image=Image.open("C:\\Users\\ASUS\\onedrive\\Desktop\\school1\\admin1.webp")
    photo=ImageTk.PhotoImage(image)
    l1=tkinter.Button(f4,image=photo,bd=0)
    l1.place(x=0,y=0,height=550,width=1920)
    
    # admin database connecetivity
    def admin_submit():
        
        if n.get()=='' or e.get()=='' or p.get()=='' or cp.get()=='':
            messagebox.showinfo('error',"all fields are required")
        elif p.get() != cp.get():
            messagebox.showinfo('error','Please enter correct your confirm password')
        else:
            messagebox.showinfo('sucessfully')
            user=n.get()
            email=e.get()
            phone=no.get()
            pswd=p.get()
            c_pswd=cp.get()
            mycon = pymysql.connect(host="localhost",user="root",password="",db="admin_login")
            mycur = mycon.cursor()
            mycur.execute("INSERT INTO admin_data (user,email,phone,pswd,c_pswd) VALUES (\'"+user+"\',\'"+email+"\', \'"+phone+"\',\'"+pswd+"\',\'"+c_pswd+"\');")
            mycon.commit()
            mycon.close()
     

            if(mycon):
                messagebox.showinfo('connection sucessfullly')
            else:
                messagebox.error('faield')
    n=tkinter.StringVar()
    e=tkinter.StringVar()
    no=tkinter.StringVar()
    p=tkinter.StringVar()
    cp=tkinter.StringVar()
    
    main_f=tkinter.Frame(f4,bg="navy blue")
    main_f.place(x=560,y=20,height=500,width=500)
    admin_f=tkinter.Frame(main_f,bg="white") 
    admin_f.place(x=5,y=5,height=490,width=490)
    adminl1=tkinter.Label(admin_f,text="Admin Register Here",fg="sky blue",bg="white",font="arial 20 bold")
    adminl1.place(x=110,y=10)
    ad=tkinter.Label(admin_f,text="Full Name ",fg="black",bg="white",font="arial 14 bold")
    ad.place(x=20,y=60)
    entry=tkinter.Entry(admin_f,bg="white",font="arial 10",textvariable=n)
    entry.place(x=20,y=90,height=30,width=440)
    admin_class1=tkinter.Label(admin_f,text="Class you teach",fg="black",bg="white",font="arial 14 bold")
    admin_class1.place(x=20,y=130)
    admin_class=tkinter.Checkbutton(admin_f,text="I to IV",fg="black",bg="white",font="arial 10 bold")
    admin_class.place(x=20,y=160)
    admin_class=tkinter.Checkbutton(admin_f,text="V to VIII",fg="black",bg="white",font="arial 10 bold")
    admin_class.place(x=100,y=160)
    admin_class=tkinter.Checkbutton(admin_f,text="IX to X",fg="black",bg="white",font="arial 10 bold")
    admin_class.place(x=170,y=160)
    email=tkinter.Label(admin_f,text=" E-mail",fg="black",bg="white",font="arial 12 bold")
    email.place(x=20,y=190)
    email1=tkinter.Entry(admin_f,bg="white",textvariable=e)
    email1.place(x=20,y=215,height=30,width=440)
    phone=tkinter.Label(admin_f,text=" Phone No.",fg="black",bg="white",font="arial 12 bold")
    phone.place(x=20,y=250)
    phone1=tkinter.Entry(admin_f,bg="white",textvariable=no)
    phone1.place(x=20,y=275,height=30,width=440)
    pswd=tkinter.Label(admin_f,text=" Password",fg="black",bg="white",font="arial 12 bold")
    pswd.place(x=20,y=310)
    pswd1=tkinter.Entry(admin_f,bg="white",textvariable=p)
    pswd1.place(x=20,y=335,height=30,width=440)
    c_pswd=tkinter.Label(admin_f,text="Confirm Password",fg="black",bg="white",font="arial 12 bold")
    c_pswd.place(x=20,y=370)
    c_pswd=tkinter.Entry(admin_f,bg="white",textvariable=cp)
    c_pswd.place(x=20,y=395,height=30,width=440)
    check=tkinter.Checkbutton(admin_f,text="I agree all the term's and condition",fg="black",bg="white",font="arial 10 bold")
    check.place(x=30,y=430)
    al=tkinter.Label(admin_f,text="Already have an account.",fg="black",bg="white",font="arial 10 bold")
    al.place(x=10,y=460)
    al_ac=tkinter.Button(admin_f,text="Login",fg="red",bg="white",bd=0,font="arial 10 bold",command=tech_portal)
    al_ac.place(x=175,y=460)
    bttn=tkinter.Button(admin_f,text="Submit",bg="red",fg="white",font="aral 12 bold",cursor='hand2',command=admin_submit)
    bttn.place(x=340,y=435)
    
    
    f5=tkinter.Frame(root,bg="navy blue")
    f5.place(x=00,y=730,height=150,width=1920)
    bttm=tkinter.Label(f5,text="© हे शालेय शिक्षण व क्रीडा विभागाचे अधिकृत संकेतस्थळ आहे. सर्व हक्क सुरक्षित.",fg="white",bg="navy blue")
    bttm.place(x=550,y=10)
    bttm=tkinter.Label(f5,text="© 2024 This is the official website of School Education and Sports Department, Govt of Jharkhand.All Rights Reserved.",fg="white",bg="navy blue",font="arial 8 bold")
    bttm.place(x=370,y=30)
    
    root.mainloop()   
    
    
def tech_portal():
    # admin data fetching code
    def admin_login():
        if e1.get()=="" or e2.get()=="":
            messagebox.showinfo('error','all filed required')
        else:
            mycon = pymysql.connect(host="localhost",user="root",password="",db="admin_login")
            mycur = mycon.cursor()
            mycur.execute("select * from admin_data where email=%s and pswd=%s",(e1.get(),e2.get()))
            row=mycur.fetchone()
            if(row==None):
                messagebox.showinfo('Envaild','invaild username or password')
            else:
                messagebox.showinfo('Sucessfully')
                
            mycon.commit()
            mycon.close()
    
    root=tkinter.Toplevel()
    root.geometry("1920x1080")
    
    f=tkinter.Frame(root,bg="blue")
    f.place(x=0,y=0,height=30,width=1920)
    a1=tkinter.Label(f,text="JPS: Jharkhand Public School (official website)",fg="white",bg="blue",font="arial 12 bold")
    a1.place(x=0,y=5)
    # png icon helpdesk
    img9=tkinter.PhotoImage(name="image_10",file="helpdesk.png")
    i=tkinter.Label(f,image=img9,fg="black",bg="white",font="arial 14 bold")
    i.place(x=1360,y=5)
    a2=tkinter.Label(f,text="Helpdesk",fg="white",bg="blue",font="arial 12 bold")
    a2.place(x=1400,y=5)


    f1=tkinter.Frame(root,bg="white")
    f1.place(x=0,y=30,height=105,width=1920)
    # logo frame
    flogo=tkinter.Frame(f1,bg="white",highlightthickness=2)
    flogo.place(x=0,y=0,height=105,width=180)
    # png icon school logo
    school_img=tkinter.PhotoImage(name="school_1",file="jplogo.png") 
    i=tkinter.Label(flogo,image=school_img,fg="black",bg="white",font="arial 12 bold")
    i.place(x=30,y=0)

    b1=tkinter.Label(f1,text="झारखंड पब्लिक स्कूल",fg="black",bg="white")
    b1.place(x=200,y=5)
    b2=tkinter.Label(f1,text="झारखंड शासन",fg="black",bg="white")
    b2.place(x=220,y=20)
    b3=tkinter.Label(f1,text="____________________________",fg="black",bg="white")
    b3.place(x=200,y=35)
    b4=tkinter.Label(f1,text="Jharkhand Public School",fg="black",bg="white",font="arial 12 bold")
    b4.place(x=200,y=55)
    b4=tkinter.Label(f1,text="Government of Jharkhand",fg="black",bg="white",font="arial 12 bold")
    b4.place(x=200,y=75)
    b5=tkinter.Label(f1,text="Email Us:",fg="black",bg="white",font="arial 12")
    b5.place(x=1100,y=30)
    # png icon email
    img10=tkinter.PhotoImage(name="image_11",file="email.png")
    i=tkinter.Label(f1,image=img10,fg="black",bg="white",font="arial 14 bold")
    i.place(x=1070,y=30)
    b6=tkinter.Label(f1,text="jps123@gmail.com",fg="black",bg="white",font="arial 12 bold")
    b6.place(x=1100,y=50)
    # ashoka frame
    ashk_f=tkinter.Frame(f1,bg="white",highlightthickness=1)
    ashk_f.place(x=1370,y=0,height=105,width=210)
    # png icon ashoka
    ashk=tkinter.PhotoImage(name="ashokstambh",file="ashk3.png") 
    i=tkinter.Label(ashk_f,image=ashk,fg="black",bg="white",font="arial 14 bold")
    i.place(x=0,y=5)

    # menu frame
    f2=tkinter.Frame(root,bg="blue")
    f2.place(x=0,y=135,height=60,width=1920)
    # menu
    c1=tkinter.Button(f2,text="Home",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="blue",command=home,cursor='hand2')
    c1.place(x=130,y=15)
    # menubutton
    menubutton=tkinter.Menubutton(f2,text="About us",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",cursor='hand2')
    menu=tkinter.Menu(menubutton,tearoff=False)
    menubutton["menu"]=menu
    menu.add_command(label="principle message",command=p_msg)
    menubutton.place(x=210,y=15) 

    menubutton=tkinter.Menubutton(f2,text="Academic",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",cursor='hand2')
    menu=tkinter.Menu(menubutton,tearoff=False)
    menubutton["menu"]=menu
    menu.add_command(label="Academic Calendar",command=calendar)
    menu.add_command(label="List Of Holidays",command=holiday)
    menu.add_command(label="Event at a Schedule",command=event)
    menu.add_command(label="Annual Report 2021-2022",command=report1)   
    menu.add_command(label="Annual Report 2022-2023",command=report2)
    menubutton.place(x=320,y=15) 


    menubutton=tkinter.Menubutton(f2,text="Facilities",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",cursor='hand2')
    menu=tkinter.Menu(menubutton,tearoff=False)
    menubutton["menu"]=menu
    menu.add_command(label="E-Library",command=library)
    menu.add_command(label="Hostels",command=hostel)
    menu.add_command(label="Canteen",command=canteen)
    menu.add_command(label="Medical Clinic",command=medical)
    menu.add_command(label="Health Club",command=health_club)
    menu.add_command(label="Wi-Fi Campus",command=wifi)
    menubutton.place(x=435,y=15) 

       
    menubutton=tkinter.Menubutton(f2,text="Gallery",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",cursor='hand2')
    menu=tkinter.Menu(menubutton,tearoff=False)
    menubutton["menu"]=menu
    menu.add_command(label="Image Gallery",command=img_gallery)
    menu.add_command(label="Video Gallery",command=video_gallery)
    menubutton.place(x=545,y=15) 

    c1=tkinter.Button(f2,text="Key Persons",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",command=key_person,cursor='hand2')
    c1.place(x=650,y=15)
    c1=tkinter.Button(f2,text="Web Information Manager",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",command=web_desiner,cursor='hand2')
    c1.place(x=775,y=15)
    c1=tkinter.Button(f2,text="Contact",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",cursor='hand2',command=contact)
    c1.place(x=980,y=15)

    
    f3=tkinter.Frame(root,bg="white")
    f3.place(x=0,y=190,height=600,width=1920)
    l=tkinter.Label(f3,text="Jharkhand Education Portal",fg="red",bg="white",font="arial 16 bold")
    l.place(x=50,y=30)
    l1=tkinter.Label(f3,text="Teacher's Information details will be availble soon.",fg="black",bg="white",font="arial 12")
    l1.place(x=55,y=60)
    
    f4=tkinter.Frame(root,bg="white")
    f4.place(x=0,y=190,height=500,width=1920)
    image=Image.open("C:\\Users\\ASUS\\onedrive\\Desktop\\school1\\admin1.webp")
    photo=ImageTk.PhotoImage(image)
    l1=tkinter.Button(f4,image=photo,bd=0)
    l1.place(x=0,y=0,height=500,width=1920)
    f6=tkinter.Frame(f4,bg="navy blue")
    f6.place(x=550,y=80,height=270,width=490)
    f7=tkinter.Frame(f6,bg="white")
    f7.place(x=10,y=10,height=250,width=470)
    adm=tkinter.Label(f7,text="Please enter your information",fg="sky blue",bg="white",font="arial 18 bold")
    adm.place(x=70,y=10)
    user=tkinter.Label(f7,text="Username",fg="black",bg="white",font="arial 14 bold")
    user.place(x=30,y=70)
    # png icon user
    user_icon=tkinter.PhotoImage(name="username",file="user1.png")
    i=tkinter.Label(f7,image=user_icon,fg="black",bg="white",font="arial 14 bold")
    i.place(x=5,y=75)
    e1=tkinter.Entry(f7)
    e1.place(x=30,y=100,width=400,height=30)
    pswd=tkinter.Label(f7,text="Passward",fg="black",bg="white",font="arial 14 bold")
    pswd.place(x=30,y=130)
    # png icon pswd
    psswd_icon=tkinter.PhotoImage(name="passward",file="psswd.png")
    i=tkinter.Label(f7,image=psswd_icon,fg="black",bg="white",font="arial 14 bold")
    i.place(x=5,y=135)
    e2=tkinter.Entry(f7)
    e2.place(x=30,y=160,width=400,height=30)
    
    sign1=tkinter.Label(f7,text="Dont have an account?",fg="black",bg="white",font="arial 8 bold")
    sign1.place(x=20,y=210)
    sign2=tkinter.Button(f7,text="Sign in",fg="blue",bg="white",font="arial 10 bold",cursor='hand2',bd=0,command=admin_sign)
    sign2.place(x=145,y=210)
    forg=tkinter.Button(f7,text="forget passwod",fg="red",bg="white",font="arial 8 bold",cursor='hand2',bd=0,command=admin_forget)
    forg.place(x=30,y=225)
    bttn=tkinter.Button(f7,text="Login",bg="red",fg="white",font="aral 16 bold",cursor='hand2',command=admin_login)
    bttn.place(x=340,y=190)
    
    f5=tkinter.Frame(root,bg="navy blue")
    f5.place(x=00,y=680,height=150,width=1920)
    bttm=tkinter.Label(f5,text="© हे शालेय शिक्षण व क्रीडा विभागाचे अधिकृत संकेतस्थळ आहे. सर्व हक्क सुरक्षित.",fg="white",bg="navy blue")
    bttm.place(x=550,y=20)
    bttm=tkinter.Label(f5,text="© 2024 This is the official website of School Education and Sports Department, Govt of Jharkhand.All Rights Reserved.",fg="white",bg="navy blue",font="arial 12 bold")
    bttm.place(x=350,y=50)
    
    root.mainloop()
    

       
    
def marks():
    root=tkinter.Toplevel()
    root.geometry("1920x1080")

    f=tkinter.Frame(root,bg="blue")
    f.place(x=0,y=0,height=30,width=1920)
    a1=tkinter.Label(f,text="JPS: Jharkhand Public School (official website)",fg="white",bg="blue",font="arial 12 bold")
    a1.place(x=0,y=5)
    # png icon helpdesk
    img9=tkinter.PhotoImage(name="image_10",file="helpdesk.png")
    i=tkinter.Label(f,image=img9,fg="black",bg="white",font="arial 14 bold")
    i.place(x=1360,y=5)
    a2=tkinter.Label(f,text="Helpdesk",fg="white",bg="blue",font="arial 12 bold")
    a2.place(x=1400,y=5)


    f1=tkinter.Frame(root,bg="white")
    f1.place(x=0,y=30,height=105,width=1920)
    # logo frame
    flogo=tkinter.Frame(f1,bg="white",highlightthickness=2)
    flogo.place(x=0,y=0,height=105,width=180)
    # png icon school logo
    school_img=tkinter.PhotoImage(name="school_1",file="jplogo.png") 
    i=tkinter.Label(flogo,image=school_img,fg="black",bg="white",font="arial 12 bold")
    i.place(x=30,y=0)

    b1=tkinter.Label(f1,text="झारखंड पब्लिक स्कूल",fg="black",bg="white")
    b1.place(x=200,y=5)
    b2=tkinter.Label(f1,text="झारखंड शासन",fg="black",bg="white")
    b2.place(x=220,y=20)
    b3=tkinter.Label(f1,text="____________________________",fg="black",bg="white")
    b3.place(x=200,y=35)
    b4=tkinter.Label(f1,text="Jharkhand Public School",fg="black",bg="white",font="arial 12 bold")
    b4.place(x=200,y=55)
    b4=tkinter.Label(f1,text="Government of Jharkhand",fg="black",bg="white",font="arial 12 bold")
    b4.place(x=200,y=75)
    b5=tkinter.Label(f1,text="Email Us:",fg="black",bg="white",font="arial 12")
    b5.place(x=1100,y=30)
    # png icon email
    img10=tkinter.PhotoImage(name="image_11",file="email.png")
    i=tkinter.Label(f1,image=img10,fg="black",bg="white",font="arial 14 bold")
    i.place(x=1070,y=30)
    b6=tkinter.Label(f1,text="jps123@gmail.com",fg="black",bg="white",font="arial 12 bold")
    b6.place(x=1100,y=50)
    # ashoka frame
    ashk_f=tkinter.Frame(f1,bg="white",highlightthickness=1)
    ashk_f.place(x=1370,y=0,height=105,width=210)
    # png icon ashoka
    ashk=tkinter.PhotoImage(name="ashokstambh",file="ashk3.png") 
    i=tkinter.Label(ashk_f,image=ashk,fg="black",bg="white",font="arial 14 bold")
    i.place(x=0,y=5)

    # menu frame
    f2=tkinter.Frame(root,bg="blue")
    f2.place(x=0,y=135,height=60,width=1920)
    # menu
    c1=tkinter.Button(f2,text="Home",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="blue",command=home,cursor='hand2')
    c1.place(x=130,y=15)
    # menubutton
    menubutton=tkinter.Menubutton(f2,text="About us",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",cursor='hand2')
    menu=tkinter.Menu(menubutton,tearoff=False)
    menubutton["menu"]=menu
    menu.add_command(label="principle message",command=p_msg)
    menubutton.place(x=210,y=15) 

    menubutton=tkinter.Menubutton(f2,text="Academic",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",cursor='hand2')
    menu=tkinter.Menu(menubutton,tearoff=False)
    menubutton["menu"]=menu
    menu.add_command(label="Academic Calendar",command=calendar)
    menu.add_command(label="List Of Holidays",command=holiday)
    menu.add_command(label="Event at a Schedule",command=event)
    menu.add_command(label="Annual Report 2021-2022",command=report1)   
    menu.add_command(label="Annual Report 2022-2023",command=report2)
    menubutton.place(x=320,y=15) 


    menubutton=tkinter.Menubutton(f2,text="Facilities",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",cursor='hand2')
    menu=tkinter.Menu(menubutton,tearoff=False)
    menubutton["menu"]=menu
    menu.add_command(label="E-Library",command=library)
    menu.add_command(label="Hostels",command=hostel)
    menu.add_command(label="Canteen",command=canteen)
    menu.add_command(label="Medical Clinic",command=medical)
    menu.add_command(label="Health Club",command=health_club)
    menu.add_command(label="Wi-Fi Campus",command=wifi)
    menubutton.place(x=435,y=15) 

       
    menubutton=tkinter.Menubutton(f2,text="Gallery",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",cursor='hand2')
    menu=tkinter.Menu(menubutton,tearoff=False)
    menubutton["menu"]=menu
    menu.add_command(label="Image Gallery",command=img_gallery)
    menu.add_command(label="Video Gallery",command=video_gallery)
    menubutton.place(x=545,y=15) 

    c1=tkinter.Button(f2,text="Key Persons",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",command=key_person,cursor='hand2')
    c1.place(x=650,y=15)
    c1=tkinter.Button(f2,text="Web Information Manager",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",command=web_desiner,cursor='hand2')
    c1.place(x=775,y=15)
    c1=tkinter.Button(f2,text="Contact",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",cursor='hand2',command=contact)
    c1.place(x=980,y=15)

    
    f3=tkinter.Frame(root,bg="white")
    f3.place(x=0,y=190,height=600,width=1920)
    l=tkinter.Label(f3,text="Jharkhand Education Portal",fg="red",bg="white",font="arial 16 bold")
    l.place(x=50,y=30)
    l1=tkinter.Label(f3,text="Result:- Comming Soon.",fg="black",bg="white",font="arial 12")
    l1.place(x=55,y=60)


    f4=tkinter.Frame(root,bg="navy blue")
    f4.place(x=00,y=680,height=150,width=1920)
    bttm=tkinter.Label(f4,text="© हे शालेय शिक्षण व क्रीडा विभागाचे अधिकृत संकेतस्थळ आहे. सर्व हक्क सुरक्षित.",fg="white",bg="navy blue")
    bttm.place(x=550,y=20)
    bttm=tkinter.Label(f4,text="© 2024 This is the official website of School Education and Sports Department, Govt of Jharkhand.All Rights Reserved.",fg="white",bg="navy blue",font="arial 12 bold")
    bttm.place(x=350,y=50)
    
    root.mainloop()


def fee_structure():
    root=tkinter.Toplevel()
    root.geometry("1920x1080")

    f=tkinter.Frame(root,bg="blue")
    f.place(x=0,y=0,height=30,width=1920)
    a1=tkinter.Label(f,text="JPS: Jharkhand Public School (official website)",fg="white",bg="blue",font="arial 12 bold")
    a1.place(x=0,y=5)
    # png icon helpdesk
    img9=tkinter.PhotoImage(name="image_10",file="helpdesk.png")
    i=tkinter.Label(f,image=img9,fg="black",bg="white",font="arial 14 bold")
    i.place(x=1360,y=5)
    a2=tkinter.Label(f,text="Helpdesk",fg="white",bg="blue",font="arial 12 bold")
    a2.place(x=1400,y=5)


    f1=tkinter.Frame(root,bg="white")
    f1.place(x=0,y=30,height=105,width=1920)
    # logo frame
    flogo=tkinter.Frame(f1,bg="white",highlightthickness=2)
    flogo.place(x=0,y=0,height=105,width=180)
    # png icon school logo
    school_img=tkinter.PhotoImage(name="school_1",file="jplogo.png") 
    i=tkinter.Label(flogo,image=school_img,fg="black",bg="white",font="arial 12 bold")
    i.place(x=30,y=0)

    b1=tkinter.Label(f1,text="झारखंड पब्लिक स्कूल",fg="black",bg="white")
    b1.place(x=200,y=5)
    b2=tkinter.Label(f1,text="झारखंड शासन",fg="black",bg="white")
    b2.place(x=220,y=20)
    b3=tkinter.Label(f1,text="____________________________",fg="black",bg="white")
    b3.place(x=200,y=35)
    b4=tkinter.Label(f1,text="Jharkhand Public School",fg="black",bg="white",font="arial 12 bold")
    b4.place(x=200,y=55)
    b4=tkinter.Label(f1,text="Government of Jharkhand",fg="black",bg="white",font="arial 12 bold")
    b4.place(x=200,y=75)
    b5=tkinter.Label(f1,text="Email Us:",fg="black",bg="white",font="arial 12")
    b5.place(x=1100,y=30)
    # png icon email
    img10=tkinter.PhotoImage(name="image_11",file="email.png")
    i=tkinter.Label(f1,image=img10,fg="black",bg="white",font="arial 14 bold")
    i.place(x=1070,y=30)
    b6=tkinter.Label(f1,text="jps123@gmail.com",fg="black",bg="white",font="arial 12 bold")
    b6.place(x=1100,y=50)
    # ashoka frame
    ashk_f=tkinter.Frame(f1,bg="white",highlightthickness=1)
    ashk_f.place(x=1370,y=0,height=105,width=210)
    # png icon ashoka
    ashk=tkinter.PhotoImage(name="ashokstambh",file="ashk3.png") 
    i=tkinter.Label(ashk_f,image=ashk,fg="black",bg="white",font="arial 14 bold")
    i.place(x=0,y=5)

    # menu frame
    f2=tkinter.Frame(root,bg="blue")
    f2.place(x=0,y=135,height=60,width=1920)
    # menu
    c1=tkinter.Button(f2,text="Home",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="blue",command=home,cursor='hand2')
    c1.place(x=130,y=15)
   # menubutton
    menubutton=tkinter.Menubutton(f2,text="About us",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",cursor='hand2')
    menu=tkinter.Menu(menubutton,tearoff=False)
    menubutton["menu"]=menu
    menu.add_command(label="principle message",command=p_msg)
    menubutton.place(x=210,y=15) 

    menubutton=tkinter.Menubutton(f2,text="Academic",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",cursor='hand2')
    menu=tkinter.Menu(menubutton,tearoff=False)
    menubutton["menu"]=menu
    menu.add_command(label="Academic Calendar",command=calendar)
    menu.add_command(label="List Of Holidays",command=holiday)
    menu.add_command(label="Event at a Schedule",command=event)
    menu.add_command(label="Annual Report 2021-2022",command=report1)   
    menu.add_command(label="Annual Report 2022-2023",command=report2)
    menubutton.place(x=320,y=15) 


    menubutton=tkinter.Menubutton(f2,text="Facilities",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",cursor='hand2')
    menu=tkinter.Menu(menubutton,tearoff=False)
    menubutton["menu"]=menu
    menu.add_command(label="E-Library",command=library)
    menu.add_command(label="Hostels",command=hostel)
    menu.add_command(label="Canteen",command=canteen)
    menu.add_command(label="Medical Clinic",command=medical)
    menu.add_command(label="Health Club",command=health_club)
    menu.add_command(label="Wi-Fi Campus",command=wifi)
    menubutton.place(x=435,y=15) 

       
    menubutton=tkinter.Menubutton(f2,text="Gallery",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",cursor='hand2')
    menu=tkinter.Menu(menubutton,tearoff=False)
    menubutton["menu"]=menu
    menu.add_command(label="Image Gallery",command=img_gallery)
    menu.add_command(label="Video Gallery",command=video_gallery)
    menubutton.place(x=545,y=15) 

    c1=tkinter.Button(f2,text="Key Persons",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",command=key_person,cursor='hand2')
    c1.place(x=650,y=15)
    c1=tkinter.Button(f2,text="Web Information Manager",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",command=web_desiner,cursor='hand2')
    c1.place(x=775,y=15)
    c1=tkinter.Button(f2,text="Contact",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",cursor='hand2',command=contact)
    c1.place(x=980,y=15)

    
    f3=tkinter.Frame(root,bg="white")
    f3.place(x=0,y=190,height=600,width=1920)


    
    fee=tkinter.Frame(f3,bg="#66ffb3")
    fee.place(x=0,y=0,height=35,width=1920)
    fee1=tkinter.Label(fee,text="Fee Structure",fg="white",bg="#66ffb3",font="arial 14 bold",cursor='hand2')
    fee1.place(x=120,y=5)
    fee2=tkinter.Frame(f3,bg="red")
    fee2.place(x=280,y=35,height=400,width=980)
    image=Image.open("C:\\Users\\ASUS\\onedrive\\Desktop\\school1\\fee_str.png")
    photo=ImageTk.PhotoImage(image)
    l1=tkinter.Button(fee2,image=photo)
    l1.place(x=0,y=0,height=400,width=980)
    
    
    
    
    f4=tkinter.Frame(root,bg="navy blue")
    f4.place(x=00,y=680,height=150,width=1920)
    bttm=tkinter.Label(f4,text="© हे शालेय शिक्षण व क्रीडा विभागाचे अधिकृत संकेतस्थळ आहे. सर्व हक्क सुरक्षित.",fg="white",bg="navy blue")
    bttm.place(x=550,y=20)
    bttm=tkinter.Label(f4,text="© 2024 This is the official website of School Education and Sports Department, Govt of Jharkhand.All Rights Reserved.",fg="white",bg="navy blue",font="arial 12 bold")
    bttm.place(x=350,y=50)
    
    root.mainloop()
    
def sport_member():
    root=tkinter.Toplevel()
    root.geometry("1920x1080")
    
    f=tkinter.Frame(root,bg="blue")
    f.place(x=0,y=0,height=30,width=1920)
    a1=tkinter.Label(f,text="JPS: Jharkhand Public School (official website)",fg="white",bg="blue",font="arial 12 bold")
    a1.place(x=0,y=5)
    # png icon helpdesk
    img9=tkinter.PhotoImage(name="image_10",file="helpdesk.png")
    i=tkinter.Button(f,image=img9,fg="black",bg="white",font="arial 14 bold",bd=0,command=help_desk,cursor='hand2')
    i.place(x=1370,y=10)
    a2=tkinter.Label(f,text="Helpdesk",fg="white",bg="blue",font="arial 12 bold")
    a2.place(x=1400,y=5)


    f1=tkinter.Frame(root,bg="white")
    f1.place(x=0,y=30,height=105,width=1920)
    # logo frame
    flogo=tkinter.Frame(f1,bg="white",highlightthickness=2)
    flogo.place(x=0,y=0,height=105,width=180)
    # png icon school logo
    school_img=tkinter.PhotoImage(name="school_1",file="jplogo.png") 
    i=tkinter.Label(flogo,image=school_img,fg="black",bg="white",font="arial 12 bold")
    i.place(x=30,y=0)

    b1=tkinter.Label(f1,text="झारखंड पब्लिक स्कूल",fg="black",bg="white")
    b1.place(x=200,y=5)
    b2=tkinter.Label(f1,text="झारखंड शासन",fg="black",bg="white")
    b2.place(x=220,y=20)
    b3=tkinter.Label(f1,text="____________________________",fg="black",bg="white")
    b3.place(x=200,y=35)
    b4=tkinter.Label(f1,text="Jharkhand Public School",fg="black",bg="white",font="arial 12 bold")
    b4.place(x=200,y=55)
    b4=tkinter.Label(f1,text="Government of Jharkhand",fg="black",bg="white",font="arial 12 bold")
    b4.place(x=200,y=75)
    b5=tkinter.Label(f1,text="Email Us:",fg="black",bg="white",font="arial 12")
    b5.place(x=1100,y=30)
    # png icon email
    img10=tkinter.PhotoImage(name="image_11",file="email.png")
    i=tkinter.Label(f1,image=img10,fg="black",bg="white",font="arial 14 bold")
    i.place(x=1070,y=30)
    b6=tkinter.Label(f1,text="jps123@gmail.com",fg="black",bg="white",font="arial 12 bold")
    b6.place(x=1100,y=50)
    # ashoka frame
    ashk_f=tkinter.Frame(f1,bg="white",highlightthickness=1)
    ashk_f.place(x=1370,y=0,height=105,width=210)
    # png icon ashoka
    ashk=tkinter.PhotoImage(name="ashokstambh",file="ashk3.png") 
    i=tkinter.Label(ashk_f,image=ashk,fg="black",bg="white",font="arial 14 bold")
    i.place(x=0,y=5)

    # menu frame
    f2=tkinter.Frame(root,bg="blue")
    f2.place(x=0,y=135,height=60,width=1920)
    # menu
    c1=tkinter.Button(f2,text="Home",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="blue",command=home,cursor='hand2')
    c1.place(x=130,y=15)
    # menubutton
    menubutton=tkinter.Menubutton(f2,text="About us",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",cursor='hand2')
    menu=tkinter.Menu(menubutton,tearoff=False)
    menubutton["menu"]=menu
    menu.add_command(label="principle message",command=p_msg)
    menubutton.place(x=210,y=15) 

    menubutton=tkinter.Menubutton(f2,text="Academic",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",cursor='hand2')
    menu=tkinter.Menu(menubutton,tearoff=False)
    menubutton["menu"]=menu
    menu.add_command(label="Academic Calendar",command=calendar)
    menu.add_command(label="List Of Holidays",command=holiday)
    menu.add_command(label="Event at a Schedule",command=event)
    menu.add_command(label="Annual Report 2021-2022",command=report1)   
    menu.add_command(label="Annual Report 2022-2023",command=report2)
    menubutton.place(x=320,y=15) 


    menubutton=tkinter.Menubutton(f2,text="Facilities",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",cursor='hand2')
    menu=tkinter.Menu(menubutton,tearoff=False)
    menubutton["menu"]=menu
    menu.add_command(label="E-Library",command=library)
    menu.add_command(label="Hostels",command=hostel)
    menu.add_command(label="Canteen",command=canteen)
    menu.add_command(label="Medical Clinic",command=medical)
    menu.add_command(label="Health Club",command=health_club)
    menu.add_command(label="Wi-Fi Campus",command=wifi)
    menubutton.place(x=435,y=15) 

       
    menubutton=tkinter.Menubutton(f2,text="Gallery",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",cursor='hand2')
    menu=tkinter.Menu(menubutton,tearoff=False)
    menubutton["menu"]=menu
    menu.add_command(label="Image Gallery",command=img_gallery)
    menu.add_command(label="Video Gallery",command=video_gallery)
    menubutton.place(x=545,y=15) 

    c1=tkinter.Button(f2,text="Key Persons",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",command=key_person,cursor='hand2')
    c1.place(x=650,y=15)
    c1=tkinter.Button(f2,text="Web Information Manager",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",command=web_desiner,cursor='hand2')
    c1.place(x=775,y=15)
    c1=tkinter.Button(f2,text="Contact",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",cursor='hand2',command=contact)
    c1.place(x=980,y=15)

    
    f3=tkinter.Frame(root,bg="white")
    f3.place(x=0,y=190,height=600,width=1920)
    f4=tkinter.Frame(f3,bg="#4da6ff")
    f4.place(x=0,y=0,width=1920,height=50)
    sp=tkinter.Label(f4,text=" Our Sports",bg="#4da6ff",fg="white",font="aral 16 bold")
    sp.place(x=80,y=10)
    img_f=tkinter.Frame(f3,bg="white")
    img_f.place(x=50,y=130,height=260,width=400)
    image=Image.open("C:\\Users\\ASUS\\onedrive\\Desktop\\school1\\sport.jpg")
    photo=ImageTk.PhotoImage(image)
    l1=tkinter.Label(img_f,image=photo,bd=0)
    l1.place(x=0,y=0,height=200,width=400)
    l1=tkinter.Button(img_f,text="Kabadi",bg="white",fg="black",font="arial 14 bold",bd=0)
    l1.place(x=170,y=200)
    l1=tkinter.Label(img_f,text="JPS, KODERMA, JHARKHAND",bg="white",fg="black",font="arial 10 ")
    l1.place(x=120,y=230)
    
    img1_f=tkinter.Frame(f3,bg="white")
    img1_f.place(x=470,y=130,height=260,width=400)
    image1=Image.open("C:\\Users\\ASUS\\onedrive\\Desktop\\school1\\hockey.jpg")
    photo1=ImageTk.PhotoImage(image1)
    l1=tkinter.Label(img1_f,image=photo1,bd=0)
    l1.place(x=0,y=0,height=200,width=400)
    l1=tkinter.Button(img1_f,text="Hockey",bg="white",fg="black",font="arial 14 bold",bd=0)
    l1.place(x=170,y=200)
    l1=tkinter.Label(img1_f,text="JPS, KODERMA, JHARKHAND",bg="white",fg="black",font="arial 10 ")
    l1.place(x=120,y=230)
    
    img2_f=tkinter.Frame(f3,bg="white")
    img2_f.place(x=890,y=130,height=260,width=400)
    image2=Image.open("C:\\Users\\ASUS\\onedrive\\Desktop\\school1\\bollyball.jpg")
    photo2=ImageTk.PhotoImage(image2)
    l1=tkinter.Label(img2_f,image=photo2,bd=0)
    l1.place(x=0,y=0,height=200,width=400)
    l1=tkinter.Button(img2_f,text="Bollyball",bg="white",fg="black",font="arial 14 bold",bd=0)
    l1.place(x=150,y=200)
    l1=tkinter.Label(img2_f,text="JPS, KODERMA, JHARKHAND",bg="white",fg="black",font="arial 10 ")
    l1.place(x=110,y=230)
    
    


    f4=tkinter.Frame(root,bg="navy blue")
    f4.place(x=00,y=680,height=150,width=1920)
    bttm=tkinter.Label(f4,text="© हे शालेय शिक्षण व क्रीडा विभागाचे अधिकृत संकेतस्थळ आहे. सर्व हक्क सुरक्षित.",fg="white",bg="navy blue")
    bttm.place(x=550,y=20)
    bttm=tkinter.Label(f4,text="© 2024 This is the official website of School Education and Sports Department, Govt of Jharkhand.All Rights Reserved.",fg="white",bg="navy blue",font="arial 12 bold")
    bttm.place(x=350,y=50)
    
    root.mainloop()


def home():
    root=tkinter.Toplevel()
    root.geometry("1920x1080")
    def help_desk():
        help_f=tkinter.Frame(f1,bg="white")
        help_f.place(x=1300,y=0,height=20,width=180)
        msg=tkinter.Label(help_f,text="jps123@gmail.com",bg="#E3E3E3",fg="black",font="arial 10 bold")
        msg.place(x=5,y=0)
    f=tkinter.Frame(root,bg="blue")
    f.place(x=0,y=0,height=30,width=1920)
    a1=tkinter.Label(f,text="JPS: Jharkhand Public School (official website)",fg="white",bg="blue",font="arial 12 bold")
    a1.place(x=0,y=5)
    # png icon helpdesk
    img9=tkinter.PhotoImage(name="image_10",file="helpdesk.png")
    i=tkinter.Button(f,image=img9,fg="black",bg="white",font="arial 14 bold",bd=0,command=help_desk,cursor='hand2')
    i.place(x=1370,y=10)
    a2=tkinter.Button(f,text="Helpdesk",fg="white",bg="blue",font="arial 12 bold",command=help_desk,bd=0,cursor='hand2')
    a2.place(x=1400,y=5)


    f1=tkinter.Frame(root,bg="white")
    f1.place(x=0,y=30,height=105,width=1920)
    # logo frame
    flogo=tkinter.Frame(f1,bg="white",highlightthickness=2)
    flogo.place(x=0,y=0,height=105,width=180)
    # png icon school logo
    school_img=tkinter.PhotoImage(name="school_1",file="jplogo.png") 
    i=tkinter.Label(flogo,image=school_img,fg="black",bg="white",font="arial 12 bold")
    i.place(x=30,y=0)

    b1=tkinter.Label(f1,text="झारखंड पब्लिक स्कूल",fg="black",bg="white")
    b1.place(x=200,y=5)
    b2=tkinter.Label(f1,text="झारखंड शासन",fg="black",bg="white")
    b2.place(x=220,y=20)
    b3=tkinter.Label(f1,text="____________________________",fg="black",bg="white")
    b3.place(x=200,y=35)
    b4=tkinter.Label(f1,text="Jharkhand Public School",fg="black",bg="white",font="arial 12 bold")
    b4.place(x=200,y=55)
    b4=tkinter.Label(f1,text="Government of Jharkhand",fg="black",bg="white",font="arial 12 bold")
    b4.place(x=200,y=75)
    b5=tkinter.Label(f1,text="Email Us:",fg="black",bg="white",font="arial 12")
    b5.place(x=1100,y=30)
    # png icon email
    img10=tkinter.PhotoImage(name="image_11",file="email.png")
    i=tkinter.Label(f1,image=img10,fg="black",bg="white",font="arial 14 bold")
    i.place(x=1070,y=30)
    b6=tkinter.Label(f1,text="jps123@gmail.com",fg="black",bg="white",font="arial 12 bold")
    b6.place(x=1100,y=50)
    # ashoka frame
    ashk_f=tkinter.Frame(f1,bg="white",highlightthickness=1)
    ashk_f.place(x=1370,y=0,height=105,width=210)
    # png icon ashoka
    ashk=tkinter.PhotoImage(name="ashokstambh",file="ashk3.png") 
    i=tkinter.Label(ashk_f,image=ashk,fg="black",bg="white",font="arial 14 bold")
    i.place(x=0,y=5)

    # menu frame
    f2=tkinter.Frame(root,bg="blue")
    f2.place(x=0,y=135,height=60,width=1920)
    # menu
    c1=tkinter.Button(f2,text="Home",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="blue",command=home,cursor='hand2')
    c1.place(x=130,y=15)
    # menubutton
    menubutton=tkinter.Menubutton(f2,text="About us",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",cursor='hand2')
    menu=tkinter.Menu(menubutton,tearoff=False)
    menubutton["menu"]=menu
    menu.add_command(label="principle message",command=p_msg)
    menubutton.place(x=210,y=15) 

    menubutton=tkinter.Menubutton(f2,text="Academic",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",cursor='hand2')
    menu=tkinter.Menu(menubutton,tearoff=False)
    menubutton["menu"]=menu
    menu.add_command(label="Academic Calendar")
    menu.add_command(label="List Of Holidays")
    menu.add_command(label="Event at a Schedule")
    menu.add_command(label="Annual Report 2021-2022")   
    menu.add_command(label="Annual Report 2022-2023")
    menubutton.place(x=320,y=15) 


    menubutton=tkinter.Menubutton(f2,text="Facilities",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",cursor='hand2')
    menu=tkinter.Menu(menubutton,tearoff=False)
    menubutton["menu"]=menu
    menu.add_command(label="E-Library")
    menu.add_command(label="Hostels")
    menu.add_command(label="Canteen")
    menu.add_command(label="Medical Clinic")
    menu.add_command(label="Health Club")
    menu.add_command(label="Wi-Fi Campus")
    menubutton.place(x=435,y=15) 

       
    menubutton=tkinter.Menubutton(f2,text="Gallery",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",cursor='hand2')
    menu=tkinter.Menu(menubutton,tearoff=False)
    menubutton["menu"]=menu
    menu.add_command(label="Image Gallery")
    menu.add_command(label="Video Gallery")
    menubutton.place(x=545,y=15) 
    
    c1=tkinter.Button(f2,text="Key Persons",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",command=key_person,cursor='hand2')
    c1.place(x=650,y=15)
    c1=tkinter.Button(f2,text="Web Information Manager",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",command=web_desiner,cursor='hand2')
    c1.place(x=775,y=15)
    c1=tkinter.Button(f2,text="Contact",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",cursor='hand2',command=contact)
    c1.place(x=980,y=15)



    # background frame 
    f3=tkinter.Frame(root,bg="white")
    f3.place(x=0,y=190,height=600,width=1920)
    # bckground image
    image=Image.open("C:\\Users\\ASUS\\onedrive\\Desktop\\school1\\\img11.jpg")
    photo=ImageTk.PhotoImage(image)
    l1=tkinter.Label(f3,image=photo,bd=0)
    l1.place(x=0,y=0)

    #main frame all portal
    f4=tkinter.Frame(root,bg="navy blue")
    f4.place(x=20,y=230,height=520,width=490)
    l1=tkinter.Label(f4,text="Web Links",fg="white",bg="navy blue",font="arial 14 bold")
    l1.place(x=190,y=10)
     
    f5=tkinter.Frame(f4,bg="white")
    f5.place(x=30,y=70,height=120,width=130)     
    #png icon student portal
    img=tkinter.PhotoImage(name="image_1",file="student prfile.png") 
    i=tkinter.Button(f5,image=img,fg="black",bg="white",font="arial 12 bold",bd=0,cursor='hand2',command=student)
    i.place(x=40,y=20)
    btn1=tkinter.Button(f5,text="Student portal",fg="black",bg="white",font="arial 12 bold",bd=0,activebackground="#EBEBEB",activeforeground="black",command=student,cursor='hand2')    
    btn1.place(x=8,y=80)
 
 
    f6=tkinter.Frame(f4,bg="#EBEBEB")
    f6.place(x=180,y=70,height=120,width=130)
    #png icon school portal
    img1=tkinter.PhotoImage(name="image_2",file="school.png")
    i=tkinter.Button(f6,image=img1,fg="black",bg="white",font="arial 12 bold",bd=0,cursor='hand2',command=school_portal)
    i.place(x=40,y=20)
    btn1=tkinter.Button(f6,text="School portal",fg="black",bg="#EBEBEB",font="arial 12 bold",bd=0,activebackground="#EBEBEB",activeforeground="black",command=school_portal,cursor='hand2')
    btn1.place(x=8,y=80)
 
    f7=tkinter.Frame(f4,bg="#EBEBEB")
        #png icon admission
    img2=tkinter.PhotoImage(name="image_3",file="admission.png")
    f7.place(x=330,y=70,height=120,width=130)
    i=tkinter.Button(f7,image=img2,fg="black",bg="white",font="arial 12 bold",bd=0,cursor='hand2',command=admission)
    i.place(x=40,y=20)
    btn1=tkinter.Button(f7,text="Admission ",fg="black",bg="#EBEBEB",font="arial 12 bold",bd=0,activebackground="#EBEBEB",activeforeground="black",command=admission,cursor='hand2')
    btn1.place(x=17,y=80)
 
    f8=tkinter.Frame(f4,bg="#EBEBEB")
    f8.place(x=30,y=220,height=120,width=130)
    #png icon examaton
    img3=tkinter.PhotoImage(name="image_4",file="registation.png")
    i=tkinter.Button(f8,image=img3,fg="black",bg="white",font="arial 12 bold",bd=0,cursor='hand2',command=examation)
    i.place(x=40,y=20)
    btn2=tkinter.Button(f8,text="Examation",fg="black",bg="#EBEBEB",font="arial 12 bold",bd=0,activebackground="#EBEBEB",activeforeground="black",command=examation,cursor='hand2')
    btn2.place(x=18,y=80)

 
    f9=tkinter.Frame(f4,bg="#EBEBEB")
    f9.place(x=180,y=220,height=120,width=130)
    #png icon staff portal
    img4=tkinter.PhotoImage(name="image_5",file="Staff.png")
    i=tkinter.Button(f9,image=img4,fg="black",bg="white",font="arial 12 bold",bd=0,cursor='hand2',command=stf_portal)
    i.place(x=40,y=20)
    btn2=tkinter.Button(f9,text="Staff portal",fg="black",bg="#EBEBEB",font="arial 12 bold",bd=0,activebackground="#EBEBEB",activeforeground="black",command=stf_portal,cursor='hand2')
    btn2.place(x=14,y=80)

 
    f10=tkinter.Frame(f4,bg="#EBEBEB")
    f10.place(x=330,y=220,height=120,width=130)
    #png icon teachers portal
    img5=tkinter.PhotoImage(name="image_6",file="teacher.png")
    i=tkinter.Button(f10,image=img5,fg="black",bg="white",font="arial 12 bold",bd=0,cursor='hand2',command=tech_portal)
    i.place(x=40,y=20)
    btn2=tkinter.Button(f10,text="Teacher portal",fg="black",bg="#EBEBEB",font="arial 12 bold",bd=0,activebackground="#EBEBEB",activeforeground="black",command=tech_portal,cursor='hand2')
    btn2.place(x=6,y=80)

 
    f11=tkinter.Frame(f4,bg="#EBEBEB")
    f11.place(x=30,y=370,height=120,width=130)
    #png icon marksheet
    img6=tkinter.PhotoImage(name="image_7",file="marksheet.png")
    i=tkinter.Button(f11,image=img6,fg="black",bg="white",font="arial 12 bold",bd=0,cursor='hand2',command=marks)
    i.place(x=40,y=20)
    btn1=tkinter.Button(f11,text="Marksheet",fg="black",bg="#EBEBEB",font="arial 12 bold",bd=0,activebackground="#EBEBEB",activeforeground="black",command=marks,cursor='hand2')
    btn1.place(x=17,y=80)



    f12=tkinter.Frame(f4,bg="#EBEBEB")
    f12.place(x=180,y=370,height=120,width=130)
    #png icon fee
    img7=tkinter.PhotoImage(name="image_8",file="money.png") 
    i=tkinter.Button(f12,image=img7,fg="black",bg="white",font="arial 12 bold",bd=0,cursor='hand2',command=fee_structure)
    i.place(x=40,y=20)
    btn1=tkinter.Button(f12,text="Fee portal",fg="black",bg="#EBEBEB",font="arial 12 bold",bd=0,activebackground="#EBEBEB",activeforeground="black",command=fee_structure,cursor='hand2')
    btn1.place(x=19,y=80)

 
    f13=tkinter.Frame(f4,bg="#EBEBEB")
    f13.place(x=330,y=370,height=120,width=130)
    #png icon sports
    img8=tkinter.PhotoImage(name="image_9",file="sports.png")
    i=tkinter.Button(f13,image=img8,fg="black",bg="white",font="arial 12 bold",bd=0,cursor='hand2',command=sport_member)
    i.place(x=40,y=20)
    btn1=tkinter.Button(f13,text="Sports portal",fg="black",bg="#EBEBEB",font="arial 12 bold",bd=0,activebackground="#EBEBEB",activeforeground="black",command=sport_member,cursor='hand2')
    btn1.place(x=8,y=80)


    
    root.mainloop()



f=tkinter.Frame(root,bg="blue")
f.place(x=0,y=0,height=30,width=1920)
a1=tkinter.Label(f,text="JPS: Jharkhand Public School (official website)",fg="white",bg="blue",font="arial 12 bold")
a1.place(x=0,y=5)
# png icon helpdesk
img9=tkinter.PhotoImage(name="image_10",file="helpdesk.png")
i=tkinter.Button(f,image=img9,fg="black",bg="white",font="arial 14 bold",bd=0,command=help_desk,cursor='hand2')
i.place(x=1370,y=10)

a2=tkinter.Button(f,text="Helpdesk",fg="white",bg="blue",font="arial 12 bold",command=help_desk,bd=0,cursor='hand2')
a2.place(x=1400,y=5)


f1=tkinter.Frame(root,bg="white")
f1.place(x=0,y=30,height=105,width=1920)
# logo frame
flogo=tkinter.Frame(f1,bg="white",highlightthickness=2)
flogo.place(x=0,y=0,height=105,width=180)
# png icon school logo
school_img=tkinter.PhotoImage(name="school_1",file="jplogo.png") 
i=tkinter.Label(flogo,image=school_img,fg="black",bg="white",font="arial 12 bold")
i.place(x=30,y=0)

b1=tkinter.Label(f1,text="झारखंड पब्लिक स्कूल",fg="black",bg="white")
b1.place(x=200,y=5)
b2=tkinter.Label(f1,text="झारखंड शासन",fg="black",bg="white")
b2.place(x=220,y=20)
b3=tkinter.Label(f1,text="____________________________",fg="black",bg="white")
b3.place(x=200,y=35)
b4=tkinter.Label(f1,text="Jharkhand Public School",fg="black",bg="white",font="arial 12 bold")
b4.place(x=200,y=55)
b4=tkinter.Label(f1,text="Government of Jharkhand",fg="black",bg="white",font="arial 12 bold")
b4.place(x=200,y=75)
b5=tkinter.Label(f1,text="Email Us:",fg="black",bg="white",font="arial 12")
b5.place(x=1100,y=30)
# png icon email
img10=tkinter.PhotoImage(name="image_11",file="email.png")
i=tkinter.Label(f1,image=img10,fg="black",bg="white",font="arial 14 bold")
i.place(x=1070,y=30)
b6=tkinter.Label(f1,text="jps123@gmail.com",fg="black",bg="white",font="arial 12 bold")
b6.place(x=1100,y=50)
# ashoka frame
ashk_f=tkinter.Frame(f1,bg="white",highlightthickness=1)
ashk_f.place(x=1370,y=0,height=105,width=210)
# png icon ashoka
ashk=tkinter.PhotoImage(name="ashokstambh",file="ashk3.png") 
i=tkinter.Label(ashk_f,image=ashk,fg="black",bg="white",font="arial 14 bold")
i.place(x=0,y=5)

# menu frame
f2=tkinter.Frame(root,bg="blue")
f2.place(x=0,y=135,height=60,width=1920)
# menu
c1=tkinter.Button(f2,text="Home",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="blue",command=home,cursor='hand2')
c1.place(x=130,y=15)
# menubutton
menubutton=tkinter.Menubutton(f2,text="About us",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",cursor='hand2')
menu=tkinter.Menu(menubutton,tearoff=False)
menubutton["menu"]=menu
menu.add_command(label="principle message",command=p_msg)
menubutton.place(x=210,y=15) 

menubutton=tkinter.Menubutton(f2,text="Academic",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",cursor='hand2')
menu=tkinter.Menu(menubutton,tearoff=False)
menubutton["menu"]=menu
menu.add_command(label="Academic Calendar",command=calendar)
menu.add_command(label="List Of Holidays",command=holiday)
menu.add_command(label="Event at a Schedule",command=event)
menu.add_command(label="Annual Report 2021-2022",command=report1)
menu.add_command(label="Annual Report 2022-2023",command=report2)
menubutton.place(x=320,y=15) 


menubutton=tkinter.Menubutton(f2,text="Facilities",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",cursor='hand2')
menu=tkinter.Menu(menubutton,tearoff=False)
menubutton["menu"]=menu
menu.add_command(label="E-Library",command=library)
menu.add_command(label="Hostels",command=hostel)
menu.add_command(label="Canteen",command=canteen)
menu.add_command(label="Medical Clinic",command=medical)
menu.add_command(label="Health Club",command=health_club)
menu.add_command(label="Wi-Fi Campus",command=wifi)
menubutton.place(x=435,y=15) 

       
menubutton=tkinter.Menubutton(f2,text="Gallery",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",cursor='hand2')
menu=tkinter.Menu(menubutton,tearoff=False)
menubutton["menu"]=menu
menu.add_command(label="Image Gallery",command=img_gallery)
menu.add_command(label="Video Gallery",command=video_gallery)
menubutton.place(x=545,y=15)  


c1=tkinter.Button(f2,text="Key Persons",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",command=key_person,cursor='hand2')
c1.place(x=650,y=15)
c1=tkinter.Button(f2,text="Web Information Manager",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",command=web_desiner,cursor='hand2')
c1.place(x=775,y=15)
c1=tkinter.Button(f2,text="Contact",fg="white",bg="blue",font="arial 11 bold",bd=0,activebackground="blue",activeforeground="white",cursor='hand2',command=contact)
c1.place(x=980,y=15)



# background frame 
f3=tkinter.Frame(root,bg="white")
f3.place(x=0,y=190,height=600,width=1920)
# bckground image
image=Image.open("C:\\Users\\ASUS\\OneDrive\\Desktop\\school1\\img11.jpg")
photo=ImageTk.PhotoImage(image)
l1=tkinter.Label(f3,image=photo,bd=0)
l1.place(x=0,y=0)

#main frame all portal
f4=tkinter.Frame(root,bg="navy blue")
f4.place(x=20,y=230,height=520,width=490)
l1=tkinter.Label(f4,text="Web Links",fg="white",bg="navy blue",font="arial 14 bold")
l1.place(x=190,y=10)
     
f5=tkinter.Frame(f4,bg="white")
f5.place(x=30,y=70,height=120,width=130)     
#png icon student portal
img=tkinter.PhotoImage(name="image_1",file="student prfile.png") 
i=tkinter.Button(f5,image=img,fg="black",bg="white",font="arial 12 bold",bd=0,cursor='hand2',command=student)
i.place(x=40,y=20)
btn1=tkinter.Button(f5,text="Student portal",fg="black",bg="white",font="arial 12 bold",bd=0,activebackground="#EBEBEB",activeforeground="black",command=student,cursor='hand2')
btn1.place(x=8,y=80)
 
 
f6=tkinter.Frame(f4,bg="#EBEBEB")
f6.place(x=180,y=70,height=120,width=130)
#png icon school portal
img1=tkinter.PhotoImage(name="image_2",file="school.png")
i=tkinter.Button(f6,image=img1,fg="black",bg="white",font="arial 12 bold",bd=0,cursor='hand2',command=school_portal)
i.place(x=40,y=20)
btn1=tkinter.Button(f6,text="School portal",fg="black",bg="#EBEBEB",font="arial 12 bold",bd=0,activebackground="#EBEBEB",activeforeground="black",command=school_portal,cursor='hand2')
btn1.place(x=8,y=80)
 
f7=tkinter.Frame(f4,bg="#EBEBEB")
#png icon admission
img2=tkinter.PhotoImage(name="image_3",file="admission.png")
f7.place(x=330,y=70,height=120,width=130)
i=tkinter.Button(f7,image=img2,fg="black",bg="white",font="arial 12 bold",bd=0,cursor='hand2',command=admission)
i.place(x=40,y=20)
btn1=tkinter.Button(f7,text="Admission ",fg="black",bg="#EBEBEB",font="arial 12 bold",bd=0,activebackground="#EBEBEB",activeforeground="black",command=admission,cursor='hand2')
btn1.place(x=17,y=80)
 
f8=tkinter.Frame(f4,bg="#EBEBEB")
f8.place(x=30,y=220,height=120,width=130)
#png icon examaton
img3=tkinter.PhotoImage(name="image_4",file="registation.png")
i=tkinter.Button(f8,image=img3,fg="black",bg="white",font="arial 12 bold",bd=0,cursor='hand2',command=examation)
i.place(x=40,y=20)
btn2=tkinter.Button(f8,text="Examation",fg="black",bg="#EBEBEB",font="arial 12 bold",bd=0,activebackground="#EBEBEB",activeforeground="black",command=examation,cursor='hand2')
btn2.place(x=18,y=80)

 
f9=tkinter.Frame(f4,bg="#EBEBEB")
f9.place(x=180,y=220,height=120,width=130)
#png icon staff portal
img4=tkinter.PhotoImage(name="image_5",file="Staff.png")
i=tkinter.Button(f9,image=img4,fg="black",bg="white",font="arial 12 bold",bd=0,cursor='hand2',command=stf_portal)
i.place(x=40,y=20)
btn2=tkinter.Button(f9,text="Staff portal",fg="black",bg="#EBEBEB",font="arial 12 bold",bd=0,activebackground="#EBEBEB",activeforeground="black",command=stf_portal,cursor='hand2')
btn2.place(x=14,y=80)

 
f10=tkinter.Frame(f4,bg="#EBEBEB")
f10.place(x=330,y=220,height=120,width=130)
#png icon teachers portal
img5=tkinter.PhotoImage(name="image_6",file="teacher.png")
i=tkinter.Button(f10,image=img5,fg="black",bg="white",font="arial 12 bold",bd=0,cursor='hand2',command=tech_portal)
i.place(x=40,y=20)
btn2=tkinter.Button(f10,text="Teacher portal",fg="black",bg="#EBEBEB",font="arial 12 bold",bd=0,activebackground="#EBEBEB",activeforeground="black",command=tech_portal,cursor='hand2')
btn2.place(x=6,y=80)

 
f11=tkinter.Frame(f4,bg="#EBEBEB")
f11.place(x=30,y=370,height=120,width=130)
#png icon marksheet
img6=tkinter.PhotoImage(name="image_7",file="marksheet.png")
i=tkinter.Button(f11,image=img6,fg="black",bg="white",font="arial 12 bold",bd=0,cursor='hand2',command=marks)
i.place(x=40,y=20)
btn1=tkinter.Button(f11,text="Marksheet",fg="black",bg="#EBEBEB",font="arial 12 bold",bd=0,activebackground="#EBEBEB",activeforeground="black",command=marks,cursor='hand2')
btn1.place(x=17,y=80)



f12=tkinter.Frame(f4,bg="#EBEBEB")
f12.place(x=180,y=370,height=120,width=130)
#png icon fee
img7=tkinter.PhotoImage(name="image_8",file="money.png") 
i=tkinter.Button(f12,image=img7,fg="black",bg="white",font="arial 12 bold",bd=0,cursor='hand2',command=fee_structure)
i.place(x=40,y=20)
btn1=tkinter.Button(f12,text="Fee portal",fg="black",bg="#EBEBEB",font="arial 12 bold",bd=0,activebackground="#EBEBEB",activeforeground="black",command=fee_structure,cursor='hand2')
btn1.place(x=19,y=80)

 
f13=tkinter.Frame(f4,bg="#EBEBEB")
f13.place(x=330,y=370,height=120,width=130)
#png icon sports
img8=tkinter.PhotoImage(name="image_9",file="sports.png")
i=tkinter.Button(f13,image=img8,fg="black",bg="white",font="arial 12 bold",bd=0,cursor='hand2',command=sport_member)
i.place(x=40,y=20)
btn1=tkinter.Button(f13,text="Sports portal",fg="black",bg="#EBEBEB",font="arial 12 bold",bd=0,activebackground="#EBEBEB",activeforeground="black",command=sport_member,cursor='hand2')
btn1.place(x=8,y=80)



root.mainloop()