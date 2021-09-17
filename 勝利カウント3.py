import tkinter
import tkinter.filedialog
import os

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

# メンバーの呼び出しと登録の関数
def func1():
    global win
    global lose
    global player
    global member
    global member_win
    global member_lose
    player = Entry1.get()
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
    Entry2.configure(state="normal")
    Entry3.configure(state="normal")
    Entry4.configure(state="normal")
    Entry5.configure(state="normal")
    Entry2.delete(0, tkinter.END)
    Entry3.delete(0, tkinter.END)
    Entry4.delete(0, tkinter.END)
    Entry5.delete(0, tkinter.END)
    Entry2.insert(tkinter.END, now_win)
    Entry3.insert(tkinter.END, now_lose)
    Entry4.insert(tkinter.END, win)
    Entry5.insert(tkinter.END, lose)
    Entry2.configure(state="readonly")
    Entry3.configure(state="readonly")
    Entry4.configure(state="readonly")
    Entry5.configure(state="readonly")

# 勝利数変更の関数
def func2():
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
        Entry2.configure(state="normal")
        Entry4.configure(state="normal")
        Entry2.delete(0, tkinter.END)
        Entry4.delete(0, tkinter.END)
        Entry2.insert(tkinter.END, now_win)
        Entry4.insert(tkinter.END, win)
        Entry2.configure(state="readonly")
        Entry4.configure(state="readonly")

# 敗北数変更の関数
def func3():
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
        Entry3.configure(state="normal")
        Entry5.configure(state="normal")
        Entry3.delete(0, tkinter.END)
        Entry5.delete(0, tkinter.END)
        Entry3.insert(tkinter.END, now_lose)
        Entry5.insert(tkinter.END, lose)
        Entry3.configure(state="readonly")
        Entry5.configure(state="readonly")

# バックアップ作成
def func4():
    buckup_file = tkinter.filedialog.asksaveasfilename(filetypes=[("テキストファイル", ".txt")],defaultextension="txt")
    with open(buckup_file, "w") as f:
        f.write(str(member)+"\n")
        f.write(str(member_win)+"\n")
        f.write(str(member_lose)+"\n")
        f.write(str(win)+"\n")
        f.write(str(lose))

def func5():
    global win
    global lose
    global member
    global member_win
    global member_lose
    file_path = tkinter.filedialog.askopenfilename(filetypes=[("テキストファイル", "*.txt")],title="バックアップファイルを選択",multiple="False")
    if len(file_path) == 0:
        return
    with open(file_path, "r") as f:
        lines = f.readlines()
    member = eval(lines[0])
    member_win = eval(lines[1])
    member_lose = eval(lines[2])
    win = int(lines[3])
    lose = int(lines[4])
    Entry4.configure(state="normal")
    Entry5.configure(state="normal")
    Entry4.delete(0, tkinter.END)
    Entry5.delete(0, tkinter.END)
    Entry4.insert(tkinter.END, win)
    Entry5.insert(tkinter.END, lose)
    Entry4.configure(state="readonly")
    Entry5.configure(state="readonly")

# サブウィンドウが閉じられた時の処理
def end():
    os._exit(0)

app = tkinter.Tk()
# アプリのタイトル、サイズ（変更不可）、背景色
app.title("ポケサー24レート")
app.geometry("500x300")
app.resizable(width=False, height=False)
app.configure(bg="light steel blue")

# ラベルの作成と配置
label1 = tkinter.Label(text="プレイヤー", font=("", "20"))
label1.place(x=30, y=10)

label2 = tkinter.Label(text="個人戦績", font=("", "20"))
label2.place(x=30, y=110)

label3 = tkinter.Label(text="勝", font=("", "30"))
label3.place(x=265, y=141)

label4 = tkinter.Label(text="敗", font=("", "30"))
label4.place(x=425, y=141)

label5 = tkinter.Label(text="総合戦績", font=("", "20"))
label5.place(x=30, y=210)

label6 = tkinter.Label(text="勝", font=("", "30"))
label6.place(x=265, y=241)

label7 = tkinter.Label(text="敗", font=("", "30"))
label7.place(x=425, y=241)

# テキストボックスの作成と配置
Entry1 = tkinter.Entry(width=9, font=("", "40")) 
Entry1.place(x=180, y=30)

Entry2 = tkinter.Entry(width=3, font=("", "40"))
Entry2.configure(state="readonly")
Entry2.place(x=180, y=130)

Entry3 = tkinter.Entry(width=3, font=("", "40")) 
Entry3.configure(state="readonly")
Entry3.place(x=340, y=130)

Entry4 = tkinter.Entry(width=3, font=("", "40")) 
Entry4.configure(state="readonly")
Entry4.place(x=180, y=230)

Entry5 = tkinter.Entry(width=3, font=("", "40")) 
Entry5.configure(state="readonly")
Entry5.place(x=340, y=230)

# ボタンのみのウィンドウを作成
Buttons = tkinter.Toplevel()
Buttons.title("ボタン")
Buttons.geometry("200x250")
Buttons.resizable(width=False, height=False)
Buttons.configure(bg="light steel blue")
Buttons.protocol("WM_DELETE_WINDOW", end)

# ボタンの作成と配置
read_button1 = tkinter.Button(Buttons,text="名前を確定",command=func1,bg="lemon chiffon", font=("", "20"))
read_button1.pack(padx=10, pady=10)

read_button2 = tkinter.Button(Buttons,text="勝ち",command=func2,bg="lemon chiffon", font=("", "20"))
read_button2.place(x=24, y=80)

read_button3 = tkinter.Button(Buttons,text="負け",command=func3,bg="lemon chiffon", font=("", "20"))
read_button3.place(x=101, y=80)

read_button4 = tkinter.Button(Buttons,text="保存",command=func4,bg="lemon chiffon", font=("", "20"))
read_button4.place(x=22, y=180)

read_button5 = tkinter.Button(Buttons,text="復元",command=func5,bg="lemon chiffon", font=("", "20"))
read_button5.place(x=101, y=180)


# GUIアプリ生成
app.mainloop()