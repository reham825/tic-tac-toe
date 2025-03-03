import random
from tkinter import *
def clicked(r, c):
    global player

    if buttons[r][c]['text'] == "" and checkwinner() != True:
        buttons[r][c]['text'] = player
        if player == 'X':
            player = 'O'
        else:
            player = 'X'
        turn_message.config(text=f"{player} player turn")
    checkwinner()
    
def checkwinner():
    for i in range(3):
        if buttons[i][0]['text'] == buttons[i][1]['text'] == buttons[i][2]['text'] != '':
            turn_message.config(
                text=f"{buttons[i][0]['text']} win")
            return True
        elif buttons[0][i]['text'] == buttons[1][i]['text'] == buttons[2][i]['text'] != '':
            turn_message.config(
                text=f"{buttons[0][i]['text']} win")
            return True
        elif buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != '':
            turn_message.config(
                text=f"{buttons[0][0]['text']} win")
            return True
        elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != '':
            turn_message.config(
                text=f"{buttons[0][2]['text']} win")
            return True






window=Tk()
message_frame = Frame(master=window)
message_frame.pack()
turn_message = Label(master=message_frame, text="Ready?????")
turn_message.pack()
button_frame = Frame(master=window)
button_frame.pack()
players = ["X", "O"]
player = random.choice(players)
buttons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

for row in range(3):
    # buttons[row][col].rowconfigure(row, weight=1, minsize=50)
    # buttons[row][col].columnconfigure(row, weight=1, minsize=50)
    for col in range(3):
        buttons[row][col] = Button(master=button_frame,
                                   text="",
                                   width=5,
                                   height=2,
                                   relief="solid",
                                   padx=10,
                                   pady=10,
                                   command=lambda r=row, c=col: clicked(r, c))
        buttons[row][col].grid(row=row, column=col)
window.mainloop()
