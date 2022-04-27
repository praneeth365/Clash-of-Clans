from re import T
import time
from colorama import Fore, Back, Style
from src.Barbarians import Troops
from src.input import input_to
from src.King import King
from src.Barbarians import Troops
from src.Buildings import Buildings,Hut,TownHall,WizardTower
from src.Canon import Canons
from src.AerialTroop import Ballons
from src.archer import Archer
from src.queen import Queen
import os


canon_symbol="\U0001F4A3"
king_symbol="\U0001F934"
hut_symbol="\U0001F3E0"
building_symbol="\U0001F3E2"
spark_symbol="\U00012728"
tower_symbol="\U0001F5FC"
ballon_symbol="\U0001F388"
archer_symbol="\U0001F3F9"
queen_symbol="\U0001F478"
start_time=time.time()
current_attacks=[]
cnt1=0
cnt2=0
cnt3=0
game_done=False
Win=False


def do_health(king_flag):
    num=king.health
    if(king_flag==False):
        num=queen.health
    healthDashes=50
    dashConvert = num/healthDashes      
    print("|",end="")

    for i in range(20):
        if(i<dashConvert):
            print(Back.GREEN,end="")
            print(" ",end="")
            print(Style.RESET_ALL,end="")
        else:
            print(" ",end="")
    print("|") 


def distance(a,b):
    return abs(a.x-b.x)+abs(a.y-b.y)
  

def king_attack():
    if(king.attack==False and king.start_attack==True):
        attack=False
        if(distance(king,hut1)==2):
            attack=True
            king.current_attack=1
        elif(distance(king,hut2)==2):
            attack=True
            king.current_attack=2
        elif(distance(king,hut3)==2):
            attack=True
            king.current_attack=3
        elif(distance(king,hut4)==2):
            attack=True
            king.current_attack=4
        elif(distance(king,hut5)==2):
            attack=True
            king.current_attack=5
        elif(king.x<=3 and king.x>=-5 and king.y<=3 and king.y>=-7):
            attack=True 
            king.current_attack=6  
        elif(distance(king,canon1)<=2):
            attack=True
            king.current_attack=7
        elif(distance(king,canon2)<=2):
            attack=True
            king.current_attack=8       
        elif(distance(king,canon3)<=2):
            attack=True
            king.current_attack=9    
        elif(distance(king,canon4)<=2):
            attack=True
            king.current_attack=10
        elif(distance(king,tower1)<=2):
            attack=True 
            king.current_attack=11   
        elif(distance(king,tower2)<=2):
            attack=True 
            king.current_attack=12              
        if(attack==True):
            king.attack=True    
    elif(king.attack==True):
        if(king.current_attack==1):
            if(hut1.health<=0 or distance(hut1,king)!=2 ):
                king.current_attack=-1
                king.attack=False
                king.start_attack=False
            else:
                hut1.update_health(king.damage)          
        elif(king.current_attack==2):
            if(hut2.health<=0 or distance(hut2,king)!=2):
                king.current_attack=-1
                king.attack=False
                king.start_attack=False
            else:
                hut2.update_health(king.damage)  
        elif(king.current_attack==3):
            if(hut3.health<=0 or distance(hut3,king)!=2):
                king.current_attack=-1
                king.attack=False
                king.start_attack=False
            else:
                hut3.update_health(king.damage) 
        elif(king.current_attack==4):
            if(hut4.health<=0 or distance(hut4,king)!=2):
                king.current_attack=-1
                king.attack=False
                king.start_attack=False
            else:
                hut4.update_health(king.damage) 
        elif(king.current_attack==5):
            if(hut5.health<=0 or distance(hut5,king)!=2):
                king.current_attack=-1
                king.attack=False
                king.start_attack=False
            else:
                hut5.update_health(king.damage)
        elif(king.current_attack==6):
            if(townhall.health<=0 or king.x>3 or king.x<-5 or king.y>3 or king.y<-7):
                king.current_attack=-1
                king.attack=False
                king.start_attack=False
            else:
                townhall.update_health(king.damage)  
        elif(king.current_attack==7):
            if(canon1.health<=0 or distance(canon1,king)!=2):
                king.current_attack=-1
                king.attack=False
                king.start_attack=False
            else:
                canon1.update_health(king.damage)
        elif(king.current_attack==8):
            if(canon2.health<=0 or distance(canon2,king)!=2):
                king.current_attack=-1
                king.attack=False
                king.start_attack=False
            else:
                canon2.update_health(king.damage)     
        elif(king.current_attack==9):
            if(canon3.health<=0 or distance(canon3,king)!=2):
                king.current_attack=-1
                king.attack=False
                king.start_attack=False
            else:
                canon3.update_health(king.damage)
        elif(king.current_attack==10):
            if(canon4.health<=0 or distance(canon4,king)!=2):
                king.current_attack=-1
                king.attack=False
                king.start_attack=False
            else:
                canon4.update_health(king.damage)
        elif(king.current_attack==11):
            if(tower1.health<=0 or distance(tower1,king)!=2):
                king.current_attack=-1
                king.attack=False
                king.start_attack=False
            else:
                tower1.update_health(king.damage)
        elif(king.current_attack==12):
            if(tower2.health<=0 or distance(tower2,king)!=2):
                king.current_attack=-1
                king.attack=False
                king.start_attack=False
            else:
                tower2.update_health(king.damage)    

def fun(queen,a):
    x1=-100
    y1=-100
    if(queen.last_move=="w"):
        x1=queen.x
        y1=queen.y+16
    elif(queen.last_move=="a"):
        x1=queen.x-16
        y1=queen.y
    elif(queen.last_move=="s"):
        x1=queen.x
        y1=queen.y-16
    elif(queen.last_move=="d"):
        x1=queen.x+16
        y1=queen.y

    if(a.name=="Town Hall"):
            if((abs(x1+3)<=4 and abs(y1-1)<=4 )or (abs(x1+1)<=4 and abs(y1-1)<=4 ) or (abs(x1-1)<=4 and abs(y1-1)<=4 ) or (abs(x1+1)<=4 and abs(y1+1)<=4 ) or (abs(x1+1)<=4 and abs(y1+3)<=4 ) or (abs(x1+1)<=4 and abs(y1+5)<=4 )):
                return True
            else:
                return False    
    else:
        if(abs(x1-a.x)<=4 and abs(y1-a.y)<=4):
            return True
        else:
            return False    


