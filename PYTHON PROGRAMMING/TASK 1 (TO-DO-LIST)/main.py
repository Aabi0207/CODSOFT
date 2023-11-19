# import everything from the tkinter module
from tkinter import *

# imports messagebox function form the tkinter module
from tkinter import messagebox


def newTask():
    """
        Create a function to create and add new tasks to the to-do list
    """
    task = my_entry.get()
    if task != "":
        with open(file=r"TASK 1 (TO-DO-LIST)\todos.txt", mode="a", encoding="UTF-8") as data_file:
            data_file.write(f"{task}\n")
        lb.insert(END, task)
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("warning", "Please enter some task.")


def deleteTask():
    """
        Deletes the tasks from teh to-do list
    """
    marked = lb.curselection()
    if marked:
        del_text = lb.get(marked)
        # Read the content of the file
        with open(r"TASK 1 (TO-DO-LIST)\todos.txt", 'r', encoding="utf-8") as file:
            lines = file.readlines()

        # Remove the specified line
        lines = [line for line in lines if line != del_text]

        # Write the modified content back to the file
        with open(r"TASK 1 (TO-DO-LIST)\todos.txt", 'w', encoding="utf-8") as file:
            file.writelines(lines)

    lb.delete(ANCHOR)


def mark_task():
    """
        Marks the task as complete by adding the tick mark above the selected task
    """
    marked=lb.curselection()
    if marked:
        temp=marked[0]
        #store the text of selected item in a string
        task=lb.get(marked)
        #update it 
        temp_marked=task+" ✔"
        #delete it then insert it 

        with open(r"TASK 1 (TO-DO-LIST)\todos.txt", 'r', encoding="utf-8") as file:
            lines = file.readlines()

        # Remove the specified line
        lines = [line for line in lines if line.strip() != task]
        lines.append(f"{temp_marked}\n")

        # Write the modified content back to the file
        with open(r"TASK 1 (TO-DO-LIST)\todos.txt", 'w', encoding="utf-8") as file:
            file.writelines(lines)
        lb.delete(temp)
        lb.insert(END, temp_marked)
    else:
        messagebox.showwarning("Warning", "Please first selct a task.")


# Create a window to display everything 
ws = Tk()
ws.geometry('550x550+500+200')
ws.title('PythonGuides')
ws.config(bg='#BE3144')
ws.resizable(width=False, height=False)

# Create a frame which will hold the list box and a scrollbar within it
frame = Frame(ws)
frame.pack(pady=10)

# Create a list box
lb = Listbox(
    frame,
    width=25,
    height=8,
    font=('Times', 18),
    bd=0,
    fg='#464646',
    highlightthickness=0,
    selectbackground='#a6a6a6',
    activestyle="none",
    bg="#F1EAFF"
)
lb.pack(side=LEFT, fill=BOTH)

# Create a scrollbar which will go on the right side of the frame which we will use to scroll in y direction
sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

with open(r"TASK 1 (TO-DO-LIST)\todos.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

for line in lines:
    lb.insert(END, line)

# Create an entry field where we can type the tasks of our choice 
my_entry = Entry(
    ws,
    font=('times', 24),
    )

my_entry.pack(pady=20)

# Create an another frame to hold the add task and delete task button
button_frame = Frame(ws)
button_frame.pack(pady=20)

# Create the required buttons
addTask_btn = Button(
    button_frame,
    text='Add Task',
    font=('times 14'),
    bg='#c5f776',
    padx=20,
    pady=10,
    command=newTask
)
addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

delTask_btn = Button(
    button_frame,
    text='Delete Task',
    font=('times 14'),
    bg='#ff8b61',
    padx=20,
    pady=10,
    command=deleteTask
)
delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

# Create another frame which will hold a button to mark the task to be compleated
mark_complete_frame = Frame(ws)
mark_complete_frame.pack(pady=20)

mark_complete_button = Button(
    mark_complete_frame,
    text='Mark as Complete',
    font=('times 14'),
    bg='#83A2FF',
    padx=20,
    pady=10,
    command=mark_task
)
mark_complete_button.pack(fill=BOTH, expand=True)

# Mainloop function stops the screen from disappearing
ws.mainloop()