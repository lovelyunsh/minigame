import random
import time
import numpy as np
import os

#baseball game ------------------------------------------------
game_num = []
def make_gamenum(game_num):
   game_num = [0,1,2,3,4,5,6,7,8,9]
   random.shuffle(game_num)

   return game_num[:4]

def compare(ans,game_num):
   st = 0
   ba = 0
   a = ans[0]
   b = ans[1]
   c = ans[2]
   d = ans[3]
   try :
      a, b, c , d = int(a), int(b), int(c), int(d)
   except:
      print('숫자를 쓰세요 좀')
      return 0,0
   ans = [a,b,c,d]
   for i in range(4):
      if ans[i] == game_num[i]:
         st+=1
      ba += game_num.count(ans[i])
   ba = ba - st
   print('%d strike %d ball'%(st,ba))
   return st,ba

   
def baseball_game_start():
   game_num = []
   game_num = make_gamenum(game_num)
   print('게임 시작')
   strike = 0
   ball = 0
   while(True):
      while(True):
         your_ans = ''
         your_ans = input('예측값 4자리 입력')
         
         if len(your_ans) == 4 :
            if your_ans.count(your_ans[0]) == 1 and your_ans.count(your_ans[1]) == 1 and your_ans.count(your_ans[2]) == 1 and your_ans.count(your_ans[3]) == 1 :
               break
            else :
               print('중복된 숫자를 쓰지 마세요')
         else :
            print('숫자를 4자리 쓰세요')
      strike,ball = compare(your_ans,game_num)
      if strike == 4:
         print('니가 이겼어요')
         break

#up_down_game----------------------------------------------------
def up_down_game():
   answer = random.randint(1,200)
   print('게임시작')
   while(True):
      while(True):
         try :
            your_ans = int(input('예측값 1~200사이 숫자 하나 입력'))
            break
         except :
            print('숫자만 입력하세요')
      if answer> your_ans:
         print('up')
      elif answer<your_ans:
         print('down')
      else :
         print('니가 이겼어요')
         break

#3X3 Bingo_game-----------------------------------------------------
def make_bingo():
   bingo = list(range(30))
   random.shuffle(bingo)
   bingo = bingo[:16]
   bingo = np.array(bingo)
   bingo = np.reshape(bingo,(4,4))
   bingo = list(bingo)
   for i in range(len(bingo)):
      bingo[i] = list(bingo[i])
   return bingo
def display_bingo(a):
   print('-'*32)
   for i in range(len(a)):
      for j in range(len(a[i])) :
         print('  ', a[i][j] ,'\t' , end = '')
      if i == len(a)-1 :
         print('your bingo')
      else :
         print('|                               |\n'*2)
   print('-'*32)
      
def display_com_bingo(a):
   print('-'*32)
   for i in range(len(a)):
      for j in range(len(a[i])) :
         if a[i][j] == 'X' :
            print('|',a[i][j] ,'|\t' , end = '')
         else :
            print('|???|\t' , end = '')
      if i == len(a)-1 :
         print('com\'s bingo')
      else :
         print('|                               |\n'*3)
   print('-'*32)
   print('\n\n')


def check_bingo(u_bingo,com_bingo,num):
   check = False
   win = False
   try :
      abc = u_bingo[0].index(num)
      u_bingo[0][abc] = 'X'
   except :
      try :
         abc = u_bingo[1].index(num)
         u_bingo[1][abc] = 'X'
      except :
         try :
            abc = u_bingo[2].index(num)
            u_bingo[2][abc] = 'X'
         except :
            try :
               abc = u_bingo[3].index(num)
               u_bingo[3][abc] = 'X'
            except :
               print('왜 없냐?')
   try :
      abc = com_bingo[0].index(num)
      com_bingo[0][abc] = 'X'
      check = True
   except :
      try :
         abc = com_bingo[1].index(num)
         com_bingo[1][abc] = 'X'
         check = True
      except :
         try :
            abc = com_bingo[2].index(num)
            com_bingo[2][abc] = 'X'
            check = True
            
         except :
            try :
               abc = com_bingo[3].index(num)
               com_bingo[3][abc] = 'X'
               check = True
            except :
               print('')
   if u_bingo[0].count('X') == 4:
      if u_bingo[1].count('X') == 4 :
         if u_bingo[2].count('X') == 4:
            if u_bingo[3].count('X') == 4:
               win = True
   return u_bingo,com_bingo,check,win
            
   
   
