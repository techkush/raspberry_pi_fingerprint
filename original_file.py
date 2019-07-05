import tkinter as tk
import sys

window_size = "1366x768"
# --------------------------------
root = tk.Tk()
root.title("SLIIT -  Main Menu")
root.geometry(window_size) 
# --------------------------------

# Student Registration ---
def stu_reg():
    stu_reg = tk.Toplevel(root)
    stu_reg.title("SLIIT - Student Registration")
    stu_reg.geometry(window_size)


    root.withdraw()

# Administrator window ---
def lec_fing():
    lec_fing = tk.Toplevel()
    lec_fing.title("SLIIT - Lecturer Login")
    lec_fing.geometry(window_size)


    tk.Button(lec_fing, text="Sub select", command=sub_sel).pack()
    root.withdraw()

# Select Subjects ---
def sub_sel():
    sub_sel = tk.Toplevel()
    sub_sel.title("SLIIT - Select Subject")
    sub_sel.geometry(window_size)

    tk.Label(sub_sel, text = "Selct the subject").pack()
    tk.Button(sub_sel, text="Sub 01", command = lambda: save_sub("sub01")).pack()
    tk.Button(sub_sel, text="Sub 02", command = lambda: save_sub("sub02")).pack()
    tk.Button(sub_sel, text="Sub 03", command = lambda: save_sub("sub03")).pack()
    tk.Button(sub_sel, text="Sub 04", command = lambda: save_sub("sub04")).pack()


# save subject to the text file ---
def save_sub(subject):
    print(subject)

    f = open("database/subject.txt", "w")
    f.write(subject)
    f.close()

    wek_sel()


# Select week number
def wek_sel():
    wek_sel = tk.Toplevel()
    wek_sel.title("SLIIT - Select Week Number")
    wek_sel.geometry(window_size)
    
    tk.Label(wek_sel, text = "Selct the Week number").pack()
    tk.Button(wek_sel, text="Week 01", command = lambda: save_wek("week01")).pack()
    tk.Button(wek_sel, text="Week 02", command = lambda: save_wek("week02")).pack()
    tk.Button(wek_sel, text="Week 03", command = lambda: save_wek("week03")).pack()
    tk.Button(wek_sel, text="Week 04", command = lambda: save_wek("week04")).pack()
    tk.Button(wek_sel, text="Week 05", command = lambda: save_wek("week05")).pack()
    tk.Button(wek_sel, text="Week 06", command = lambda: save_wek("week06")).pack()

# save subject to the text file ---
def save_wek(week):
    print(week)
    f = open("database/weeknum.txt", "w")
    f.write(week)
    f.close()

    mark_att()

def mark_att():
    mark_att = tk.Toplevel()
    mark_att.title("SLIIT - Mark Attendance")
    mark_att.geometry(window_size)


    tk.Button(mark_att, text="Exit", command=sys.exit).pack()


tk.Button(root, text="Administrator", command=lec_fing).pack()
tk.Button(root, text="Student Registration", command=stu_reg).pack()

root.mainloop()
