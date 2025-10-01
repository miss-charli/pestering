import tkinter as tk
import popup

#Time in between popup windows in ms
idleTime = 1000

#Boolean flag to see if popups should be generated
boolPopup = False

def idle_time_update(value):

    global idleTime
    #Convert to seconds
    idleTime = (value * 1000)

def start_popup():
    global boolPopup
    boolPopup = True

def stop_popup():
    global boolPopup
    boolPopup = False

#Root window
settings_gui = tk.Tk()

titleLabel = tk.Label(settings_gui, text="Settings")
titleLabel.pack()

startButton = tk.Button(settings_gui, text="Start", command=start_popup)
startButton.pack()

stopButton = tk.Button(settings_gui, text="Stop", command=stop_popup)
stopButton.pack()

idleTimeLabel = tk.Label(settings_gui, text="Idle Time")
idleTimeLabel.pack()

idleTimeSlider = tk.Scale(settings_gui, orient="horizontal", from_=10, to=3600, label="Idle Time", command=idle_time_update)
idleTimeSlider.pack()

settings_gui.after(idleTime, popup.popup, settings_gui,"Subject","Demo","A",["A","B","C","D"])

settings_gui.mainloop()