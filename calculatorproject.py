from  tkinter import *
from  tkinter.messagebox import *

window= Tk()
font= ('Verdana', 22,'bold')
#important function

def clear():
    ex=textField.get()
    ex=ex[0:len(ex)-1]
    textField.delete(0,END)
    textField.insert(0,ex)


def all_clear():
    textField.delete(0,END)

#click function
def click_btn_function(event):
  print("btn clicked")
  b =event.widget
  text=b['text']
  print(text)


  if text=='x':
      textField.insert(END,"*")

      return





  if text=='=':
      try:
          ex=textField.get()
          anser = eval(ex)
          textField.delete(0, END)
          textField.insert(0,anser)
      except Exception as e:
          print("Error..",e)
          showerror("Error",e)



      return




  textField.insert(END,text)




window.geometry('500x300')
window.minsize(300,350)
window.title('MyCalculator')
#textfield
textField=Entry(window,font=font,width=44,justify=CENTER)
textField.pack(side=TOP,padx=10,pady=10,fill=X)
  #button
buttonFrame=Frame(window)
buttonFrame.pack(side=TOP)
#adding button
temp=1
for i in range(0,3):
    for j in range(0,3):
        btn=Button(buttonFrame,text=str(temp),font=font,width=4,pady=5,padx=5,relief='groove',activebackground='orange',activeforeground='black')
        btn.grid(row=i,column=j)
        temp=temp+1

        btn.bind('<Button-1>',click_btn_function)



        zeroBtn=Button(buttonFrame,text='0',font=font,width=4,pady=5,padx=5,relief='groove')
        zeroBtn.grid(row=3  ,column=0)

        dotBtn = Button(buttonFrame, text='.', font=font, width=4, pady=5, padx=5, relief='groove')
        dotBtn.grid(row=3, column=1)

        equalBtn = Button(buttonFrame, text='=', font=font, width=4, pady=5, padx=5, relief='groove')
        equalBtn.grid(row=3, column=2)

        plusBtn = Button(buttonFrame, text='+', font=font, width=4, pady=5, padx=5, relief='groove')
        plusBtn.grid(row=0, column=3)

        minuslBtn = Button(buttonFrame, text='-', font=font, width=4, pady=5, padx=5, relief='groove')
        minuslBtn.grid(row=1, column=3)

    multiBtn = Button(buttonFrame, text='x', font=font, width=4, pady=5, padx=5, relief='groove')
    multiBtn.grid(row=2, column=3)

    devBtn = Button(buttonFrame, text='/', font=font, width=4, pady=5, padx=5, relief='groove')
    devBtn.grid(row=3, column=3)

    clrBtn = Button(buttonFrame, text='<--', font=font, width=11, pady=5, padx=5, relief='groove',command=clear)
    clrBtn.grid(row=4, column=0 ,columnspan=2)

    allclrBtn = Button(buttonFrame, text='AC', font=font, width=11, pady=5, padx=5, relief='groove',command=all_clear)

    allclrBtn.grid(row=4, column=2 ,columnspan=2,)





#binding all btn
zeroBtn.bind('<Button-1>',click_btn_function)
devBtn.bind('<Button-1>',click_btn_function)
equalBtn.bind('<Button-1>',click_btn_function)
plusBtn.bind('<Button-1>',click_btn_function)
minuslBtn.bind('<Button-1>',click_btn_function)
multiBtn.bind('<Button-1>',click_btn_function)
devBtn .bind('<Button-1>',click_btn_function)




window.mainloop()