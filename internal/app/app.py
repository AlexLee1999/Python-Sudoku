import random
from tkinter import *
import tkinter.messagebox
import internal.time.count_time as time
import internal.shared_function.shared_function as shared
import internal.game.sudoku as sudoku


class app(object):
    def __init__(self):
        self.point = 0
        self.problem = 0
        self.during_game = False
        self.main = Tk()
        self.main.title('Sudoku')
        self.canvas = Canvas(self.main, width=1000, height=20)
        self.canvas.pack()
        self.time = time.Time(1, 0, 0)
        Button(self.main, text='Easy', command=self.easy,
               bg='white', font='Arial', width=10).pack()
        Button(self.main, text='Normal', command=self.normal,
               bg='white', font='Arial', width=10).pack()
        Button(self.main, text='Hard', command=self.hard,
               bg='white', font='Arial', width=10).pack()
        Button(self.main, text='Finish Game', command=self.over,
               bg='white', font='Arial', width=10).pack()
        self.easy_list = [1, 2, 3, 4, 5]
        self.normal_list = [1, 2, 3, 4, 5]
        self.hard_list = [1, 2, 3, 4, 5]
        self.countdown()
        self.main.mainloop()

    def easy(self):
        if self.easy_list == []:
            tkinter.messagebox.showinfo(
                title='Result', message='No problems left.')
        else:
            self.problem += 1
            num = random.randint(1, len(self.easy_list))
            number = self.easy_list.pop(num - 1)
            name = './Problems/easy' + str(number) + '.txt'
            file = open(name, 'r')
            que = eval(file.readline())
            ans = eval(file.readline())
            level = 1
            self.during_game = True
            a = sudoku.sudoku(que, ans, level, self.problem)
            self.point += a.get_point()

    def normal(self):
        if self.normal_list == []:
            tkinter.messagebox.showinfo(
                title='Result',  message='No problems left.')
        else:
            self.problem += 1
            num = random.randint(1, len(self.normal_list))
            number = self.normal_list.pop(num - 1)
            name = './Problems/normal' + str(number) + '.txt'
            file = open(name, 'r')
            que = eval(file.readline())
            ans = eval(file.readline())
            level = 2
            a = sudoku.sudoku(que, ans, level, self.problem)
            self.point += a.get_point()

    def hard(self):
        if self.hard_list == []:
            tkinter.messagebox.showinfo(
                title='Result', message='No problems left.')
        else:
            self.problem += 1
            num = random.randint(1, len(self.hard_list))
            number = self.hard_list.pop(num - 1)
            name = './Problems/normal' + str(number) + '.txt'
            file = open(name, 'r')
            que = eval(file.readline())
            ans = eval(file.readline())
            level = 3
            a = sudoku.sudoku(que, ans, level, self.problem)
            self.point += a.get_point()

    def countdown(self):
        self.canvas.delete(ALL)
        self.time += -1
        self.canvas.create_text(54, 12.5, text=self.time, font='Arial')
        if shared.time_to_int(self.time) == 0:
            tkinter.messagebox.showinfo(
                title='Result',  message='Times up! You got ' + str(self.point) + ' points in total!')
            self.main.destroy()
        else:
            self.canvas.after(1000,  self.countdown)

    def over(self):
        tkinter.messagebox.showinfo(
            title='Result',  message='You got '+str(self.point)+' points in total!')
        self.main.destroy()