def queen_attack():
    global current_attacks
    if(queen.attack==False and queen.start_attack==True):
        attack=False
        if(fun(queen,hut1)):
            attack=True
            queen.current_attack=1
            current_attacks.append(1)
        if(fun(queen,hut2)):
            attack=True
            queen.current_attack=2
            current_attacks.append(2)
        if(fun(queen,hut3)):
            attack=True
            queen.current_attack=3
            current_attacks.append(3)
        if(fun(queen,hut4)):
            attack=True
            queen.current_attack=4
            current_attacks.append(4)
        if(fun(queen,hut5)):
            attack=True
            queen.current_attack=5
            current_attacks.append(5)
        if(fun(queen,townhall)):
            attack=True 
            queen.current_attack=6 
            current_attacks.append(6) 
        if(fun(queen,canon1)):
            attack=True
            queen.current_attack=7
            current_attacks.append(7)
        if(fun(queen,canon2)):
            attack=True
            queen.current_attack=8
            current_attacks.append(8)       
        if(fun(queen,canon3)):
            attack=True
            queen.current_attack=9
            current_attacks.append(9)    
        if(fun(queen,canon4)):
            attack=True
            queen.current_attack=10
            current_attacks.append(10)
        if(fun(queen,tower1)):
            attack=True 
            queen.current_attack=11
            current_attacks.append(11)   
        if(fun(queen,tower2)):
            attack=True 
            queen.current_attack=12
            current_attacks.append(12)                
        if(attack==True):
            queen.attack=True  
        print(queen.attack)          
    elif(queen.attack==True):
        print(current_attacks)
        print("ppv")
        if 1 in current_attacks:
            if(hut1.health<=0 or fun(queen,hut1)==False):
                current_attacks.remove(1)
            else:
                hut1.update_health(queen.damage)          
        if 2 in current_attacks:
            if(hut2.health<=0 or fun(queen,hut2)==False):
                current_attacks.remove(2)                
            else:
                hut2.update_health(queen.damage)  
        if 3 in current_attacks:
            if(hut3.health<=0 or fun(queen,hut3)==False):
                current_attacks.remove(3)
            else:
                hut3.update_health(queen.damage) 
        if 4 in current_attacks:
            print("ppv")
            if(hut4.health<=0 or fun(queen,hut4)==False):
                current_attacks.remove(4)
            else:
                hut4.update_health(queen.damage)  
        if 5 in current_attacks:
            if(hut5.health<=0 or fun(queen,hut5)==False):
                current_attacks.remove(5)
            else:
                hut5.update_health(queen.damage) 
        if 6 in current_attacks:
            if(townhall.health<=0 or fun(queen,townhall)==False):
                current_attacks.remove(6)
            else:
                townhall.update_health(king.damage)  
        if 7 in current_attacks:
            if(canon1.health<=0 or fun(queen,canon1)==False):
                current_attacks.remove(7)
            else:
                canon1.update_health(queen.damage)
        if 8 in current_attacks:
            if(canon2.health<=0 or fun(queen,canon2)==False):
                current_attacks.remove(8)
            else:
                canon2.update_health(queen.damage)    
        if 9 in current_attacks:
            if(canon3.health<=0 or fun(queen,canon3)==False):
                current_attacks.remove(9)
            else:
                canon3.update_health(queen.damage) 
        if 10 in current_attacks:
            if(canon4.health<=0 or fun(queen,canon4)==False):
                current_attacks.remove(10)
            else:
                canon4.update_health(queen.damage) 
        if 11 in current_attacks:
            if(tower1.health<=0 or fun(queen,tower1)==False):
                current_attacks.remove(11)
            else:
                tower1.update_health(queen.damage)
        if 12 in current_attacks:
            if(tower2.health<=0 or fun(queen,tower2)==False):
                current_attacks.remove(12)
            else:
                tower2.update_health(queen.damage) 
        print(current_attacks)
        print(fun(queen,hut4))
        if(len(current_attacks)==0):
            queen.attack=False   
            queen.start_attack=False     

