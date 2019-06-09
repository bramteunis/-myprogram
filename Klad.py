from tkinter import *
import tkinter as tk
import time, re, webbrowser, zipfile, shutil, os
from tkinter import Tk, PhotoImage, messagebox, ttk
import urllib.request as urllib2
from pathlib import Path

needed="1"
access1 = float
access1 = (0)

username = os.getlogin()


medium_font= ('Verdana',20); small_font= ('Verdana',10)
LG = tk.Tk();LG.configure(background="white");LG.title("Schoolsysteem");LG.resizable(False, False)
localtime=time.asctime(time.localtime(time.time()))
width = LG.winfo_screenwidth()
height = LG.winfo_screenheight()

w3 = (width / 426.67); width3=round(w3)
w5 = (width / 256); width5=round(w5)
w9 = (width / 142.2); width9=round(w9)
w10 = (width / 128); width10=round(w10)
w15 = (width / 85.3); width15=round(w15)
w20 = (width / 64); width20=round(w20)
w25 = (width / 51.2); width25=round(w25)
w30 = (width / 42.6); width30=round(w30)
w43 = (width / 29.53); width43=round(w43)
w55 = (width / 23.27); width55=round(w55)
w90 = (width / 14.22); width90=round(w90)
w100 = (width / 12.8); width100=round(w100)
w110 = (width / 11.63); width110=round(w110)
w145 = (width / 8.83); width145=round(w145)
w150 = (width / 8.53); width150=round(w150)
w155 = (width / 8.258); width155=round(w155)
w170 = (width / 7.5294); width170=round(w170)
w175 = (width / 7.3142); width175=round(w175)
w180 = (width / 7.11); width180=round(w180)
w200 = (width / 6.4); width200=round(w200)
w210 = (width / 6.0952); width210=round(w210)
w225 = (width / 5.68); width225=round(w225)
w250 = (width / 5.12); width250=round(w250)
w275 = (width / 4.654); width275=round(w275)
w290 = (width / 4.42); width290=round(w290)
w300 = (width / 4.266); width300=round(w300)
w325 = (width / 3.938); width325=round(w325)
w350 = (width / 3.66); width350=round(w350)
w375 = (width / 3.41); width375=round(w375)
w380 = (width / 3.37); width380=round(w380)
w390 = (width / 3.28); width390=round(w390)
w400 = (width / 3.2); width400=round(w400)
w420 = (width / 3.047); width420=round(w420)
w425 = (width / 3.011); width425=round(w425)
w450 = (width / 2.84); width450=round(w450)
w470 = (width / 2.7234); width470=round(w470)
w475 = (width / 2.694); width475=round(w475)
w500 = (width / 2.56); width500=round(w500)
w525 = (width / 2.438); width525=round(w525)
w550 = (width / 2.33); width550=round(w550)
w560 = (width / 2.2857); width560=round(w560)
w570 = (width / 2.2456); width570=round(w570)
w575 = (width / 2.226); width575=round(w575)
w600 = (width / 2.13); width600=round(w600)
w625 = (width / 2.048); width625=round(w625)
w650 = (width / 1.9692); width650=round(w650)
w655 = (width / 1.9541); width655=round(w655)
w700 = (width / 1.8285); width700=round(w700)
w740 = (width / 1.7297); width740=round(w740)
w750 = (width / 1.7067); width750=round(w750)
w830 = (width / 1.5422); width830=round(w830)
w920 = (width / 1.3913); width920=round(w920)
w930 = (width / 1.3763); width930=round(w930)
w1010 = (width / 1.2673); width1010=round(w1010)
w1100 = (width / 1.1636); width1100=round(w1100)
w1110 = (width / 1.1531); width1110=round(w1110)
w1190 = (width / 1.0756); width1190=round(w1190)
w1210 = (width / 1.0578); width1210=round(w1210)
w1240 = (width / 1.0322); width1240=round(w1240)
if height >= 721:
    LG.geometry("1280x720")
if width >= 1281:
    LG.geometry("1280x720")
else: LG.attributes('-fullscreen',True)
value1 = StringVar(); value2 = StringVar(); value3 = StringVar(); var3=StringVar()
kleur1string = StringVar()
wachtwoord1=StringVar()
wachtwoord2=StringVar();gebruiker10=StringVar();wachtwoordherstel=StringVar();data=StringVar()
loginofniet10=StringVar()
boolean=StringVar()
inlog=StringVar()
img1 = PhotoImage(file="close.png")
img2 = PhotoImage(file="vergroot.png")
img3 = PhotoImage(file="menu.png")
img4 = PhotoImage(file="bergen.png")
img7 = PhotoImage(file="weekvooruit.png")
img8 = PhotoImage(file="start.png")
img9 = PhotoImage(file="stop.png")
img10 = PhotoImage(file="info1.png")
LG.iconbitmap(default='icon.ico')

with open('safecolor.txt', 'r') as f: safecolor = f.read()
with open('loginofniet.txt', 'r') as f: loginofniet11 = f.read()
with open('height1.txt', 'r') as f: height1 = f.read()
with open('height2.txt', 'r') as f: height2 = f.read()
with open('height3.txt', 'r') as f: height3 = f.read()
with open('height4.txt', 'r') as f: height4 = f.read()
with open('height5.txt', 'r') as f: height5 = f.read()
with open('rechten.txt', 'r') as f: rechten = f.read()
with open('gebruiker1.txt', 'r') as file: data = file.readlines()
c1 = open("gebruiker1.txt", "r").readlines()[10]; counter1=c1.strip()
changey1 = open("changey1.txt", "r").readlines()
changey2 = open("changey2.txt", "r").readlines()
if counter1 == '1': gebruikersnaamup = '2'
if counter1 == '2': gebruikersnaamup = '3'
if counter1 == '3': gebruikersnaamup = '4'
if counter1 == '4': gebruikersnaamup = '5'
if counter1 == '5': pass
r2 = open("rechten2.txt", "r").readlines()[0]; rechten2=r2.strip()
r3 = open("rechten2.txt", "r").readlines()[1]; rechten3=r3.strip()
r4 = open("rechten2.txt", "r").readlines()[2]; rechten4=r4.strip()
r5 = open("rechten2.txt", "r").readlines()[3]; rechten5=r5.strip()
r6 = open("rechten2.txt", "r").readlines()[4]; rechten6=r6.strip()

def Gebruikersnaam1():
    if value3.get() == gebruiker1 and value1.get() == wachtwoord1 :
        homepage(); inlog.set("1")
        TF = open('rechten.txt', 'w'); TF.write(rechten2); TF.close()
        a4 = open("gebruiker1.txt", "r").readlines()[16]; aantal4=a4.strip()
        data[16] = aantal4 + '1'+'\n'
        with open('gebruiker1.txt', 'w') as file: file.writelines( data )
        data[21] = '1' + '\n'
        with open('gebruiker1.txt', 'w') as file: file.writelines( data )
def Gebruikersnaam2():
    if value3.get() == gebruiker2 and value1.get() == wachtwoord2 :
        homepage(); inlog="2"
        GU = "2"; TF = open('rechten.txt', 'w'); TF.write(GU); TF.close()
        data[21] = '2' + '\n'
        with open('gebruiker1.txt', 'w') as file: file.writelines( data )
def Gebruikersnaam3():
    if value3.get() == gebruiker3 and value1.get() == wachtwoord3 :
        homepage(); inlog="3"
        GU = "3"; TF = open('rechten.txt', 'w'); TF.write(GU); TF.close()
        data[21] = '3' + '\n'
        with open('gebruiker1.txt', 'w') as file: file.writelines( data )
def Gebruikersnaam4():
    if value3.get() == gebruiker4 and value1.get() == wachtwoord4 :
        homepage(); inlog="4"
        GU = "4"; TF = open('rechten.txt', 'w'); TF.write(GU); TF.close()
        data[21] = '4' + '\n'
        with open('gebruiker1.txt', 'w') as file: file.writelines( data )
def Gebruikersnaam5():
    if value3.get() == gebruiker5 and value1.get() == wachtwoord5 :
        homepage(); inlog="5"
        GU = "5"; TF = open('rechten.txt', 'w'); TF.write(GU); TF.close()
        data[21] = '5' + '\n'
        with open('gebruiker1.txt', 'w') as file: file.writelines( data )
def Gebruikers2(): Gebruikersnaam1(); Gebruikersnaam2();
def Gebruikers3(): Gebruikersnaam1(); Gebruikersnaam2(); Gebruikersnaam3()
def Gebruikers4(): Gebruikersnaam1(); Gebruikersnaam2(); Gebruikersnaam3(); Gebruikersnaam4()
def Gebruikers5(): Gebruikersnaam1(); Gebruikersnaam2(); Gebruikersnaam3(); Gebruikersnaam4(); Gebruikersnaam5()


def sluiten(): HoverButton(LG, image=img1,bg="white",bd=0,command=LG.destroy).place(x=1240,y=5); HoverButton(LG, image=img2,bg="white",bd=0,command=homepage).place(x=1210,y=5)
class HoverButton(tk.Button):
        def __init__(self, master, **kw):
            tk.Button.__init__(self,master=master,**kw)
            self.defaultBackground = self["background"]
            self.bind("<Enter>", self.on_enter)
            self.bind("<Leave>", self.on_leave)
        def on_enter(self, e):
            self['background'] = self['activebackground']
        def on_leave(self, e):
            self['background'] = self.defaultBackground
def changebackground():     
    self.defaultBackground = self["background"]
    self['background'] = "yellow"

def homepage():
    with open('safecolor.txt', 'r') as f: safecolor = f.read()
    frame4 = Canvas( LG, bg ="white", height=750, width=1300,bd=0); image = frame4.create_image(1300,-100,anchor=NE,image=img4); frame4.place(x=-5,y=0)
    starframe=Frame(LG,width=1500,height=20,bg='white',bd=0).place(x=0,y=0)
    b1 = Button(LG, text='Start',        padx=2, pady=0, bd=0, fg="black",font=('arial', 10), width= 12, height=2,bg=safecolor).grid(row=0,column=1)
    b2 = Button(LG, text='Gebruikers',   padx=2, pady=0, bd=0, fg="black",font=('arial', 10), width= 12, height=2,bg=safecolor,command=gebruikers).grid(row=0,column=2)
    b3 = Button(LG,                      padx=2, pady=0, bd=0, fg="black",font=('arial', 10), width= 50, height=2,bg=safecolor).grid(row=0,column=3)
    b4 = Button(LG, text='Knorth',       padx=2, pady=0, bd=0, fg="black",font=('arial', 10), width= 12, height=2,command=knorth,bg=safecolor).grid(row=0,column=4)
    b5 = Button(LG, text='Agenda',    padx=2, pady=0, bd=0, fg="black",font=('arial', 10), width= 12, height=2,bg=safecolor,command=agenda).grid(row=0,column=5)
    b6 = Button(LG, text='Kalender',     padx=2, pady=0, bd=0, fg="black",font=('arial', 10), width= 12, height=2,bg=safecolor).grid(row=0,column=6)
    b7 = Button(LG, text='instellingen', padx=2, pady=0, bd=0, fg="black",font=('arial', 10), width= 12, height=2,command=instellingen,bg=safecolor).grid(row=0,column=7)
    b8 = Button(LG, text='Exit',         padx=2, pady=0, bd=0, fg="black",font=('arial', 10), width= 12, height=2,command=LG.destroy,bg=safecolor).grid(row=0,column=8)
    b9 = Button(LG,                      padx=2, pady=0, bd=0, fg="black",font=('arial', 10), width= 19, height=2,bg=safecolor).grid(row=0,column=9)
    b10 = Label (LG, text=localtime,      padx=0, pady=0, bd=0, fg="black",font=('arial', 10), width= 20, height=2,bg=safecolor).grid(row=0,column=9)
class hoverFrame(tk.Frame):
    def __init__(self, master, **kw):
        tk.Frame.__init__(self,master=master,**kw)
        self.defaultBackground = self["background"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)
    def on_enter(self, e):
        self['background'] = self['activebackground']
    def on_leave(self, e):
        self['background'] = self.defaultBackground
class agenda():
    def __init__(self):
        LG.attributes('-fullscreen',True)
        c = Canvas(LG,width=width,height=height,bg="white", highlightthickness=0);c.place(x=0,y=0)
        HoverButton(LG, image=img1,bg="white",bd=0,command=LG.destroy).place(x=width1240,y=width5); HoverButton(LG, image=img2,bg="white",bd=0,command=homepage).place(x=width1210,y=width5)
        def frames1():
            Frame(LG,bg=safecolor,width=width3,height=width500).place(x=var4,y=width150)
        var4=(width20);frames1();var4=(width200);frames1();var4=(width380);frames1();var4=(width560);frames1();var4=(width740);frames1();var4=(width920);frames1();var4=(width1100);frames1()
        Frame(LG,bg=safecolor,width=width,height=width3).place(x=0,y=width145)
        Frame(LG,bg=safecolor,width=width,height=width3).place(x=0,y=width150)
        Frame(LG,bg=safecolor,width=width,height=width3).place(x=0,y=width650)
        Frame(LG,bg=safecolor,width=width,height=width3).place(x=0,y=width655)
        datum1=int 
        datum1=(20)
        datum7="26"
        jaar1="2019"
        for char in '-.,\n': Text=localtime.replace(char,' ')
        Text=Text.lower();word_list=Text.split();maand=word_list[1];jaar=word_list[4];dag=word_list[0];datum=word_list[2]
        if maand=="may":maand="Mei"
        if maand=="june":maand="Juni"
        if dag=="mon":color1="gray80"
        else:color1="white"
        if dag=="tue":color2="gray80"
        else:color2="white"
        if dag=="wed":color3="gray80"
        else:color3="white"
        if dag=="thu":color4="gray80"
        else:color4="white"
        if dag=="fri":color5="gray80"
        else:color5="white"
        if dag=="sat":color6="gray80"
        else:color6="white"
        if dag=="sun" and jaar==jaar1 and datum==datum7:color7="gray80"
        else:color7="white"
        Frame(LG,width=width180,height=width55,bg=color1).place(x=width20,y=width90);Label(LG,text=f"Maandag {datum1}",font=('arial',width15,'bold'),bg=color1).place(x=width30,y=width100)
        Frame(LG,width=width180,height=width55,bg=color2).place(x=width200,y=width90);Label(LG,text=f"Dinsdag {datum1 + (1)}",font=('arial',width15,'bold'),bg=color2).place(x=width210,y=width100)
        Frame(LG,width=width180,height=width55,bg=color3).place(x=width380,y=width90);Label(LG,text=f"Woensdag {datum1 + (2)}",font=('arial',width15,'bold'),bg=color3).place(x=width390,y=width100)
        Frame(LG,width=width180,height=width55,bg=color4).place(x=width560,y=width90);Label(LG,text=f"Donderdag {datum1 + (3)}",font=('arial',width15,'bold'),bg=color4).place(x=width570,y=width100)
        Frame(LG,width=width180,height=width55,bg=color5).place(x=width740,y=width90);Label(LG,text=f"Vrijdag {datum1 + (4)}",font=('arial',width15,'bold'),bg=color5).place(x=width750,y=width100)
        Frame(LG,width=width180,height=width55,bg=color6).place(x=width920,y=width90);Label(LG,text=f"Zaterdag {datum1 + (5)}",font=('arial',width15,'bold'),bg=color6).place(x=width930,y=width100)
        Frame(LG,width=width180,height=width55,bg=color7).place(x=width1100,y=width90);Label(LG,text=f"Zondag {datum1 + (6)}",font=('arial',width15,'bold'),bg=color7).place(x=width1110,y=width100)
        Label(LG,text=f"{maand} {jaar1}",font=('arial',width20,'bold'),bg="white").place(x=width100,y=width20)
        class buttons1():
            def __init__(self):
                t1 = Frame(LG,width=width170,height=width43,bg="white",bd=0)
                t1.bind("<ButtonRelease-1>", self.s1)
                t1.place(x=width25,y=width155)
            def s1(self):
                #clickedx=width25;clickedy=width155
                if __name__ == "__main__":
                    test()
            def test(self, event):
                tk=Tk();tk.geometry(f"{width420}x{width300}");tk.title("Planning maken");tk.configure(background="white");tk.resizable(False, False)
                rowvariable = (1)
                def buttons2():
                    def save():
                        t1 = Frame(LG,width=width170,height=width43,bg="blue",bd=0)
                        t1.bind("<ButtonRelease-1>", lambda event: test())
                        t1.place(x=width25,y=width155)
                        print(clickedy)
                    Button(tk,text=huiswerk,font=('arial',width10),bd=0,bg="white").grid(row=rowvariable,column=1)
                    Button(tk,text="Opslaan",font=('arial',12),bd=0,bg="gray80",relief="ridge",command=save).place(x=340,y=260)
                aboutStud = Entry(tk,font=('arial',12),bg="gray80",bd=0)
                aboutStud.insert(END, "Eigen invoer")
                aboutStud.place(x=220,y=10)
                Frame(tk,bg=safecolor,width=width3,height=width300).place(x=width200,y=0)
                if huiswerk1 != "": huiswerk=huiswerk1; buttons2()
                #else:
                #    test = len(huiswerk1)
                #    if test >= (29):
                #        Button(huiswerk,text=huiswerk1,font=('arial',10),bd=0,bg="white").grid(row=rowvariable,column=1)
                #    else:
                #        def test():
                #            def place():
                #                Button(testframe,text=huiswerk1,font=('arial',15),bd=0,bg="red").grid(row=0,column=0)
                #            Button(huiswerk,text=huiswerk1,font=('arial',15),bd=0,bg="red").grid(row=rowvariable,column=1)
                #            testframe= Frame(testtk,width=180,height=47).place(x=290,y=200)
                #            Button(testframe, width=200, height=47, compound="c",bd=0,bg="red",command=place).place(x=290,y=200)
                #        Button(huiswerk,text=huiswerk1,font=('arial',15),bd=0,bg="white",command=test).grid(row=rowvariable,column=1
        buttons1()
        def times():
            c.create_text (10, var5, text =tijd, font = ("times", width10,'bold'))
        tijd=(12);var5=(width175);times();tijd=(13);var5=(width225);times();tijd=(14);var5=(width275);times();tijd=(13);var5=(width325);times()
        tijd=(14);var5=(width375);times();tijd=(15);var5=(width425);times();tijd=(16);var5=(width475);times();tijd=(17);var5=(width525);times()
        tijd=(18);var5=(width575);times();tijd=(19);var5=(width625);times()
        def lines():
            def l():c.create_text (var1, var2, text = "-------------------------------------------", font = ("times", width9))
            var2=(width200);l();var2=(width250);l();var2=(width300);l();var2=(width350);l();var2=(width400);l();var2=(width450);l();var2=(width500);l();var2=(width550);l();var2=(width600);l();var2=(width650);l();
        var1=(width110);lines();var1=(width290);lines();var1=(width470);lines();var1=(width650);lines();var1=(width830);lines();var1=(width1010);lines();var1=(width1190);lines()
        #testtk=Tk()
        #rowvariable = (1)
        #huiswerk = Frame(testtk,width=100,bg="white",bd=0,height=height).place(x=20,y=20)
        h1 = open("gebruiker1.txt", "r").readlines()[77]; huiswerk1=h1.strip()
        h2 = open("gebruiker1.txt", "r").readlines()[78]; huiswerk2=h2.strip()
        h3 = open("gebruiker1.txt", "r").readlines()[79]; huiswerk3=h3.strip()
        h4 = open("gebruiker1.txt", "r").readlines()[80]; huiswerk4=h4.strip()
        h5 = open("gebruiker1.txt", "r").readlines()[81]; huiswerk5=h5.strip()
        h6 = open("gebruiker1.txt", "r").readlines()[82]; huiswerk6=h6.strip()
        h7 = open("gebruiker1.txt", "r").readlines()[83]; huiswerk7=h7.strip()
        h8 = open("gebruiker1.txt", "r").readlines()[84]; huiswerk8=h8.strip()
        h9 = open("gebruiker1.txt", "r").readlines()[85]; huiswerk9=h9.strip()
        h10 = open("gebruiker1.txt", "r").readlines()[86]; huiswerk10=h10.strip()
        h11 = open("gebruiker1.txt", "r").readlines()[87]; huiswerk11=h11.strip()
        h12 = open("gebruiker1.txt", "r").readlines()[88]; huiswerk12=h12.strip()
        h13 = open("gebruiker1.txt", "r").readlines()[89]; huiswerk13=h13.strip()
        h14 = open("gebruiker1.txt", "r").readlines()[90]; huiswerk14=h14.strip()
        h15 = open("gebruiker1.txt", "r").readlines()[91]; huiswerk15=h15.strip()
        h16 = open("gebruiker1.txt", "r").readlines()[92]; huiswerk16=h16.strip()
        h17 = open("gebruiker1.txt", "r").readlines()[93]; huiswerk17=h17.strip()
        h18 = open("gebruiker1.txt", "r").readlines()[94]; huiswerk18=h18.strip()
        h19 = open("gebruiker1.txt", "r").readlines()[95]; huiswerk19=h19.strip()
        h20 = open("gebruiker1.txt", "r").readlines()[96]; huiswerk20=h20.strip()
