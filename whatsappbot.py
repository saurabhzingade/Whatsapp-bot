import tkinter as tk
from selenium import webdriver


driver = webdriver.Firefox()
driver.get('https://web.whatsapp.com/')    

def bot():
    
    name= e1.get()
    msg = e2.get()
    count = int(e3.get())
    msg_box=driver.find_element_by_class_name('_1Plpp')#msg box
    for i in range(count):
        msg_box.send_keys(msg)
        button= driver.find_element_by_class_name('_35EW6')
        button.click()
        
m=tk.Tk()
m.title('Whats App bomb')
m.geometry('300x200')

msg=tk.StringVar()
name = tk.StringVar()
count = tk.IntVar()

label1=tk.Label(m, text='Enter name of person or group')
label2=tk.Label(m, text='Enter message here')
label3 = tk.Label(m,text='No of times:')
e1=tk.Entry(m,textvariable=name)
e2=tk.Entry(m,textvariable=msg)
e3=tk.Entry(m,textvariable=count)
button1 = tk.Button(m,text='Send', width=15,command=bot)



label1.grid(row=0,column=0)
e1.grid(row=0,column=1)
label2.grid(row=1,column=0)
e2.grid(row=1,column=1)
label3.grid(row=2,column=0)
e3.grid(row=2,column=1)
button1.grid(row=3,column=1)


m.mainloop()

