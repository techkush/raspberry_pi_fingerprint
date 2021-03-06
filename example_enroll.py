import Tkinter as tk
import sys
import hashlib
import time
from pyfingerprint.pyfingerprint import PyFingerprint
import requests
import json

# "1366x768"
window_size = "480x320"
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
    
    tk.Button(lec_fing, text="Touch", command=lec_database).pack()
    
    root.withdraw()


# Get data from lecturer database
def lec_database():
    f = in_sensor()
    try:
        print('Waiting for finger...')
        while ( f.readImage() == False ):
            pass
        f.convertImage(0x01)
        result = f.searchTemplate()
        positionNumber = result[0]
        accuracyScore = result[1]
        if ( positionNumber == -1 ):
            print('No match found!')

	    lec_fing()

        else:
            print('Found template at position #' + str(positionNumber))
            print('The accuracy score is: ' + str(accuracyScore))
        f.loadTemplate(positionNumber, 0x01)
        characterics = str(f.downloadCharacteristics(0x01)).encode('utf-8')
        print('SHA-2 hash of template: ' + hashlib.sha256(characterics).hexdigest())

	payloads = { 'method': 1, 'fingprint': hashlib.sha256(characterics).hexdigest() }
	r = requests.post('http://192.168.1.8:3000', json = payloads)
	req_text = r.text
	data = json.loads(req_text)

	print(data['name'])

	sub_sel(data['name'])

    except Exception as e:
        print('Operation failed!')
        print('Exception message: ' + str(e))

# Select Subjects ---
def sub_sel(lec_name):
    sub_sel = tk.Toplevel()
    sub_sel.title("SLIIT - Select Subject")
    sub_sel.geometry(window_size)

    tk.Label(sub_sel, text = "Selct the subject").pack()
    tk.Label(sub_sel, text = "Lecturer name : " + lec_name).pack()
    tk.Button(sub_sel, text="Industrial Management and marketing", command = lambda: save_sub("im_mm", lec_name)).pack()
    tk.Button(sub_sel, text="Foundation of digital design", command = lambda: save_sub("fo_dd", lec_name)).pack()
    tk.Button(sub_sel, text="Industrial Engineering", command = lambda: save_sub("in_en", lec_name)).pack()
    tk.Button(sub_sel, text="Production and operations managemnt", command = lambda: save_sub("po_am", lec_name)).pack()


# save subject to the text file ---
def save_sub(subject, lec_name):
    print(subject)
    wek_sel(subject, lec_name)


# Select week number
def wek_sel(subject, lec_name):
    wek_sel = tk.Toplevel()
    wek_sel.title("SLIIT - Select Week Number")
    wek_sel.geometry(window_size)
    
    tk.Label(wek_sel, text = "Selct the Week number").pack()
    tk.Label(wek_sel, text = "Lecturer name : " + lec_name).pack()
    tk.Button(wek_sel, text="Week 01", command = lambda: save_wek("week1", subject, lec_name)).pack()
    tk.Button(wek_sel, text="Week 02", command = lambda: save_wek("week2", subject, lec_name)).pack()
    tk.Button(wek_sel, text="Week 03", command = lambda: save_wek("week3", subject, lec_name)).pack()
    tk.Button(wek_sel, text="Week 04", command = lambda: save_wek("week4", subject, lec_name)).pack()
    tk.Button(wek_sel, text="Week 05", command = lambda: save_wek("week5", subject, lec_name)).pack()
    tk.Button(wek_sel, text="Week 06", command = lambda: save_wek("week6", subject, lec_name)).pack()

# save subject to the text file ---
def save_wek(week, subject, lec_name):
    print(week)
    mark_att(week, subject, lec_name, "--- Place your finger ---")

def mark_att(week, subject, lec_name, message):
    mark_att = tk.Toplevel()
    mark_att.title("SLIIT - Mark Attendance")
    mark_att.geometry(window_size)

    
    if subject == "im_mm":
	sub = "Industrial Management and marketing"
    if subject == "fo_dd":
	sub = "Foundation of digital design"
    if subject == "in_en":
	sub = "Industrial Engineering"
    if subject == "po_am":
	sub = "Production and operations managemnt"


    tk.Label(mark_att, text = "Lecturer name : " + lec_name).pack()  
    tk.Label(mark_att, text = "Subject : " + sub).pack()
    tk.Label(mark_att, text = "Week : " + week).pack()  
    tk.Label(mark_att, text = message).pack()  

    tk.Button(mark_att, text="Touch", command= lambda: mark_attendance(week, subject, lec_name)).pack()
    tk.Button(mark_att, text="Exit", command=sys.exit).pack()

# Mark attendance
def mark_attendance(week, subject, lec_name):
    f = in_sensor()
    try:
        print('Waiting for finger...')
        while ( f.readImage() == False ):
            pass
        f.convertImage(0x01)
        result = f.searchTemplate()
        positionNumber = result[0]
        accuracyScore = result[1]
        if ( positionNumber == -1 ):
            print('No match found!')

	    mark_att(week, subject, lec_name, "--- No student ---")

        else:
            print('Found template at position #' + str(positionNumber))
            print('The accuracy score is: ' + str(accuracyScore))
        f.loadTemplate(positionNumber, 0x01)
        characterics = str(f.downloadCharacteristics(0x01)).encode('utf-8')
        print('SHA-2 hash of template: ' + hashlib.sha256(characterics).hexdigest())

	payloads = { 'method': 2, 'fingprint': hashlib.sha256(characterics).hexdigest(), 'subject': subject, 'week': week }
	r = requests.post('http://192.168.1.8:3000', json = payloads)

	req_text = r.text
	data = json.loads(req_text)

	print(data['id'])
	print(data['name'])
	
	mark_att_con(data['id'], data['name'], week, subject, lec_name, " ")

    except Exception as e:
        print('Operation failed!')
        print('Exception message: ' + str(e))

def mark_att_con(id, name, week, subject, lec_name, message):
    mark_att_con = tk.Toplevel()
    mark_att_con.title("SLIIT - Mark Attendance")
    mark_att_con.geometry(window_size)

    tk.Label(mark_att_con, text = "ID : " + id).pack()  
    tk.Label(mark_att_con, text = "Name : " + name).pack()
    tk.Button(mark_att_con, text="Okay", command= lambda: mark_att(week, subject, lec_name, "--- Place your finger ---")).pack()
    

# Initialize Sensor
def in_sensor():
    try:
        f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)
        if (f.verifyPassword() == False):
            raise ValueError('The given fingerprint sensor password is wrong!')
        return f
    except Exception as e:
        print('The fingerprint sensor could not be initialized!')
        print('Exception message: ' + str(e))
        exit(1)

    print('Currently used templates: ' + str(f.getTemplateCount()) +
        '/' + str(f.getStorageCapacity()))
    
tk.Button(root, text="Administrator", command=lec_fing).pack()
tk.Button(root, text="Student Registration", command=stu_reg).pack()

root.mainloop()