def gebruikers():
    r1 = open("gebruiker1.txt", "r").readlines()[11]; rechten1=r1.strip()
    r1 = open("gebruiker1.txt", "r").readlines()[12]; rechten2=r1.strip()
    r1 = open("gebruiker1.txt", "r").readlines()[13]; rechten3=r1.strip()
    r1 = open("gebruiker1.txt", "r").readlines()[14]; rechten4=r1.strip()
    r1 = open("gebruiker1.txt", "r").readlines()[15]; rechten5=r1.strip()
    r1 = open("gebruiker1.txt", "r").readlines()[21]; user1=r1.strip()
    if rechten1 == "1" and user1 == "1" or rechten2 == "1" and user1 == "2" or rechten3 == "1" and user1 == "3" or rechten4 == "1" and user1 == "4" or rechten5 == "1" and user1 == "5":
        c1 = open("gebruiker1.txt", "r").readlines()[10]; counter1=c1.strip()
        with open('safecolor.txt', 'r') as f: safecolor = f.read()
        def sluiten(): HoverButton(LG, image=img1,bg="white",bd=0,command=LG.destroy).place(x=1240,y=5); HoverButton(LG, image=img2,bg="white",bd=0,command=homepage).place(x=1210,y=5)
        Frame(LG,width=1300,height=800,bg="white").place(x=0,y=0)
        Frame(LG,width=200,height=800,bg="gray20").place(x=0,y=0); sluiten()
        var1=IntVar(); var1.set(0)
        def test():
            Label(LG,text="Persoonlijke informatie",font=('arial',25,'bold'),bg="white").place(x=600,y=20)
            Frame(LG,width=800,height=2,bg=safecolor).place(x=400,y=100)
            Frame(LG,width=800,height=2,bg=safecolor).place(x=400,y=104)
            Frame(LG,width=800,height=2,bg=safecolor).place(x=400,y=400)
            Frame(LG,width=800,height=2,bg=safecolor).place(x=400,y=404)
            Frame(LG,width=2,height=304,bg=safecolor).place(x=400,y=100)
            Frame(LG,width=2,height=296,bg=safecolor).place(x=404,y=104)
            Frame(LG,width=2,height=296,bg=safecolor).place(x=1196,y=104)
            Frame(LG,width=2,height=304,bg=safecolor).place(x=1200,y=100)
            a4 = open("gebruiker1.txt", "r").readlines()[16]; aantal4=a4.strip()
            count = 0
            for i in aantal4:
                if i == '1': count = count + 1
            g1 = open("gebruiker1.txt", "r").readlines()[0]; gebruiker1 = g1.strip()
            g1 = open("gebruiker1.txt", "r").readlines()[5]; wachtwoord1 = g1.strip()
            g1 = open("gebruiker1.txt", "r").readlines()[22]; leeftijd1 = g1.strip()
            g1 = open("gebruiker1.txt", "r").readlines()[27]; email1 = g1.strip()
            Label(LG,text=f"{gebruiker1} heeft {count} keer ingelogd",bg="white",font=('arial',15,'bold')).place(x=430,y=200)
            class HoverLabel(tk.Button):
                def __init__(self, master, **kw):
                    tk.Label.__init__(self,master=master,**kw)
                    self.bind("<Enter>", self.on_enter)
                    self.bind("<Leave>", self.on_leave)
                def on_enter(self, e):
                    Label(LG,text="Hiermee geeft u de gebruiker het recht \n om andere gebruikers te verwijderen",bd=0, font=('arial',8)).place(x=663,y=150)
                def on_leave(self, e):
                    Frame(LG,bg="white",width=190,height=40,bd=0).place(x=663,y=150)
            HoverLabel(LG,image=img10).place(x=653,y=125)
            s = ttk.Style()
            s.configure('my.TCheckbutton', font=('arial', 15,'bold'))
            ttk.Checkbutton(LG,text="Administrator rechten",style='my.TCheckbutton',variable=var1).place(x=430,y=140)
            Label(LG,text=f"Wachtwoord is: {wachtwoord1}",font=('arial',15,'bold')).place(x=430,y=260)
            Label(LG,text=f"Email is: {email1}",font=('arial',15,'bold')).place(x=860,y=140)
            Label(LG,text=f"Leeftijd is: {leeftijd1}",font=('arial',15,'bold')).place(x=860,y=200)
            def opslaan():
                if var1.get() == 1:
                    data[11] = '1' + '\n'
                    with open('gebruiker1.txt', 'w') as file: file.writelines( data )
                else:
                    data[11] = '0' + '\n'
                    with open('gebruiker1.txt', 'w') as file: file.writelines( data )
            g1 = open("safecolor.txt", "r").readlines()[0]; safecolor12 = g1.strip()
            if safecolor12 == "white":
                fg1="black"
            else:
                fg1="white"
            Button(LG,text="Opslaan",command=opslaan,bg=safecolor,bd=0,relief="groove",fg=fg1 ,font=('arial',12,'bold')).place(x=1130,y=410)
        if counter1 == '1':
            g1 = open("gebruiker1.txt", "r").readlines()[0]; gebruiker1=g1.strip()
            w1 = open("gebruiker1.txt", "r").readlines()[5]; wachtwoord1=w1.strip()
            HoverButton(LG,text=gebruiker1,bd=0,fg="white",font=('arial', 15, 'bold'), width= 15, height=1,bg="gray20",activebackground="gray30").place(x=0,y=0)
        if counter1 == '2':
            g1 = open("gebruiker1.txt", "r").readlines()[0]; gebruiker1=g1.strip()
            g2 = open("gebruiker1.txt", "r").readlines()[1]; gebruiker2=g2.strip()
            w1 = open("gebruiker1.txt", "r").readlines()[5]; wachtwoord1=w1.strip()
            w2 = open("gebruiker1.txt", "r").readlines()[6]; wachtwoord2=w2.strip()
            HoverButton(LG,text=gebruiker1,bd=0,fg="white",font=('arial', 15, 'bold'), width= 15, height=1,bg="gray20",activebackground="gray30").place(x=0,y=0)
            HoverButton(LG,text=gebruiker2,bd=0,fg="white",font=('arial', 15, 'bold'), width= 15, height=1,bg="gray20",activebackground="gray30").place(x=0,y=50)
        if counter1 == '3':
            g1 = open("gebruiker1.txt", "r").readlines()[0]; gebruiker1=g1.strip()
            g2 = open("gebruiker1.txt", "r").readlines()[1]; gebruiker2=g2.strip()
            g3 = open("gebruiker1.txt", "r").readlines()[2]; gebruiker3=g3.strip()
            w1 = open("gebruiker1.txt", "r").readlines()[5]; wachtwoord1=w1.strip()
            w2 = open("gebruiker1.txt", "r").readlines()[6]; wachtwoord2=w2.strip()
            w3 = open("gebruiker1.txt", "r").readlines()[7]; wachtwoord3=w3.strip()
            HoverButton(LG,text=gebruiker1,bd=0,fg="white",font=('arial', 15, 'bold'), width= 15, height=1,bg="gray20",activebackground="gray30").place(x=0,y=0)
            HoverButton(LG,text=gebruiker2,bd=0,fg="white",font=('arial', 15, 'bold'), width= 15, height=1,bg="gray20",activebackground="gray30").place(x=0,y=50)
            HoverButton(LG,text=gebruiker3,bd=0,fg="white",font=('arial', 15, 'bold'), width= 15, height=1,bg="gray20",activebackground="gray30").place(x=0,y=100)
        if counter1 == '4':
            g1 = open("gebruiker1.txt", "r").readlines()[0]; gebruiker1=g1.strip()
            g2 = open("gebruiker1.txt", "r").readlines()[1]; gebruiker2=g2.strip()
            g3 = open("gebruiker1.txt", "r").readlines()[2]; gebruiker3=g3.strip()
            g4 = open("gebruiker1.txt", "r").readlines()[3]; gebruiker4=g4.strip()
            w1 = open("gebruiker1.txt", "r").readlines()[5]; wachtwoord1=w1.strip()
            w2 = open("gebruiker1.txt", "r").readlines()[6]; wachtwoord2=w2.strip()
            w3 = open("gebruiker1.txt", "r").readlines()[7]; wachtwoord3=w3.strip()
            w4 = open("gebruiker1.txt", "r").readlines()[8]; wachtwoord4=w4.strip()
            HoverButton(LG,text=gebruiker1,bd=0,fg="white",font=('arial', 15, 'bold'), width= 15, height=1,bg="gray20",command=test,activebackground="gray30").place(x=0,y=15)
            HoverButton(LG,text=gebruiker2,bd=0,fg="white",font=('arial', 15, 'bold'), width= 15, height=1,bg="gray20",activebackground="gray30").place(x=0,y=65)
            HoverButton(LG,text=gebruiker3,bd=0,fg="white",font=('arial', 15, 'bold'), width= 15, height=1,bg="gray20",activebackground="gray30").place(x=0,y=115)
            HoverButton(LG,text=gebruiker4,bd=0,fg="white",font=('arial', 15, 'bold'), width= 15, height=1,bg="gray20",activebackground="gray30").place(x=0,y=165)
        if counter1 == '5':
            g1 = open("gebruiker1.txt", "r").readlines()[0]; gebruiker1=g1.strip()
            g2 = open("gebruiker1.txt", "r").readlines()[1]; gebruiker2=g2.strip()
            g3 = open("gebruiker1.txt", "r").readlines()[2]; gebruiker3=g3.strip()
            g4 = open("gebruiker1.txt", "r").readlines()[3]; gebruiker4=g4.strip()
            g5 = open("gebruiker1.txt", "r").readlines()[4]; gebruiker5=g5.strip()
            w1 = open("gebruiker1.txt", "r").readlines()[5]; wachtwoord1=w1.strip()
            w2 = open("gebruiker1.txt", "r").readlines()[6]; wachtwoord2=w2.strip()
            w3 = open("gebruiker1.txt", "r").readlines()[7]; wachtwoord3=w3.strip()
            w4 = open("gebruiker1.txt", "r").readlines()[8]; wachtwoord4=w4.strip()
            w5 = open("gebruiker1.txt", "r").readlines()[9]; wachtwoord5=w5.strip()
            HoverButton(LG,text=gebruiker1,bd=0,fg="white",font=('arial', 15, 'bold'), width= 15, height=1,bg="gray20",activebackground="gray30").place(x=0,y=0)
            HoverButton(LG,text=gebruiker2,bd=0,fg="white",font=('arial', 15, 'bold'), width= 15, height=1,bg="gray20",activebackground="gray30").place(x=0,y=50)
            HoverButton(LG,text=gebruiker3,bd=0,fg="white",font=('arial', 15, 'bold'), width= 15, height=1,bg="gray20",activebackground="gray30").place(x=0,y=100)
            HoverButton(LG,text=gebruiker4,bd=0,fg="white",font=('arial', 15, 'bold'), width= 15, height=1,bg="gray20",activebackground="gray30").place(x=0,y=150)
            HoverButton(LG,text=gebruiker5,bd=0,fg="white",font=('arial', 15, 'bold'), width= 15, height=1,bg="gray20",activebackground="gray30").place(x=0,y=200)
    else:
        messagebox.showinfo("Systeem", "Je hebt geen toegang tot dit")