def tower_attack(a):
    range=a.range
    attack_x=-100
    attack_y=-100        
    if(a.alive==True and ballon1.alive==True and abs(a.x-ballon1.x)<=2*a.range and abs(a.y-ballon1.y)<=2*a.range):
        attack_x=ballon1.x
        attack_y=ballon1.y
        ballon1.update_health(a.damage)
    elif(a.alive==True and ballon2.alive==True and abs(a.x-ballon2.x)<=2*a.range and abs(a.y-ballon2.y)<=2*a.range):
        attack_x=ballon2.x
        attack_y=ballon2.y
        ballon2.update_health(a.damage)    
    elif(a.alive==True and troop11.alive==True and abs(a.x-troop11.x)<=2*a.range and abs(a.y-troop11.y)<=2*range):
        attack_x=troop11.x
        attack_y=troop11.y
        troop11.update_health(a.damage)
    elif(a.alive==True and troop12.alive==True and abs(a.x-troop12.x)<=2*a.range and abs(a.y-troop12.y)<=2*range):
        attack_x=troop12.x
        attack_y=troop12.y
        troop12.update_health(a.damage)
    elif(a.alive==True and troop13.alive==True and abs(a.x-troop13.x)<=2*a.range and abs(a.y-troop13.y)<=2*range):
        attack_x=troop13.x
        attack_y=troop13.y
        troop13.update_health(a.damage)
    elif(a.alive==True and troop14.alive==True and abs(a.x-troop14.x)<=2*a.range and abs(a.y-troop14.y)<=2*range):
        attack_x=troop14.x
        attack_y=troop14.y
        troop14.update_health(a.damage)
    elif(a.alive==True and troop15.alive==True and abs(a.x-troop15.x)<=2*a.range and abs(a.y-troop15.y)<=2*range):
        attack_x=troop15.x
        attack_y=troop15.y
        troop15.update_health(a.damage)                                
    elif(a.alive==True and troop21.alive==True and abs(a.x-troop21.x)<=2*a.range and abs(a.y-troop21.y)<=2*range):
        attack_x=troop21.x
        attack_y=troop21.y
        troop21.update_health(a.damage)
    elif(a.alive==True and troop22.alive==True and abs(a.x-troop22.x)<=2*a.range and abs(a.y-troop22.y)<=2*range):
        attack_x=troop22.x
        attack_y=troop22.y
        troop22.update_health(a.damage)
    elif(a.alive==True and troop23.alive==True and abs(a.x-troop23.x)<=2*a.range and abs(a.y-troop23.y)<=2*range):
        attack_x=troop23.x
        attack_y=troop23.y 
        troop23.update_health(a.damage)
    elif(a.alive==True and troop24.alive==True and abs(a.x-troop24.x)<=2*a.range and abs(a.y-troop24.y)<=2*range):
        attack_x=troop24.x
        attack_y=troop24.y
        troop24.update_health(a.damage)
    elif(a.alive==True and troop25.alive==True and abs(a.x-troop25.x)<=2*canon1.range and abs(a.y-troop25.y)<=2*range):
        attack_x=troop25.x
        attack_y=troop25.y
        troop25.update_health(a.damage)                                
    elif(a.alive==True and troop31.alive==True and abs(a.x-troop31.x)<=2*a.range and abs(a.y-troop31.y)<=2*range):
        attack_x=troop31.x
        attack_y=troop31.y
        troop31.update_health(a.damage) 
    elif(a.alive==True and troop32.alive==True and abs(a.x-troop32.x)<=2*a.range and abs(a.y-troop32.y)<=2*range):
        attack_x=troop32.x
        attack_y=troop32.y
        troop32.update_health(a.damage)
    elif(a.alive==True and troop33.alive==True and abs(a.x-troop33.x)<=2*a.range and abs(a.y-troop33.y)<=2*range):
        attack_x=troop33.x
        attack_y=troop33.y
        troop33.update_health(a.damage)
    elif(a.alive==True and troop34.alive==True and abs(a.x-troop34.x)<=2*a.range and abs(a.y-troop34.y)<=2*range):
        attack_x=troop34.x
        attack_y=troop34.y
        troop34.update_health(a.damage)
    elif(a.alive==True and troop35.alive==True and abs(a.x-troop35.x)<=2*a.range and abs(a.y-troop35.y)<=2*range):
        attack_x=troop35.x
        attack_y=troop35.y
        troop35.update_health(a.damage)  
    elif(a.alive==True and king.alive==True and abs(a.x-king.x)<=2*a.range and abs(a.y-king.y)<=2*range):
        attack_x=king.x
        attack_y=king.y
        king.update_health(a.damage)  
    elif(a.alive==True and queen.alive==True and abs(a.x-queen.x)<=2*a.range and abs(a.y-queen.y)<=2*range):
        attack_x=queen.x
        attack_y=queen.y
        queen.update_health(a.damage)
    elif(a.alive==True and archer1.alive==True and abs(a.x-archer1.x)<=2*a.range and abs(a.y-archer1.y)<=2*range):
        attack_x=archer1.x
        attack_y=archer1.y
        archer1.update_health(a.damage) 
    elif(a.alive==True and archer2.alive==True and abs(a.x-archer2.x)<=2*a.range and abs(a.y-archer2.y)<=2*range):
        attack_x=archer2.x
        attack_y=archer2.y
        archer2.update_health(a.damage) 
    elif(a.alive==True and archer3.alive==True and abs(a.x-archer3.x)<=2*a.range and abs(a.y-archer3.y)<=2*range):
        attack_x=archer3.x
        attack_y=archer3.y
        archer3.update_health(a.damage)                                        

    if(attack_x==-100 and attack_y==-100):
        return 0
    else:
        if(king.alive==True and abs(king.x-attack_x)<=2 and abs(king.y-attack_y)<=2):
            king.update_health(a.damage)
        if(troop11.alive==True and abs(troop11.x-attack_x)<=2 and abs(troop11.y-attack_y)<=2):
            troop11.update_health(a.damage)
        if(troop12.alive==True and abs(troop12.x-attack_x)<=2 and abs(troop12.y-attack_y)<=2):
            troop12.update_health(a.damage)            
        if(troop13.alive==True and abs(troop13.x-attack_x)<=2 and abs(troop13.y-attack_y)<=2):
            troop13.update_health(a.damage)
        if(troop14.alive==True and abs(troop14.x-attack_x)<=2 and abs(troop14.y-attack_y)<=2):
            troop14.update_health(a.damage)
        if(troop15.alive==True and abs(troop15.x-attack_x)<=2 and abs(troop15.y-attack_y)<=2):
            troop15.update_health(a.damage)
        if(troop21.alive==True and abs(troop21.x-attack_x)<=2 and abs(troop21.y-attack_y)<=2):
            troop21.update_health(a.damage)
        if(troop22.alive==True and abs(troop22.x-attack_x)<=2 and abs(troop22.y-attack_y)<=2):
            troop22.update_health(a.damage)            
        if(troop23.alive==True and abs(troop23.x-attack_x)<=2 and abs(troop23.y-attack_y)<=2):
            troop23.update_health(a.damage)
        if(troop24.alive==True and abs(troop24.x-attack_x)<=2 and abs(troop24.y-attack_y)<=2):
            troop24.update_health(a.damage)
        if(troop25.alive==True and abs(troop25.x-attack_x)<=2 and abs(troop25.y-attack_y)<=2):
            troop25.update_health(a.damage)
        if(troop31.alive==True and abs(troop31.x-attack_x)<=2 and abs(troop31.y-attack_y)<=2):
            troop31.update_health(a.damage)
        if(troop32.alive==True and abs(troop32.x-attack_x)<=2 and abs(troop32.y-attack_y)<=2):
            troop32.update_health(a.damage)            
        if(troop33.alive==True and abs(troop33.x-attack_x)<=2 and abs(troop33.y-attack_y)<=2):
            troop33.update_health(a.damage)
        if(troop34.alive==True and abs(troop34.x-attack_x)<=2 and abs(troop34.y-attack_y)<=2):
            troop34.update_health(a.damage)
        if(troop35.alive==True and abs(troop35.x-attack_x)<=2 and abs(troop35.y-attack_y)<=2):
            troop35.update_health(a.damage) 
        if(ballon1.alive==True and abs(ballon1.x-attack_x)<=2 and abs(ballon1.y-attack_y)<=2):
            ballon1.update_health(a.damage)
        if(ballon2.alive==True and abs(ballon2.x-attack_x)<=2 and abs(ballon2.y-attack_y)<=2):
            ballon2.update_health(a.damage) 
        if(queen.alive==True and abs(queen.x-attack_x)<=2 and abs(queen.y-attack_y)<=2):
            queen.update_health(a.damage)
        if(archer1.alive==True and abs(archer1.x-attack_x)<=2 and abs(archer1.y-attack_y)<=2):
            archer1.update_health(a.damage)
        if(archer2.alive==True and abs(archer2.x-attack_x)<=2 and abs(archer2.y-attack_y)<=2):
            archer2.update_health(a.damage)
        if(archer3.alive==True and abs(archer3.x-attack_x)<=2 and abs(archer3.y-attack_y)<=2):
            archer3.update_health(a.damage)                                                                      


def ballon_attack(a):
    if(a.alive==True):
        flag=False
        if(canon1.alive==False and canon2.alive==False and canon3.alive==False and canon4.alive==False and tower1.alive==False and tower2.alive==False):
            flag=True
            a.name="barbarian"
        if(flag):
            barbarian_attack(a)/home
        else:
            if(abs(a.x-a.destination_x)+abs(a.y-a.destination_y)==2):
                a.attack=True
            if(a.attack_complete==True):
                calculate_destination(a)
                a.attack_complete=False
                a.attack=False
            elif(a.attack==False and abs(a.x-a.destination_x)+abs(a.y-a.destination_y)>2):
                if(a.destination_y<a.y):
                    a.y=a.y-2
                    a.timer=0
                    a.start_time=time.time()
                elif(a.destination_y>a.y):
                    a.y=a.y+2
                    a.timer=0
                    a.start_time=time.time()
                else:
                    if(a.destination_x<a.x):
                        a.x=a.x-2
                        a.timer=king.health0
                        a.start_time=time.time()
                    elif(a.destination_x>a.x):
                        a.x=a.x+2
                        a.timer=0
                        a.start_time=time.time()   
            else:
                if(tower1.alive==True and tower1.x==a.destination_x and tower1.y==a.destination_y):
                    tower1.update_health(a.damage)
                    if(tower1.alive==False):
                        a.attack_complete=True
                elif(tower2.alive==True and tower2.x==a.destination_x and tower2.y==a.destination_y):
                    tower2.update_health(a.damage)
                    if(tower2.alive==False):
                        a.attack_complete=True
                elif(canon1.alive==True and canon1.x==a.destination_x and canon1.y==a.destination_y):
                    canon1.update_health(a.damage)
                    if(canon1.alive==False):
                        a.attack_complete=True
                elif(canon2.alive==True and canon2.x==a.destination_x and canon2.y==a.destination_y):
                    canon2.update_health(a.damage)
                    if(canon2.alive==False):
                        a.attack_complete=True
                elif(canon3.alive==True and canon3.x==a.destination_x and canon3.y==a.destination_y):
                    canon3.update_health(a.damage)
                    if(canon3.alive==False):
                        a.attack_complete=True
                elif(canon4.alive==True and canon4.x==a.destination_x and canon4.y==a.destination_y):
                    canon4.update_health(a.damage)
                    if(canon4.alive==False):
                        a.attack_complete=True 
                else:
                    a.attack_complete=True                                                                                                               



