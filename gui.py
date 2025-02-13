from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import numpy as np
#from my_utils import 

def run_hangman():
  # Create New Window
  top = Toplevel()
  top.title("HangMan")
  top.geometry("800x600")
  top.resizable(width=False, height=False)
  frame = create_frame(top)
  frame.pack()

def reset_all(frame, master):
  frame.destroy()
  frame = create_frame(master)
  frame.pack()

def create_frame(master):
  top = LabelFrame(master)
  # Create Frames for display and text buttons
  display = LabelFrame(top)
  display.pack()
  game = LabelFrame(top)
  game.pack()

  # Options buttons
  options = LabelFrame(top)
  options.pack()

  global guessed, word, numWrong
  guessed = ''
  word = ''
  numWrong = 0
  # Get random word from list
  fp = open(r"assets/files/hangman/wordlist.txt", 'r')
  lines = fp.readlines()
  line = np.random.randint(0, len(lines))
  word = lines[line]
  fp.close()
  # Create variable to store and display letters guessed
  for x in range(1, len(word)):
    if x == len(word) - 1:
      guessed += '_'
    else:
      guessed += '_  '

  # Display Default HangMan image
  img0 = ImageTk.PhotoImage(Image.open("assets/images/hangman/0.png"))
  render_image = Label(display, image=img0)
  render_image.image = img0
  render_image.grid(row=0, column=0)

  # Display Empty word to guess
  global word_display
  word_display = Label(display, text=guessed, font=('Arial', 20, 'bold'), padx=10, pady=10)
  word_display.grid(row=1, column=0)

  # Reset the gameDriver
  reset_btn = Button(options, text="Reset", command=lambda: reset_all(top, master))
  reset_btn.pack()

  # Keyboard
  #Q = Button(game, text='Q', padx=10, pady=5, foreground='black', command=lambda: guess_letter('q', Q))

  return top

if False:
    root = Tk()
    root.title("Home")
    root.geometry("400x400")
    root.resizable(width=False, height=False)

    main_frame = LabelFrame(root, pady=40, padx=40)
    main_frame.pack()
    main_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
    home_title = Label(main_frame, text="Select Game", font=('Arial', 40, 'bold'))
    home_title.grid(row=0, column=0, columnspan=2, pady=(0, 10))
    hangMan_btn = Button(main_frame, text="HangMan", font=('Arial', 20, 'bold'), command=run_hangman)
    hangMan_btn.grid(row=1, column=0, pady=10, ipadx=6, ipady=5)
    sudoku_btn = Button(main_frame, text="Sudoku", font=('Arial', 20, 'bold'), command=run_sudoku)
    sudoku_btn.grid(row=1, column=1, pady=10, ipadx=10, ipady=5)

    root.mainloop()