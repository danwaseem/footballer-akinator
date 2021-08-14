from Tkinter import *
import os
def bye():
    os._exit(0)
class AKINATOR:
    
    def __init__(self):
        self.L=[]

    def start(self):
        root = Tk()
        root.wm_title("Game")
        T = Text(root, height=4, width=100)
        T.pack()
        T.insert(END, "Think of a player from Real Madrid/FC Barcelona Current Squad \n You need to know players nationality, position and age \n Lets Start ?")
        Button(root, text='OK', command=lambda:self.cont(root)).pack(fill=X)
        mainloop()
    def team(self):
        root = Tk()
        root.wm_title("Question")
        T = Text(root, height=2, width=50)
        T.pack()
        T.insert(END, "Is your player from Real Madrid? ")
        Button(root, text='Yes', command=lambda:self.add('rm',root)).pack(fill=X)
        Button(root, text='No', command=lambda:self.add('fcb',root)).pack(fill=X)
        mainloop()
    def add(self,alpha,root):
        self.L+=[alpha]
        root.quit()
        return
    def cont(self,root):
        root.quit()
        pass
    def country(self):
        root = Tk()
        root.wm_title("Question")
        T = Text(root, height=2, width=50)
        T.pack()
        T.insert(END, "Which Country is your Player from? ")
        Button(root, text='Spain', command=lambda:self.add('s',root)).pack(fill=X)
        Button(root, text='Portugal', command=lambda:self.add('p',root)).pack(fill=X)
        Button(root, text='Brazil', command=lambda:self.add('b',root)).pack(fill=X)
        Button(root, text='France', command=lambda:self.add('f',root)).pack(fill=X)
        Button(root, text='Argentina', command=lambda:self.add('a',root)).pack(fill=X)
        Button(root, text='Crotia', command=lambda:self.add('c',root)).pack(fill=X)
        Button(root, text='Germany', command=lambda:self.add('g',root)).pack(fill=X)
        Button(root, text='Other', command=lambda:self.add('o',root)).pack(fill=X)
        mainloop()
    def position(self):
        root = Tk()
        root.wm_title("Question")
        T = Text(root, height=2, width=50)
        T.pack()
        T.insert(END, "Which position does your player play ? ")
        Button(root, text='Goalkeeping', command=lambda:self.add('gk',root)).pack(fill=X)
        Button(root, text='Defence', command=lambda:self.add('df',root)).pack(fill=X)
        Button(root, text='Midfield', command=lambda:self.add('mf',root)).pack(fill=X)
        Button(root, text='Attack', command=lambda:self.add('ak',root)).pack(fill=X)

        mainloop()
    def age (self):
        root = Tk()
        root.wm_title("Question")
        T = Text(root, height=1, width=50)
        T.pack()
        T.insert(END, "Enter players Age ")

        
        e = Entry(root)
        e.pack()
        s=e.get()
        Button(root,text="Submit", command=lambda:self.add(e.get(),root)).pack()

        mainloop()
    def same(self):
        if self.L==['rm','s','ak','24']:
            root = Tk()
            root.wm_title("Question")
            T = Text(root, height=2, width=50)
            T.pack()
            T.insert(END, "Did your player play in Juventus ? ")
            Button(root, text='Yes', command=lambda:self.add('y',root)).pack(fill=X)
            Button(root, text='No', command=lambda:self.cont(root)).pack(fill=X)
            mainloop()
        elif self.L==['fcb','f','df','23']:
            root = Tk()
            root.wm_title("Question")
            T = Text(root, height=2, width=50)
            T.pack()
            T.insert(END, "Did your player play in Sevilla ? ")
            Button(root, text='Yes', command=lambda:self.add('y',root)).pack(fill=X)
            Button(root, text='No', command=lambda:self.cont(root)).pack(fill=X)
            mainloop()
        elif self.L==['fcb','f','df','23']:
            root = Tk()
            root.wm_title("Question")
            T = Text(root, height=2, width=50)
            T.pack()
            T.insert(END, "Did your player play in PSG ? ")
            Button(root, text='Spain', command=lambda:self.add('y',root)).pack(fill=X)
            Button(root, text='Portugal', command=lambda:self.cont(root)).pack(fill=X)
            mainloop()
        
    def select(self):
        s1=['rm','s','df','30']#sergio ramos
        s2=['rm','s','df','25']#dani carvajal
        s3=['rm','s','df','27']#nacho
        s4=['rm','s','gk','30']#kiko casilla
        s5=['rm','s','ak','25']#lucas vazquez
        s6=['rm','s','ak','21']#marco asensio
        s7=['rm','s','ak','24','y']#morata
        s8=['rm','s','ak','24']#isco
        s9=['rm','s','gk','23']#ruben yanez
        s10=['fcb','s','gk','28']#jordi masip
        s11=['fcb','s','df','29']#gerard pique
        s12=['fcb','s','df','27','y']#jordi Alba
        s13=['fcb','s','df','27']#aleix vidal
        s14=['fcb','s','df','24']#sergi roberto
        s15=['fcb','s','mf','28']#sergio busquets
        s16=['fcb','s','mf','32']#andres iniesta
        s17=['fcb','s','mf','23']#denis suarez
        s18=['fcb','s','ak','23']#paco alcacer
        p1=['rm','p','df','33']#pepe
        p2=['rm','p','df','28']#fabio coentrao
        p3=['rm','p','ak','32']#cristiano ronaldo
        p4=['fcb','p','ak','23']#andre gomes
        b1=['rm','b','df','28']#marcelo
        b2=['rm','b','df','25']#danilo
        b3=['rm','b','mf','24']#casemiro
        b4=['rm','b','mf','23']#lucas silva
        b5=['fcb','b','mf','23']#rafinha
        b6=['fcb','b','ak','24']#neymar
        f1=['rm','f','df','23']#raphael varane
        f2=['rm','f','ak','29']#karim benzema
        f3=['fcb','f','df','23']#samuel umtiti
        f4=['fcb','f','df','23','y']#lucas digne
        f5=['fcb','f','df','33']#jeremy mathieu
        a1=['fcb','a','df','32']#javier mascherano
        a2=['fcb','f','ak','29']#lionel messi
        c1=['rm','c','mf','31']#luka modric
        c2=['rm','c','mf','22']#mateo kovacic
        c3=['fcb','c','mf','28']#ivan rakitic
        g1=['rm','g','mf','27']#toni kroos
        g2=['fcb','g','gk','24']#marc-andre ter stegan
        o1=['rm','o','gk','30']#keylor navas
        o2=['rm','o','mf','25']#james rodriguez
        o3=['rm','o','ak','27']#gareth bale
        o4=['rm','o','ak','23']#mariano diaz
        o5=['fcb','o','gk','27']#jasper cillessen
        o6=['fcb','o','mf','29']#arda turan
        o7=['fcb','o','ak','29']#luis suarez
        if self.L==s1:
            fil=open("sergio ramos.txt","r")
            rd=fil.read()
            root = Tk()
            root.wm_title("Player Information")
            T = Text(root, height=20, width=50)
            T.pack()
            T.insert(END, rd)
            Button(root, text='Quit', command=bye).pack()
            mainloop()
        elif self.L==s2:
            fil=open("dani carvajal.txt","r")
            rd=fil.read()
            root = Tk()
            root.wm_title("Player Information")
            T = Text(root, height=20, width=100)
            T.pack()
            T.insert(END, rd)
            Button(root, text='Quit', command=bye).pack(fill=X)
            mainloop()
        elif self.L==s3:
            fil=open("nacho.txt","r")
            rd=fil.read()
            root = Tk()
            root.wm_title("Player Information")
            T = Text(root, height=20, width=100)
            T.pack()
            T.insert(END, rd)
            Button(root, text='Quit', command=bye).pack(fill=X)
            mainloop()
        elif self.L==s4:
            fil=open("kiko casilla.txt","r")
            rd=fil.read()
            root = Tk()
            root.wm_title("Player Information")
            T = Text(root, height=20, width=100)
            T.pack()
            T.insert(END, rd)
            Button(root, text='Quit', command=bye).pack(fill=X)
            mainloop()
        elif self.L==s5:
            fil=open("lucas vazquez.txt","r")
            rd=fil.read()
            root = Tk()
            root.wm_title("Player Information")
            T = Text(root, height=20, width=100)
            T.pack()
            T.insert(END, rd)
            Button(root, text='Quit', command=bye).pack(fill=X)
            mainloop()
        elif self.L==s6:
            fil=open("marco asensio.txt","r")
            rd=fil.read()
            root = Tk()
            root.wm_title("Player Information")
            T = Text(root, height=20, width=100)
            T.pack()
            T.insert(END, rd)
            Button(root, text='Quit', command=bye).pack(fill=X)
            mainloop()
        elif self.L==s7:
            fil=open("morata.txt","r")
            rd=fil.read()
            root = Tk()
            root.wm_title("Player Information")
            T = Text(root, height=20, width=100)
            T.pack()
            T.insert(END, rd)
            Button(root, text='Quit', command=bye).pack(fill=X)
            mainloop()
        elif self.L==s8:
            fil=open("isco.txt","r")
            rd=fil.read()
            root = Tk()
            root.wm_title("Player Information")
            T = Text(root, height=20, width=100)
            T.pack()
            T.insert(END, rd)
            Button(root, text='Quit', command=bye).pack(fill=X)
            mainloop()
        elif self.L==s9:
            fil=open("ruben yanez.txt","r")
            rd=fil.read()
            root = Tk()
            root.wm_title("Player Information")
            T = Text(root, height=20, width=100)
            T.pack()
            T.insert(END, rd)
            Button(root, text='Quit', command=bye).pack(fill=X)
            mainloop()
        elif self.L==s10:
            fil=open("jordi masip.txt","r")
            rd=fil.read()
            root = Tk()
            root.wm_title("Player Information")
            T = Text(root, height=20, width=100)
            T.pack()
            T.insert(END, rd)
            Button(root, text='Quit', command=bye).pack(fill=X)
            mainloop()
        elif self.L==s11:
            fil=open("gerrard pique.txt","r")
            rd=fil.read()
            root = Tk()
            root.wm_title("Player Information")
            T = Text(root, height=20, width=100)
            T.pack()
            T.insert(END, rd)
            Button(root, text='Quit', command=bye).pack(fill=X)
            mainloop()
        elif self.L==s12:
            fil=open("jordi alba.txt","r")
            rd=fil.read()
            root = Tk()
            root.wm_title("Player Information")
            T = Text(root, height=20, width=100)
            T.pack()
            T.insert(END, rd)
            Button(root, text='Quit', command=bye).pack(fill=X)
            mainloop()
        elif self.L==s13:
            fil=open("aleix vidal.txt","r")
            rd=fil.read()
            root = Tk()
            root.wm_title("Player Information")
            T = Text(root, height=20, width=100)
            T.pack()
            T.insert(END, rd)
            Button(root, text='Quit', command=bye).pack(fill=X)
            mainloop()
        elif self.L==s14:
            fil=open("sergi roberto.txt","r")
            rd=fil.read()
            root = Tk()
            root.wm_title("Player Information")
            T = Text(root, height=20, width=100)
            T.pack()
            T.insert(END, rd)
            Button(root, text='Quit', command=bye).pack(fill=X)
            mainloop()
        elif self.L==s15:
            fil=open("sergio busquets.txt","r")
            rd=fil.read()
            root = Tk()
            root.wm_title("Player Information")
            T = Text(root, height=20, width=100)
            T.pack()
            T.insert(END, rd)
            Button(root, text='Quit', command=bye).pack(fill=X)
            mainloop()
        elif self.L==s16:
            fil=open("andres iniesta.txt","r")
            rd=fil.read()
            root = Tk()
            root.wm_title("Player Information")
            T = Text(root, height=20, width=100)
            T.pack()
            T.insert(END, rd)
            Button(root, text='Quit', command=bye).pack(fill=X)
            mainloop()
        elif self.L==s17:
            fil=open("denis suarez.txt","r")
            rd=fil.read()
            root = Tk()
            root.wm_title("Player Information")
            T = Text(root, height=20, width=100)
            T.pack()
            T.insert(END, rd)
            Button(root, text='Quit', command=bye).pack(fill=X)
            mainloop()
        elif self.L==s18:
            fil=open("paco alcacer.txt","r")
            rd=fil.read()
            root = Tk()
            root.wm_title("Player Information")
            T = Text(root, height=20, width=100)
            T.pack()
            T.insert(END, rd)
            Button(root, text='Quit', command=bye).pack(fill=X)
            mainloop()
        elif self.L==p1:
            fil=open("pepe.txt","r")
            rd=fil.read()
            root = Tk()
            root.wm_title("Player Information")
            T = Text(root, height=20, width=100)
            T.pack()
            T.insert(END, rd)
            Button(root, text='Quit', command=bye).pack(fill=X)
            mainloop()
        elif self.L==p2:
            fil=open("fabio coentrao.txt","r")
            rd=fil.read()
            root = Tk()
            root.wm_title("Player Information")
            T = Text(root, height=20, width=100)
            T.pack()
            T.insert(END, rd)
            Button(root, text='Quit', command=bye).pack(fill=X)
            mainloop()
        elif self.L==p3:
            fil=open("cristiano ronaldo.txt","r")
            rd=fil.read()
            root = Tk()
            root.wm_title("Player Information")
            T = Text(root, height=20, width=100)
            T.pack()
            T.insert(END, rd)
            Button(root, text='Quit', command=bye).pack(fill=X)
            mainloop()
        elif self.L==p4:
            fil=open("andre gomes.txt","r")
            rd=fil.read()
            root = Tk()
            root.wm_title("Player Information")
            T = Text(root, height=20, width=100)
            T.pack()
            T.insert(END, rd)
            Button(root, text='Quit', command=bye).pack(fill=X)
            mainloop()
        elif self.L==b1:
            fil=open("marcelo.txt","r")
            rd=fil.read()
            root = Tk()
            root.wm_title("Player Information")
            T = Text(root, height=20, width=100)
            T.pack()
            T.insert(END, rd)
            Button(root, text='Quit', command=bye).pack(fill=X)
            mainloop()
        elif self.L==b2:
            fil=open("danilo.txt","r")
            rd=fil.read()
            root = Tk()
            root.wm_title("Player Information")
            T = Text(root, height=20, width=100)
            T.pack()
            T.insert(END, rd)
            Button(root, text='Quit', command=bye).pack(fill=X)
            mainloop()
        elif self.L==b3:
            fil=open("casemiro.txt","r")
            rd=fil.read()
            root = Tk()
            root.wm_title("Player Information")
            T = Text(root, height=20, width=100)
            T.pack()
            T.insert(END, rd)
            Button(root, text='Quit', command=bye).pack(fill=X)
            mainloop()
        elif self.L==b4:
            fil=open("lucas silva.txt","r")
            rd=fil.read()
            root = Tk()
            root.wm_title("Player Information")
            T = Text(root, height=20, width=100)
            T.pack()
            T.insert(END, rd)
            Button(root, text='Quit', command=bye).pack(fill=X)
            mainloop()
        elif self.L==b5:
            fil=open("rafinha.txt","r")
            rd=fil.read()
            root = Tk()
            root.wm_title("Player Information")
            T = Text(root, height=20, width=100)
            T.pack()
            T.insert(END, rd)
            Button(root, text='Quit', command=bye).pack(fill=X)
            mainloop()
        elif self.L==b6:
            fil=open("neymar.txt","r")
            rd=fil.read()
            root = Tk()
            root.wm_title("Player Information")
            T = Text(root, height=20, width=100)
            T.pack()
            T.insert(END, rd)
            Button(root, text='Quit', command=bye).pack(fill=X)
            mainloop()
        elif self.L==f1:
            fil=open("raphael varane.txt","r")
            rd=fil.read()
            root = Tk()
            root.wm_title("Player Information")
            T = Text(root, height=20, width=100)
            T.pack()
            T.insert(END, rd)
            Button(root, text='Quit', command=bye).pack(fill=X)
            mainloop()
        elif self.L==f2:
            fil=open("karim benzema.txt","r")
            rd=fil.read()
            root = Tk()
            root.wm_title("Player Information")
            T = Text(root, height=20, width=100)
            T.pack()
            T.insert(END, rd)
            Button(root, text='Quit', command=bye).pack(fill=X)
            mainloop()
        elif self.L==f3:
            fil=open("samuel umtiti.txt","r")
            rd=fil.read()
            root = Tk()
            root.wm_title("Player Information")
            T = Text(root, height=20, width=100)
            T.pack()
            T.insert(END, rd)
            Button(root, text='Quit', command=bye).pack(fill=X)
            mainloop()
        elif self.L==f4:
            fil=open("lucas digne.txt","r")
            rd=fil.read()
            root = Tk()
            root.wm_title("Player Information")
            T = Text(root, height=20, width=100)
            T.pack()
            T.insert(END, rd)
            Button(root, text='Quit', command=bye).pack(fill=X)
            mainloop()
        elif self.L==f5:
            fil=open("jeremy mathieu.txt","r")
            rd=fil.read()
            root = Tk()
            root.wm_title("Player Information")
            T = Text(root, height=20, width=100)
            T.pack()
            T.insert(END, rd)
            Button(root, text='Quit', command=bye).pack(fill=X)
            mainloop()
        elif self.L==a1:
            fil=open("javier mascherano.txt","r")
            rd=fil.read()
            root = Tk()
            root.wm_title("Player Information")
            T = Text(root, height=20, width=100)
            T.pack()
            T.insert(END, rd)
            Button(root, text='Quit', command=bye).pack(fill=X)
            mainloop()
        elif self.L==a2:
            fil=open("lionel messi.txt","r")
            rd=fil.read()
            root = Tk()
            root.wm_title("Player Information")
            T = Text(root, height=20, width=100)
            T.pack()
            T.insert(END, rd)
            Button(root, text='Quit', command=bye).pack(fill=X)
            mainloop()
        elif self.L==c1:
            fil=open("luka modric.txt","r")
            rd=fil.read()
            root = Tk()
            root.wm_title("Player Information")
            T = Text(root, height=20, width=100)
            T.pack()
            T.insert(END, rd)
            Button(root, text='Quit', command=bye).pack(fill=X)
            mainloop()
        elif self.L==c2:
            fil=open("mateo kovacic.txt","r")
            rd=fil.read()
            root = Tk()
            root.wm_title("Player Information")
            T = Text(root, height=20, width=100)
            T.pack()
            T.insert(END, rd)
            Button(root, text='Quit', command=bye).pack(fill=X)
            mainloop()
        elif self.L==c3:
            fil=open("ivan rakitic.txt","r")
            rd=fil.read()
            root = Tk()
            root.wm_title("Player Information")
            T = Text(root, height=20, width=100)
            T.pack()
            T.insert(END, rd)
            Button(root, text='Quit', command=bye).pack(fill=X)
            mainloop()
        elif self.L==g1:
            fil=open("toni kroos.txt","r")
            rd=fil.read()
            root = Tk()
            root.wm_title("Player Information")
            T = Text(root, height=20, width=100)
            T.pack()
            T.insert(END, rd)
            Button(root, text='Quit', command=bye).pack(fill=X)
            mainloop()
        elif self.L==g2:
            fil=open("ter stegan.txt","r")
            rd=fil.read()
            root = Tk()
            root.wm_title("Player Information")
            T = Text(root, height=20, width=100)
            T.pack()
            T.insert(END, rd)
            Button(root, text='Quit', command=bye).pack(fill=X)
            mainloop()
        elif self.L==o1:
            fil=open("keylor navas.txt","r")
            rd=fil.read()
            root = Tk()
            root.wm_title("Player Information")
            T = Text(root, height=20, width=100)
            T.pack()
            T.insert(END, rd)
            Button(root, text='Quit', command=bye).pack(fill=X)
            mainloop()
        elif self.L==o2:
            fil=open("james rodriguez.txt","r")
            rd=fil.read()
            root = Tk()
            root.wm_title("Player Information")
            T = Text(root, height=20, width=100)
            T.pack()
            T.insert(END, rd)
            Button(root, text='Quit', command=bye).pack(fill=X)
            mainloop()
        elif self.L==o3:
            fil=open("gareth bale.txt","r")
            rd=fil.read()
            root = Tk()
            root.wm_title("Player Information")
            T = Text(root, height=20, width=100)
            T.pack()
            T.insert(END, rd)
            Button(root, text='Quit', command=bye).pack(fill=X)
            mainloop()
        elif self.L==o4:
            fil=open("mariano diaz.txt","r")
            rd=fil.read()
            root = Tk()
            root.wm_title("Player Information")
            T = Text(root, height=20, width=100)
            T.pack()
            T.insert(END, rd)
            Button(root, text='Quit', command=bye).pack(fill=X)
            mainloop()
        elif self.L==o5:
            fil=open("jasper.txt","r")
            rd=fil.read()
            root = Tk()
            root.wm_title("Player Information")
            T = Text(root, height=20, width=100)
            T.pack()
            T.insert(END, rd)
            Button(root, text='Quit', command=bye).pack(fill=X)
            mainloop()
        elif self.L==o6:
            fil=open("arda turan.txt","r")
            rd=fil.read()
            root = Tk()
            root.wm_title("Player Information")
            T = Text(root, height=20, width=100)
            T.pack()
            T.insert(END, rd)
            Button(root, text='Quit', command=bye).pack(fill=X)
            mainloop()
        elif self.L==o7:
            fil=open("luis suarez.txt","r")
            rd=fil.read()
            root = Tk()
            root.wm_title("Player Information")
            T = Text(root, height=20, width=100)
            T.pack()
            T.insert(END, rd)
            Button(root, text='Quit', command=bye).pack(fill=X)
            mainloop()
    def game (self):
        self.start()
        self.team()
        self.country()
        self.position()
        self.age()
        self.same()
        self.select()
        
            
                


aj=AKINATOR()
aj.game()










  
        
        
        
    
        