def healthdisplay(a,x):
    if(a.health>=x/2):
        print(Back.GREEN,end="")
    elif(a.health<=x/2 and a.health>=x/5):
        print(Back.YELLOW,end="")
    else:
        print(Back.RED,end="")           

def calculate_destination(a):
    shortest_x=-100
    shortest_y=100
    shortest_distance=1000
    flag=True
    if(a.name=="ballon"):
        flag=False
    if(canon1.alive==True):
        if(shortest_distance>distance(canon1,a)):
            shortest_distance=distance(canon1,a)
            shortest_x=canon1.x
            shortest_y=canon1.y
    if(canon2.alive==True):
        if(shortest_distance>distance(canon2,a)):
            shortest_distance=distance(canon2,a)
            shortest_x=canon2.x
            shortest_y=canon2.y
    if(canon3.alive==True):
        if(shortest_distance>distance(canon3,a)):
            shortest_distance=distance(canon3,a)
            shortest_x=canon3.x
            shortest_y=canon3.y
    if(canon4.alive==True):
        if(shortest_distance>distance(canon4,a)):
            shortest_distance=distance(canon4,a)
            shortest_x=canon4.x
            shortest_y=canon4.y
    if(tower1.alive==True):
        if(shortest_distance>distance(tower1,a)):
            shortest_distance=distance(tower1,a)
            shortest_x=tower1.x
            shortest_y=tower1.y
    if(tower2.alive==True):
        if(shortest_distance>distance(tower2,a)):
            shortest_distance=distance(tower2,a)
            shortest_x=tower2.x
            shortest_y=tower2.y                                                            
    if(flag and hut1.alive==True):
        if(shortest_distance>distance(hut1,a)):
            shortest_distance=distance(hut1,a)
            shortest_x=hut1.x
            shortest_y=hut1.y
    if(flag and hut2.alive==True):
        if(shortest_distance>distance(hut2,a)):
            shortest_distance=distance(hut2,a)
            shortest_x=hut2.x
            shortest_y=hut2.y
    if(flag and hut3.alive==True):
        if(shortest_distance>distance(hut3,a)):
            shortest_distance=distance(hut3,a)
            shortest_x=hut3.x
            shortest_y=hut3.y
    if(flag and hut4.alive==True):
        if(shortest_distance>distance(hut4,a)):
            shortest_distance=distance(hut4,a)
            shortest_x=hut4.x
            shortest_y=hut4.y
    if(flag and hut5.alive==True):
        if(shortest_distance>distance(hut5,a)):
            shortest_distance=distance(hut5,a)
            shortest_x=hut5.x
            shortest_y=hut5.y
    if(flag and townhall.alive==True):
        if(abs(a.x+3)+abs(a.y-1)<shortest_distance):
            shortest_distance=abs(a.x+3)+abs(a.y-1)
            shortest_x=-3
            shortest_y=1
        if(abs(a.x+3)+abs(a.y+1)<shortest_distance):
            shortest_distance=abs(a.x+3)+abs(a.y+1)
            shortest_x=-3
            shortest_y=-1 
        if(abs(a.x+3)+abs(a.y+3)<shortest_distance):
            shortest_distance=abs(a.x+3)+abs(a.y+3)
            shortest_x=-3
            shortest_y=-3                       
        if(abs(a.x+3)+abs(a.y+5)<shortest_distance):
            shortest_distance=abs(a.x+3)+abs(a.y+5)
            shortest_x=-3
            shortest_y=-5
        if(abs(a.x+1)+abs(a.y-1)<shortest_distance):
            shortest_distance=abs(a.x+1)+abs(a.y-1)
            shortest_x=-1
            shortest_y=1
        if(abs(a.x+1)+abs(a.y+1)<shortest_distance):
            shortest_distance=abs(a.x+1)+abs(a.y+1)
            shortest_x=-1
            shortest_y=-1 
        if(abs(a.x+1)+abs(a.y+3)<shortest_distance):
            shortest_distance=abs(a.x+1)+abs(a.y+3)
            shortest_x=-1
            shortest_y=-3                       
        if(abs(a.x+1)+abs(a.y+5)<shortest_distance):
            shortest_distance=abs(a.x+1)+abs(a.y+5)
            shortest_x=-1
            shortest_y=-5
        if(abs(a.x-1)+abs(a.y-1)<shortest_distance):
            shortest_distance=abs(a.x-1)+abs(a.y-1)
            shortest_x=1
            shortest_y=1
        if(abs(a.x-1)+abs(a.y+1)<shortest_distance):
            shortest_distance=abs(a.x-1)+abs(a.y+1)
            shortest_x=1
            shortest_y=-1 
        if(abs(a.x-1)+abs(a.y+3)<shortest_distance):
            shortest_distance=abs(a.x-1)+abs(a.y+3)
            shortest_x=1
            shortest_y=-3                       
        if(abs(a.x-1)+abs(a.y+5)<shortest_distance):
            shortest_distance=abs(a.x-1)+abs(a.y+5)
            shortest_x=1
            shortest_y=-5 

    a.destination_x=shortest_x
    a.destination_y=shortest_y 
    

