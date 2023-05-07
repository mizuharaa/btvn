import tkinter as tk
from tkinter import ttk
#Window initialize
window = tk.Tk()
window.title('Mutiple choice programme')
window.geometry('900x700')
window.resizable(False,False)

#Font
font = ('Times New Roman', 22)
sfont = ('Helvetica', 22)

lbframe_question = tk.LabelFrame(window, text = 'Questions', font = font, fg = 'blue')
lbframe_question.pack()
text_question = tk.Text(master = lbframe_question, font = font, fg = 'green', height = 6)
text_question.pack(fill='both', expand=True, padx = 5 , pady = 5)

lbframe_options = tk.LabelFrame(master = window, text = 'Answers/Choices', font = sfont, fg = 'blue')
lbframe_options.pack(fill = 'both', expand=True)

#Answer 1
ans1_text = tk.Text(master = lbframe_options, font = font, fg = 'black', height = 4, width = 18, borderwidth = 2, relief='groove')
ans1_text.grid(column = 1, row = 1, padx = 10, pady = 10)
ans1_cbttn = tk.Checkbutton(master = lbframe_options, text = 'A', font = font, height = 2, width = 3, borderwidth = 2, relief = 'groove')
ans1_cbttn.grid(column = 0, row = 1, padx = 10, pady = 10)

#Answer 2
ans2_text = tk.Text(master = lbframe_options, font = font, fg = 'black', height = 4, width = 18, borderwidth = 2, relief='groove')
ans2_text.grid(column = 7, row = 1, padx = 20, pady = 10)
ans2_cbttn = tk.Checkbutton(master = lbframe_options, text = 'B', font = font, height = 2, width = 3, borderwidth = 2, relief = 'groove')
ans2_cbttn.grid(column = 6, row = 1, padx = 20, pady = 10)

#Answer 3
ans3_text = tk.Text(master = lbframe_options, font = font, fg = 'black', height = 4, width = 18, borderwidth = 2, relief='groove')
ans3_text.grid(column = 1, row = 2, padx = 10, pady = 10)
ans3_cbttn = tk.Checkbutton(master = lbframe_options, text = 'C', font = font, height = 2, width = 3, borderwidth = 2, relief = 'groove')
ans3_cbttn.grid(column = 0, row = 2, padx = 10, pady = 10)

#Answer 4
ans4_text = tk.Text(master = lbframe_options, font = font, fg = 'black', height = 4, width = 18, borderwidth = 2, relief='groove')
ans4_text.grid(column = 7, row = 2, padx = 20, pady = 10)
ans4_cbttn = tk.Checkbutton(master = lbframe_options, text = 'D', font = font, height = 2, width = 3, borderwidth = 2, relief = 'groove')
ans4_cbttn.grid(column = 6, row = 2, padx = 20, pady = 10)

#Extra buttons
lbframe_extra = tk.LabelFrame(master = window, font = font, text = 'Functions', fg = 'blue')
lbframe_extra.pack(fill = 'both')

#Previous Function
photoprev_img = tk.PhotoImage(file = r'C:\Users\Daniel\Downloads\prevbut.png')
prev_button = tk.Button(master = lbframe_extra, text = 'Prev', image = photoprev_img, compound = 'left')
prev_button.grid(column = 1, row = 1, padx = 5, pady = 5)

#Next Function
photonext_img = tk.PhotoImage(file = r'C:\Users\Daniel\Downloads\nextbut.png')
next_button = tk.Button(master = lbframe_extra, text = 'Next', image = photonext_img, compound = 'right')
next_button.grid(column = 2, row = 1, padx = 5, pady = 5)

#Miscellaneous
finish_button = tk.Button(master = lbframe_extra, font = sfont, text = 'Nộp bài', fg = 'blue', height = 0, width = 10)
finish_button.place(x = 600, y = -12)
window.mainloop()