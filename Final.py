from tkinter import*
import tkinter.messagebox
import random
demo=False
class Time:
    def __init__(self,hour,mi,second):
        self.second=second
        self.mi=mi
        self.hour=hour
    def __str__(self):
        return ('Time %.2d:%.2d:%.2d'%(self.hour,self.mi,self.second))
    
    def __add__(self,other):
        t=self.second+self.mi*60+self.hour*3600
        q=t+other
        return int_to_time(q)
def time_to_int(t):
    mi=t.hour*60+t.mi
    seconds=mi*60+t.second
    return seconds
        
def int_to_time(t):
        second=t%60
        mi=(t%3600)//60
        hour=t//3600
        return Time(hour,mi,second)
class app:
    def __init__(self):
        global point,canvas,time,main,easylist,normallist,hardlist,problem
        point=0
        problem=0
        main=Tk()
        main.title('Sudoku')        
        canvas = Canvas(main, width = 110, height = 20) 
        canvas.pack() 
        time = Time(1,0,0)   #設少一點可以看她關        
        Button(main,text='Easy',command=self.easy,bg='white',font='Arial',width=10).pack()
        Button(main,text='Normal',command=self.normal,bg='white',font='Arial',width=10).pack()
        Button(main,text='Hard',command=self.hard,bg='white',font='Arial',width=10).pack()
        Button(main,text='Finish Game',command=self.over,bg='white',font='Arial',width=10).pack()
        Button(main,text='Demo',command=self.demo,bg='white',font='Arial',width=10).pack()
        easylist=[1,2,3,4,5]
        normallist=[1,2,3,4,5]
        hardlist=[1,2,3,4,5]
        self.countdown()
        
        main.mainloop()
        
    def easy(self):
        global easylist,problem,demo
        demo=False
        if easylist == []:
            tkinter.messagebox.showinfo(title='Result', message='No problems left.')
        else:
            problem=problem+1
            num=random.randint(1,len(easylist))#這個範圍就是題庫數量
            number=easylist.pop(num-1)
            name='easy'+str(number)+'.txt'
            file=open(name,'r')
            que=eval(file.readline())
            ans=eval(file.readline())
            level=1
            a=sudoku(que,ans,level)
            
        
    def normal(self):
        global normallist,problem,demo
        demo=False
        if normallist == []:
            tkinter.messagebox.showinfo(title='Result', message='No problems left.')
        else:
            problem=problem+1
            num=random.randint(1,len(normallist))#這個範圍就是題庫數量
            number=normallist.pop(num-1)
            name='normal'+str(number)+'.txt'
            file=open(name,'r')
            que=eval(file.readline())
            ans=eval(file.readline())
            level=2
            a=sudoku(que,ans,level)
        
    def hard(self):
        global hardlist,problem,demo
        demo=False
        if hardlist == []:
            tkinter.messagebox.showinfo(title='Result', message='No problems left.')
        else:
            problem=problem+1
            num=random.randint(1,len(hardlist))#這個範圍就是題庫數量
            number=hardlist.pop(num-1)
            name='normal'+str(number)+'.txt'
            file=open(name,'r')
            que=eval(file.readline())
            ans=eval(file.readline())
            level=3
            a=sudoku(que,ans,level)
    def demo(self):
        global demo
        demo=True
        num=random.randint(1,2)
        name='demo'+str(num)+'.txt'
        
        file=open(name,'r')
        que=eval(file.readline())
        ans=eval(file.readline())
        level=1
        a=sudoku(que,ans,level)
        
    def countdown(self):
        global canvas,time,main,window
        canvas.delete(ALL) 
        global time 
        time += -1 
        canvas.create_text(54, 12.5, text=time,font='Arial') 
        if time_to_int(time) == 0: 
            tkinter.messagebox.showinfo(title='Result', message='Times up! You got '+str(point)+' points in total!')
            #window.destroy()
            main.destroy()
        else: 
            canvas.after(1000, self.countdown)
    def over(self):
        global main
        tkinter.messagebox.showinfo(title='Result', message='You got '+str(point)+' points in total!')
        main.destroy()
        

  
     