def barbarian_attack(a):
    if(a.alive==True):
        if(abs(a.x-a.destination_x)<=2 and abs(a.y-a.destination_y)<=2):
            a.attack=True
        if(a.attack_complete==True):
            calculate_destination(a)
            a.attack_complete=False
            a.attack=False
        elif(a.attack==False and (abs(a.x-a.destination_x)>2 or abs(a.y-a.destination_y)>2) ):
            if(a.destination_y<a.y):
                a.y=a.y-2
                a.timer=0
                a.start_time=time.time()
            elif(a.destination_y>a.y):
                a.y=a.y+2
                a.timer=0
                a.start_time=time.time()

            if(a.destination_x<a.x):
                a.x=a.x-2
                a.timer=0
                a.start_time=time.time()
            elif(a.destination_x>a.x):
                a.x=a.x+2
                a.timer=0
                a.start_time=time.time()
        else:
            if(canon1.alive==True and canon1.x==a.destination_x and canon1.y==a.destination_y):
                canon1.update_health(a.damage)
                if(canon1.alive==False):
                    a.attack_complete=True
            elif(canon2.alive==True and canon2.x==a.destination_x and canon2.y==a.destination_y):
                canon2.update_health(a.damage)
                if(canon2.alive==False):
                    a.attack_complete=True
            elif(canon3.alive==True and canon3.x==a.destination_x and canon3.y==a.destination_y):
                canon3.update_health(a.damage)
                if(canon3.alive==False):
                    a.attack_complete=True
            elif(canon4.alive==True and canon4.x==a.destination_x and canon4.y==a.destination_y):
                canon4.update_health(a.damage)
                if(canon4.alive==False):
                    a.attack_complete=True
            elif(hut1.alive==True and hut1.x==a.destination_x and hut1.y==a.destination_y):
                hut1.update_health(a.damage)
                if(hut1.alive==False):
                    a.attack_complete=True
            elif(hut2.alive==True and hut2.x==a.destination_x and hut2.y==a.destination_y):
                hut2.update_health(a.damage)
                if(hut2.alive==False):
                    a.attack_complete=True
            elif(hut3.alive==True and hut3.x==a.destination_x and hut3.y==a.destination_y):
                hut3.update_health(a.damage)
                if(hut3.alive==False):
                    a.attack_complete=True
            elif(hut4.alive==True and hut4.x==a.destination_x and hut4.y==a.destination_y):
                hut4.update_health(a.damage)
                if(hut4.alive==False):
                    a.attack_complete=True
            elif(hut5.alive==True and hut5.x==a.destination_x and hut5.y==a.destination_y):
                hut5.update_health(a.damage)
                if(hut5.alive==False):
                    a.attack_complete=True 
            elif(townhall.alive==True and a.x<=3 and a.x>=-5 and a.y>=-7 and a.y<=3):
                townhall.update_health(a.damage)
                if(townhall.alive==False):
                    a.attack_complete=True
            elif(tower1.alive==True and tower1.x==a.destination_x and tower1.y==a.destination_y):
                tower1.update_health(a.damage)
                if(tower1.alive==False):
                    a.attack_complete=True
            elif(tower2.alive==True and tower2.x==a.destination_x and tower2.y==a.destination_y):
                tower2.update_health(a.damage)
                if(tower2.alive==False):
                    a.attack_complete=True                            
            else:
                a.attack_complete=True   


def archer_attack(a):
    if(a.alive==True):
        if(abs(a.x-a.destination_x)<=2*a.range and abs(a.y-a.destination_y)<=2*a.range):
            a.attack=True
        if(a.attack_complete==True):
            calculate_destination(a)
            a.attack_complete=False
            a.attack=False
        elif(a.attack==False and (abs(a.x-a.destination_x)>2 or abs(a.y-a.destination_y)>2) ):
            if(a.destination_y<a.y):
                a.y=a.y-2
                a.timer=0
                a.start_time=time.time()
            elif(a.destination_y>a.y):
                a.y=a.y+2
                a.timer=0
                a.start_time=time.time()

            if(a.destination_x<a.x):
                a.x=a.x-2
                a.timer=0
                a.start_time=time.time()
            elif(a.destination_x>a.x):
                a.x=a.x+2
                a.timer=0
                a.start_time=time.time()
        else:
            if(canon1.alive==True and canon1.x==a.destination_x and canon1.y==a.destination_y):
                canon1.update_health(a.damage)
                if(canon1.alive==False):
                    a.attack_complete=True
            elif(canon2.alive==True and canon2.x==a.destination_x and canon2.y==a.destination_y):
                canon2.update_health(a.damage)
                if(canon2.alive==False):
                    a.attack_complete=True
            elif(canon3.alive==True and canon3.x==a.destination_x and canon3.y==a.destination_y):
                canon3.update_health(a.damage)
                if(canon3.alive==False):
                    a.attack_complete=True
            elif(canon4.alive==True and canon4.x==a.destination_x and canon4.y==a.destination_y):
                canon4.update_health(a.damage)
                if(canon4.alive==False):
                    a.attack_complete=True
            elif(hut1.alive==True and hut1.x==a.destination_x and hut1.y==a.destination_y):
                hut1.update_health(a.damage)
                if(hut1.alive==False):
                    a.attack_complete=True
            elif(hut2.alive==True and hut2.x==a.destination_x and hut2.y==a.destination_y):
                hut2.update_health(a.damage)
                if(hut2.alive==False):
                    a.attack_complete=True
            elif(hut3.alive==True and hut3.x==a.destination_x and hut3.y==a.destination_y):
                hut3.update_health(a.damage)
                if(hut3.alive==False):
                    a.attack_complete=True
            elif(hut4.alive==True and hut4.x==a.destination_x and hut4.y==a.destination_y):
                hut4.update_health(a.damage)
                if(hut4.alive==False):
                    a.attack_complete=True
            elif(hut5.alive==True and hut5.x==a.destination_x and hut5.y==a.destination_y):
                hut5.update_health(a.damage)
                if(hut5.alive==False):
                    a.attack_complete=True 
            elif(townhall.alive==True and a.x<=3 and a.x>=-5 and a.y>=-7 and a.y<=3):
                townhall.update_health(a.damage)
                if(townhall.alive==False):
                    a.attack_complete=True
            elif(tower1.alive==True and tower1.x==a.destination_x and tower1.y==a.destination_y):
                tower1.update_health(a.damage)
                if(tower1.alive==False):
                    a.attack_complete=True
            elif(tower2.alive==True and tower2.x==a.destination_x and tower2.y==a.destination_y):
                tower2.update_health(a.damage)
                if(tower2.alive==False):
                    a.attack_complete=True                            
            else:
                a.attack_complete=True



def heal_spell(a,h):
    if(a.alive==True and a.num_heal<=2):
        a.num_heal+=1
        if((a.health*3)/2<=h):
            a.health=(a.health*3)/2
        else:
            a.health=h


def rage_spell(a):
    if(a.alive==True and a.num_rage<=2):
        a.num_rage+=1
        a.damage=a.damage*2
        a.speed=a.speed*2


