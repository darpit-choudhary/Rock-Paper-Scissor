import tkinter as tk
import random
import time
import tkinter.messagebox as tmsg

root = tk.Tk()
root.geometry("600x500")
root.maxsize(600,500)
root.title("Rock Paper Scissor")
root.config(bg = 'seashell3')
#rock paper scissor list
lst = ['Rock', 'Paper', 'Scissor']


# define the reset and close function  
def reset():
    computer_display.delete(0,tk.END)
    result_display.delete(0,tk.END)
    user_display.delete(0, tk.END)

def close():
    ans = tmsg.askquestion("Exit", "Are you running away human?")
    if ans == 'yes':
        root.destroy()
    else:
        reset()
        
#define the play function 
def play():
    random_output = random.choice(lst)
    string1 = user_display.get()
    string = string1.capitalize()             # to make sure both lowercase and uppercase work
    computer_display.insert(0, random_output)
    time.sleep(1)
    if string == random_output:
       result_display.insert(0, 'Are you reading my mind, human?')
    elif string == 'Rock' and random_output == 'Paper':
       result_display.insert(0, 'Haha! to think a mere human would stand a chance against me')
    elif string == 'Rock' and random_output == 'Scissor':
        result_display.insert(0, "Damn human, you won't win next time")
    elif string == 'Paper' and random_output == 'Rock':
        result_display.insert(0, 'Haha! to think a mere human would stand a chance against me')
    elif string == 'Paper' and random_output == 'Scissor':
        result_display.insert(0, "Damn human, you won't win next time")
    elif string == 'Scissor' and random_output == 'Paper':
        result_display.insert(0, 'Haha! to think a mere human would stand a chance against me')
    elif string == 'Scissor' and random_output == 'Rock':
        result_display.insert(0, "Damn human, you won't win next time")
    else:
        result_display.insert(0, "Choose one from rock, paper or scissor")
        
        
#Headline and Blankline to create blank lines   
Blankline = tk.Label(root, bg = 'seashell3').pack()
Headline = tk.Label(root, text = "Rock Paper Scissor!!", font = 'comicalsansms 30 bold', bg = 'seashell3').pack()
Blankline = tk.Label(root, bg = 'seashell3').pack()

user = tk.Label(root, text = 'Human chose', font = 'luida 15', bg = 'seashell3').pack(side = 'top')
#entries
user_display = tk.Entry(root, font = 'georgia 15', bg = 'antiquewhite2')
user_display.pack(side = 'top', ipadx = 5)

Blankline = tk.Label(root, bg = 'seashell3').pack()

#Button
b=tk.Button(root, text = 'Go!!', font = 'lucida 15 bold', command = play, borderwidth = 5, relief = 'raised').pack()

#black linkes to create space
Blankline = tk.Label(root, bg = 'seashell3').pack()

computer = tk.Label(root, text = 'Advanced life form chose', font = 'luida 15', bg = 'seashell3').pack(side = 'top')
computer_display = tk.Entry(root, font = 'georgia 15', bg = 'antiquewhite2')
computer_display.pack(side = 'top')

#blank lines to create space
Blankline = tk.Label(root, bg = 'seashell3').pack()

#blank lines to create space
result = tk.Label(root, text = "Result", font = 'lucida 15', bg = 'seashell3').pack(side = 'top')
result_display = tk.Entry(root, font = 'georgia 15', bg = 'antiquewhite2')
result_display.pack(side = 'top', fill = 'x', padx = 15)

Blankline = tk.Label(root, bg = 'seashell3').pack()
#Reset and Exit button
b=tk.Button(root, text = 'Reset', font = 'lucida 15 bold', command = reset, borderwidth = 5, relief = 'raised').pack(padx = 20, side = 'left')
b=tk.Button(root, text = 'Exit', font = 'lucida 15 bold', command = close, borderwidth = 5, relief = 'raised').pack(padx = 20, side = 'right')

root.mainloop()