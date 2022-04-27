import time


class King:
    def __init__(self,health,x,y,alive,attack,current_attack,damage,start_attack,speed,timer,start_time,num_heal,num_rage):
        self.health=health
        self.x=x
        self.y=y
        self.alive=alive
        self.attack=attack
        self.current_attack=current_attack
        self.damage=damage
        self.start_attack=start_attack
        self.speed=speed
        self.timer=timer
        self.start_time=start_time
        self.num_heal=num_heal
        self.num_rage=num_rage
        self.name="king"
    def update_coordinates(self,move):
        if(move=="w" and self.timer>=1/self.speed):
            self.y=self.y+2
            self.timer=0
            self.start_time=time.time()
        elif(move=="a" and self.timer>=1/self.speed):
            self.x=self.x-2
            self.timer=0
            self.start_time=time.time()
        elif(move=="s" and self.timer>=1/self.speed):
            self.y=self.y-2
            self.timer=0
            self.start_time=time.time()
        elif(move=="d" and self.timer>=1/self.speed):
            self.x=self.x+2                
            self.timer=0
            self.start_time=time.time()
    def update_health(self,damage):
        self.health=self.health-damage
        if(self.health<=0):
            self.alive=False