def canon_attack(a):
    range=a.range
    if(a.alive==True and king.alive==True and abs(a.x-king.x)<=2*a.range and abs(a.y-king.y)<=2*range):
        king.update_health(a.damage)
    elif(a.alive==True and queen.alive==True and abs(a.x-queen.x)<=2*a.range and abs(a.y-queen.y)<=2*range):
        queen.update_health(a.damage)                               
    elif(a.alive==True and troop11.alive==True and abs(a.x-troop11.x)<=2*a.range and abs(a.y-troop11.y)<=2*range):
        troop11.update_health(a.damage)
    elif(a.alive==True and troop12.alive==True and abs(a.x-troop12.x)<=2*a.range and abs(a.y-troop12.y)<=2*range):
        troop12.update_health(a.damage)
    elif(a.alive==True and troop13.alive==True and abs(a.x-troop13.x)<=2*a.range and abs(a.y-troop13.y)<=2*range):
        troop13.update_health(a.damage)
    elif(a.alive==True and troop14.alive==True and abs(a.x-troop14.x)<=2*a.range and abs(a.y-troop14.y)<=2*range):
        troop14.update_health(a.damage)
    elif(a.alive==True and troop15.alive==True and abs(a.x-troop15.x)<=2*a.range and abs(a.y-troop15.y)<=2*range):
        troop15.update_health(a.damage)                                
    elif(a.alive==True and troop21.alive==True and abs(a.x-troop21.x)<=2*a.range and abs(a.y-troop21.y)<=2*range):
        troop21.update_health(a.damage)
    elif(a.alive==True and troop22.alive==True and abs(a.x-troop22.x)<=2*a.range and abs(a.y-troop22.y)<=2*range):
        troop22.update_health(a.damage)
    elif(a.alive==True and troop23.alive==True and abs(a.x-troop23.x)<=2*a.range and abs(a.y-troop23.y)<=2*range):
        troop23.update_health(a.damage)
    elif(a.alive==True and troop24.alive==True and abs(a.x-troop24.x)<=2*a.range and abs(a.y-troop24.y)<=2*range):
        troop24.update_health(a.damage)
    elif(a.alive==True and troop25.alive==True and abs(a.x-troop25.x)<=2*canon1.range and abs(a.y-troop25.y)<=2*range):
        troop25.update_health(a.damage)                                
    elif(a.alive==True and troop31.alive==True and abs(a.x-troop31.x)<=2*a.range and abs(a.y-troop31.y)<=2*range):
        troop31.update_health(a.damage) 
    elif(a.alive==True and troop32.alive==True and abs(a.x-troop32.x)<=2*a.range and abs(a.y-troop32.y)<=2*range):
        troop32.update_health(a.damage)
    elif(a.alive==True and troop33.alive==True and abs(a.x-troop33.x)<=2*a.range and abs(a.y-troop33.y)<=2*range):
        troop33.update_health(a.damage)
    elif(a.alive==True and troop34.alive==True and abs(a.x-troop34.x)<=2*a.range and abs(a.y-troop34.y)<=2*range):
        troop34.update_health(a.damage)
    elif(a.alive==True and troop35.alive==True and abs(a.x-troop35.x)<=2*a.range and abs(a.y-troop35.y)<=2*range):
        troop35.update_health(a.damage)
    elif(a.alive==True and archer1.alive==True and abs(a.x-archer1.x)<=2*range and abs(a.y-archer1.y)<=2*range):
        archer1.update_health(a.damage)
    elif(a.alive==True and archer2.alive==True and abs(a.x-archer2.x)<=2*range and abs(a.y-archer2.y)<=2*range):
        archer2.update_health(a.damage)
    elif(a.alive==True and archer3.alive==True and abs(a.x-archer3.x)<=2*range and abs(a.y-archer3.y)<=2*range):
        archer3.update_health(a.damage)                                                     


def Game_done():
    global game_done
    global Win
    if(townhall.alive==False and canon1.alive==False and canon2.alive==False and canon3.alive==False and canon4.alive==False and hut1.alive==False and hut2.alive==False and hut3.alive==False and hut4.alive==False and hut5.alive==False and tower1.health<=0 and tower2.health<=0):
        game_done=True
        Win=True
    elif(king.alive==False and troop11.health<=0 and troop12.health<=0 and troop13.health<=0 and troop14.health<=0 and troop15.health<=0 and troop21.health<=0 and troop22.health<=0 and troop23.health<=0 and troop24.health<=0 and troop25.health<=0 and troop31.health<=0 and troop32.health<=0 and troop33.health<=0 and troop34.health<=0 and troop35.health<=0 and ballon1.health<=0 and ballon2.health<=0 and queen.health<=0 and archer1.health<=0 and archer2.health<=0 and archer3.health<=0):    
        game_done=True
        Win=False


