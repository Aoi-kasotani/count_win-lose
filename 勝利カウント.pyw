import tkinter

global win
global lose
global player
global member
global member_win
global member_lose

win= 0
lose = 0
player = ""
member = []
member_win = []
member_lose = []

class Application(tkinter.Tk):
    def __init__(self):
        super().__init__()

        # アプリのタイトル、サイズ（変更不可）、背景色
        self.title("ポケサー24レート")
        self.geometry('600x300')
        self.resizable(width=False, height=False)
        self.configure(bg='light steel blue')

        # ラベルの作成と配置
        self.label1 = tkinter.Label(text='プレイヤー', font=("", "20"))
        self.label1.place(x=30, y=10)

        self.label2 = tkinter.Label(text='個人戦績', font=("", "20"))
        self.label2.place(x=30, y=110)

        self.label3 = tkinter.Label(text='勝', font=("", "30"))
        self.label3.place(x=265, y=141)

        self.label4 = tkinter.Label(text='敗', font=("", "30"))
        self.label4.place(x=425, y=141)

        self.label5 = tkinter.Label(text='総合戦績', font=("", "20"))
        self.label5.place(x=30, y=210)

        self.label6 = tkinter.Label(text='勝', font=("", "30"))
        self.label6.place(x=265, y=241)

        self.label7 = tkinter.Label(text='敗', font=("", "30"))
        self.label7.place(x=425, y=241)

        # テキストボックスの作成と配置
        self.path1 = tkinter.Entry(width=9, font=("", "40")) 
        self.path1.place(x=180, y=30)

        self.path2 = tkinter.Entry(width=3, font=("", "40"))
        self.path2.configure(state='readonly')
        self.path2.place(x=180, y=130)

        self.path3 = tkinter.Entry(width=3, font=("", "40")) 
        self.path3.configure(state='readonly')
        self.path3.place(x=340, y=130)

        self.path4 = tkinter.Entry(width=3, font=("", "40")) 
        self.path4.configure(state='readonly')
        self.path4.place(x=180, y=230)

        self.path5 = tkinter.Entry(width=3, font=("", "40")) 
        self.path5.configure(state='readonly')
        self.path5.place(x=340, y=230)

        # ボタンの作成と配置
        self.read_button1 = tkinter.Button(self,text='名前を確定',command=self.read_button_func1,bg='lemon chiffon', font=("", "20"))
        self.read_button1.place(x=440, y=40)

        self.read_button2 = tkinter.Button(self,text='勝ち',command=self.read_button_func2,bg='lemon chiffon', font=("", "20"))
        self.read_button2.place(x=500, y=140)
    
        self.read_button3 = tkinter.Button(self,text='負け',command=self.read_button_func3,bg='lemon chiffon', font=("", "20"))
        self.read_button3.place(x=500, y=240)

    # メンバーの呼び出しと登録の関数
    def read_button_func1(self):
        global win
        global lose
        global player
        global member
        global member_win
        global member_lose
        player = self.path1.get()
        if player == "":
            return
        elif player in member:
            num = member.index(player)
            now_win = member_win[num]
            now_lose = member_lose[num]
        else:
            member.append(player)
            member_win.append(0)
            member_lose.append(0)
            num = member.index(player)
            now_win = member_win[num]
            now_lose = member_lose[num]
        self.path2.configure(state='normal')
        self.path3.configure(state='normal')
        self.path4.configure(state='normal')
        self.path5.configure(state='normal')
        self.path2.delete(0, tkinter.END)
        self.path3.delete(0, tkinter.END)
        self.path4.delete(0, tkinter.END)
        self.path5.delete(0, tkinter.END)
        self.path2.insert(tkinter.END, now_win)
        self.path3.insert(tkinter.END, now_lose)
        self.path4.insert(tkinter.END, win)
        self.path5.insert(tkinter.END, lose)
        self.path2.configure(state='readonly')
        self.path3.configure(state='readonly')
        self.path4.configure(state='readonly')
        self.path5.configure(state='readonly')

    # 勝利数変更の関数
    def read_button_func2(self):
        global win
        global player
        global member
        global member_win
        if player == "":
            return
        else:    
            num = member.index(player)
            member_win[num] = member_win[num] + 1
            now_win = member_win[num]
            win = win + 1
            self.path2.configure(state='normal')
            self.path4.configure(state='normal')
            self.path2.delete(0, tkinter.END)
            self.path4.delete(0, tkinter.END)
            self.path2.insert(tkinter.END, now_win)
            self.path4.insert(tkinter.END, win)
            self.path2.configure(state='readonly')
            self.path4.configure(state='readonly')

    # 敗北数変更の関数
    def read_button_func3(self):
        global lose
        global player
        global member
        global member_lose
        if player == "":
            return
        else:
            num = member.index(player)
            member_lose[num] = member_lose[num] + 1
            now_lose = member_lose[num]
            lose = lose + 1
            self.path3.configure(state='normal')
            self.path5.configure(state='normal')
            self.path3.delete(0, tkinter.END)
            self.path5.delete(0, tkinter.END)
            self.path3.insert(tkinter.END, now_lose)
            self.path5.insert(tkinter.END, lose)
            self.path3.configure(state='readonly')
            self.path5.configure(state='readonly')

# GUIアプリ生成
app = Application()
app.mainloop()