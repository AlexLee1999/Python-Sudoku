from tkinter import *
import random
import tkinter.messagebox


class sudoku(object):
    def __init__(self, que, ans, level, problem):
        self.riddle = que
        self.solution = ans
        self.your_ans = self.riddle
        self.level = level
        self.window = Tk()
        self.window.title('Solve')
        canvas = Canvas(self.window, width=110, height=20)
        canvas.pack()
        canvas.create_text(54, 12.5, text='Problem %d' % problem, font='Arial')
        f = Frame(self.window)
        f.pack()
        self.hint_list = []
        v = []
        k = 0
        for i in range(9):
            for j in range(9):
                if self.riddle[i][j] == 0:
                    self.hint_list.append([i, j])
                    v.append(StringVar())
        for i in range(9):
            for j in range(9):
                if self.riddle[i][j] != 0:
                    if 0 <= i <= 2 and 0 <= j <= 2:
                        Label(f, text=self.riddle[i][j], bg='black', fg='white', width=2, font='Arial').grid(row=i, column=j)
                    elif 6 <= i <= 8 and 0 <= j <= 2:
                        Label(f, text=self.riddle[i][j], bg='black', fg='white', width=2, font='Arial').grid(row=i, column=j)
                    elif 3 <= i <= 5 and 3 <= j <= 5:
                        Label(f, text=self.riddle[i][j], bg='black', fg='white', width=2, font='Arial').grid(row=i, column=j)
                    elif 0 <= i <= 2 and 6 <= j <= 8:
                        Label(f, text=self.riddle[i][j], bg='black', fg='white', width=2, font='Arial').grid(row=i, column=j)
                    elif 6 <= i <= 8 and 6 <= j <= 8:
                        Label(f, text=self.riddle[i][j], bg='black', fg='white', width=2, font='Arial').grid(row=i, column=j)
                    else:
                        Label(f, text=self.riddle[i][j], bg='white', fg='black', width=2, font='Arial').grid(row=i, column=j)
                else:
                    if 0 <= i <= 2 and 0 <= j <= 2:
                        self.riddle[i][j] = Entry(f, width=2, justify=RIGHT, relief=SUNKEN, textvariable=v[k], bg='black', fg='white', font='Arial')
                        self.riddle[i][j].grid(row=i, column=j)
                        k += 1
                    elif 6 <= i <= 8 and 0 <= j <= 2:
                        self.riddle[i][j] = Entry(f, width=2, justify=RIGHT, relief=SUNKEN, textvariable=v[k], bg='black', fg='white', font='Arial')
                        self.riddle[i][j].grid(row=i, column=j)
                        k += 1
                    elif 3 <= i <= 5 and 3 <= j <= 5:
                        self.riddle[i][j] = Entry(f, width=2, justify=RIGHT, relief=SUNKEN, textvariable=v[k], bg='black', fg='white', font='Arial')
                        self.riddle[i][j].grid(row=i, column=j)
                        k += 1
                    elif 0 <= i <= 2 and 6 <= j <= 8:
                        self.riddle[i][j] = Entry(f, width=2, justify=RIGHT, relief=SUNKEN, textvariable=v[k], bg='black', fg='white', font='Arial')
                        self.riddle[i][j].grid(row=i, column=j)
                        k += 1
                    elif 6 <= i <= 8 and 6 <= j <= 8:
                        self.riddle[i][j] = Entry(f, width=2, justify=RIGHT, relief=SUNKEN, textvariable=v[k], bg='black', fg='white', font='Arial')
                        self.riddle[i][j].grid(row=i, column=j)
                        k += 1
                    else:
                        self.riddle[i][j] = Entry(f, width=2, justify=RIGHT, relief=SUNKEN, textvariable=v[k], bg='white', fg='black', font='Arial')
                        self.riddle[i][j].grid(row=i, column=j)
                        k += 1
        Button(self.window, text='Finish', command=self.is_valid).pack()
        Button(self.window, text='Hint', command=self.hint).pack()
        self.window.mainloop()

    def is_valid(self):
        ct = 0
        for i in range(9):
            for j in range(9):
                if type(self.riddle[i][j]) == int:
                    pass
                else:
                    try:
                        self.your_ans[i][j] = eval(self.riddle[i][j].get())
                    except SyntaxError:
                        ct += 1
        if ct != 0:
            tkinter.messagebox.showwarning(title='Result', message='Some input is invalid.')
        if self.your_ans == self.solution:
            point += self.level*10
            tkinter.messagebox.showinfo(title='Result', message='Corect! You got ' + str(point) + ' points')
            self.window.destroy()
        else:
            tkinter.messagebox.showwarning(title='Result', message='Wrong answer!')

    def hint(self):
        if self.hint_list == []:
            tkinter.messagebox.showinfo(title='Result',  message='No hints left.')
        else:
            a = random.randint(1, len(self.hint_list))
            b = self.hint_list.pop(a - 1)
            x = b[0]
            y = b[1]
            tkinter.messagebox.showinfo(title='Hint', message='Row %d Column %d is %d' % (x + 1, y + 1, self.solution[x][y]))
            point -= 1