class instellingen:
    def safecolor1(self): GU = "grey99";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor2(self): GU = "grey75";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor3(self): GU = "grey60";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor4(self): GU = "grey40";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor5(self): GU = "grey30";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor6(self): GU = "grey20";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor7(self): GU = "grey10";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor8(self): GU = "grey1";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor9(self): GU = "Bisque";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor10(self): GU = "Bisque2";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor11(self): GU = "Bisque3";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor12(self): GU = "Bisque4";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor13(self): GU = "RoyalBlue1";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor14(self): GU = "RoyalBlue2";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor15(self): GU = "RoyalBlue3";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor16(self): GU = "RoyalBlue4";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor17(self): GU = "LightSteelBlue1";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor18(self): GU = "LightSteelBlue2";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor19(self): GU = "LightSteelBlue3";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor20(self): GU = "LightSteelBlue4";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor21(self): GU = "cyan1";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor22(self): GU = "cyan2";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor23(self): GU = "cyan3";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor24(self): GU = "cyan4";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor25(self): GU = "lawn Green";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor26(self): GU = "green2";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor27(self): GU = "green3";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor28(self): GU = "green4";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor29(self): GU = "khaki1";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor30(self): GU = "khaki2";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor31(self): GU = "khaki3";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor32(self): GU = "khaki4";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor33(self): GU = "yellow";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor34(self): GU = "yellow2";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor35(self): GU = "yellow3";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor36(self): GU = "yellow4";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor37(self): GU = "red";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor38(self): GU = "red2";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor39(self): GU = "red3";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor40(self): GU = "red4";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor41(self): GU = "coral1";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor42(self): GU = "coral2";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor43(self): GU = "coral3";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor44(self): GU = "coral4";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor45(self): GU = "Orange Red";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor46(self): GU = "Orangered2";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor47(self): GU = "Orangered3";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor48(self): GU = "Orangered4";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor49(self): GU = "Maroon1";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor50(self): GU = "Maroon2";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor51(self): GU = "Maroon3";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor52(self): GU = "Maroon4";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor53(self): GU = "plum1";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor54(self): GU = "plum2";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor55(self): GU = "plum3";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor56(self): GU = "plum4";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor57(self): GU = "purple1";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor58(self): GU = "purple2";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor59(self): GU = "purple3";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor60(self): GU = "purple4";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor61(self): GU = "thistle1";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor62(self): GU = "thistle1";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor63(self): GU = "thistle1";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor64(self): GU = "thistle1";oTF = open('safecolor.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor101(self): GU = "grey99";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor102(self): GU = "grey75";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor103(self): GU = "grey60";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor104(self): GU = "grey40";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor105(self): GU = "grey30";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor106(self): GU = "grey20";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor107(self): GU = "grey10";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor108(self): GU = "grey1";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor109(self): GU = "Bisque";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor110(self): GU = "Bisque2";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor111(self): GU = "Bisque3";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor112(self): GU = "Bisque4";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor113(self): GU = "RoyalBlue1";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor114(self): GU = "RoyalBlue2";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor115(self): GU = "RoyalBlue3";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor116(self): GU = "RoyalBlue4";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor117(self): GU = "LightSteelBlue1";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor118(self): GU = "LightSteelBlue2";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor119(self): GU = "LightSteelBlue3";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor120(self): GU = "LightSteelBlue4";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor121(self): GU = "cyan1";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor122(self): GU = "cyan2";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor123(self): GU = "cyan3";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor124(self): GU = "cyan4";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor125(self): GU = "lawn Green";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor126(self): GU = "green2";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor127(self): GU = "green3";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor128(self): GU = "green4";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor129(self): GU = "khaki1";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor130(self): GU = "khaki2";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor131(self): GU = "khaki3";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor132(self): GU = "khaki4";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor133(self): GU = "yellow";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor134(self): GU = "yellow2";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor135(self): GU = "yellow3";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor136(self): GU = "yellow4";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor137(self): GU = "red";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor138(self): GU = "red2";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor139(self): GU = "red3";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor140(self): GU = "red4";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor141(self): GU = "coral1";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor142(self): GU = "coral2";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor143(self): GU = "coral3";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor144(self): GU = "coral4";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor145(self): GU = "Orange Red";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor146(self): GU = "Orangered2";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor147(self): GU = "Orangered3";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor148(self): GU = "Orangered4";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor149(self): GU = "Maroon1";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor150(self): GU = "Maroon2";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor151(self): GU = "Maroon3";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor152(self): GU = "Maroon4";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor153(self): GU = "plum1";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor154(self): GU = "plum2";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor155(self): GU = "plum3";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor156(self): GU = "plum4";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor157(self): GU = "purple1";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor158(self): GU = "purple2";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor159(self): GU = "purple3";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor160(self): GU = "purple4";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor161(self): GU = "thistle1";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor162(self): GU = "thistle1";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor163(self): GU = "thistle1";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def safecolor164(self): GU = "thistle1";oTF = open('safecolor2.txt', 'w'); oTF.write(GU); oTF.close()
    def thema(self):
        with open('safecolor.txt', 'r') as f: safecolor = f.read()
        with open('safecolor2.txt', 'r') as f: safecolor = f.read()
        Canvas(LG,width=1000,height=750,bg="white",bd=0).place(x=300,y=0);sluiten(); Label(LG,font=('arial', 25),bg='white',fg="black",text="Thema's").place(x=350,y=30); Label(LG,text="Hoofd kleur",font=('arial', 18, 'bold'),bg="white").place(x=690,y=150); f1 = Frame(LG,width=870,bg="grey85",bd=0,height=200).place(x=335,y=185); HoverButton(LG,bg="grey99",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor1).place(x=350,y=200); HoverButton(LG,bg="grey75",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor2).place(x=400,y=200); HoverButton(LG,bg="grey60",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor3).place(x=450,y=200); HoverButton(LG,bg="grey40",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor4).place(x=500,y=200); HoverButton(LG,bg="grey30",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor5).place(x=550,y=200); HoverButton(LG,bg="grey20",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor6).place(x=600,y=200); HoverButton(LG,bg="grey10",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor7).place(x=650,y=200); HoverButton(LG,bg="grey1",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor8).place(x=700,y=200); HoverButton(LG,bg="Bisque",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor9).place(x=350,y=245); HoverButton(LG,bg="Bisque2",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor10).place(x=400,y=245); HoverButton(LG,bg="Bisque3",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor11).place(x=450,y=245); HoverButton(LG,bg="Bisque4",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor12).place(x=500,y=245); HoverButton(LG,bg="RoyalBlue1",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor13).place(x=550,y=245); HoverButton(LG,bg="RoyalBlue2",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor14).place(x=600,y=245); HoverButton(LG,bg="RoyalBlue3",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor15).place(x=650,y=245); HoverButton(LG,bg="RoyalBlue4",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor16).place(x=700,y=245); HoverButton(LG,bg="LightSteelBlue1",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor17).place(x=350,y=290); HoverButton(LG,bg="LightSteelBlue2",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor18).place(x=400,y=290); HoverButton(LG,bg="LightSteelBlue3",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor19).place(x=450,y=290); HoverButton(LG,bg="LightSteelBlue4",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor20).place(x=500,y=290); HoverButton(LG,bg="cyan1",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor21).place(x=550,y=290); HoverButton(LG,bg="cyan2",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor22).place(x=600,y=290); HoverButton(LG,bg="cyan3",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor23).place(x=650,y=290); HoverButton(LG,bg="cyan4",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor24).place(x=700,y=290); HoverButton(LG,bg="lawn Green",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor25).place(x=350,y=335); HoverButton(LG,bg="green2",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor26).place(x=400,y=335); HoverButton(LG,bg="green3",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor27).place(x=450,y=335); HoverButton(LG,bg="green4",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor28).place(x=500,y=335); HoverButton(LG,bg="khaki1",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor29).place(x=550,y=335); HoverButton(LG,bg="khaki2",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor30).place(x=600,y=335); HoverButton(LG,bg="khaki3",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor31).place(x=650,y=335); HoverButton(LG,bg="khaki4",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor32).place(x=700,y=335); HoverButton(LG,bg="yellow",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor33).place(x=800,y=200); HoverButton(LG,bg="yellow2",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor34).place(x=850,y=200); HoverButton(LG,bg="yellow3",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor35).place(x=900,y=200); HoverButton(LG,bg="yellow4",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor36).place(x=950,y=200); HoverButton(LG,bg="red",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor37).place(x=1000,y=200); HoverButton(LG,bg="red2",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor38).place(x=1050,y=200); HoverButton(LG,bg="red3",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor39).place(x=1100,y=200); HoverButton(LG,bg="red4",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor40).place(x=1150,y=200); HoverButton(LG,bg="coral1",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor41).place(x=800,y=245); HoverButton(LG,bg="coral2",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor42).place(x=850,y=245); HoverButton(LG,bg="coral3",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor43).place(x=900,y=245); HoverButton(LG,bg="coral4",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor44).place(x=950,y=245); HoverButton(LG,bg="orange red",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor45).place(x=1000,y=245); HoverButton(LG,bg="Orangered2",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor46).place(x=1050,y=245); HoverButton(LG,bg="Orangered3",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor47).place(x=1100,y=245); HoverButton(LG,bg="Orangered4",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor48).place(x=1150,y=245); HoverButton(LG,bg="Maroon1",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor49).place(x=800,y=290); HoverButton(LG,bg="Maroon2",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor50).place(x=850,y=290); HoverButton(LG,bg="Maroon3",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor51).place(x=900,y=290); HoverButton(LG,bg="Maroon4",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor52).place(x=950,y=290); HoverButton(LG,bg="plum1",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor53).place(x=1000,y=290); HoverButton(LG,bg="plum2",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor54).place(x=1050,y=290); HoverButton(LG,bg="plum3",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor55).place(x=1100,y=290); HoverButton(LG,bg="plum4",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor56).place(x=1150,y=290); HoverButton(LG,bg="purple1",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor57).place(x=800,y=335); HoverButton(LG,bg="purple2",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor58).place(x=850,y=335); HoverButton(LG,bg="purple3",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor59).place(x=900,y=335); HoverButton(LG,bg="purple4",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor60).place(x=950,y=335); HoverButton(LG,bg="thistle1",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor61).place(x=1000,y=335); HoverButton(LG,bg="thistle2",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor62).place(x=1050,y=335); HoverButton(LG,bg="thistle3",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor63).place(x=1100,y=335); HoverButton(LG,bg="thistle4",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor64).place(x=1150,y=335); Label(LG,text="Tweede kleur",font=('arial', 18, 'bold'),bg="white").place(x=690,y=450); f1 = Frame(LG,width=870,bg="grey85",bd=0,height=200).place(x=335,y=485); HoverButton(LG,bg="grey99",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor101).place(x=350,y=500); HoverButton(LG,bg="grey75",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor102).place(x=400,y=500); HoverButton(LG,bg="grey60",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor103).place(x=450,y=500); HoverButton(LG,bg="grey40",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor104).place(x=500,y=500); HoverButton(LG,bg="grey30",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor105).place(x=550,y=500); HoverButton(LG,bg="grey20",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor106).place(x=600,y=500); HoverButton(LG,bg="grey10",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor107).place(x=650,y=500); HoverButton(LG,bg="grey1",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor108).place(x=700,y=500); HoverButton(LG,bg="Bisque",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor109).place(x=350,y=545); HoverButton(LG,bg="Bisque2",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor110).place(x=400,y=545); HoverButton(LG,bg="Bisque3",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor111).place(x=450,y=545); HoverButton(LG,bg="Bisque4",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor112).place(x=500,y=545); HoverButton(LG,bg="RoyalBlue1",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor113).place(x=550,y=545); HoverButton(LG,bg="RoyalBlue2",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor114).place(x=600,y=545); HoverButton(LG,bg="RoyalBlue3",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor115).place(x=650,y=545); HoverButton(LG,bg="RoyalBlue4",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor116).place(x=700,y=545); HoverButton(LG,bg="LightSteelBlue1",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor117).place(x=350,y=590); HoverButton(LG,bg="LightSteelBlue2",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor118).place(x=400,y=590); HoverButton(LG,bg="LightSteelBlue3",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor119).place(x=450,y=590); HoverButton(LG,bg="LightSteelBlue4",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor120).place(x=500,y=590); HoverButton(LG,bg="cyan1",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor121).place(x=550,y=590); HoverButton(LG,bg="cyan2",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor122).place(x=600,y=590); HoverButton(LG,bg="cyan3",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor123).place(x=650,y=590); HoverButton(LG,bg="cyan4",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor124).place(x=700,y=590); HoverButton(LG,bg="lawn Green",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor125).place(x=350,y=635); HoverButton(LG,bg="green2",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor126).place(x=400,y=635); HoverButton(LG,bg="green3",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor127).place(x=450,y=635); HoverButton(LG,bg="green4",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor128).place(x=500,y=635); HoverButton(LG,bg="khaki1",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor129).place(x=550,y=635); HoverButton(LG,bg="khaki2",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor130).place(x=600,y=635); HoverButton(LG,bg="khaki3",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor131).place(x=650,y=635); HoverButton(LG,bg="khaki4",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor132).place(x=700,y=635); HoverButton(LG,bg="yellow",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor133).place(x=800,y=500); HoverButton(LG,bg="yellow2",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor134).place(x=850,y=500); HoverButton(LG,bg="yellow3",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor135).place(x=900,y=500); HoverButton(LG,bg="yellow4",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor136).place(x=950,y=500); HoverButton(LG,bg="red",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor137).place(x=1000,y=500); HoverButton(LG,bg="red2",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor138).place(x=1050,y=500); HoverButton(LG,bg="red3",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor139).place(x=1100,y=500); HoverButton(LG,bg="red4",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor140).place(x=1150,y=500); HoverButton(LG,bg="coral1",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor141).place(x=800,y=545); HoverButton(LG,bg="coral2",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor142).place(x=850,y=545); HoverButton(LG,bg="coral3",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor143).place(x=900,y=545); HoverButton(LG,bg="coral4",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor144).place(x=950,y=545); HoverButton(LG,bg="orange red",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor145).place(x=1000,y=545); HoverButton(LG,bg="Orangered2",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor146).place(x=1050,y=545); HoverButton(LG,bg="Orangered3",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor147).place(x=1100,y=545); HoverButton(LG,bg="Orangered4",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor148).place(x=1150,y=545); HoverButton(LG,bg="Maroon1",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor149).place(x=800,y=590); HoverButton(LG,bg="Maroon2",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor150).place(x=850,y=590); HoverButton(LG,bg="Maroon3",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor151).place(x=900,y=590); HoverButton(LG,bg="Maroon4",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor152).place(x=950,y=590); HoverButton(LG,bg="plum1",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor153).place(x=1000,y=590); HoverButton(LG,bg="plum2",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor154).place(x=1050,y=590); HoverButton(LG,bg="plum3",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor155).place(x=1100,y=590); HoverButton(LG,bg="plum4",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor156).place(x=1150,y=590); HoverButton(LG,bg="purple1",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor157).place(x=800,y=635); HoverButton(LG,bg="purple2",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor158).place(x=850,y=635); HoverButton(LG,bg="purple3",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor159).place(x=900,y=635); HoverButton(LG,bg="purple4",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor160).place(x=950,y=635); HoverButton(LG,bg="thistle1",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor161).place(x=1000,y=635); HoverButton(LG,bg="thistle2",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor162).place(x=1050,y=635); HoverButton(LG,bg="thistle3",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor163).place(x=1100,y=635); HoverButton(LG,bg="thistle4",width=5,height=2,padx=2, pady=2,bd=0,activebackground='red',command=self.safecolor164).place(x=1150,y=635)
    def wachtwoord():
        Canvas(LG,width=1000,height=750,bg="white",bd=0).place(x=300,y=0)
        e2=Entry(LG,textvariable=wachtwoord2).place(x=400,y=300)
        e3=Entry(LG,textvariable=gebruiker10).place(x=400,y=200)
        box=ttk.Combobox(LG,textvariable=loginofniet10,font=small_font,state='readonly'); box['values']=('Als ik het programma opstart','Nooit'); remembertest=box.current(0); box.place(x=400,y=140)
        Label(LG,text="Aanmeldingsopties",font=('arial', 20),bg="white").place(x=400,y=30)
        Label(LG,text="Aanmelding vereisen",font=('arial', 16),bg="white").place(x=400,y=80)
        Label(LG,text="Wanneer moet er een log in scherm getoont worden?",font=('arial', 12),bg="white").place(x=400,y=110)
        def nieuwwachtwoord(): fline=wachtwoord2.get();src=open("wachtwoord1.txt","w"); src.writelines(fline); src.close(); return
        def nieuwegebruiker(): GU = gebruiker10.get(); oTF = open('gebruiker1.txt', 'w'); oTF.write(GU); oTF.close(); return
        def loginofnietsafe(): GU = loginofniet10.get(); oTF = open('loginofniet.txt', 'w'); oTF.write(GU); oTF.close(); return
        def loginofniet(): loginofnietsafe(); homepage()
        def loginofniet2(): loginofnietsafe(); LG.destroy()
        HoverButton(LG, image=img1,bg="white",bd=0,command=loginofniet2).place(x=1240,y=5); HoverButton(LG, image=img2,bg="white",bd=0,command=loginofniet).place(x=1210,y=5)
        Button(LG,text="update",font=('arial', 20),bg="red",command=nieuwegebruiker).place(x=500,y=200)
        Button(LG,text="update",font=('arial', 20),bg="red",command=nieuwwachtwoord).place(x=500,y=300)
    def gebruikersnaam():
        r1 = open("gebruiker1.txt", "r").readlines()[11]; rechten1=r1.strip()
        r1 = open("gebruiker1.txt", "r").readlines()[12]; rechten2=r1.strip()
        r1 = open("gebruiker1.txt", "r").readlines()[13]; rechten3=r1.strip()
        r1 = open("gebruiker1.txt", "r").readlines()[14]; rechten4=r1.strip()
        r1 = open("gebruiker1.txt", "r").readlines()[15]; rechten5=r1.strip()
        r1 = open("gebruiker1.txt", "r").readlines()[21]; user1=r1.strip()
        g1 = open("gebruiker1.txt", "r").readlines()[0]; gebruiker1=g1.strip()
        g2 = open("gebruiker1.txt", "r").readlines()[1]; gebruiker2=g2.strip()
        g3 = open("gebruiker1.txt", "r").readlines()[2]; gebruiker3=g3.strip()
        g4 = open("gebruiker1.txt", "r").readlines()[3]; gebruiker4=g4.strip()
        g5 = open("gebruiker1.txt", "r").readlines()[4]; gebruiker5=g5.strip()
        if rechten1 == "1" and user1 == "1" or rechten2 == "1" and user1 == "2" or rechten3 == "1" and user1 == "3" or rechten4 == "1" and user1 == "4" or rechten5 == "1" and user1 == "5":
            def del1(): messagebox.showinfo("Systeem", "Deze gebruiker kun je niet verwijderen")
            def del2():
                def run():
                    with open('gebruiker1.txt', 'w') as file: file.writelines( data )
                g5 = open("gebruiker1.txt", "r").readlines()[5]; gebruiker5=g5.strip()
                g5 = open("gebruiker1.txt", "r").readlines()[10]; wachtwoord=g5.strip()
                if wachtwoord=="5": data[10]='4' + '\n'; run()
                if wachtwoord=="4": data[10]='3' + '\n'; run()
                if wachtwoord=="3": data[10]='2' + '\n'; run()
                if wachtwoord=="2": data[10]='1' + '\n'; run()
                g5 = open("gebruiker1.txt", "r").readlines()[10]; wachtwoord=g5.strip()
                data[5]= '' + '\n' + gebruiker5 + '\n'; run()
                data[10]= '' + '\n' + wachtwoord + '\n'; run()
                data[1]=''; run(); data[6]=''; run()
                messagebox.showinfo("Systeem", "De gebruiker is verwijderd"); gebruikersnaam()
            def del3():
                def run():
                    with open('gebruiker1.txt', 'w') as file: file.writelines( data )
                g5 = open("gebruiker1.txt", "r").readlines()[5]; gebruiker5=g5.strip()
                g5 = open("gebruiker1.txt", "r").readlines()[10]; wachtwoord=g5.strip()
                if wachtwoord=="5": data[10]='4' + '\n'; run()
                if wachtwoord=="4": data[10]='3' + '\n'; run()
                if wachtwoord=="3": data[10]='2' + '\n'; run()
                g5 = open("gebruiker1.txt", "r").readlines()[10]; wachtwoord=g5.strip()
                data[5]= '' + '\n' + gebruiker5 + '\n'; run()
                data[10]= '' + '\n' + wachtwoord + '\n'; run()
                data[2]=''; run(); data[7]=''; run()
                messagebox.showinfo("Systeem", "De gebruiker is verwijderd"); gebruikersnaam()
            def del4():
                def run():
                    with open('gebruiker1.txt', 'w') as file: file.writelines( data )
                g5 = open("gebruiker1.txt", "r").readlines()[5]; gebruiker5=g5.strip()
                g5 = open("gebruiker1.txt", "r").readlines()[10]; wachtwoord=g5.strip()
                if wachtwoord=="5": data[10]='4' + '\n'; run()
                if wachtwoord=="4": data[10]='3' + '\n'; run()
                g5 = open("gebruiker1.txt", "r").readlines()[10]; wachtwoord=g5.strip()
                data[5]= '' + '\n' + gebruiker5 + '\n'; run()
                data[10]= '' + '\n' + wachtwoord + '\n'; run()
                data[3]=''; run(); data[8]=''; run()
                messagebox.showinfo("Systeem", "De gebruiker is verwijderd"); gebruikersnaam()
            def del5():
                def run():
                    with open('gebruiker1.txt', 'w') as file: file.writelines( data )
                g5 = open("gebruiker1.txt", "r").readlines()[5]; gebruiker5=g5.strip()
                data[10]='4' + '\n'; run()
                g5 = open("gebruiker1.txt", "r").readlines()[10]; wachtwoord=g5.strip()
                data[5]= '' + '\n' + gebruiker5 + '\n'; run()
                data[10]= '' + '\n' + wachtwoord + '\n'; run()
                data[4]=''; run(); data[9]=''; run()
                messagebox.showinfo("Systeem", "De gebruiker is verwijderd"); gebruikersnaam()
            def a1(): g1 = open("gebruiker1.txt", "r").readlines()[0]; gebruiker1=g1.strip(); HoverButton(LG,text=gebruiker1,bd=0,bg='gray20',font=('arial', 15),fg="white",width=20,activebackground='gray30').place(x=900,y=150);HoverButton(LG,bg='red',activebackground='red4',bd=0,font=('arial', 24),text='x',width=2,command=del1).place(x=1120,y=150)
            def a2(): g2 = open("gebruiker1.txt", "r").readlines()[1]; gebruiker2=g2.strip(); HoverButton(LG,text=gebruiker2,bd=0,bg='gray20',font=('arial', 15),fg="white",width=20,activebackground='gray30').place(x=900,y=200);HoverButton(LG,bg='red',activebackground='red4',bd=0,font=('arial', 24),text='x',width=2,command=del2).place(x=1120,y=200)
            def a3(): g3 = open("gebruiker1.txt", "r").readlines()[2]; gebruiker3=g3.strip(); HoverButton(LG,text=gebruiker3,bd=0,bg='gray20',font=('arial', 15),fg="white",width=20,activebackground='gray30').place(x=900,y=250);HoverButton(LG,bg='red',activebackground='red4',bd=0,font=('arial', 24),text='x',width=2,command=del3).place(x=1120,y=250)
            def a4(): g4 = open("gebruiker1.txt", "r").readlines()[3]; gebruiker4=g4.strip(); HoverButton(LG,text=gebruiker4,bd=0,bg='gray20',font=('arial', 15),fg="white",width=20,activebackground='gray30').place(x=900,y=300);HoverButton(LG,bg='red',activebackground='red4',bd=0,font=('arial', 24),text='x',width=2,command=del4).place(x=1120,y=300)
            def a5(): g5 = open("gebruiker1.txt", "r").readlines()[4]; gebruiker5=g5.strip(); HoverButton(LG,text=gebruiker5,bd=0,bg='gray20',font=('arial', 15),fg="white",width=20,activebackground='gray30').place(x=900,y=350);HoverButton(LG,bg='red',activebackground='red4',bd=0,font=('arial', 24),text='x',width=2,command=del5).place(x=1120,y=350)
            Canvas(LG,width=1000,height=750,bg="white",bd=0).place(x=300,y=0)
            Entry(LG,font=('arial', 15),bd=2,relief="groove",textvariable=gebruiker10).place(x=400,y=200)
            wachtwoord2 = StringVar()
            wachtwoord3 = StringVar()
            leeftijd = StringVar()
            email = StringVar()
            Entry(LG,show='*',font=('arial', 15),bd=2,relief="groove",textvariable=wachtwoord2).place(x=400,y=250)
            Entry(LG,show='*',font=('arial', 15),bd=2,relief="groove",textvariable=wachtwoord3).place(x=400,y=300)
            Entry(LG,font=('arial', 15),bd=2,relief="groove",textvariable=leeftijd).place(x=400,y=350)
            Entry(LG,font=('arial', 15),bd=2,relief="groove",textvariable=email).place(x=400,y=400)
            Label(LG,text="Nieuwe gebruiker toevoegen",font=('arial', 20),bg="white").place(x=400,y=30)
            Label(LG,text="Gebruikersnaam:",font=('arial', 10),bg="white").place(x=400,y=178)
            Label(LG,text="Wachtwoord:",font=('arial', 10),bg="white").place(x=400,y=228)
            Label(LG,text="Herhaal Wachtwoord:",font=('arial', 10),bg="white").place(x=400,y=278)
            Label(LG,text="Leeftijd:",font=('arial', 10),bg="white").place(x=400,y=328)
            Label(LG,text="Email:",font=('arial', 10),bg="white").place(x=400,y=378)
            r1 = open("gebruiker1.txt", "r").readlines()[10]; counter1=r1.strip()
            stop=StringVar()
            stop.set("0")
            def degebruikers():
                r1 = open("gebruiker1.txt", "r").readlines()[10]; counter1=r1.strip()
                if counter1 == "3":
                    xwidth= 156
                if counter1 == "4":
                    xwidth= 209
                else:
                    xwidth=156
                Frame(LG,width=220,height=xwidth,bg="gray20").place(x=900,y=150)
                if counter1 == '1': a1()
                if counter1 == '2': a1();a2()
                if counter1 == '3': a1();a2();a3()
                if counter1 == '4': a1();a2();a3();a4()
                if counter1 == '5': a1();a2();a3();a4();a5()
            degebruikers()
            def nieuwegebruiker1():
                if wachtwoord2.get()=="" or wachtwoord3.get()=="" or gebruiker10.get()=="" or leeftijd.get()=="" or email.get()=="":
                    messagebox.showinfo("Systeem", "Je mag geen velden leeg laten")
                    stop.set("1")
                    degebruikers()
                if gebruiker10.get() == gebruiker1 or gebruiker10.get() == gebruiker2 or gebruiker10.get() == gebruiker3 or gebruiker10.get() == gebruiker4 or gebruiker10.get() == gebruiker5:
                    messagebox.showinfo("Systeem", "Deze gebruikersnaam word al gebruikt")
                    stop.set("1")
                    degebruikers()
                if wachtwoord2.get() == wachtwoord3.get() and stop.get() == "0":
                    c1 = open("gebruiker1.txt", "r").readlines()[10]; counter1=c1.strip()
                    if counter1 == '1':
                        data[10]='2' + '\n'
                        with open('gebruiker1.txt', 'w') as file: file.writelines( data )
                    if counter1 == '2':
                        data[10]='3' + '\n'
                        with open('gebruiker1.txt', 'w') as file: file.writelines( data )
                    if counter1 == '3':
                        data[10]='4' + '\n'
                        with open('gebruiker1.txt', 'w') as file: file.writelines( data )
                    if counter1 == '4':
                        data[10]='5' + '\n'
                        with open('gebruiker1.txt', 'w') as file: file.writelines( data )
                    if counter1 == '5':
                        messagebox.showinfo("Systeem", "Je hebt al het maximaal aantal gebruikers")
                    def writeit1():
                        def run():
                            with open('gebruiker1.txt', 'w') as file: file.writelines( data )
                        if counter1 == '1':
                            data[1] = gebruiker10.get() + '\n'; run()
                            data[6] = wachtwoord2.get() + '\n'; run()
                            data[23] = leeftijd.get() + '\n'; run()
                            data[28] = email.get() + '\n'; run()
                        if counter1 == '2':
                            data[2] = gebruiker10.get() + '\n'; run()
                            data[7] = wachtwoord2.get() + '\n'; run()
                            data[24] = leeftijd.get() + '\n'; run()
                            data[29] = email.get() + '\n'; run()
                        if counter1 == '3':
                            data[3] = gebruiker10.get() + '\n'; run()
                            data[8] = wachtwoord2.get() + '\n'; run()
                            data[25] = leeftijd.get() + '\n'; run()
                            data[30] = email.get() + '\n'; run()
                        if counter1 == '4':
                            data[4] = gebruiker10.get() + '\n'; run()
                            data[9] = wachtwoord2.get() + '\n'; run()
                            data[26] = leeftijd.get() + '\n'; run()
                            data[31] = email.get() + '\n'; run()
                        if counter1 == '5':
                            pass
                    writeit1()
                    messagebox.showinfo("Systeem", "gelukt de gebruiker is toegevoegd")
                    degebruikers()
                else:
                    messagebox.showinfo("Systeem", "Wachtwoorden komen niet overeen")
                    gebruikersnaam()
            def loginofniet(): homepage()
            def loginofniet2(): LG.destroy()
            HoverButton(LG, image=img1,bg="white",bd=0,command=loginofniet2).place(x=1240,y=5); HoverButton(LG, image=img2,bg="white",bd=0,command=loginofniet).place(x=1210,y=5)
            Button(LG,text="Update",font=('arial', 13),bg="gray20",relief="ridge",command=nieuwegebruiker1,fg="white").place(x=550,y=500)
        else:
            messagebox.showinfo("Systeem", "Je hebt geen toegang tot dit")
    def __init__(self):
        Canvas(LG,width=1280,height=750,bd=0,bg="white").place(x=0,y=0);sluiten()
        Frame(LG,width=300,height=1000,bg='gray20',bd=0).place(x=0,y=0)
        Label(LG,font=('arial', 15, 'bold'),bg='gray20',fg="white",text="Systeem").place(x=20,y=30)
        Button(LG,font=('arial', 15),bg='gray20',fg="white",text="Thema's",bd=0,command=self.thema).place(x=40,y=65)
        Button(LG,font=('arial', 15),bg='gray20',fg="white",text="Wachtwoord",bd=0,command=self.wachtwoord).place(x=40,y=100)
        Button(LG,font=('arial', 15),bg='gray20',fg="white",text="gebruikersnaam",bd=0,command=self.gebruikersnaam).place(x=40,y=145)
def forgotLG():
    Frame(LG,width=500,height=750,bd=0,bg="white").place(x=0,y=0)
    Label(LG,font=('arial',15, 'bold'),text="Op welk huis nummer woon ik").place(x=50,y=50)
    Button(LG,text="<--",command=LG.destroy).place(x=0,y=0)
    def wachtwoordverkrijgen():
        if wachtwoordherstel.get() == "68":
            Label(LG,text=wachtwoord1,font=('arial',15,'bold'),width=10).place(x=50,y=200)
        else:
            Label(LG,text="Antwoord is fout",fg="red",font=('arial',15,'bold')).place(x=50,y=200)
    e1=Entry(LG,textvariable=wachtwoordherstel).place(x=50,y=100)
    Button(LG,text="Herstel",command=wachtwoordverkrijgen).place(x=50,y=150)
def knorth():
    Canvas(LG,bg='white',bd=0,width=1350,height=800).place(x=0,y=0)
    c1 = open("gebruiker1.txt", "r").readlines()[32]; f_contents1=c1.strip()
    c1 = open("gebruiker1.txt", "r").readlines()[33]; f_contents2=c1.strip()
    c1 = open("gebruiker1.txt", "r").readlines()[34]; f_contents3=c1.strip()
    c1 = open("gebruiker1.txt", "r").readlines()[35]; f_contents4=c1.strip()

    c1 = open("gebruiker1.txt", "r").readlines()[41]; f_contents5=c1.strip()
    c1 = open("gebruiker1.txt", "r").readlines()[42]; f_contents6=c1.strip()
    c1 = open("gebruiker1.txt", "r").readlines()[43]; f_contents7=c1.strip()
    c1 = open("gebruiker1.txt", "r").readlines()[44]; f_contents8=c1.strip()

    c1 = open("gebruiker1.txt", "r").readlines()[50]; f_contents9=c1.strip()
    c1 = open("gebruiker1.txt", "r").readlines()[51]; f_contents10=c1.strip()
    c1 = open("gebruiker1.txt", "r").readlines()[52]; f_contents11=c1.strip()
    c1 = open("gebruiker1.txt", "r").readlines()[53]; f_contents12=c1.strip()

    c1 = open("gebruiker1.txt", "r").readlines()[59]; f_contents13=c1.strip()
    c1 = open("gebruiker1.txt", "r").readlines()[60]; f_contents14=c1.strip()
    c1 = open("gebruiker1.txt", "r").readlines()[61]; f_contents15=c1.strip()
    c1 = open("gebruiker1.txt", "r").readlines()[62]; f_contents16=c1.strip()

    c1 = open("gebruiker1.txt", "r").readlines()[68]; f_contents17=c1.strip()
    c1 = open("gebruiker1.txt", "r").readlines()[69]; f_contents18=c1.strip()
    c1 = open("gebruiker1.txt", "r").readlines()[70]; f_contents19=c1.strip()
    c1 = open("gebruiker1.txt", "r").readlines()[71]; f_contents20=c1.strip()

    c1 = open("gebruiker1.txt", "r").readlines()[77]; f_contents21=c1.strip()
    c1 = open("gebruiker1.txt", "r").readlines()[78]; f_contents22=c1.strip()
    c1 = open("gebruiker1.txt", "r").readlines()[79]; f_contents23=c1.strip()
    c1 = open("gebruiker1.txt", "r").readlines()[80]; f_contents24=c1.strip()

    c1 = open("gebruiker1.txt", "r").readlines()[86]; f_contents25=c1.strip()
    c1 = open("gebruiker1.txt", "r").readlines()[87]; f_contents26=c1.strip()
    c1 = open("gebruiker1.txt", "r").readlines()[88]; f_contents27=c1.strip()
    c1 = open("gebruiker1.txt", "r").readlines()[89]; f_contents28=c1.strip()

    c1 = open("gebruiker1.txt", "r").readlines()[95]; f_contents29=c1.strip()
    c1 = open("gebruiker1.txt", "r").readlines()[96]; f_contents30=c1.strip()
    c1 = open("gebruiker1.txt", "r").readlines()[97]; f_contents31=c1.strip()
    c1 = open("gebruiker1.txt", "r").readlines()[98]; f_contents32=c1.strip()

    c1 = open("gebruiker1.txt", "r").readlines()[104]; f_contents33=c1.strip()
    c1 = open("gebruiker1.txt", "r").readlines()[105]; f_contents34=c1.strip()
    c1 = open("gebruiker1.txt", "r").readlines()[106]; f_contents35=c1.strip()
    c1 = open("gebruiker1.txt", "r").readlines()[107]; f_contents36=c1.strip()

    c1 = open("gebruiker1.txt", "r").readlines()[108]; f_contents37=c1.strip()
    c1 = open("gebruiker1.txt", "r").readlines()[109]; f_contents38=c1.strip()
    c1 = open("gebruiker1.txt", "r").readlines()[110]; f_contents39=c1.strip()
    c1 = open("gebruiker1.txt", "r").readlines()[111]; f_contents40=c1.strip()

    c1 = open("gebruiker1.txt", "r").readlines()[117]; f_contents41=c1.strip()
    c1 = open("gebruiker1.txt", "r").readlines()[118]; f_contents42=c1.strip()
    c1 = open("gebruiker1.txt", "r").readlines()[119]; f_contents43=c1.strip()
    c1 = open("gebruiker1.txt", "r").readlines()[120]; f_contents44=c1.strip()
    c1 = open("gebruiker1.txt", "r").readlines()[121]; f_contents45=c1.strip()

    c1 = open("gebruiker1.txt", "r").readlines()[122]; f_contents46=c1.strip()
    c1 = open("gebruiker1.txt", "r").readlines()[123]; f_contents47=c1.strip()
    c1 = open("gebruiker1.txt", "r").readlines()[124]; f_contents48=c1.strip()
    c1 = open("gebruiker1.txt", "r").readlines()[125]; f_contents49=c1.strip()
    c1 = open("gebruiker1.txt", "r").readlines()[126]; f_contents50=c1.strip()
    c1 = open("gebruiker1.txt", "r").readlines()[127]; f_contents51=c1.strip()
    c1 = open("gebruiker1.txt", "r").readlines()[128]; f_contents52=c1.strip()
    c1 = open("gebruiker1.txt", "r").readlines()[129]; f_contents53=c1.strip()
    c1 = open("gebruiker1.txt", "r").readlines()[130]; f_contents54=c1.strip()
    c1 = open("gebruiker1.txt", "r").readlines()[131]; f_contents55=c1.strip()
    c1 = open("gebruiker1.txt", "r").readlines()[132]; f_contents56=c1.strip()
    c1 = open("gebruiker1.txt", "r").readlines()[133]; f_contents57=c1.strip()
    c1 = open("gebruiker1.txt", "r").readlines()[134]; f_contents58=c1.strip()
    c1 = open("gebruiker1.txt", "r").readlines()[135]; f_contents59=c1.strip()
    c1 = open("gebruiker1.txt", "r").readlines()[136]; f_contents60=c1.strip()
    c1 = open("gebruiker1.txt", "r").readlines()[137]; f_contents61=c1.strip()
    c1 = open("gebruiker1.txt", "r").readlines()[138]; f_contents62=c1.strip()
    c1 = open("gebruiker1.txt", "r").readlines()[139]; f_contents63=c1.strip()
    c1 = open("gebruiker1.txt", "r").readlines()[140]; f_contents64=c1.strip()
    c1 = open("gebruiker1.txt", "r").readlines()[141]; f_contents65=c1.strip()
    c1 = open("gebruiker1.txt", "r").readlines()[142]; f_contents66=c1.strip()
    c1 = open("gebruiker1.txt", "r").readlines()[143]; f_contents67=c1.strip()
    c1 = open("gebruiker1.txt", "r").readlines()[144]; f_contents68=c1.strip()
    c1 = open("gebruiker1.txt", "r").readlines()[145]; f_contents69=c1.strip()
    c1 = open("gebruiker1.txt", "r").readlines()[146]; f_contents70=c1.strip()
    c1 = open("gebruiker1.txt", "r").readlines()[147]; f_contents71=c1.strip()

    with open('extravak1.txt', 'r') as f: f_contents72 = f.read()
    with open('safecolor.txt', 'r') as f: safecolor = f.read()
    with open('safecolor2.txt', 'r') as f: safecolor2 = f.read()
    changey1 = open("changey1.txt", "r").readlines()
    changey2 = open("changey2.txt", "r").readlines()
    def weekvooruitspoelen():
        GT = ""
        oTF = open('maandagtoetsen.txt', 'w'); oTF.write(f_contents47); oTF.close()
        oTF = open('week2maandagtoetsen.txt', 'w'); oTF.write(GT); oTF.close()
        oTF = open('dinsdagtoetsen.txt', 'w'); oTF.write(f_contents48); oTF.close()
        oTF = open('week2dinsdagtoetsen.txt', 'w'); oTF.write(GT); oTF.close()
        oTF = open('woensdagtoetsen.txt', 'w'); oTF.write(f_contents49); oTF.close()
        oTF = open('week2woensdagtoetsen.txt', 'w'); oTF.write(GT); oTF.close()
        oTF = open('donderdagtoetsen.txt', 'w'); oTF.write(f_contents50); oTF.close()
        oTF = open('week2donderdagtoetsen.txt', 'w'); oTF.write(GT); oTF.close()
        oTF = open('vrijdagtoetsen.txt', 'w'); oTF.write(f_contents51); oTF.close()
        oTF = open('week2vrijdagtoetsen.txt', 'w'); oTF.write(GT); oTF.close()
        if f_contents47 == "": oTF = open('maandagtoetsen.txt', 'w'); oTF.write(""); oTF.close()
        if f_contents48 == "": oTF = open('dinsdagtoetsen.txt', 'w'); oTF.write(""); oTF.close()
        if f_contents49 == "": oTF = open('woensdagtoetsen.txt', 'w'); oTF.write(""); oTF.close()
        if f_contents50 == "": oTF = open('donderdagtoetsen.txt', 'w'); oTF.write(""); oTF.close()
        if f_contents51 == "": oTF = open('vrijdagtoetsen.txt', 'w'); oTF.write(""); oTF.close()
        oTF = open('maandaghuiswerk1.txt', 'w'); oTF.write(f_contents52); oTF.close()
        if f_contents52 == "": oTF = open('maandaghuiswerk1.txt', 'w'); oTF.write(""); oTF.close()
        oTF = open('week2maandaghuiswerk1.txt', 'w'); oTF.write(GT); oTF.close()
        oTF = open('maandaghuiswerk1.txt', 'w'); oTF.write(f_contents53); oTF.close()
        if f_contents53 == "": oTF = open('maandaghuiswerk2.txt', 'w'); oTF.write(""); oTF.close()
        oTF = open('week2maandaghuiswerk2.txt', 'w'); oTF.write(GT); oTF.close()
        oTF = open('maandaghuiswerk1.txt', 'w'); oTF.write(f_contents54); oTF.close()
        if f_contents54 == "": oTF = open('maandaghuiswerk3.txt', 'w'); oTF.write(""); oTF.close()
        oTF = open('week2maandaghuiswerk3.txt', 'w'); oTF.write(GT); oTF.close()
        oTF = open('maandaghuiswerk1.txt', 'w'); oTF.write(f_contents55); oTF.close()
        if f_contents55 == "": oTF = open('maandaghuiswerk4.txt', 'w'); oTF.write(""); oTF.close()
        oTF = open('week2maandaghuiswerk4.txt', 'w'); oTF.write(GT); oTF.close()
        oTF = open('dinsdaghuiswerk1.txt', 'w'); oTF.write(f_contents56); oTF.close()
        if f_contents56 == "": oTF = open('dinsdaghuiswerk1.txt', 'w'); oTF.write(""); oTF.close()
        oTF = open('week2dinsdaghuiswerk1.txt', 'w'); oTF.write(GT); oTF.close()
        oTF = open('dinsdaghuiswerk1.txt', 'w'); oTF.write(f_contents57); oTF.close()
        if f_contents57 == "": oTF = open('dinsdaghuiswerk2.txt', 'w'); oTF.write(""); oTF.close()
        oTF = open('week2dinsdaghuiswerk2.txt', 'w'); oTF.write(GT); oTF.close()
        oTF = open('dinsdaghuiswerk1.txt', 'w'); oTF.write(f_contents58); oTF.close()
        if f_contents58 == "": oTF = open('dinsdaghuiswerk3.txt', 'w'); oTF.write(""); oTF.close()
        oTF = open('week2dinsdaghuiswerk3.txt', 'w'); oTF.write(GT); oTF.close()
        oTF = open('dinsdaghuiswerk1.txt', 'w'); oTF.write(f_contents59); oTF.close()
        if f_contents59 == "": oTF = open('dinsdaghuiswerk4.txt', 'w'); oTF.write(""); oTF.close()
        oTF = open('week2dinsdaghuiswerk4.txt', 'w'); oTF.write(GT); oTF.close()
        oTF = open('woensdaghuiswerk1.txt', 'w'); oTF.write(f_contents60); oTF.close()
        if f_contents60 == "": oTF = open('woensdaghuiswerk1.txt', 'w'); oTF.write(""); oTF.close()
        oTF = open('week2woensdaghuiswerk1.txt', 'w'); oTF.write(GT); oTF.close()
        oTF = open('woensdaghuiswerk1.txt', 'w'); oTF.write(f_contents61); oTF.close()
        if f_contents61 == "": oTF = open('woensdaghuiswerk2.txt', 'w'); oTF.write(""); oTF.close()
        oTF = open('week2woensdaghuiswerk2.txt', 'w'); oTF.write(GT); oTF.close()
        oTF = open('woensdaghuiswerk1.txt', 'w'); oTF.write(f_contents62); oTF.close()
        if f_contents62 == "": oTF = open('woensdaghuiswerk3.txt', 'w'); oTF.write(""); oTF.close()
        oTF = open('week2woensdaghuiswerk3.txt', 'w'); oTF.write(GT); oTF.close()
        oTF = open('woensdaghuiswerk1.txt', 'w'); oTF.write(f_contents63); oTF.close()
        if f_contents63 == "": oTF = open('woensdaghuiswerk4.txt', 'w'); oTF.write(""); oTF.close()
        oTF = open('week2woensdaghuiswerk4.txt', 'w'); oTF.write(GT); oTF.close()
        oTF = open('donderdaghuiswerk1.txt', 'w'); oTF.write(f_contents64); oTF.close()
        if f_contents64 == "": oTF = open('donderdaghuiswerk1.txt', 'w'); oTF.write(""); oTF.close()
        oTF = open('week2donderdaghuiswerk1.txt', 'w'); oTF.write(GT); oTF.close()
        oTF = open('donderdaghuiswerk1.txt', 'w'); oTF.write(f_contents65); oTF.close()
        if f_contents65 == "": oTF = open('donderdaghuiswerk2.txt', 'w'); oTF.write(""); oTF.close()
        oTF = open('week2donderdaghuiswerk2.txt', 'w'); oTF.write(GT); oTF.close()
        oTF = open('donderdaghuiswerk1.txt', 'w'); oTF.write(f_contents66); oTF.close()
        if f_contents66 == "": oTF = open('donderdaghuiswerk3.txt', 'w'); oTF.write(""); oTF.close()
        oTF = open('week2donderdaghuiswerk3.txt', 'w'); oTF.write(GT); oTF.close()
        oTF = open('donderdaghuiswerk1.txt', 'w'); oTF.write(f_contents67); oTF.close()
        if f_contents67 == "": oTF = open('donderdaghuiswerk4.txt', 'w'); oTF.write(""); oTF.close()
        oTF = open('week2donderdaghuiswerk4.txt', 'w'); oTF.write(GT); oTF.close()
        oTF = open('vrijdaghuiswerk1.txt', 'w'); oTF.write(f_contents68); oTF.close()
        if f_contents68 == "": oTF = open('vrijdaghuiswerk1.txt', 'w'); oTF.write(""); oTF.close()
        oTF = open('week2vrijdaghuiswerk1.txt', 'w'); oTF.write(GT); oTF.close()
        oTF = open('vrijdaghuiswerk1.txt', 'w'); oTF.write(f_contents69); oTF.close()
        if f_contents69 == "": oTF = open('vrijdaghuiswerk2.txt', 'w'); oTF.write(""); oTF.close()
        oTF = open('week2vrijdaghuiswerk2.txt', 'w'); oTF.write(GT); oTF.close()
        oTF = open('vrijdaghuiswerk1.txt', 'w'); oTF.write(f_contents70); oTF.close()
        if f_contents70 == "": oTF = open('vrijdaghuiswerk3.txt', 'w'); oTF.write(""); oTF.close()
        oTF = open('week2vrijdaghuiswerk3.txt', 'w'); oTF.write(GT); oTF.close()
        oTF = open('vrijdaghuiswerk1.txt', 'w'); oTF.write(f_contents71); oTF.close()
        if f_contents71 == "": oTF = open('vrijdaghuiswerk4.txt', 'w'); oTF.write(""); oTF.close()
        oTF = open('week2vrijdaghuiswerk4.txt', 'w'); oTF.write(GT); oTF.close()
        homepage()
    def waarschuwing():
        window = Tk()
        window.eval('tk::PlaceWindow %s center' % window.winfo_toplevel())
        window.withdraw()
        if messagebox.askyesno("Systeem", "Alles word een week voor je doorgeschoven") == True: weekvooruitspoelen()
        else: pass
        window.deiconify()
        window.destroy()
        window.quit()
    def week2():
        def witscherm(): Canvas(LG,bg='white',bd=0,width=1350,height=800).place(x=0,y=0)
        def week2mavak1(): witscherm(); Label(LG,bg='spring green',bd=0,width=45,height=18,text=f_contents52,font=('arial', 30)).place(x=300,y=0); Button(LG,bg='white',bd=0,width=22,height=4,text="Aanpassen",font=('arial', 15),command=aanpassen).place(x=0,y=0)
        def week2mavak2(): witscherm(); Label(LG,bg='spring green',bd=0,width=45,height=18,text=f_contents53,font=('arial', 30)).place(x=300,y=0); Button(LG,bg='white',bd=0,width=22,height=4,text="Aanpassen",font=('arial', 15),command=aanpassen).place(x=0,y=0)
        def week2mavak3(): witscherm(); Label(LG,bg='spring green',bd=0,width=45,height=18,text=f_contents54,font=('arial', 30)).place(x=300,y=0); Button(LG,bg='white',bd=0,width=22,height=4,text="Aanpassen",font=('arial', 15),command=aanpassen).place(x=0,y=0)
        def week2mavak4(): witscherm(); Label(LG,bg='spring green',bd=0,width=45,height=18,text=f_contents55,font=('arial', 30)).place(x=300,y=0); Button(LG,bg='white',bd=0,width=22,height=4,text="Aanpassen",font=('arial', 15),command=aanpassen).place(x=0,y=0)
        def week2divak1(): witscherm(); Label(LG,bg='spring green',bd=0,width=45,height=18,text=f_contents56,font=('arial', 30)).place(x=300,y=0); Button(LG,bg='white',bd=0,width=22,height=4,text="Aanpassen",font=('arial', 15),command=aanpassen).place(x=0,y=0)
        def week2divak2(): witscherm(); Label(LG,bg='spring green',bd=0,width=45,height=18,text=f_contents57,font=('arial', 30)).place(x=300,y=0); Button(LG,bg='white',bd=0,width=22,height=4,text="Aanpassen",font=('arial', 15),command=aanpassen).place(x=0,y=0)
        def week2divak3(): witscherm(); Label(LG,bg='spring green',bd=0,width=45,height=18,text=f_contents58,font=('arial', 30)).place(x=300,y=0); Button(LG,bg='white',bd=0,width=22,height=4,text="Aanpassen",font=('arial', 15),command=aanpassen).place(x=0,y=0)
        def week2divak4(): witscherm(); Label(LG,bg='spring green',bd=0,width=45,height=18,text=f_contents59,font=('arial', 30)).place(x=300,y=0); Button(LG,bg='white',bd=0,width=22,height=4,text="Aanpassen",font=('arial', 15),command=aanpassen).place(x=0,y=0)
        def week2wovak1(): witscherm(); Label(LG,bg='spring green',bd=0,width=45,height=18,text=f_contents60,font=('arial', 30)).place(x=300,y=0); Button(LG,bg='white',bd=0,width=22,height=4,text="Aanpassen",font=('arial', 15),command=aanpassen).place(x=0,y=0)
        def week2wovak2(): witscherm(); Label(LG,bg='spring green',bd=0,width=45,height=18,text=f_contents61,font=('arial', 30)).place(x=300,y=0); Button(LG,bg='white',bd=0,width=22,height=4,text="Aanpassen",font=('arial', 15),command=aanpassen).place(x=0,y=0)
        def week2wovak3(): witscherm(); Label(LG,bg='spring green',bd=0,width=45,height=18,text=f_contents62,font=('arial', 30)).place(x=300,y=0); Button(LG,bg='white',bd=0,width=22,height=4,text="Aanpassen",font=('arial', 15),command=aanpassen).place(x=0,y=0)
        def week2wovak4(): witscherm(); Label(LG,bg='spring green',bd=0,width=45,height=18,text=f_contents63,font=('arial', 30)).place(x=300,y=0); Button(LG,bg='white',bd=0,width=22,height=4,text="Aanpassen",font=('arial', 15),command=aanpassen).place(x=0,y=0)
        def week2dovak1(): witscherm(); Label(LG,bg='spring green',bd=0,width=45,height=18,text=f_contents64,font=('arial', 30)).place(x=300,y=0); Button(LG,bg='white',bd=0,width=22,height=4,text="Aanpassen",font=('arial', 15),command=aanpassen).place(x=0,y=0)
        def week2dovak2(): witscherm(); Label(LG,bg='spring green',bd=0,width=45,height=18,text=f_contents65,font=('arial', 30)).place(x=300,y=0); Button(LG,bg='white',bd=0,width=22,height=4,text="Aanpassen",font=('arial', 15),command=aanpassen).place(x=0,y=0)
        def week2dovak3(): witscherm(); Label(LG,bg='spring green',bd=0,width=45,height=18,text=f_contents66,font=('arial', 30)).place(x=300,y=0); Button(LG,bg='white',bd=0,width=22,height=4,text="Aanpassen",font=('arial', 15),command=aanpassen).place(x=0,y=0)
        def week2dovak4(): witscherm(); Label(LG,bg='spring green',bd=0,width=45,height=18,text=f_contents67,font=('arial', 30)).place(x=300,y=0); Button(LG,bg='white',bd=0,width=22,height=4,text="Aanpassen",font=('arial', 15),command=aanpassen).place(x=0,y=0)
        def week2vrvak1(): witscherm(); Label(LG,bg='spring green',bd=0,width=45,height=18,text=f_contents68,font=('arial', 30)).place(x=300,y=0); Button(LG,bg='white',bd=0,width=22,height=4,text="Aanpassen",font=('arial', 15),command=aanpassen).place(x=0,y=0)
        def week2vrvak2(): witscherm(); Label(LG,bg='spring green',bd=0,width=45,height=18,text=f_contents69,font=('arial', 30)).place(x=300,y=0); Button(LG,bg='white',bd=0,width=22,height=4,text="Aanpassen",font=('arial', 15),command=aanpassen).place(x=0,y=0)
        def week2vrvak3(): witscherm(); Label(LG,bg='spring green',bd=0,width=45,height=18,text=f_contents70,font=('arial', 30)).place(x=300,y=0); Button(LG,bg='white',bd=0,width=22,height=4,text="Aanpassen",font=('arial', 15),command=aanpassen).place(x=0,y=0)
        def week2vrvak4(): witscherm(); Label(LG,bg='spring green',bd=0,width=45,height=18,text=f_contents71,font=('arial', 30)).place(x=300,y=0); Button(LG,bg='white',bd=0,width=22,height=4,text="Aanpassen",font=('arial', 15),command=aanpassen).place(x=0,y=0)
        #----------dagen die lijden naar huiswerk---------#
        HoverButton(LG,bg='white',bd=0,width=16,height=4,text=f_contents1,font=('arial', 15),command=week2mavak1).place(x=100,y=140); HoverButton(LG,bg='white',bd=0,width=16,height=4,text=f_contents2,font=('arial', 15),command=week2mavak2).place(x=100,y=200); HoverButton(LG,bg='white',bd=0,width=16,height=4,text=f_contents3,font=('arial', 15),command=week2mavak3).place(x=100,y=260);b4=HoverButton(LG,bg='white',bd=0,width=16,height=4,text=f_contents4,font=('arial', 15),command=week2mavak4).place(x=100,y=320); b5=HoverButton(LG,bg='white',bd=0,width=16,height=4,text=f_contents5,font=('arial', 15),command=week2divak1).place(x=310,y=140); b6=HoverButton(LG,bg='white',bd=0,width=16,height=4,text=f_contents6,font=('arial', 15),command=week2divak2).place(x=310,y=200); b7=HoverButton(LG,bg='white',bd=0,width=16,height=4,text=f_contents7,font=('arial', 15),command=week2divak3).place(x=310,y=260); b8=HoverButton(LG,bg='white',bd=0,width=16,height=4,text=f_contents8,font=('arial', 15),command=week2divak4).place(x=310,y=320); b9=HoverButton(LG,bg='white',bd=0,width=16,height=4,text=f_contents9,font=('arial', 15),command=week2wovak1).place(x=520,y=140); b10=HoverButton(LG,bg='white',bd=0,width=16,height=4,text=f_contents10,font=('arial', 15),command=week2wovak2).place(x=520,y=200); b11=HoverButton(LG,bg='white',bd=0,width=16,height=4,text=f_contents11,font=('arial', 15),command=week2wovak3).place(x=520,y=260); b12=HoverButton(LG,bg='white',bd=0,width=16,height=4,text=f_contents12,font=('arial', 15),command=week2wovak4).place(x=520,y=320); b13=HoverButton(LG,bg='white',bd=0,width=16,height=4,text=f_contents13,font=('arial', 15),command=week2dovak1).place(x=730,y=140); b14=HoverButton(LG,bg='white',bd=0,width=16,height=4,text=f_contents14,font=('arial', 15),command=week2dovak2).place(x=730,y=200); b15=HoverButton(LG,bg='white',bd=0,width=16,height=4,text=f_contents15,font=('arial', 15),command=week2dovak3).place(x=730,y=260); b16=HoverButton(LG,bg='white',bd=0,width=16,height=4,text=f_contents16,font=('arial', 15),command=week2dovak4).place(x=730,y=320); b17=HoverButton(LG,bg='white',bd=0,width=16,height=4,text=f_contents17,font=('arial', 15),command=week2vrvak1).place(x=940,y=140); b18=HoverButton(LG,bg='white',bd=0,width=16,height=4,text=f_contents18,font=('arial', 15),command=week2vrvak2).place(x=940,y=200); b19=HoverButton(LG,bg='white',bd=0,width=16,height=4,text=f_contents19,font=('arial', 15),command=week2vrvak3).place(x=940,y=260); b20=HoverButton(LG,bg='white',bd=0,width=16,height=4,text=f_contents20,font=('arial', 15),command=week2vrvak4).place(x=940,y=320); b21=HoverButton(LG,bg='spring green',bd=0,width=4,height=10,text="<",font=('arial', 20),activebackground='gray79',command=knorth).place(x=15,y=200)
        #-------labels met de toetsen erin--------------#
        Label(LG,bg='white',bd=0,width=17,height=8,text=f_contents47,font=('arial', 15)).place(x=100,y=530)
        Label(LG,bg='white',bd=0,width=17,height=8,text=f_contents48,font=('arial', 15)).place(x=310,y=530)
        l3=Label(LG,bg='white',bd=0,width=17,height=8,text=f_contents49,font=('arial', 15)).place(x=520,y=530)
        l4=Label(LG,bg='white',bd=0,width=17,height=8,text=f_contents50,font=('arial', 15)).place(x=730,y=530)
        l5=Label(LG,bg='white',bd=0,width=17,height=8,text=f_contents51,font=('arial', 15)).place(x=940,y=530)
        #Button(LG,image=addvakimg,bd=0,bg="white").place(x=0,y=0)
        #-------labels met de dagen erop----------------#
        l6=Label(LG,bg='white',bd=0,width=16,height=4,text="Maandag",font=('arial', 15, 'bold')).place(x=100,y=60); l7=Label(LG,bg='white',bd=0,width=16,height=4,text="Dinsdag",font=('arial', 15, 'bold')).place(x=310,y=60); l8=Label(LG,bg='white',bd=0,width=16,height=4,text="Woensdag",font=('arial', 15, 'bold')).place(x=520,y=60); l9=Label(LG,bg='white',bd=0,width=16,height=4,text="Donderdag",font=('arial', 15, 'bold')).place(x=730,y=60); l0=Label(LG,bg='white',bd=0,width=16,height=4,text="Vrijdag",font=('arial', 15, 'bold')).place(x=940,y=60)

        #-------de datum bovenaan-----------------------#
        Label(LG,bg='white',bd=0,width=46,height=2,text="volgende week",font=('arial', 20, 'bold')).place(x=250,y=0)
        #-------de lijnen die als kader zijn------------#
        Canvas(LG,bg=safecolor,bd=0,height=1,width=1050).place(x=100,y=135)
        c2=Canvas(LG,bg=safecolor,bd=0,height=1,width=1050).place(x=100,y=139)
        c3=Canvas(LG,bg=safecolor,bd=0,height=1,width=1050).place(x=100,y=416)
        c4=Canvas(LG,bg=safecolor,bd=0,height=1,width=1050).place(x=100,y=420)
        c5=Canvas(LG,bg=safecolor2,bd=0,height=1,width=1050).place(x=100,y=526)
        c6=Canvas(LG,bg=safecolor2,bd=0,height=1,width=1050).place(x=100,y=530)
        c7=Canvas(LG,bg=safecolor2,bd=0,height=1,width=1050).place(x=100,y=686)
        c8=Canvas(LG,bg=safecolor2,bd=0,height=1,width=1050).place(x=100,y=690)

        c9=Canvas(LG,bg=safecolor,bd=0,height=285,width=1).place(x=98,y=135)
        c10=Canvas(LG,bg=safecolor,bd=0,height=285,width=1).place(x=102,y=135)
        c11=Canvas(LG,bg=safecolor,bd=0,height=285,width=1).place(x=308,y=135)
        c12=Canvas(LG,bg=safecolor,bd=0,height=285,width=1).place(x=312,y=135)
        c13=Canvas(LG,bg=safecolor,bd=0,height=285,width=1).place(x=518,y=135)
        c14=Canvas(LG,bg=safecolor,bd=0,height=285,width=1).place(x=522,y=135)
        c15=Canvas(LG,bg=safecolor,bd=0,height=285,width=1).place(x=728,y=135)
        c16=Canvas(LG,bg=safecolor,bd=0,height=285,width=1).place(x=732,y=135)
        c17=Canvas(LG,bg=safecolor,bd=0,height=285,width=1).place(x=938,y=135)
        c18=Canvas(LG,bg=safecolor,bd=0,height=285,width=1).place(x=942,y=135)
        c19=Canvas(LG,bg=safecolor,bd=0,height=285,width=1).place(x=1148,y=135)
        c20=Canvas(LG,bg=safecolor,bd=0,height=285,width=1).place(x=1152,y=135)

        c21=Canvas(LG,bg=safecolor2,bd=0,height=164,width=1).place(x=xwidth,y=526)
        c22=Canvas(LG,bg=safecolor2,bd=0,height=164,width=1).place(x=102,y=526)
        #c23=Canvas(LG,bg=safecolor2,bd=0,height=164,width=1).place(x=308,y=526)
        c24=Canvas(LG,bg=safecolor2,bd=0,height=164,width=1).place(x=312,y=526)
        #c25=Canvas(LG,bg=safecolor2,bd=0,height=164,width=1).place(x=518,y=526)
        c26=Canvas(LG,bg=safecolor2,bd=0,height=164,width=1).place(x=522,y=526)
        #c27=Canvas(LG,bg=safecolor2,bd=0,height=164,width=1).place(x=728,y=526)
        c28=Canvas(LG,bg=safecolor2,bd=0,height=164,width=1).place(x=732,y=526)
        #c29=Canvas(LG,bg=safecolor2,bd=0,height=164,width=1).place(x=938,y=526)
        c30=Canvas(LG,bg=safecolor2,bd=0,height=164,width=1).place(x=942,y=526)
        #c31=Canvas(LG,bg=safecolor2,bd=0,height=164,width=1).place(x=1148,y=526)
        c32=Canvas(LG,bg=safecolor2,bd=0,height=164,width=1).place(x=1152,y=526)
        c33=Label(LG,bg="white",bd=0,height=60,width=20).place(x=1160,y=180)
    def aanpassen():
        Frame(LG,bg='white',bd=0,width=1350,height=800).place(x=0,y=0)
    f_c = StringVar()
    def standaard():
        Canvas(LG,bg='white',bd=0,width=1350,height=800).place(x=0,y=0); Label(LG,bg='spring green',bd=0,width=45,height=18,text=f_c,font=('arial', 30)).place(x=300,y=0); Button(LG,bg='white',bd=0,width=22,height=4,text="Aanpassen",font=('arial', 15),command=aanpassen).place(x=0,y=0)
    def mavak1(): f_c = f_contents21; standaard()
    def mavak2(): f_c = f_contents22; standaard()
    def mavak3(): f_c = f_contents23; standaard()
    def mavak4(): f_c = f_contents24; standaard()
    def divak1(): f_c = f_contents25; standaard()
    def divak2(): f_c = f_contents26; standaard()
    def divak3(): f_c = f_contents27; standaard()
    def divak4(): f_c = f_contents28; standaard()
    def wovak1(): f_c = f_contents29; standaard()
    def wovak2(): Canvas(LG,bg='white',bd=0,width=1350,height=800).place(x=0,y=0); Label(LG,bg='spring green',bd=0,width=45,height=18,text=f_contents30,font=('arial', 30)).place(x=300,y=0); Button(LG,bg='white',bd=0,width=22,height=4,text="Aanpassen",font=('arial', 15),command=aanpassen).place(x=0,y=0)
    def wovak3(): Canvas(LG,bg='white',bd=0,width=1350,height=800).place(x=0,y=0); Label(LG,bg='spring green',bd=0,width=45,height=18,text=f_contents31,font=('arial', 30)).place(x=300,y=0); Button(LG,bg='white',bd=0,width=22,height=4,text="Aanpassen",font=('arial', 15),command=aanpassen).place(x=0,y=0)
    def wovak4(): Canvas(LG,bg='white',bd=0,width=1350,height=800).place(x=0,y=0); Label(LG,bg='spring green',bd=0,width=45,height=18,text=f_contents32,font=('arial', 30)).place(x=300,y=0); Button(LG,bg='white',bd=0,width=22,height=4,text="Aanpassen",font=('arial', 15),command=aanpassen).place(x=0,y=0)
    def dovak1(): Canvas(LG,bg='white',bd=0,width=1350,height=800).place(x=0,y=0); Label(LG,bg='spring green',bd=0,width=45,height=18,text=f_contents33,font=('arial', 30)).place(x=300,y=0); Button(LG,bg='white',bd=0,width=22,height=4,text="Aanpassen",font=('arial', 15),command=aanpassen).place(x=0,y=0)
    def dovak2(): Canvas(LG,bg='white',bd=0,width=1350,height=800).place(x=0,y=0); Label(LG,bg='spring green',bd=0,width=45,height=18,text=f_contents34,font=('arial', 30)).place(x=300,y=0); Button(LG,bg='white',bd=0,width=22,height=4,text="Aanpassen",font=('arial', 15),command=aanpassen).place(x=0,y=0)
    def dovak3(): Canvas(LG,bg='white',bd=0,width=1350,height=800).place(x=0,y=0); Label(LG,bg='spring green',bd=0,width=45,height=18,text=f_contents35,font=('arial', 30)).place(x=300,y=0); Button(LG,bg='white',bd=0,width=22,height=4,text="Aanpassen",font=('arial', 15),command=aanpassen).place(x=0,y=0)
    def dovak4(): Canvas(LG,bg='white',bd=0,width=1350,height=800).place(x=0,y=0); Label(LG,bg='spring green',bd=0,width=45,height=18,text=f_contents36,font=('arial', 30)).place(x=300,y=0); Button(LG,bg='white',bd=0,width=22,height=4,text="Aanpassen",font=('arial', 15),command=aanpassen).place(x=0,y=0)
    def vrvak1(): Canvas(LG,bg='white',bd=0,width=1350,height=800).place(x=0,y=0); Label(LG,bg='spring green',bd=0,width=45,height=18,text=f_contents37,font=('arial', 30)).place(x=300,y=0); Button(LG,bg='white',bd=0,width=22,height=4,text="Aanpassen",font=('arial', 15),command=aanpassen).place(x=0,y=0)
    def vrvak2(): Canvas(LG,bg='white',bd=0,width=1350,height=800).place(x=0,y=0); Label(LG,bg='spring green',bd=0,width=45,height=18,text=f_contents38,font=('arial', 30)).place(x=300,y=0); Button(LG,bg='white',bd=0,width=22,height=4,text="Aanpassen",font=('arial', 15),command=aanpassen).place(x=0,y=0)
    def vrvak3(): Canvas(LG,bg='white',bd=0,width=1350,height=800).place(x=0,y=0); Label(LG,bg='spring green',bd=0,width=45,height=18,text=f_contents39,font=('arial', 30)).place(x=300,y=0); Button(LG,bg='white',bd=0,width=22,height=4,text="Aanpassen",font=('arial', 15),command=aanpassen).place(x=0,y=0)
    def vrvak4(): Canvas(LG,bg='white',bd=0,width=1350,height=800).place(x=0,y=0); Label(LG,bg='spring green',bd=0,width=45,height=18,text=f_contents40,font=('arial', 30)).place(x=300,y=0); Button(LG,bg='white',bd=0,width=22,height=4,text="Aanpassen",font=('arial', 15),command=aanpassen).place(x=0,y=0)
    var1=StringVar()
    var2=StringVar()
    var3=StringVar()
    var4=StringVar()
    #-------dagen die naar huiswerk lijden----------#
    class MouseControl1(tk.Button):
        def __init__(self, master, **kw):
            tk.Button.__init__(self,master=master,**kw)
            self.bind('<Double-1>', self.double_click)
            self.defaultBackground = self["background"]
            self.bind("<Enter>", self.on_enter)
            self.bind("<Leave>", self.on_leave)
        def on_enter(self, e):
            self['background'] = self['activebackground']
        def on_leave(self, e):
            self['background'] = self.defaultBackground
        def double_click(self, event):
            Entry(LG,textvariable=var1,bd=2,relief="sunken").place(x=140,y=170)
            Button(LG,text=">>",font=('arial',10,'bold'),bd=0,bg="white",command=self.b).place(x=240,y=170)
        def b(self):
            if var1.get() == "":
                messagebox.showinfo("Systeem", "Je kunt dit veld niet leeg laten")
            else:
                test = var1.get()
                data[32]=var1.get() + '\n'
                with open('gebruiker1.txt', 'w') as file: file.writelines( data )
                MouseControl1(LG,bg='white',bd=0,width=16,text=test,font=('arial', 15),activebackground="gray50").place(x=110,y=160)
    class MouseControl2(tk.Button):
        def __init__(self, master, **kw):
            tk.Button.__init__(self,master=master,**kw)
            self.bind('<Double-1>', self.double_click)
            self.defaultBackground = self["background"]
            self.bind("<Enter>", self.on_enter)
            self.bind("<Leave>", self.on_leave)
        def on_enter(self, e):
            self['background'] = self['activebackground']
        def on_leave(self, e):
            self['background'] = self.defaultBackground
        def double_click(self, event):
            Entry(LG,textvariable=var2,bd=2,relief="sunken").place(x=140,y=210)
            Button(LG,text=">>",font=('arial',10,'bold'),bd=0,bg="white",command=self.b).place(x=240,y=210)
        def b(self):
            if var2.get() == "":
                messagebox.showinfo("Systeem", "Je kunt dit veld niet leeg laten")
            else:
                test = var2.get()
                data[33]=var2.get() + '\n'
                with open('gebruiker1.txt', 'w') as file: file.writelines( data )
                MouseControl2(LG,bg='white',bd=0,width=16,text=test,font=('arial', 15),activebackground="gray50").place(x=110,y=200)
    class MouseControl3(tk.Button):
        def __init__(self, master, **kw):
            tk.Button.__init__(self,master=master,**kw)
            self.bind('<Double-1>', self.double_click)
            self.defaultBackground = self["background"]
            self.bind("<Enter>", self.on_enter)
            self.bind("<Leave>", self.on_leave)
        def on_enter(self, e):
            self['background'] = self['activebackground']
        def on_leave(self, e):
            self['background'] = self.defaultBackground
        def double_click(self, event):
            Entry(LG,textvariable=var3,bd=2,relief="sunken").place(x=140,y=250)
            Button(LG,text=">>",font=('arial',10,'bold'),bd=0,bg="white",command=self.b).place(x=240,y=250)
        def b(self):
            if var3.get() == "":
                messagebox.showinfo("Systeem", "Je kunt dit veld niet leeg laten")
            else:
                test = var3.get()
                data[34]=var3.get() + '\n'
                with open('gebruiker1.txt', 'w') as file: file.writelines( data )
                MouseControl3(LG,bg='white',bd=0,width=16,text=f_contents3,font=('arial', 15),activebackground="gray50").place(x=110,y=240)
    class MouseControl4(tk.Button):
        def __init__(self, master, **kw): tk.Button.__init__(self,master=master,**kw); self.bind('<Double-1>', self.double_click); self.defaultBackground = self["background"]; self.bind("<Enter>", self.on_enter); self.bind("<Leave>", self.on_leave)
        def on_enter(self, e): self['background'] = self['activebackground']
        def on_leave(self, e): self['background'] = self.defaultBackground
        def double_click(self, event):
            Entry(LG,textvariable=var4,bd=2,relief="sunken").place(x=140,y=290); Button(LG,text=">>",font=('arial',10,'bold'),bd=0,bg="white",command=self.b).place(x=240,y=290)
        def b(self):
            if var4.get() == "": messagebox.showinfo("Systeem", "Je kunt dit veld niet leeg laten")
            else:
                test = var4.get()
                data[35]=var4.get() + '\n'
                with open('gebruiker1.txt', 'w') as file: file.writelines( data )
                MouseControl4(LG,bg='white',bd=0,width=16,text=test,font=('arial', 15),activebackground="gray50").place(x=110,y=280)
    class HoverButton(tk.Button):
        def __init__(self, master, **kw):
            tk.Button.__init__(self,master=master,**kw)
            self.defaultBackground = self["background"]
            self.bind("<Enter>", self.on_enter)
            self.bind("<Leave>", self.on_leave)
        def on_enter(self, e):
            self['background'] = self['activebackground']
        def on_leave(self, e):
            self['background'] = self.defaultBackground
    def vakkenmetdagen():
        HoverButton(LG,bg='white',bd=0,width=16,height=4,text=f_contents20,font=('arial', 15),command=vrvak4).place(x=940,y=320)
        HoverButton(LG,bg='white',bd=0,width=16,height=4,text=f_contents19,font=('arial', 15),command=vrvak3).place(x=940,y=260)
        HoverButton(LG,bg='white',bd=0,width=16,height=4,text=f_contents18,font=('arial', 15),command=vrvak2).place(x=940,y=200)
        HoverButton(LG,bg='white',bd=0,width=16,height=4,text=f_contents17,font=('arial', 15),command=vrvak1).place(x=940,y=140)
        HoverButton(LG,bg='white',bd=0,width=16,height=4,text=f_contents16,font=('arial', 15),command=dovak4).place(x=730,y=320)
        HoverButton(LG,bg='white',bd=0,width=16,height=4,text=f_contents15,font=('arial', 15),command=dovak3).place(x=730,y=260)
        HoverButton(LG,bg='white',bd=0,width=16,height=4,text=f_contents14,font=('arial', 15),command=dovak2).place(x=730,y=200)
        HoverButton(LG,bg='white',bd=0,width=16,height=4,text=f_contents13,font=('arial', 15),command=dovak1).place(x=730,y=140)
        HoverButton(LG,bg='white',bd=0,width=16,height=4,text=f_contents12,font=('arial', 15),command=wovak4).place(x=520,y=320)
        HoverButton(LG,bg='white',bd=0,width=16,height=4,text=f_contents11,font=('arial', 15),command=wovak3).place(x=520,y=260)
        HoverButton(LG,bg='white',bd=0,width=16,height=4,text=f_contents10,font=('arial', 15),command=wovak2).place(x=520,y=200)
        HoverButton(LG,bg='white',bd=0,width=16,height=4,text=f_contents9,font=('arial', 15),command=wovak1).place(x=520,y=140)
        HoverButton(LG,bg='white',bd=0,width=16,height=4,text=f_contents8,font=('arial', 15),command=divak4).place(x=310,y=320)
        HoverButton(LG,bg='white',bd=0,width=16,height=4,text=f_contents7,font=('arial', 15),command=divak3).place(x=310,y=260)
        HoverButton(LG,bg='white',bd=0,width=16,height=4,text=f_contents6,font=('arial', 15),command=divak2).place(x=310,y=200)
        HoverButton(LG,bg='white',bd=0,width=16,height=4,text=f_contents5,font=('arial', 15),command=divak1).place(x=310,y=140)
        MouseControl4(LG,bg='white',bd=0,width=16,text=f_contents4,font=('arial', 15),activebackground="gray50").place(x=110,y=280)
        MouseControl3(LG,bg='white',bd=0,width=16,text=f_contents3,font=('arial', 15),activebackground="gray50").place(x=110,y=240)
        MouseControl2(LG,bg='white',bd=0,width=16,text=f_contents2,font=('arial', 15),activebackground="gray50").place(x=110,y=200)
        MouseControl1(LG,bg='white',bd=0,width=16,text=f_contents1,font=('arial', 15),activebackground="gray50").place(x=110,y=160)
    vakkenmetdagen()
    #-------labels met de toetsen erin--------------#
    Label(LG,bg='white',bd=0,width=17,height=8,text=f_contents41,font=('arial', 15)).place(x=100,y=530)
    Label(LG,bg='white',bd=0,width=17,height=8,text=f_contents42,font=('arial', 15)).place(x=310,y=530)
    l3=Label(LG,bg='white',bd=0,width=17,height=8,text=f_contents43,font=('arial', 15)).place(x=520,y=530)
    l4=Label(LG,bg='white',bd=0,width=17,height=8,text=f_contents44,font=('arial', 15)).place(x=730,y=530)
    l5=Label(LG,bg='white',bd=0,width=17,height=8,text=f_contents45,font=('arial', 15)).place(x=940,y=530)
    Label(LG,bg='white',bd=0,width=160,height=4).place(x=100,y=380)
    #-------labels met de dagen erop----------------#
    l6=Label(LG,bg='white',bd=0,width=16,height=4,text="Maandag",font=('arial', 15, 'bold')).place(x=100,y=60); l7=Label(LG,bg='white',bd=0,width=16,height=4,text="Dinsdag",font=('arial', 15, 'bold')).place(x=310,y=60); l8=Label(LG,bg='white',bd=0,width=16,height=4,text="Woensdag",font=('arial', 15, 'bold')).place(x=520,y=60); l9=Label(LG,bg='white',bd=0,width=16,height=4,text="Donderdag",font=('arial', 15, 'bold')).place(x=730,y=60); l0=Label(LG,bg='white',bd=0,width=16,height=4,text="Vrijdag",font=('arial', 15, 'bold')).place(x=940,y=60)
    #-------de datum bovenaan-----------------------#
    Label(LG,bg='white',bd=0,width=46,height=2,text="deze week",font=('arial', 20, 'bold')).place(x=250,y=0)
    #-------de lijnen die als kader zijn------------#
    def lijnen():
        changey1 = open("changey1.txt", "r").readlines()
        changey2 = open("changey2.txt", "r").readlines()
        changey3 = open("changey3.txt", "r").readlines()
        changey4 = open("changey4.txt", "r").readlines()
        changey5 = open("changey5.txt", "r").readlines()
        changey6 = open("changey6.txt", "r").readlines()
        changey7 = open("changey7.txt", "r").readlines()
        changey8 = open("changey8.txt", "r").readlines()
        changey9 = open("changey9.txt", "r").readlines()
        changey10 = open("changey10.txt", "r").readlines()

        height1 = open("Extraheight1.txt", "r").readlines()
        height2 = open("Extraheight2.txt", "r").readlines()
        height3 = open("Extraheight3.txt", "r").readlines()
        height4 = open("Extraheight4.txt", "r").readlines()
        height5 = open("Extraheight5.txt", "r").readlines()
        height6 = open("Extraheight6.txt", "r").readlines()
        # liggenlijnen voor vakken
        Canvas(LG,bg=safecolor,bd=0,height=1,width=1050).place(x=100,y=135)
        Canvas(LG,bg=safecolor,bd=0,height=1,width=1050).place(x=100,y=139)

        Canvas(LG,bg=safecolor,bd=0,height=1,width=210).place(x=100,y=changey1)
        Canvas(LG,bg=safecolor,bd=0,height=1,width=210).place(x=100,y=changey2)
        Canvas(LG,bg=safecolor,bd=0,height=1,width=210).place(x=310,y=changey3)
        Canvas(LG,bg=safecolor,bd=0,height=1,width=210).place(x=310,y=changey4)
        Canvas(LG,bg=safecolor,bd=0,height=1,width=210).place(x=520,y=changey5)
        Canvas(LG,bg=safecolor,bd=0,height=1,width=210).place(x=520,y=changey6)
        Canvas(LG,bg=safecolor,bd=0,height=1,width=210).place(x=730,y=changey7)
        Canvas(LG,bg=safecolor,bd=0,height=1,width=210).place(x=730,y=changey8)
        Canvas(LG,bg=safecolor,bd=0,height=1,width=210).place(x=940,y=changey9)
        Canvas(LG,bg=safecolor,bd=0,height=1,width=210).place(x=940,y=changey10)

        # liggende lijnen voor toetsen
        c5=Canvas(LG,bg=safecolor2,bd=0,height=1,width=1050).place(x=100,y=526)
        c6=Canvas(LG,bg=safecolor2,bd=0,height=1,width=1050).place(x=100,y=530)
        c7=Canvas(LG,bg=safecolor2,bd=0,height=1,width=1050).place(x=100,y=686)
        c8=Canvas(LG,bg=safecolor2,bd=0,height=1,width=1050).place(x=100,y=690)


        # rechtopstaande lijnen voor vakken
        Canvas(LG,bg=safecolor,bd=0,height=height1,width=1).place(x=98,y=135)
        Canvas(LG,bg=safecolor,bd=0,height=height1,width=1).place(x=102,y=135)
        Canvas(LG,bg=safecolor,bd=0,height=height2,width=1).place(x=308,y=135)
        Canvas(LG,bg=safecolor,bd=0,height=height2,width=1).place(x=312,y=135)
        Canvas(LG,bg=safecolor,bd=0,height=height3,width=1).place(x=518,y=135)
        Canvas(LG,bg=safecolor,bd=0,height=height3,width=1).place(x=522,y=135)
        Canvas(LG,bg=safecolor,bd=0,height=height4,width=1).place(x=728,y=135)
        Canvas(LG,bg=safecolor,bd=0,height=height4,width=1).place(x=732,y=135)
        Canvas(LG,bg=safecolor,bd=0,height=height5,width=1).place(x=938,y=135)
        Canvas(LG,bg=safecolor,bd=0,height=height5,width=1).place(x=942,y=135)
        Canvas(LG,bg=safecolor,bd=0,height=height6,width=1).place(x=1148,y=135)
        Canvas(LG,bg=safecolor,bd=0,height=height6,width=1).place(x=1152,y=135)


        # rechtopstaande lijnen voor toetsen
        c21=Canvas(LG,bg=safecolor2,bd=0,height=164,width=1).place(x=98,y=526)
        c22=Canvas(LG,bg=safecolor2,bd=0,height=164,width=1).place(x=102,y=526)
        c23=Canvas(LG,bg=safecolor2,bd=0,height=164,width=1).place(x=308,y=526)
        c24=Canvas(LG,bg=safecolor2,bd=0,height=164,width=1).place(x=312,y=526)
        c25=Canvas(LG,bg=safecolor2,bd=0,height=164,width=1).place(x=518,y=526)
        c26=Canvas(LG,bg=safecolor2,bd=0,height=164,width=1).place(x=522,y=526)
        c27=Canvas(LG,bg=safecolor2,bd=0,height=164,width=1).place(x=728,y=526)
        c28=Canvas(LG,bg=safecolor2,bd=0,height=164,width=1).place(x=732,y=526)
        c29=Canvas(LG,bg=safecolor2,bd=0,height=164,width=1).place(x=938,y=526)
        c30=Canvas(LG,bg=safecolor2,bd=0,height=164,width=1).place(x=942,y=526)
        c31=Canvas(LG,bg=safecolor2,bd=0,height=164,width=1).place(x=1148,y=526)
        c32=Canvas(LG,bg=safecolor2,bd=0,height=164,width=1).place(x=1152,y=526)


    lijnen()
    b21=HoverButton(LG,bg=safecolor,bd=0,width=4,height=10,text=">",font=('arial', 20),activebackground='gray79',command=week2).place(x=1190,y=200)
    def komendeweken():
        with open('dezemaand1.txt', 'r') as f: dezemaand1 = f.read()
        wekende=Tk(); wekende.attributes('-fullscreen',True); wekende.configure(background='white')
        def dezeweekmaand1():
            f= open("dezemaand1.txt"); studGradeString = ""
            for i in f: studGradeString += i; aboutStud.insert(1.0, studGradeString); f.close(); return
        def openFiles1(selection):
            if selection == "februari/april": dezeweekmaand1()
        def maandopslaan1():
             GU = aboutStud.get(1.0,END)
             oTF = open('dezemaand1.txt', 'w'); oTF.write(GU); oTF.close(); return

        aboutStud = Text(wekende); aboutStud.place(x=40,y=100)
        menu_bar = Menu(wekende)
        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Quit!", command=dezeweekmaand1)
        file_menu.add_command(label="Exit!", command=wekende.destroy)
        file_menu.add_command(label="End!", command=wekende.destroy)
        menu_bar.add_cascade(label="File", menu=file_menu)

        Label(wekende,font=('arial',15),text=dezemaand1,bg="white",bd=0).place(x=800,y=50)

        Button(wekende,bg="white",bd=0,text="opslaan",command=maandopslaan1).place(x=0,y=500)
        wekende.config(menu=menu_bar)
        wekende.mainloop()
    def overzicht():
        t1=Tk(); t1.attributes('-fullscreen',True); t1.configure(background='white')
        def overzichtweek2():
            Frame(t1,bg="white",bd=0,height=560,width=245).place(x=300,y=35); Frame(t1,bg="white",bd=0,height=560,width=245).place(x=970,y=35)
            Label(t1,font=('arial',15),text=f_contents52,bg="white",bd=0).place(x=300,y=35);Label(t1,font=('arial',15),text=f_contents53,bg="white",bd=0).place(x=300,y=85)
            Label(t1,font=('arial',15),text=f_contents54,bg="white",bd=0).place(x=300,y=135); Label(t1,font=('arial',15),text=f_contents55,bg="white",bd=0).place(x=300,y=185); Label(t1,font=('arial',15),text=f_contents56,bg="white",bd=0).place(x=300,y=235); Label(t1,font=('arial',15),text=f_contents57,bg="white",bd=0).place(x=300,y=285); Label(t1,font=('arial',15),text=f_contents58,bg="white",bd=0).place(x=300,y=335); Label(t1,font=('arial',15),text=f_contents59,bg="white",bd=0).place(x=300,y=385); Label(t1,font=('arial',15),text=f_contents60,bg="white",bd=0).place(x=300,y=435); Label(t1,font=('arial',15),text=f_contents61,bg="white",bd=0).place(x=300,y=485); Label(t1,font=('arial',15),text=f_contents62,bg="white",bd=0).place(x=300,y=535); Label(t1,font=('arial',15),text=f_contents63,bg="white",bd=0).place(x=300,y=585); Label(t1,font=('arial',15),text=f_contents64,bg="white",bd=0).place(x=970,y=35); Label(t1,font=('arial',15),text=f_contents65,bg="white",bd=0).place(x=970,y=85); Label(t1,font=('arial',15),text=f_contents66,bg="white",bd=0).place(x=970,y=135); Label(t1,font=('arial',15),text=f_contents67,bg="white",bd=0).place(x=970,y=185); Label(t1,font=('arial',15),text=f_contents68,bg="white",bd=0).place(x=970,y=235); Label(t1,font=('arial',15),text=f_contents69,bg="white",bd=0).place(x=970,y=285); Label(t1,font=('arial',15),text=f_contents70,bg="white",bd=0).place(x=970,y=335); Label(t1,font=('arial',15),text=f_contents71,bg="white",bd=0).place(x=970,y=385)
        menu_bar = Menu(t1)
        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Week 1", command=overzicht)
        file_menu.add_command(label="Week 2", command=overzichtweek2)
        file_menu.add_command(label="End!", command=t1.destroy)
        menu_bar.add_cascade(label="File", menu=file_menu)
        t1.config(menu=menu_bar)
        #----------de labels met dagen erin--------#
        Label(t1,font=('arial',20),text="Maandag",bg="white",bd=0).place(x=80,y=35); Label(t1,font=('arial',20),text="Dinsdag",bg="white",bd=0).place(x=80,y=235); Label(t1,font=('arial',20),text="Woensdag",bg="white",bd=0).place(x=80,y=435); Label(t1,font=('arial',20),text="Donderdag",bg="white",bd=0).place(x=750,y=35); Label(t1,font=('arial',20),text="Vrijdag",bg="white",bd=0).place(x=750,y=235)
        #----------de labels met het huiswekr erin--------#
        Label(t1,font=('arial',15),text=f_contents21,bg="white",bd=0).place(x=300,y=35); Label(t1,font=('arial',15),text=f_contents22,bg="white",bd=0).place(x=300,y=85); Label(t1,font=('arial',15),text=f_contents23,bg="white",bd=0).place(x=300,y=135); Label(t1,font=('arial',15),text=f_contents24,bg="white",bd=0).place(x=300,y=185); Label(t1,font=('arial',15),text=f_contents25,bg="white",bd=0).place(x=300,y=235); Label(t1,font=('arial',15),text=f_contents26,bg="white",bd=0).place(x=300,y=285); Label(t1,font=('arial',15),text=f_contents27,bg="white",bd=0).place(x=300,y=335); Label(t1,font=('arial',15),text=f_contents28,bg="white",bd=0).place(x=300,y=385); Label(t1,font=('arial',15),text=f_contents29,bg="white",bd=0).place(x=300,y=435); Label(t1,font=('arial',15),text=f_contents30,bg="white",bd=0).place(x=300,y=485); Label(t1,font=('arial',15),text=f_contents31,bg="white",bd=0).place(x=300,y=535); Label(t1,font=('arial',15),text=f_contents32,bg="white",bd=0).place(x=300,y=585); Label(t1,font=('arial',15),text=f_contents33,bg="white",bd=0).place(x=970,y=35); Label(t1,font=('arial',15),text=f_contents34,bg="white",bd=0).place(x=970,y=85); Label(t1,font=('arial',15),text=f_contents35,bg="white",bd=0).place(x=970,y=135); Label(t1,font=('arial',15),text=f_contents36,bg="white",bd=0).place(x=970,y=185); Label(t1,font=('arial',15),text=f_contents37,bg="white",bd=0).place(x=970,y=235); Label(t1,font=('arial',15),text=f_contents38,bg="white",bd=0).place(x=970,y=285); Label(t1,font=('arial',15),text=f_contents39,bg="white",bd=0).place(x=970,y=335); Label(t1,font=('arial',15),text=f_contents40,bg="white",bd=0).place(x=970,y=385)
        #----------de groene lijnen eromheen--------#
        Canvas(t1,bg=safecolor,bd=0,height=1,width=500).place(x=50,y=26); Canvas(t1,bg=safecolor,bd=0,height=1,width=500).place(x=50,y=30); Canvas(t1,bg=safecolor,bd=0,height=1,width=500).place(x=50,y=626); Canvas(t1,bg=safecolor,bd=0,height=1,width=500).place(x=50,y=630); Canvas(t1,bg=safecolor,bd=0,height=604,width=2).place(x=46,y=26); Canvas(t1,bg=safecolor,bd=0,height=604,width=2).place(x=50,y=26); Canvas(t1,bg=safecolor,bd=0,height=604,width=2).place(x=546,y=26); Canvas(t1,bg=safecolor,bd=0,height=604,width=2).place(x=550,y=26); Canvas(t1,bg=safecolor,bd=0,height=1,width=500).place(x=720,y=26); Canvas(t1,bg=safecolor,bd=0,height=1,width=500).place(x=720,y=30); Canvas(t1,bg=safecolor,bd=0,height=1,width=500).place(x=720,y=626); Canvas(t1,bg=safecolor,bd=0,height=1,width=500).place(x=720,y=630); Canvas(t1,bg=safecolor,bd=0,height=604,width=2).place(x=716,y=26); Canvas(t1,bg=safecolor,bd=0,height=604,width=2).place(x=720,y=26); Canvas(t1,bg=safecolor,bd=0,height=604,width=2).place(x=1216,y=26); Canvas(t1,bg=safecolor,bd=0,height=604,width=2).place(x=1220,y=26)
        t1.mainloop()
    def sidemenu():
        Canvas(LG,width=200,height=750,bg="black",bd=0).place(x=-4,y=0)
        Button(LG, image=img3 ,bd=0,bg="white",command=knorth).place(x=203,y=3)
        HoverButton(LG,width=16,height=2,fg="white",font=('arial',15,'bold'),text="komende weken",bd=0,activebackground='gray15',bg="black",command=komendeweken).place(x=0,y=0)
        HoverButton(LG,width=16,height=2,fg="white",font=('arial',15,'bold'),text="overzicht",bd=0,activebackground='gray15',bg="black",command=overzicht).place(x=0,y=50)

        sluiten()
    Button(LG, image=img3 ,bd=0,bg="white",command=sidemenu).place(x=3,y=3);sluiten()
    Button(LG, image=img7 ,bd=0,bg="white",command=waarschuwing).place(x=10,y=670)
def algemeen():
    pass
def baas():
    pass
def personeel():
    pass
class app():
    def __init__(self):
        #Button(LG,text="run",command=self.run_progressBar).place(x=0,y=0)
        Label(LG,text="Bezig met Updaten", font=('arial',20,'bold'),bg="white").place(x=530,y=400)
        s = ttk.Style()
        s.theme_use('default')
        s.configure("Horizontal.TProgressbar", foreground='red', background='red')
        self.progress_bar = ttk.Progressbar(LG,style="Horizontal.TProgressbar", orient = 'horizontal', length = 400)
        self.progress_bar.place(x=450,y=500)
        #def run_progressBar(self):
         
        self.progress_bar['maximum']=100

        for i in range(101):
            time.sleep(0.03)
            self.progress_bar["value"] = i
            self.progress_bar.update()
        self.progress_bar["value"] = 0
def internet_on():
    def wifi():
        data = urllib2.urlopen('https://github.com/bramteunis/-myprogram/blob/master/test.txt').read()
        data1 = re.findall(r'<td id="LC1" class="blob-code blob-code-inner js-file-line">(.*?)</td>',str(data))
        if data1[0] == needed: pass
        else:
            if messagebox.askyesno("Systeem", "Je hebt een update nodig. Wil je deze downloaden") == True:
                access1 = (1)
                webbrowser.open_new_tab('https://github.com/bramteunis/-myprogram/archive/master.zip')
                for x in range (0,100):
                    app()
                    my_file = Path(f'C:/Users/{username}/Downloads/-myprogram-master.zip')
                    if my_file.is_file():
                        shutil.rmtree(f'C:/Users/{username}/Desktop/extracted_content/-myprogram-master')   
                        #shutil.move('-myprogram-master.zip','C:/Users/bramt/Desktop')
                        zib_obj = zipfile.ZipFile(f'C:/Users/{username}/Downloads/-myprogram-master.zip','r')
                        zib_obj.extractall(f'C:/Users/{username}/Desktop/extracted_content')
                        zib_obj.close()
                        os.remove(f"C:/Users/{username}/Downloads/-myprogram-master.zip")
                        break
                    else:
                        #counter = float
                        #counter += (1)
                        #if counter == (99):
                        #    messagebox.showinfo("Systeem", "Controleer of je Internet hebt en probeer het opnieuw")
                        pass
            else: app()
        

    def geenwifi():
        pass
    try:
        urllib2.urlopen('http://216.58.192.142', timeout=1)
        wifi()
    except urllib2.URLError as err:
        geenwifi()
        
if loginofniet11 == "Nooit":
    internet_on()
    homepage()
else:
    internet_on()
    if access1 == (1):
        frame1 = Canvas( LG, bg ="white", height=4830,highlightthickness=0, width=1810,bd=0)
        image1 = PhotoImage(file="beginschermfoto3.png")
        image = frame1.create_image( 1000, 0, anchor = NE,image=image1)
        var = IntVar()
        frame1.place(x=500,y=-3)

        frame2 = Canvas( LG, bg ="white", height=130,highlightthickness=0, width=284,bd=0)
        image2 = PhotoImage(file="logo1.png")
        image = frame2.create_image(284,0,anchor=NE,image=image2)
        frame2.place(x=20,y=30)

        frame3 = Canvas( LG, bg ="white", height=30, width=30,highlightthickness=0,bd=0)
        image3 = PhotoImage(file="terug1.png")
        image = frame3.create_image(40,0,anchor=NE,image=image3)
        frame3.place(x=50,y=679)

        Button(LG,text='Forgot your password?',width=20,bd=0,height=1,font=('arial', 13),bg="white",fg="blue",command=forgotLG).place(x=140,y=600)
        Button(LG,text='Exit',width=7,bd=0,height=1,font=('arial', 8),bg="white",command=LG.destroy).place(x=85,y=683)

        Label(LG,text='Username:',bd=0,font=('arial', 10),bg="white").place(x=70,y=270)
        Label(LG,text='Password:',bd=0,font=('arial', 10),bg="white").place(x=70,y=370)
        L7=Label(LG,text='Good afternoon,',bd=0,font=('arial', 15, 'bold'),bg="white").place(x=70,y=180)
        L8=Label(LG,text='welcome back!',bd=0,font=('arial', 14),bg="white").place(x=230,y=181)
        L9=Label(LG,text='Feel free to login anytime.',bd=0,font=('arial', 11),bg="white").place(x=70,y=210)
        Checkbutton(LG,text="remember me",bg="white",variable=var3,onvalue=1,offvalue=0).place(x=70,y=470)
        t1=Entry(LG,show='*',textvariable=value1,bd=2,font=medium_font,relief="groove").place(x=70,y=400)
        if counter1 == '1':
            g1 = open("gebruiker1.txt", "r").readlines()[0]; gebruiker1=g1.strip()
            w1 = open("gebruiker1.txt", "r").readlines()[5]; wachtwoord1=w1.strip()
            Button(LG,text='login',bd=0,fg="white",font=('arial', 20), width= 20, height=1, command= Gebruikersnaam1,bg=safecolor,relief="ridge").place(x=70,y=540)
            box=ttk.Combobox(LG,textvariable=value3,font=medium_font,state='readonly'); box['values']=(gebruiker1); remembertest=box.current(0)
            box.place(x=70,y=300)
        if counter1 == '2':
            g1 = open("gebruiker1.txt", "r").readlines()[0]; gebruiker1=g1.strip()
            g2 = open("gebruiker1.txt", "r").readlines()[1]; gebruiker2=g2.strip()
            w1 = open("gebruiker1.txt", "r").readlines()[5]; wachtwoord1=w1.strip()
            w2 = open("gebruiker1.txt", "r").readlines()[6]; wachtwoord2=w2.strip()
            Button(LG,text='login',bd=0,fg="white",font=('arial', 20), width= 20, height=1, command= Gebruikers2,bg=safecolor,relief="ridge").place(x=70,y=540)
            box=ttk.Combobox(LG,textvariable=value3,font=medium_font,state='readonly'); box['values']=(gebruiker1,gebruiker2); remembertest=box.current(0)
            box.place(x=70,y=300)
        if counter1 == '3':
            g1 = open("gebruiker1.txt", "r").readlines()[0]; gebruiker1=g1.strip()
            g2 = open("gebruiker1.txt", "r").readlines()[1]; gebruiker2=g2.strip()
            g3 = open("gebruiker1.txt", "r").readlines()[2]; gebruiker3=g3.strip()
            w1 = open("gebruiker1.txt", "r").readlines()[5]; wachtwoord1=w1.strip()
            w2 = open("gebruiker1.txt", "r").readlines()[6]; wachtwoord2=w2.strip()
            w3 = open("gebruiker1.txt", "r").readlines()[7]; wachtwoord3=w3.strip()
            Button(LG,text='login',bd=0,fg="white",font=('arial', 20), width= 20, height=1, command= Gebruikers3,bg=safecolor,relief="ridge").place(x=70,y=540)
            box=ttk.Combobox(LG,textvariable=value3,font=medium_font,state='readonly'); box['values']=(gebruiker1,gebruiker2,gebruiker3); remembertest=box.current(0)
            box.place(x=70,y=300)
        if counter1 == '4':
            g1 = open("gebruiker1.txt", "r").readlines()[0]; gebruiker1=g1.strip()
            g2 = open("gebruiker1.txt", "r").readlines()[1]; gebruiker2=g2.strip()
            g3 = open("gebruiker1.txt", "r").readlines()[2]; gebruiker3=g3.strip()
            g4 = open("gebruiker1.txt", "r").readlines()[3]; gebruiker4=g4.strip()
            w1 = open("gebruiker1.txt", "r").readlines()[5]; wachtwoord1=w1.strip()
            w2 = open("gebruiker1.txt", "r").readlines()[6]; wachtwoord2=w2.strip()
            w3 = open("gebruiker1.txt", "r").readlines()[7]; wachtwoord3=w3.strip()
            w4 = open("gebruiker1.txt", "r").readlines()[8]; wachtwoord4=w4.strip()
            Button(LG,text='login',bd=0,fg="white",font=('arial', 20), width= 20, height=1, command= Gebruikers4,bg=safecolor,relief="ridge").place(x=70,y=540)
            box=ttk.Combobox(LG,textvariable=value3,font=medium_font,state='readonly'); box['values']=(gebruiker1,gebruiker2,gebruiker3,gebruiker4); remembertest=box.current(0)
            box.place(x=70,y=300)
        if counter1 == '5':
            g1 = open("gebruiker1.txt", "r").readlines()[0]; gebruiker1=g1.strip()
            g2 = open("gebruiker1.txt", "r").readlines()[1]; gebruiker2=g2.strip()
            g3 = open("gebruiker1.txt", "r").readlines()[2]; gebruiker3=g3.strip()
            g4 = open("gebruiker1.txt", "r").readlines()[3]; gebruiker4=g4.strip()
            g5 = open("gebruiker1.txt", "r").readlines()[4]; gebruiker5=g5.strip()
            w1 = open("gebruiker1.txt", "r").readlines()[5]; wachtwoord1=w1.strip()
            w2 = open("gebruiker1.txt", "r").readlines()[6]; wachtwoord2=w2.strip()
            w3 = open("gebruiker1.txt", "r").readlines()[7]; wachtwoord3=w3.strip()
            w4 = open("gebruiker1.txt", "r").readlines()[8]; wachtwoord4=w4.strip()
            w5 = open("gebruiker1.txt", "r").readlines()[9]; wachtwoord5=w5.strip()
            Button(LG,text='login',bd=0,fg="white",font=('arial', 20), width= 20, height=1, command= Gebruikers5,bg=safecolor,relief="ridge").place(x=70,y=540)
            box=ttk.Combobox(LG,textvariable=value3,font=medium_font,state='readonly'); box['values']=(gebruiker1,gebruiker2,gebruiker3,gebruiker4,gebruiker5); box.current(0)
            box.place(x=70,y=300)
        def sluiten1(): LG.destroy()
    else:
        LG.destroy()
        
LG.mainloop()
