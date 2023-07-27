# Let's import the tkinter module to create GUIs
import tkinter as tk

# Let's see what is inside the tkinter directory
# print(dir(tk))

# Let's create a empty GUI / root GUI
root = tk.Tk()

# let' define the function 
def add():
    print('Adding the task to the list')
   
    # let's get the text written inside the entry widget
    data = entry.get()

    # let's check first if data is empty or not
    if data:
        # shift that text to listbox
        # arguments : index number (0 --> First element), data you want put
        # task_list.insert(0, data)
        task_list.insert(tk.END,data)
    
        # let's clean the entry widget
        entry.delete(0, tk.END)

def delete():
    print('Deleting task from the list')  

    # let's delete the active element from the list
    task_list.delete(tk.ACTIVE)


# let's define the width & height of GUI
root.geometry('400x400') 

# let's fixed the size of gui by passing false value in width and height of gui
root.resizable(width=False, height=False)

# let' change the title
root.title('To Do List')

# let's add entry widget 
entry = tk.Entry(root , bg ='pink')
entry.pack(padx=30, pady=10, fill='x')

# let's add a button-----> add task 
# In command parameter, we only put the function name
add_button = tk.Button(root,text='Add Task', width=20, bg='purple', fg='black',command=add)
add_button.pack()

# let's add the task list
task_list = tk.Listbox(root, bg ='pink')
task_list.pack(fill='x',padx = 20, pady = 10 )


# let's add the delete button 
delete_button = tk.Button(root,text='Delete Task', width=20, bg ='#7eafac',command=delete)
delete_button.pack()

# lets call the mainloop function
# It display's the GUI continuously and it listen for any event of GUI
root.mainloop()