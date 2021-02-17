from tkinter import *
from tkinter import messagebox
from db import Database
#account name, email, sim, fiverr/paypal

db =  Database('store.db')

def populate_list():
    sim_list.delete(0, END)
    for row in db.fetch():
        # id = str(row[0]) + "        "
        # account = row[1] + "        "
        # email = row[2] + "      "
        # sim = row[3] + "        "
        # profile = row[4] + "        "
        # data = id + account + email + sim + profile
        sim_list.insert(END,row)    

def add_item():
    if account.get() == '' or email.get() == '' or sim.get() == '' or profile.get() == '':
        messagebox.showerror('Required Fields', 'Please include all fields')
        return
    db.insert(account.get(), email.get(), sim.get(), profile.get())
    sim_list.insert(END,account.get(), email.get(), sim.get(), profile.get())
    
    clear_text()
    populate_list()

def select_item(event):
    try:
        global selected_item
        index = sim_list.curselection()[0]
        selected_item = sim_list.get(index)
        
        account_entry.delete(0, END)
        account_entry.insert(END, selected_item[1])
        email_entry.delete(0, END)
        email_entry.insert(END, selected_item[2])
        sim_entry.delete(0, END)
        sim_entry.insert(END, selected_item[3])
        profile_entry.delete(0, END)
        profile_entry.insert(END, selected_item[4])
    except IndexError:
        pass

def remove_item():
    db.remove(selected_item[0])
    clear_text()
    populate_list()

def update_item(): 
    db.update(selected_item[0],account.get(), email.get(), sim.get(), profile.get())
    populate_list()

def clear_text():
    account_entry.delete(0, END)
    email_entry.delete(0, END)
    sim_entry.delete(0, END)
    profile_entry.delete(0, END)
    

# Create window Object
app = Tk()

# Account Name
account = StringVar()
account_label = Label(app,text='Account', font=('bold',14),pady=20)
account_label.grid(row=0,column=0, sticky=W)
account_entry = Entry(app, textvariable=account)
account_entry.grid(row=0,column=1)

# Email
email = StringVar()
email_label = Label(app,text='Email', font=('bold',14))
email_label.grid(row=0,column=2, sticky=W)
email_entry = Entry(app, textvariable=email)
email_entry.grid(row=0,column=3)

# Sim
sim = StringVar()
sim_label = Label(app,text='Sim', font=('bold',14))
sim_label.grid(row=1,column=0, sticky=W)
sim_entry = Entry(app, textvariable=sim)
sim_entry.grid(row=1,column=1)

# Profile
profile = StringVar()
profile_label = Label(app,text='Profile', font=('bold',14))
profile_label.grid(row=1,column=2, sticky=W)
profile_entry = Entry(app, textvariable=profile)
profile_entry.grid(row=1,column=3)

# Sim List(Listboc)
sim_list = Listbox(app, height=8, width=75, border=0)
sim_list.grid(row=3, column=0, columnspan=3, rowspan=6, pady=20, padx=20)

# Create scrollbar
scrollbar = Scrollbar(app)
scrollbar.grid(row=3,column=3)

# Attach scrollbar to Listbox
sim_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=sim_list.yview)

# Bind select
sim_list.bind('<<ListboxSelect>>',select_item)
# Buttons

add_btn = Button(app, text="Add Sim", width=12, command=add_item)
add_btn.grid(row=2,column=0,pady=20)

update_btn = Button(app, text="Update Sim", width=12, command=update_item)
update_btn.grid(row=2,column=1)

remove_btn = Button(app, text="Remove Sim", width=12, command=remove_item)
remove_btn.grid(row=2,column=2)

clear_btn = Button(app, text="Clear Input", width=12, command=clear_text)
clear_btn.grid(row=2,column=3)


app.title("Sim Manager")
app.geometry('700x350')


# Populate data

populate_list()

# Start program
app.mainloop()