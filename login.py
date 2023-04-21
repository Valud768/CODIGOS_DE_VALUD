from tkinter import *						
import tkinter as tk
from tkinter import messagebox as mb
import sqlite3		

conn=sqlite3.connect('login.db')
c=conn.cursor()

def create_table():
	c.execute("CREATE TABLE IF NOT EXISTS usuarios(Nombre TEXT,Apellido TEXT ,Usuario TEXT,Pass TEXT)")
	conn.commit()
	c.close()
	conn.close()

create_table()


ventana=tk.Tk()
ventana.title("_Mi primer Login_")	
ventana.geometry("280x450+300+250")	
	
color='#c5e2f6'			
ventana['bg']=color		

Label(ventana,bg=color,text="Login").pack()

Label(ventana,text="Usuario : ",bg=color).pack()	
caja1=Entry(ventana)										
caja1.pack()																
Label(ventana,text="Contraseña : ",bg=color).pack()	
caja2=Entry(ventana,show="*")												
caja2.pack()							

db=sqlite3.connect('login.db')		
c=db.cursor()

def login():				
	usuario=caja1.get()		
	contr=caja2.get()		
	c.execute('SELECT * FROM usuarios WHERE Usuario = ? AND Pass = ?',(usuario,contr))
	if c.fetchall():
		mb.showinfo(title="Login Correcto",message="Usuario y contraseña correctos")		
	else:
		mb.showerror(title="Login incorrecto",message="Usuario o contraseña incorrecto")	
	
def nuevaVentana():							
	newVentana=tk.Toplevel(ventana)			
	newVentana.title("Registro de Usuario")	
	newVentana.geometry("300x290+800+250")	
	newVentana['bg']=color					
	
	labeExample=tk.Label(newVentana,text="Registro : ").pack	
	Label(newVentana,text="Nombre : ").pack()		
	caja3=Entry(newVentana)															
	caja3.pack()
	Label(newVentana,text="Apellidos : ").pack()	
	caja4=Entry(newVentana)															
	caja4.pack()
	Label(newVentana,text="Usuario : ").pack()		
	caja5=Entry(newVentana)															
	caja5.pack()
	Label(newVentana,text="Contraseña : ").pack()	
	caja6=Entry(newVentana,show="*")												
	caja6.pack()	
	Label(newVentana,text="Repita la Contraseña : ").pack()	
	caja7=Entry(newVentana,show="*")															 
	caja7.pack()
	def registro():				
		Nombre=caja3.get()		
		Apellido=caja4.get()	
		Usr_reg=caja5.get()		
		Contra_reg=caja6.get()	
		Contra_reg_2=caja7.get() 
		if(Contra_reg==Contra_reg_2):		
			
			c.execute("INSERT INTO usuarios values(\'"+Nombre+"\',\'"+Apellido+"\',\'"+Usr_reg+"\',\'"+Contra_reg+"')")
			db.commit()			
			mb.showinfo(title="Registro Correcto",message="Hola "+Nombre+" "+Apellido+" ¡¡ \nSu registro fue exitoso.")
			newVentana.destroy()		
		else:	
			mb.showerror(title="Contraseña Incorrecta",message="Error¡¡¡ \nLas contraseñas no coinciden.")
    
	buttons=tk.Button(newVentana,text="Registrar ¡",command=registro,bg=color).pack(side="bottom")


Label(ventana,text=" ",bg=color).pack()
Button(text=" ENTRAR ",command=login,bg='#a6d4f2').pack()
Label(ventana,text=" ",bg=color).pack()
Label(ventana,text="No tienes una cuenta ? : ",bg=color).pack()
boton1=Button(ventana,text="REGISTRO",bg='#a6d4f2',command=nuevaVentana).pack()


ventana.mainloop()