import builtins
from functools import partial
from tkinter import*
def calc():
    s=(inp.get())
    val=True
    num=0
    dec=[]
    i=0
    inval=['1010','1011','1100','1101','1110','1111']                   #list of invalid BCD numbers
    if s=="":
        val=""
    else:
        if len(s)%4!=0:                                                     #checks if the BCD number can be broken into groups of 4 bits
            val=False
        else:
            ls=[s[i:i+4] for i in range (0,len(s),4)]
            for i in ls:                                                    #checks if any invlaid BCD numbers are entered
                for j in inval:
                    if i==j:
                        val=False
                        break
    if val=="":
        st.config(background="Red")
        out.config(text="Entry Field can't be blank",background="Red",foreground="White") 
    elif val==True:
        for i in ls:
            try:
                dec.append(int(i,2))
            except:
                st.config(background="Red")
                out.config(text="Enter a BCD number",background="Red",foreground="White")                                           #converts the sting in ls to int and also appends the decimal equivalent in dec 
        ls=[]
        for i in dec:
            ls.append(str(i))
        num=int("".join(ls))
        st.config(background="Green")
        out.config(text="%X"%num,foreground="Black",background="Green")    #prints the result
    elif val==False:
        st.config(background="Red")
        out.config(text="Enter a Valid BCD number",background="Red",foreground="White")  
    return
window=Tk()
window.title("BCD to HEX converter")
window.geometry("500x350")
window.configure(bg="#76BED0")
lb=Label(window,text="BCD to Hexadecimal Converter",bg="#76BED0",font=("MS Reference Sans Serif",15)).place(relx=0.5,rely=0.12,anchor=CENTER)
inp=Entry(window)
inp.place(relx=0.5,rely=0.25,anchor=CENTER)
resultlabel=Label(window,text="Output",bg="#76BED0",font=("Product Sans",15)).place(relx=0.5,rely=0.37,anchor=CENTER)
st=Canvas(window,bg="White",height=30,width=500,highlightthickness=1,highlightbackground="Black")
st.place(x=0,y=150)
out=Label(window,background="white")
out.place(relx=0.5,y=165,anchor=CENTER)
cal=Button(window,text="Convert",font=("Product Sans",12),height=1,width=9,command=calc,background="White",foreground="Black",activebackground="#c8ff80",borderwidth=0,highlightthickness=0.5)
cal.place(relx=0.5,y=210,anchor=CENTER)
window.mainloop()