def bingo_game():
   c_bingo = make_bingo()
   cc_bingo = c_bingo[:]
   u_bingo = [[],[],[],[]]
   for i in range(4):
      for j in range(4):
         while(True):
            try :
               c = int(input('빙고에 쓸 숫자를 쓰세요.(0~30 중복 x)'))
               if c >30 or c<0 :
                  print('말 좀 들으세요 0~30')
               elif u_bingo[0].count(c) == 1 :
                  print('말 좀 들어요 중복x')
               elif u_bingo[1].count(c) == 1 :
                  print('말 좀 들어요 중복x')
               elif u_bingo[2].count(c) == 1 :
                  print('말 좀 들어요 중복x')
               elif u_bingo[3].count(c) == 1 :
                  print('말 좀 들어요 중복x')
               else :
                  break
            except :
               print('숫자를 쓰세요 좀')
         u_bingo[i].append(c)
         if len(u_bingo[3]) == 4:
            uu_bingo = u_bingo[:]
            print('complete')
            print('게임을 시작할게요~')
         else :
            
            display_bingo(u_bingo)
   turn = 0
   first = True
   while(True):
      check = False
      win = False
      if turn == 0:
         if first ==True:
            
            display_com_bingo(cc_bingo)
            display_bingo(u_bingo)
            first =False
         while(True):
            try :
               your_num = int(input('It\'s your turn hit a number :'))
               if u_bingo[0].count(your_num) == 0 and u_bingo[1].count(your_num) == 0 and u_bingo[2].count(your_num) == 0 and u_bingo[3].count(your_num) == 0 :
                  print('숫자를 당신 빙고에서 고르세요')
               else :
                  u_bingo,cc_bingo,check, win = check_bingo(u_bingo,cc_bingo,your_num)
                  if win == True :
                     print('니가 이겼어요')
                     return
                  if check == True :
                     
                     display_bingo(u_bingo)
                     display_com_bingo(cc_bingo)
                     
                     print('computer have number %d kkkk'%your_num)
                     time.sleep(2)
                     turn = 1
                  elif check == False :
                     
                     display_com_bingo(cc_bingo)
                     display_bingo(u_bingo)
                     print('computer don\'t have number %d'%your_num)
                  break
            except :
               print('숫자를 쓰세요 쫌')
      if turn == 1 :
         num12 = 0 
         print('컴퓨터가 숫자를 고민중이에요')
         while(True):
            time.sleep(1)
            com_num = random.randint(0,15)
            col = com_num // 4
            row = com_num % 4
            if cc_bingo[col][row] == 'X':
               print('컴퓨터가 숫자를 고민중이에요')
            else :
               num12 = cc_bingo[col][row]
               break
         cc_bingo,u_bingo,check,win = check_bingo(cc_bingo,u_bingo,cc_bingo[col][row])
         if win == True:
            print('컴퓨터가 이겼어요')
            return
         if check == True :
            
            display_com_bingo(cc_bingo)
            display_bingo(u_bingo)
            print('Computer pick %s'%num12)
            print('Oh you have %s'%num12)
            turn = 0
         elif check == False :
            
            display_bingo(u_bingo)
            display_com_bingo(cc_bingo)
            
            print('Computer pick %s'%num12)
            print('You don\'t have number %s'%num12)

   
   
         
         
   
   
   

#game_select-------------------------------------------
def game_select():
   while(True):
      game = input('[1]야구게임 [2]업다운게임 [3]빙고게임 [4]게임종료')
      if game =='1' :
         baseball_game_start()
      elif game == '2' :
         up_down_game()
      elif game == '3' :
         bingo_game()
      elif game == '4' :
         return
      else :
         print('있는 얘들 중에 골라요 ^^')
game_select()

