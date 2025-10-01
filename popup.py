import tkinter as tk
from functools import partial

correct_answer = ""

def success(popup,questionLabel):
    questionLabel["text"] = "Correct! Good Job!"
    popup.after(1000, popup.destroy)

def wrong(popup):
    wrong_notice = tk.Toplevel(popup)
    wrongLabel = tk.Label(wrong_notice, text="Wrong answer")
    wrongLabel.pack()
    wrong_notice.mainloop()
    pass

def check_answer(answer, popup, questionLabel):
    global correct_answer
    print("E IS EQUAL TO:" + answer)
    if correct_answer == answer:
        success(popup, questionLabel)
    else:
        wrong(popup)

def popup(root,subject, question,answer,answer_options):
    global correct_answer
    correct_answer = answer
    popup = tk.Toplevel(root)
    popup.title(subject)
    questionLabel = tk.Label(popup,text="Question:"+question)
    questionLabel.pack()
    optionButton = []
    optionButtonCount = 0
    for option in answer_options:
        optionButton.append(tk.Button(popup,text=option))
        print("THE CURRENT OPTION IS: " + str(optionButtonCount))
        optionButton[optionButtonCount].pack()
        optionButton[optionButtonCount].config(command=partial(check_answer, option, popup, questionLabel))
        optionButtonCount += 1
    popup.mainloop()
    pass