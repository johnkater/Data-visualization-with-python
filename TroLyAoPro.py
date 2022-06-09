# Đồ án trí tuệ nhân tạo : Phát triển Trợ lý ảo tiếng việt


'''------------HOÀNG MINH NHẬT     STT: 36     MSSV : 19133042------------------------------------------'''

# thư viện trợ lý ảo----------------------------
import speech_recognition as sr
from gtts import gTTS
import os
import playsound
from datetime import datetime
import wikipedia 
# thư viện game caro----------------------------
from tkinter import *
from functools import partial
import random
# thư viện game 8 số-----------------------------
from copy import deepcopy
import numpy as np
import time
#-------------------------------------------------
# Hàm tính toán có giao diện----------------------------------
def Caculator(): 
    def btnClick(numbers): # button nhập 
        global operator
        operator = operator + str(numbers)
        text_Input.set(operator)
    def btnClear(): # Button xóa 
        global operator
        operator = ""
        text_Input.set("")
    def btnEquals(): # button kết quả 
        global operator
        result = str(eval(operator))
        text_Input.set(result)
    cal = Tk()
    cal.title("Caculator")
    operator = ""
    text_Input = StringVar()
    txtDisplay = Entry(cal,width = 30,font = ('arial',20,'bold'),textvariable=text_Input,bd=30,insertwidth=4,bg='aqua',justify='right').grid(columnspan=4)
    # dong 1
    bt7 = Button(cal,padx=30,bd=8,fg = "black",font = ('arial',20,'bold'),text ="7",command=lambda:btnClick(7),bg="silver").grid(row=1,column=0)
    bt8 = Button(cal,padx=30,bd=8,fg = "black",font = ('arial',20,'bold'),text ="8",command=lambda:btnClick(8),bg="silver").grid(row=1,column=1)
    bt9 = Button(cal,padx=30,bd=8,fg = "black",font = ('arial',20,'bold'),text ="9",command=lambda:btnClick(9),bg="silver").grid(row=1,column=2)
    btDec = Button(cal,padx=30,bd=8,fg = "black",font = ('arial',20,'bold'),text ="/",command=lambda:btnClick("/"),bg="silver").grid(row=1,column=3)
    # dong 2
    bt4 = Button(cal,padx=30,bd=8,fg = "black",font = ('arial',20,'bold'),text ="4",command=lambda:btnClick(4),bg="silver").grid(row=2,column=0)
    bt5 = Button(cal,padx=30,bd=8,fg = "black",font = ('arial',20,'bold'),text ="5",command=lambda:btnClick(5),bg="silver").grid(row=2,column=1)
    bt6 = Button(cal,padx=30,bd=8,fg = "black",font = ('arial',20,'bold'),text ="6",command=lambda:btnClick(6),bg="silver").grid(row=2,column=2)
    btMul = Button(cal,padx=30,bd=8,fg = "black",font = ('arial',20,'bold'),text ="*",command=lambda:btnClick("*"),bg="silver").grid(row=2,column=3)
    # dong 3
    bt1 = Button(cal,padx=30,bd=8,fg = "black",font = ('arial',20,'bold'),text ="1",command=lambda:btnClick(1),bg="silver").grid(row=3,column=0)
    bt2 = Button(cal,padx=30,bd=8,fg = "black",font = ('arial',20,'bold'),text ="2",command=lambda:btnClick(2),bg="silver").grid(row=3,column=1)
    bt3 = Button(cal,padx=30,bd=8,fg = "black",font = ('arial',20,'bold'),text ="3",command=lambda:btnClick(3),bg="silver").grid(row=3,column=2)
    btSub = Button(cal,padx=30,bd=8,fg = "black",font = ('arial',20,'bold'),text ="-",command=lambda:btnClick("-"),bg="silver").grid(row=3,column=3)
    # dong 4
    btCls = Button(cal,padx=30,bd=8,fg = "black",font = ('arial',20,'bold'),text ="C",command=btnClear,bg="silver").grid(row=4,column=0)
    btDot = Button(cal,padx=30,bd=8,fg = "black",font = ('arial',20,'bold'),text =".",command=lambda:btnClick("."),bg="silver").grid(row=4,column=1)
    bt0 = Button(cal,padx=30,bd=8,fg = "black",font = ('arial',20,'bold'),text ="0",command=lambda:btnClick(0),bg="silver").grid(row=4,column=2)
    btAdd = Button(cal,padx=30,bd=8,fg = "black",font = ('arial',20,'bold'),text ="+",command=lambda:btnClick("+"),bg="silver").grid(row=4,column=3)
    # dong 5
    btOpen = Button(cal,padx=30,bd=8,fg = "black",font = ('arial',20,'bold'),text ="(",command=lambda:btnClick("("),bg="silver").grid(row=5,column=0)
    btClose = Button(cal,padx=30,bd=8,fg = "black",font = ('arial',20,'bold'),text =")",command=lambda:btnClick(")"),bg="silver").grid(row=5,column=1)
    btResult = Button(cal,padx=94,bd=8,fg = "black",font = ('arial',20,'bold'),text ="=",command=btnEquals,bg="silver").grid(row=5,column=2,columnspan=2)
    
    
    cal.mainloop()