class sudoku():
    def __init__(self,que,ans,level):
        global h,window,problem,demo
        self.riddle=que
        self.solution=ans
        self.yourans=self.riddle

        self.level=level
        window=Tk()
        window.title('Solve')
        canvas = Canvas(window, width = 110, height = 20) 
        canvas.pack()
        if demo:
            canvas.create_text(54, 12.5, text='DEMO',font='Arial')
        else:
            canvas.create_text(54, 12.5, text='Problem %d'%problem,font='Arial')
        f=Frame(window)
        f.pack()
        h=[]
        v=[]
        k=0
        for i in range(9):
            for j in range(9):
                if self.riddle[i][j] == 0:                    
                    h.append([i,j])
                    v.append(StringVar())
        for i in range(9):
            for j in range(9):
                if self.riddle[i][j]!=0:
                    if 0<=i<=2 and 0<=j<=2 :
                        Label(f,text=self.riddle[i][j],bg='black',fg='white',width = 2,font='Arial').grid(row=i,column=j)
                    elif 6<=i<=8 and 0<=j<=2 :
                        Label(f,text=self.riddle[i][j],bg='black',fg='white',width = 2,font='Arial').grid(row=i,column=j) 
                    elif 3<=i<=5 and 3<=j<=5 :
                        Label(f,text=self.riddle[i][j],bg='black',fg='white',width = 2,font='Arial').grid(row=i,column=j)
                    elif 0<=i<=2 and 6<=j<=8 :
                        Label(f,text=self.riddle[i][j],bg='black',fg='white',width = 2,font='Arial').grid(row=i,column=j)
                    elif 6<=i<=8 and 6<=j<=8 :
                        Label(f,text=self.riddle[i][j],bg='black',fg='white',width = 2,font='Arial').grid(row=i,column=j)
                    else:
                        Label(f,text=self.riddle[i][j],bg='white',fg='black',width = 2,font='Arial').grid(row=i,column=j)
                else:
                    if 0<=i<=2 and 0<=j<=2 :
                        self.riddle[i][j]=Entry(f, width = 2, justify = RIGHT, relief=SUNKEN,textvariable=v[k],bg='black',fg='white',font='Arial')
                        self.riddle[i][j].grid(row=i,column=j)
                        k=k+1
                    elif 6<=i<=8 and 0<=j<=2 :
                        self.riddle[i][j]=Entry(f, width = 2, justify = RIGHT, relief=SUNKEN,textvariable=v[k],bg='black',fg='white',font='Arial')
                        self.riddle[i][j].grid(row=i,column=j)
                        k=k+1
                    elif 3<=i<=5 and 3<=j<=5 :
                        self.riddle[i][j]=Entry(f, width = 2, justify = RIGHT, relief=SUNKEN,textvariable=v[k],bg='black',fg='white',font='Arial')
                        self.riddle[i][j].grid(row=i,column=j)
                        k=k+1
                    elif 0<=i<=2 and 6<=j<=8 :
                        self.riddle[i][j]=Entry(f, width = 2, justify = RIGHT, relief=SUNKEN,textvariable=v[k],bg='black',fg='white',font='Arial')
                        self.riddle[i][j].grid(row=i,column=j)
                        k=k+1
                    elif 6<=i<=8 and 6<=j<=8 :
                        self.riddle[i][j]=Entry(f, width = 2, justify = RIGHT, relief=SUNKEN,textvariable=v[k],bg='black',fg='white',font='Arial')
                        self.riddle[i][j].grid(row=i,column=j)
                        k=k+1
                    else:
                        self.riddle[i][j]=Entry(f, width = 2, justify = RIGHT, relief=SUNKEN,textvariable=v[k],bg='white',fg='black',font='Arial')
                        self.riddle[i][j].grid(row=i,column=j)
                        k=k+1
        Button(window,text='Finish',command=self.is_valid).pack()
        Button(window,text='Hint',command=self.hint).pack()
        window.mainloop()
    def is_valid(self):
        #answer=False
        global window,point
        ct=0
        for i in range(9):
            for j in range(9):
                if type(self.riddle[i][j])== int:
                      pass
                else:
                    try:
                        self.yourans[i][j] = eval(self.riddle[i][j].get())
                    except SyntaxError:
                        ct+=1
        if ct!=0:
            tkinter.messagebox.showwarning(title='Result', message='Some input is invalid.')
            #print(type(self.yourans))
        if self.yourans==self.solution:
            point+=self.level*10
            tkinter.messagebox.showinfo(title='Result', message='Corect! You got '+str(point)+' points')
            window.destroy()
        else:
            tkinter.messagebox.showwarning(title='Result', message='Wrong answer!')
            
    def hint(self):
        global h,point
        if h == []:
            tkinter.messagebox.showinfo(title='Result', message='No hints left.')
        else:
            a=random.randint(1,len(h))
            b=h.pop(a-1)
            x=b[0]
            y=b[1]
            tkinter.messagebox.showinfo(title='Hint', message='Row %d Column %d is %d'%(x+1,y+1,self.solution[x][y]) )
            point=point-1                  
app()
