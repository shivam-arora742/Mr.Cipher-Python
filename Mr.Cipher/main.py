# Importing Modules:
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import os
import base64

# main_self.root function:
class main_screen:
    def __init__(self):
    
        # creating tkinter root object:
        self.root=Tk()
        
        # defining its  width & height (along with x,y coordinates for when it opens)
        # & background color:
        self.root.geometry("900x670+270+20")
        self.root.configure(bg="#8E8D8D")
        # header of self.root:
        self.root.title("Mr.Cipher - Encryption / Decryption Tool")
        
        # add header icon:
        # store image to variable
        head_icon=PhotoImage(file="D:\Python_Learning\Projects\Mr.Cipher\keys.png")
        # attach it on self.root with (False- dont add it on future projects , image_variable)
        self.root.iconphoto(False,head_icon)
                 
        # Label & Textbox for message:
        Label(text="Enter Text for Encryption / Decryption",font=("Raleway",20),fg="black",bg="#8E8D8D").place(x=220,y=25)
        textbx=Text(font="Roboto 15" , bg="white",relief=GROOVE,wrap=WORD,bd=3)
        textbx.place(x=150,y=65,width=600,height=70)
        
        
        # label & entry box for secret key:
        Label(text="Enter Secret Key for Encryption / Decryption ",font=("Raleway",16),fg="black",bg="#8E8D8D").place(x=220,y=170)
        code=StringVar()
        Entry(textvariable=code,width=37,bd=2,font=("arial 22"),show="*").place(x=150,y=200)
        
    
        # defining reset function:
        def reset():
            textbx.delete(1.0,END)
            t1.delete(1.0,END)
            l1.config(background="white",foreground="black")
            encrypt_frame.config(background="white")
            t2.delete(1.0,END)
            l2.config(background="white",foreground="black")
            decrypt_frame.config(background="white")
            code.set("")
            # resetting encrypted & decrypted frame's border:
            encrypt_frame.config(highlightcolor="black",highlightbackground="black")
            decrypt_frame.config(highlightcolor="black",highlightbackground="black")
        
        # defining encrypt & decrypt fuctions:
        def encrypt():
            # get the password:
            password=code.get()
            if(password=="Shivam03@"):
                #  encrypt the message:
                message=textbx.get(1.0,END)
                
                #  here first we convert whole text chara to ascii value &
                # then encode it base64 & then again convert from ascii to plain values
                encode_msg=message.encode("ascii")
                base64_bytes=base64.b64encode(encode_msg)
                encrypt_msg=base64_bytes.decode("ascii")
                
                # updating encrypted frame border's color:
                encrypt_frame.config(background="#C33200")
                l1.config(background="#C33200",foreground="white")
                t1.insert(END,encrypt_msg)
            
            # when no password input:
            elif password=="":
                messagebox.showerror("Encryption","Please Input Password!!")
            
            # for wrong password:
            elif password != "Shivam03@":
                messagebox.showerror("Encryption","Invalid Password!!")
                
                
        def decrypt():
            # get the password:
            password=code.get()
            if(password=="Shivam03@"):
                #  encrypt the message:
                message=textbx.get(1.0,END)
                
                #  here first we convert whole text chara to ascii value &
                # then encode it base64 & then again convert from ascii to plain values
                decode_msg=message.encode("ascii")
                base64_bytes=base64.b64decode(decode_msg)
                decrypt_msg=base64_bytes.decode("ascii")
                
                # updating encrypted frame border's color:
                decrypt_frame.config(background="#007861")
                l2.config(background="#007861",foreground="white")
                t2.insert(END,decrypt_msg)
            
            # when no password input:
            elif password=="":
                messagebox.showerror("Decryption","Please Input Password!!")
            
            # for wrong password:
            elif password != "Shivam03@":
                messagebox.showerror("Decryption","Invalid Password!!")
                
            # # updating decrypted frame border's color:
            #  decrypt_frame.config(highlightcolor="#007861",highlightbackground="#007861")
        
        #Buttons for Encrypt  & Decrypt & Reset:
        Button(text="ENCRYPT" , height="2",width=18,bg="#C33200", fg="white", bd=1.5 ,font="Raleway",command=encrypt).place(x=260,y=260) 
        Button(text="DECRYPT" , height="2",width=18,bg="#007861", fg="white", bd=1.5,font="Raleway",command=decrypt).place(x=500,y=260) 
        Button(text="RESET" , height="2",width=25,bg="black", fg="#FFD903", bd=1, font="Raleway" , command=reset).place(x=340,y=330) 
        
        # defining Encryption Frame:
        encrypt_frame=Frame(self.root,highlightbackground="black",background="white",highlightthickness=3,width=370,height=220)
        encrypt_frame.grid(row=0,column=0,padx=30,pady=400)
        l1=Label(encrypt_frame,text="Your Encrypted Text is here : ",font="Robote 14")
        l1.grid(row=0,column=0,padx=60,pady=100)
        # textbox for encrypted message:
        t1=Text(encrypt_frame,font="Robote 14",fg="black",relief=GROOVE,wrap=WORD,bd=4)
        t1.place(x=30,y=140,width=300,height=50)
            
        # defining Decryption Frame:
        decrypt_frame=Frame(self.root,highlightbackground="black",background="white",highlightthickness=3,width=400,height=220)
        decrypt_frame.grid(row=0,column=4,padx=50,pady=400)
        l2=Label(decrypt_frame,text="Your Decrypted Text is here : ",font="Robote 14")
        l2.grid(row=0,column=0,padx=60,pady=100)
        # textbox for encrypted message:
        t2=Text(decrypt_frame,font="Robote 14",fg="black",relief=GROOVE,wrap=WORD,bd=4)
        t2.place(x=30,y=140,width=300,height=50)
    
        # to open it indefinitely:
        self.root.mainloop()

if __name__=="__main__":
    # testing it:
    main_screen()