def game8So():
        # nhận đầu vào của trạng thái hiện tại và đánh giá đường dẫn tốt nhất đến trạng thái mục tiêu
    def bestsolution(state):
        bestsol = np.array([], int).reshape(-1, 9)
        count = len(state) - 1
        while count != -1:
            bestsol = np.insert(bestsol, 0, state[count]['puzzle'], 0)
            count = (state[count]['parent'])
        return bestsol.reshape(-1, 3, 3)
    
           
    # hàm này kiểm tra tính duy nhất của trạng thái lặp (nó),nó đã được duyệt trước đó hay chưa.
    def all(checkarray):
        set=[]
        for it in set:
            for checkarray in it:
                return 1
            else:
                return 0
    
    
    # tính toán chi phí khoảng cách MinhNhat giữa mỗi chữ số của câu đố (trạng thái bắt đầu) và trạng thái mục tiêu
    def MinhNhat(puzzle, goal):
        a = abs(puzzle // 3 - goal // 3)
        b = abs(puzzle % 3 - goal % 3)
        mhcost = a + b
        return sum(mhcost[1:])
    
    
    
    # tính toán số lượng ô đặt sai vị trí ở trạng thái hiện tại so với trạng thái mục tiêu
    def misplaced_tiles(puzzle,goal):
        mscost = np.sum(puzzle != goal) - 1
        return mscost if mscost > 0 else 0
             
    
    # xác định tọa độ của từng giá trị mục tiêu hoặc trạng thái ban đầu
    def coordinates(puzzle):
        pos = np.array(range(9))
        for p, q in enumerate(puzzle):
            pos[q] = p
        return pos
    
    
    
    # Bắt đầu đánh giá 8-puzzle, sử dụng hàm MinhNhat heuristics 
    def evaluvate(puzzle, goal):
        steps = np.array([('up', [0, 1, 2], -3),('down', [6, 7, 8],  3),('left', [0, 3, 6], -1),('right', [2, 5, 8],  1)],
                    dtype =  [('move',  str, 1),('position', list),('head', int)])
    
        dtstate = [('puzzle',  list),('parent', int),('gn',  int),('hn',  int)]
        
         # khởi tạo cha, gn và hn, trong đó hn là lệnh gọi hàm khoảng cách MinhNhat 
        costg = coordinates(goal)
        parent = -1
        gn = 0
        hn = MinhNhat(coordinates(puzzle), costg)
        state = np.array([(puzzle, parent, gn, hn)], dtstate)
    
    # sử dụng hàng đợi ưu tiên với vị trí là khóa và fn là giá trị.
        dtpriority = [('position', int),('fn', int)]
        priority = np.array( [(0, hn)], dtpriority)
    
    
    
        while 1:
            priority = np.sort(priority, kind='mergesort', order=['fn', 'position'])     
            position, fn = priority[0]                                                 
            priority = np.delete(priority, 0, 0)  
            # sắp xếp ưu tiên hàng đợi bằng cách sử dụng sắp xếp hợp nhất, phần tử đầu tiên được chọn 
            # để khám phá loại bỏ khỏi hàng đợi những gì chúng ta đang khám phá
            puzzle, parent, gn, hn = state[position]
            puzzle = np.array(puzzle)
            # Xác định ô trống trong đầu vào 
            blank = int(np.where(puzzle == 0)[0])       
            gn = gn + 1                              
            c = 1
            start_time = time.time()
            for s in steps:
                c = c + 1
                if blank not in s['position']:
                    # tạo trạng thái mới dưới dạng bản sao của hiện tại
                    openstates = deepcopy(puzzle)                   
                    openstates[blank], openstates[blank + s['head']] = openstates[blank + s['head']], openstates[blank]             
                    # Hàm all được gọi, nếu nút đã được khám phá trước đó hay chưa
                    if ~(np.all(list(state['puzzle']) == openstates, 1)).any():    
                        end_time = time.time()
                        if (( end_time - start_time ) > 2):
                            print(" The 8 puzzle is unsolvable ! \n")
                            exit 
                        # gọi hàm MinhNhat để tính chi phí khoảng cách 
                        hn = MinhNhat(coordinates(openstates), costg)    
                        # tạo và thêm trạng thái mới trong danh sách                    
                        q = np.array([(openstates, position, gn, hn)], dtstate)         
                        state = np.append(state, q, 0)
                        # f (n) là tổng chi phí để đạt được nút và chi phí để đạt được từ nút đến trạng thái mục tiêu
                        fn = gn + hn                                        
                
                        q = np.array([(len(state) - 1, fn)], dtpriority)    
                        priority = np.append(priority, q, 0)
                        # Kiểm tra xem nút trong các biểu tượng vận hành có khớp với trạng thái mục tiêu hay không.  
                        if np.array_equal(openstates, goal):                              
                            print(' The 8 puzzle is solvable ! \n')
                            return state, len(priority)
            
                            
        return state, len(priority)
    
    
    # bắt đầu đánh giá 8 -puzzle , sử dụng phương pháp phỏng đoán các ô xếp sai vị trí   
    def evaluvate_misplaced(puzzle, goal):
        steps = np.array([('up', [0, 1, 2], -3),('down', [6, 7, 8],  3),('left', [0, 3, 6], -1),('right', [2, 5, 8],  1)],
                    dtype =  [('move',  str, 1),('position', list),('head', int)])
    
        dtstate = [('puzzle',  list),('parent', int),('gn',  int),('hn',  int)]
    
        costg = coordinates(goal)
        # khởi tạo parent, gn và hn, trong đó hn là lệnh gọi hàm misplaced_tiles  
        parent = -1
        gn = 0
        hn = misplaced_tiles(coordinates(puzzle), costg)
        state = np.array([(puzzle, parent, gn, hn)], dtstate)
    
       # sử dụng các hàng đợi ưu tiên với vị trí là khóa và fn là giá trị.
        dtpriority = [('position', int),('fn', int)]
    
        priority = np.array([(0, hn)], dtpriority)
        
        while 1:
            priority = np.sort(priority, kind='mergesort', order=['fn', 'position'])      
            position, fn = priority[0]       
            # sắp xếp hàng đợi ưu tiên bằng cách sử dụng sắp xếp hợp nhất, phần tử đầu tiên được chọn để khám phá.                                          
            priority = np.delete(priority, 0, 0)                         
            puzzle, parent, gn, hn = state[position]
            puzzle = np.array(puzzle)
             # Xác định ô trống trong đầu vào 
            blank = int(np.where(puzzle == 0)[0])   
            # Tăng cost g(n) = 1  
            gn = gn + 1                             
            c = 1
            start_time = time.time()
            for s in steps:
                c = c + 1
                if blank not in s['position']:
                     # tạo trạng thái mới dưới dạng bản sao của hiện tại
                    openstates = deepcopy(puzzle)         
                    openstates[blank], openstates[blank + s['head']] = openstates[blank + s['head']], openstates[blank]
                    # Hàm kiểm tra được gọi, nếu nút đã được khám phá trước đó hay chưa. 
                    if ~(np.all(list(state['puzzle']) == openstates, 1)).any():          
                        end_time = time.time()
                        if (( end_time - start_time ) > 2):
                            print(" The 8 puzzle is unsolvable \n")
                            break
                        # gọi hàm Misplaced_tiles để tính toán cost
                        hn = misplaced_tiles(coordinates(openstates), costg) 
                        #tạo và thêm trạng thái mới trong danh sách                    
                        q = np.array([(openstates, position, gn, hn)], dtstate)         
                        state = np.append(state, q, 0)
                        
                        # f (n) là tổng chi phí để đạt được nút và chi phí để đạt được từ nút đến trạng thái mục tiêu
                        fn = gn + hn                                        
                        
                        q = np.array([(len(state) - 1, fn)], dtpriority)
                        priority = np.append(priority, q, 0)
                        # Kiểm tra xem nút trong các biểu tượng vận hành có khớp với trạng thái mục tiêu hay không.
                        if np.array_equal(openstates, goal):                      
                            print(' The 8 puzzle is solvable \n')
                            return state, len(priority)
                            
        return state, len(priority)
    
    
    
    # ----------  Program start -----------------
    
    
     # Người dùng nhập vào trạng thái đầu 
    puzzle = []
    print(" Input vals from 0-8 for start state ")
    for i in range(0,9):
        x = int(input("enter vals :"))
        puzzle.append(x)
    
     # Người dùng nhập vào trạng thái đích       
    goal = []
    print(" Input vals from 0-8 for goal state ")
    for i in range(0,9):
        x = int(input("Enter vals :"))
        goal.append(x)
    
    
    
    n = int(input("1. MinhNhat distance \n2. Misplaced tiles\n"))
    
    if(n ==1 ): 
        state, visited = evaluvate(puzzle, goal) 
        bestpath = bestsolution(state)
        print(str(bestpath).replace('[', ' ').replace(']', ''))
        totalmoves = len(bestpath) - 1
        print('Steps to reach goal:',totalmoves)
        visit = len(state) - visited
        print('Total nodes visited: ',visit, "\n")
        print('Total generated:', len(state))
    
    if(n == 2):
        state, visited = evaluvate_misplaced(puzzle, goal) 
        bestpath = bestsolution(state)
        print(str(bestpath).replace('[', ' ').replace(']', ''))
        totalmoves = len(bestpath) - 1
        print('Steps to reach goal:',totalmoves)
        visit = len(state) - visited
        print('Total nodes visited: ',visit, "\n")
        print('Total generated:', len(state))
def tictactoe():
    class TicTacToe:
        # Hàm khởi tạo : playX là Máy tính , playerO là người chơi
        def __init__(self, playerX, playerO):
            self.board = [' '] * 9
            self.playerX, self.playerO = playerX, playerO
            self.playerX_turn = True
        # Hàm tạo bảng hiển thị trên màn hình console
        def display_board(self):
            print ('     |     |     ')
            print ('  %s  |  %s  |  %s  ' % (self.board[0],self.board[1],self.board[2]))
            print ('_____|_____|_____')
            print ('     |     |     ')
            print ('  %s  |  %s  |  %s  ' % (self.board[3],self.board[4],self.board[5]))
            print ('_____|_____|_____')
            print ('     |     |     ')
            print ('  %s  |  %s  |  %s  ' % (self.board[6],self.board[7],self.board[8]))
            print ('     |     |     ')
    
        def board_full(self):
            return not any([space == ' ' for space in self.board])
        # Kiểm tra trạng thái đích , kết thúc game -> tìm ra người chiến thắng 
        def player_wins(self, char):
            for a, b, c in [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                            (0, 3, 6), (1, 4, 7), (2, 5, 8),
                            (0, 4, 8), (2, 4, 6)]:
                if char == self.board[a] == self.board[b] == self.board[c]:
                    return True
    
            return False
    
        def play_game(self):
            print ('\nNew game!')
    
            while True:
                if self.playerX_turn:
                    player, char = self.playerX, 'X'
                else:
                    player, char = self.playerO, 'O'
    
                if player.breed == 'human':
                    self.display_board()
    
                move = player.move(self.board)
                self.board[move - 1] = char
    
                if self.player_wins(char):
                    self.display_board()
                    print (char + ' wins!')
                    break
    
                if self.board_full():
                    self.display_board()
                    print('Draw!')
                    break
    
                self.playerX_turn = not self.playerX_turn

    # Người chơi
    class Player(object):
        # Hàm khởi tạo
        def __init__(self):
            self.breed = 'human'
        # in ra thông báo "your move?" để người chơi nhập vào bước đi
        def move(self, board):
            return int(input('Your move?'))
        # người chơi sẽ chọn vị trí từ 1 đến 9 
        def available_moves(self, board):
            return [i + 1 for i in range(0, 9) if board[i] == ' ']
    
    # AI dùng giải thuật minimax
    class MinimaxPlayer(Player):
        # Hàm khởi tạo
        def __init__(self):
            self.breed = 'minimax'
        # chọn vị trí đánh ngẫu nhiên trong [1,3,7,9]
        def move(self, board):
            if len(self.available_moves(board)) == 9:
                return random.choice([1, 3, 7, 9])
    
            best_value = 0
            for move in self.available_moves(board):
                board[move - 1] = 'X'
                value = self.min_value(board)
                board[move - 1] = ' '
                if value > best_value:
                    return move
    
            return random.choice(self.available_moves(board))
        # Kiểm tra trạng thái đích xem các hàng ngang , hàng dọc , hàng chéo có lập thành 3 'X' hoặc 3 'O' không
        def terminal_test(self, board):  
            for a, b, c in [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                            (0, 3, 6), (1, 4, 7), (2, 5, 8),
                            (0, 4, 8), (2, 4, 6)]:
                if 'X' == board[a] == board[b] == board[c]:
                    return (True, 1)
                elif 'O' == board[a] == board[b] == board[c]:
                    return (True, -1)
    
            if not any([space == ' ' for space in board]):
                return (True, 0)
    
            return (False, 0)
        # tính giá trị max
        def max_value(self, board):
            in_terminal_state, utility_value = self.terminal_test(board)
            if in_terminal_state:
                return utility_value
    
            value = -100000
            for move in self.available_moves(board):
                board[move - 1] = 'X'
                value = max(value, self.min_value(board))
                board[move - 1] = ' '
    
            return value
        # tính giá trị min
        def min_value(self, board):
            in_terminal_state, utility_value = self.terminal_test(board)
            if in_terminal_state:
                return utility_value
    
            value = 100000
            for move in self.available_moves(board):
                board[move - 1] = 'O'
                value = min(value, self.max_value(board))
                board[move - 1] = ' '
    
            return value
    
    
    p1 = MinimaxPlayer()
    p2 = Player()
    
    while True:
        t = TicTacToe(p1, p2)
        t.play_game()
        print("bạn có muốn chơi nữa không ?")
        print("1. có\n2. không")
        option = input()
        if(option == '2'):
            break
        print("Lượt chơi tiếp theo :")
        print(option)
def gameCaro():
    root=Tk()
    root.title("Hoàng Minh Nhật 19133042    GAME CARO")
    Buts={}
    def xulynut(x,y):
            
            if Buts[x,y]['text'] is '' :
                    Buts[x,y]['text']=['X']
            else :
                    Buts[x,y]['text']=''                                  
    for r in range(20):
        for c in range(20):
            Buts[r,c]=Button(root,font=('arial',10,'bold'),bd=1,height=2,width=4,
                             borderwidth=2,command=partial(xulynut,x=r,y=c))
            Buts[r,c].grid(row=r,column=c)
    root.mainloop()
 #------------------------------------------           
now = datetime.now()

# initialize the recognizer
r = sr.Recognizer()

# Playing Sound
def speak(text):
    tts = gTTS(text=text, lang='vi')
    filename = 'voice5.mp3'
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)
# ----------------------------------
while True:
    # speech to text
    with sr.Microphone() as source:
        # read the audio data from the default microphone
        audio_data = r.record(source, duration=5)
        print("Đang nhận dạng...")
        # convert speech to text
        try: 
            text = r.recognize_google(audio_data,language="vi")
        except:
            text == ""
        print(text)
        
    #--process data
        if text == "":
            robot_brain = "Tôi đang lắng nghe"
            print('AI speak:',robot_brain)
            speak(robot_brain)
        
        elif "Xin chào" in text:
            robot_brain = "chào bạn tôi có thể giúp gì cho bạn"
            print('AI speak:',robot_brain)
            speak(robot_brain)
        elif "Hôm nay ngày bao nhiêu" in text:
            robot_brain = now.strftime("Hôm nay ngày %d %m %y")
            print('AI speak:',robot_brain)
            speak(robot_brain)
        elif "Mấy giờ rồi" in text:
            robot_brain = now.strftime("%H:%M:%S")
            print('AI speak:',robot_brain)
            speak(robot_brain)
        elif "tạm biệt" in text:
            robot_brain = "Hẹn gặp lại bạn nhé"
            print('AI speak:',robot_brain)
            speak(robot_brain)
            break
        elif "tính toán" in text:
            robot_brain = "Mời bạn nhập biểu thức cần tính"
            print('AI speak:',robot_brain)
            speak(robot_brain)
            #Caculator()                # Hàm tính toán có giao diện 
            operator = str(input())
            result = "kết quả là :" + str(eval(operator))
            print(result)
            speak(result)     
        elif "play caro" in text:
            robot_brain = "Được tôi sẽ chơi caro cùng bạn"
            print('AI speak:',robot_brain)
            speak(robot_brain)
            #gameCaro()                 # Game caro có giao diện
            tictactoe()
        elif "play game 8" in text:
            robot_brain = "Sau đây là các bước giải game 8 số"
            print('AI speak:',robot_brain)
            speak(robot_brain)
            game8So()
        elif text:
            wikipedia.set_lang("vi")
            robot_brain = wikipedia.summary(text,sentences=1)
            print('AI speak:',robot_brain)
            speak(robot_brain)
        else:
            robot_brain = "bạn muốn nói gì nào"
            print('AI speak:',robot_brain)
            speak(robot_brain)