def display(king_flag):
    rows=40
    columns=40
    canon_attack(canon1)
    canon_attack(canon2)
    canon_attack(canon3)
    canon_attack(canon4) 
    tower_attack(tower1)
    tower_attack(tower2) 
    archer_attack(archer1)
    archer_attack(archer2)
    archer_attack(archer3)
    king_attack()
    queen_attack()
    barbarian_attack(troop11)
    barbarian_attack(troop12)
    barbarian_attack(troop13)
    barbarian_attack(troop14)
    barbarian_attack(troop15)
    barbarian_attack(troop21)
    barbarian_attack(troop22)
    barbarian_attack(troop23)
    barbarian_attack(troop24)
    barbarian_attack(troop25)
    barbarian_attack(troop31)
    barbarian_attack(troop32) 
    barbarian_attack(troop33) 
    barbarian_attack(troop34) 
    barbarian_attack(troop35)
    ballon_attack(ballon1)
    ballon_attack(ballon2)                     
    for y in range(rows//2+1,-(rows//2),-1):
        for x in range(-(columns//2),columns//2+1,1):
            if(ballon1.alive==True and x==ballon1.x and y==ballon1.y):
                healthdisplay(ballon1,200)
                print(ballon_symbol,end="")
                print(Style.RESET_ALL,end="")
            elif(ballon2.alive==True and x==ballon2.x and y==ballon2.y):
                healthdisplay(ballon2,200)
                print(ballon_symbol,end="")
                print(Style.RESET_ALL,end="")                            
            elif(townhall.alive==True and ((x==-3 and y==1)or(x==-1 and y==1) or (x==1 and y==1) or (x==-1 and y==-1) or (x==-1 and y==-3) or (x==-1 and y==-5))):
                if(townhall.health>=500):
                    print(Back.GREEN,end="")
                elif(townhall.health<=500 and townhall.health>=200):
                    print(Back.YELLOW,end="")
                else:
                    print(Back.RED,end="")                  
                print("  ",end="")
                print(Style.RESET_ALL,end="")
            elif(king.alive==True and x==king.x and y==king.y):
                if(king.attack==True and king.start_attack==True):
                    print(Back.YELLOW,end="")
                print(king_symbol,end="")
                print(Style.RESET_ALL,end="")
            elif(queen.alive==True and x==queen.x and y==queen.y):
                if(queen.attack==True and queen.start_attack==True):
                    print(Back.YELLOW,end="")
                print(queen_symbol,end="")
                print(Style.RESET_ALL,end="")       
            elif((x==hut1.x and y==hut1.y and hut1.alive==True) or (x== hut2.x and y==hut2.y and hut2.alive==True) or (x==hut3.x and y==hut3.y and hut3.alive==True) or (x==hut4.x and y==hut4.y and hut4.alive==True) or (x==hut5.x and y==hut5.y and hut5.alive==True)):
                if(x==hut1.x and y== hut1.y and hut1.alive==True):
                    healthdisplay(hut1,250)
                    print(hut_symbol,end="")
                    print(Style.RESET_ALL,end="")
                if(x==hut2.x and y== hut2.y and hut2.alive==True):
                    healthdisplay(hut2,250)
                    print(hut_symbol,end="")
                    print(Style.RESET_ALL,end="")
                if(x==hut3.x and y== hut3.y and hut3.alive==True):
                    healthdisplay(hut3,250)
                    print(hut_symbol,end="")
                    print(Style.RESET_ALL,end="")
                if(x==hut4.x and y== hut4.y and hut4.alive==True):
                    healthdisplay(hut4,250)
                    print(hut_symbol,end="")
                    print(Style.RESET_ALL,end="")
                if(x==hut5.x and y== hut5.y and hut5.alive==True):
                    healthdisplay(hut5,250)
                    print(hut_symbol,end="")
                    print(Style.RESET_ALL,end="")                                                                                
            elif((x==canon1.x and y==canon1.y and canon1.alive==True) or (x==canon2.x and y==canon2.y and canon2.alive==True) or (x==canon3.x and y==canon3.y and canon3.alive==True) or (x==canon4.x and y==canon4.y and canon4.alive==True)):
                if(x==canon1.x and y== canon1.y and canon1.alive==True):
                    healthdisplay(canon1,400)
                    print(canon_symbol,end="")
                    print(Style.RESET_ALL,end="")                    
                if(x==canon2.x and y== canon2.y and canon2.alive==True):
                    healthdisplay(canon2,400)
                    print(canon_symbol,end="")
                    print(Style.RESET_ALL,end="")
                if(x==canon3.x and y== canon3.y and canon3.alive==True):
                    healthdisplay(canon3,400)
                    print(canon_symbol,end="")
                    print(Style.RESET_ALL,end="")
                if(x==canon4.x and y== canon4.y and canon4.alive==True):
                    healthdisplay(canon4,400)
                    print(canon_symbol,end="")
                    print(Style.RESET_ALL,end="")                                                                            
            elif(troop11.alive==True and x==troop11.x and y==troop11.y):
                healthdisplay(troop11,200)     
                print("T ",end="")
                print(Style.RESET_ALL,end="") 
            elif(troop12.alive==True and x==troop12.x and y==troop12.y):
                healthdisplay(troop12,200)                      
                print("T ",end="")
                print(Style.RESET_ALL,end="")
            elif(troop13.alive==True and x==troop13.x and y==troop13.y):
                healthdisplay(troop13,200)                      
                print("T ",end="")
                print(Style.RESET_ALL,end="")
            elif(troop14.alive==True and x==troop14.x and y==troop14.y):
                healthdisplay(troop14,200)      
                print("T ",end="")
                print(Style.RESET_ALL,end="")
            elif(troop15.alive==True and x==troop15.x and y==troop15.y):
                healthdisplay(troop15,200)      
                print("T ",end="")
                print(Style.RESET_ALL,end="")                                                                  
            elif(troop21.alive==True and x==troop21.x and y==troop21.y):
                healthdisplay(troop21,200)
                print("T ",end="")
                print(Style.RESET_ALL,end="") 
            elif(troop22.alive==True and x==troop22.x and y==troop22.y):
                healthdisplay(troop22,200)
                print("T ",end="")
                print(Style.RESET_ALL,end="") 
            elif(troop23.alive==True and x==troop23.x and y==troop23.y):
                healthdisplay(troop23,200)
                print("T ",end="")
                print(Style.RESET_ALL,end="") 
            elif(troop24.alive==True and x==troop24.x and y==troop24.y):
                healthdisplay(troop24,200)
                print("T ",end="")
                print(Style.RESET_ALL,end="") 
            elif(troop25.alive==True and x==troop25.x and y==troop25.y):
                healthdisplay(troop25,200)
                print("T ",end="")
                print(Style.RESET_ALL,end="")                                                                  
            elif(troop31.alive==True and x==troop31.x and y==troop31.y):
                healthdisplay(troop31,200)
                print("T ",end="")
                print(Style.RESET_ALL,end="") 
            elif(troop32.alive==True and x==troop32.x and y==troop32.y):
                healthdisplay(troop32,200)
                print("T ",end="")
                print(Style.RESET_ALL,end="") 
            elif(troop33.alive==True and x==troop33.x and y==troop33.y):
                healthdisplay(troop33,200)
                print("T ",end="")
                print(Style.RESET_ALL,end="") 
            elif(troop34.alive==True and x==troop34.x and y==troop34.y):
                healthdisplay(troop34,200)
                print("T ",end="")
                print(Style.RESET_ALL,end="")
            elif(troop35.alive==True and x==troop35.x and y==troop35.y):
                healthdisplay(troop35,200)
                print("T ",end="")
                print(Style.RESET_ALL,end="") 
            elif(tower1.alive==True and x==tower1.x and y==tower1.y):
                healthdisplay(tower1,400)
                print(tower_symbol,end="")
                print(Style.RESET_ALL,end="")  
            elif(tower2.alive==True and x==tower2.x and y==tower2.y):
                healthdisplay(tower2,400)
                print(tower_symbol,end="")
                print(Style.RESET_ALL,end="")
            elif(archer1.alive==True and x==archer1.x and y==archer1.y):
                healthdisplay(archer1,100)
                print(archer_symbol,end="")
                print(Style.RESET_ALL,end="")  
            elif(archer2.alive==True and x==archer2.x and y==archer2.y):
                healthdisplay(archer2,100)
                print(archer_symbol,end="")
                print(Style.RESET_ALL,end="")
            elif(archer3.alive==True and x==archer3.x and y==archer3.y):
                healthdisplay(archer3,100)
                print(archer_symbol,end="")
                print(Style.RESET_ALL,end="")                                                                                                                                                                                                        
            elif(abs(y)%2==0):
                print("- ",end="")
            elif(abs(x)%2==0):
                print("| ",end="")          
            else:
                print("  ",end="")    
        print()    
    print("")
    print(hut4.health,end="")
    if(king_flag):
        print("King health -> ",end="") 
    else:
         print("Queen health -> ",end="")         
    do_health(king_flag)          


def Update_Game(move,king_flag):
    global cnt1
    global cnt2
    global cnt3
    if((move=="a" or move=="w" or move=="s" or move=="d") and king_flag==True ):
        king.update_coordinates(move)
    elif((move=="a" or move=="w" or move=="s" or move=="d") and king_flag==False and queen.attack==False):
        queen.update_coordinates(move)    
    elif(move=="p"):
        cnt1+=1
        if(cnt1==1):
            troop11.alive=True
        elif(cnt1==2):
            troop12.alive=True
        elif(cnt1==3):
            troop13.alive=True
        elif(cnt1==4):
            troop14.alive=True
        elif(cnt1==5):
            troop15.alive=True                
    elif(move=="q"):
        cnt2+=1
        if(cnt2==1):
            troop21.alive=True
        elif(cnt2==2):
            troop22.alive=True
        elif(cnt2==3):
            troop23.alive=True
        elif(cnt2==4):
            troop24.alive=True
        elif(cnt2==5):
            troop25.alive=True                
    elif(move=="r"):
        cnt3+=1
        if(cnt3==1):
            troop31.alive=True
        elif(cnt3==2):
            troop32.alive=True
        elif(cnt3==3):
            troop33.alive=True
        elif(cnt3==4):
            troop34.alive=True
        elif(cnt3==5):
            troop35.alive=True         
    elif(move==" " and king_flag==True):
        king.start_attack=True
    elif(move==" " and king_flag==False):
        queen.start_attack=True        
    elif(move=="h"):
        heal_spell(king,1000)        
        heal_spell(troop11,200)
        heal_spell(troop12,200)                     
        heal_spell(troop13,200)
        heal_spell(troop14,200)
        heal_spell(troop15,200)
        heal_spell(troop21,200)
        heal_spell(troop22,200)
        heal_spell(troop23,200)
        heal_spell(troop24,200)
        heal_spell(troop25,200)
        heal_spell(troop31,200)
        heal_spell(troop32,200)
        heal_spell(troop33,200)
        heal_spell(troop34,200)
        heal_spell(troop35,200) 
    elif(move=="g"):
        rage_spell(king)        
        rage_spell(troop11)
        rage_spell(troop12)                     
        rage_spell(troop13)
        rage_spell(troop14)
        rage_spell(troop15)
        rage_spell(troop21)
        rage_spell(troop22)
        rage_spell(troop23)
        rage_spell(troop24)
        rage_spell(troop25)
        rage_spell(troop31)
        rage_spell(troop32)
        rage_spell(troop33)
        rage_spell(troop34)
        rage_spell(troop35)
    elif(move=="1"):
        ballon1.alive=True
    elif(move=="2"):
        ballon2.alive=True  
    elif(move=="i"):
        archer1.alive=True
    elif(move=="j"):
        archer2.alive=True
    elif(move=="k"):
        archer3.alive=True                                                                                                                                     
           
def Game():    
    player=input("enter the player you want to play(K/Q): ")
    king_flag=True
    if(player=="Q"):
        king_flag=False
    if(king_flag==False):
        king.alive=False
    else:
        queen.alive=False            
    global start_time
    f=open("replay/replay.txt","w")
    win_message = '''
          __     __          __          ___       _       __
          \ \   / /          \ \        / (_)     | |   _  \ \\
           \ \_/ /__  _   _   \ \  /\  / / _ _ __ | |  (_)  | |
            \   / _ \| | | |   \ \/  \/ / | | '_ \| |       | |
             | | (_) | |_| |    \  /\  /  | | | | |_|   _   | |
             |_|\___/ \__,_|     \/  \/   |_|_| |_(_)  (_)  | |
                                                           /_/
            '''    
    lose_message='''
                __     __           ___              __    _         __
                \ \   / /           | |             | |   | |   _   / /
                 \ \_/ /__  _   _   | |     ___  ___| |_  | |  (_) | |
                  \   / _ \| | | |  | |    / _ \/ __| __| | |      | |
                   | | (_) | |_| |  | |___| (_) \__ \ |_  |_|   _  | |
                   |_|\___/ \__,_|  |______\___/|___/\__| (_)  (_) | |
                                                                    \_\\
        '''            
    
    while True:
        Game_done()
        if(game_done==True):
            damage_done=0
            total_damage=3850
            if(hut1.alive==False):
                damage_done+=250
            if(hut2.alive==False):
                damage_done+=250
            if(hut3.alive==False):
                damage_done+=250
            if(hut4.alive==False):
                damage_done+=250
            if(hut5.alive==False):
                damage_done+=250
            if(townhall.alive==False):
                damage_done+=1000
            if(canon1.alive==False):
                damage_done+=400
            if(canon2.alive==False):
                damage_done+=400
            if(canon3.alive==False):
                damage_done+=400
            if(canon4.alive==False):
                damage_done+=400                                   
            os.system("clear")
            if(Win==True):
                print(win_message)
                break
            else:
                print(lose_message)               
                break         
        print(chr(27) + "[2J")    
        display(king_flag)
        troop11.timer=time.time()-troop11.start_time
        troop12.timer=time.time()-troop12.start_time
        troop13.timer=time.time()-troop13.start_time
        troop14.timer=time.time()-troop14.start_time
        troop15.timer=time.time()-troop15.start_time
        troop21.timer=time.time()-troop21.start_time
        troop22.timer=time.time()-troop22.start_time
        troop23.timer=time.time()-troop23.start_time
        troop24.timer=time.time()-troop24.start_time
        troop25.timer=time.time()-troop25.start_time
        troop31.timer=time.time()-troop31.start_time
        troop32.timer=time.time()-troop32.start_time
        troop33.timer=time.time()-troop33.start_time
        troop34.timer=time.time()-troop34.start_time
        troop35.timer=time.time()-troop35.start_time
        king.timer=time.time()-king.start_time
        time.sleep(0.03)
        input_val=input_to()
        current_time=time.time()-start_time
        if(input_val!=None):
            f.write("{} {}\n".format(input_val,current_time))
        Update_Game(input_val,king_flag)                

king=King(1000,9,1,True,False,-1,2,False,2,2,0,0,0)
troop11=Troops(0,2,400,17,1,False,False,-1,2,2,-100,100,True,True,0,0)
troop12=Troops(0,2,400,17,1,False,False,-1,2,2,-100,100,True,True,0,0)
troop13=Troops(0,2,400,17,1,False,False,-1,2,2,-100,100,True,True,0,0)
troop14=Troops(0,2,400,17,1,False,False,-1,2,2,-100,100,True,True,0,0)
troop15=Troops(0,2,400,17,1,False,False,-1,2,2,-100,100,True,True,0,0)
troop21=Troops(0,2,400,1,-19,False,False,-1,2,2,-100,100,True,True,0,0)
troop22=Troops(0,2,400,1,-19,False,False,-1,2,2,-100,100,True,True,0,0)
troop23=Troops(0,2,400,1,-19,False,False,-1,2,2,-100,100,True,True,0,0)
troop24=Troops(0,2,400,1,-19,False,False,-1,2,2,-100,100,True,True,0,0)
troop25=Troops(0,2,400,1,-19,False,False,-1,2,2,-100,100,True,True,0,0)
troop31=Troops(0,2,400,1,15,False,False,-1,2,2,-100,100,True,True,0,0)
troop32=Troops(0,2,400,1,15,False,False,-1,2,2,-100,100,True,True,0,0)
troop33=Troops(0,2,400,1,15,False,False,-1,2,2,-100,100,True,True,0,0)
troop34=Troops(0,2,400,1,15,False,False,-1,2,2,-100,100,True,True,0,0)
troop35=Troops(0,2,400,1,15,False,False,-1,2,2,-100,100,True,True,0,0)
hut1=Hut(250,True,-17,5)
hut2=Hut(250,True,-17,-5)
hut3=Hut(250,True,17,5)
hut4=Hut(250,True,17,-5)
hut5=Hut(250,True,-19,1)
townhall=TownHall(1000,True)
canon1=Canons(-9,9,400,3,True,4)
canon2=Canons(-9,-9,400,3,True,4)
canon3=Canons(9,9,400,3,True,4)
canon4=Canons(9,-9,400,3,True,4)
tower1=WizardTower(400,True,1,15,3,4)
tower2=WizardTower(400,True,1,-15,3,4)
ballon1=Ballons(2,200,15,15,False,False,True,0,0,-100,100)
ballon2=Ballons(2,200,-13,15,False,False,True,0,0,-100,100)
archer1=Archer(200,1,-9,-15,False,True,False,-100,-100,3)
archer2=Archer(200,1,9,-15,False,True,False,-100,-100,3)
archer3=Archer(200,1,-9,15,False,True,False,-100,-100,3)
queen=Queen(1000,17,-13,True,False,-1,2,False,'a')
Game()
