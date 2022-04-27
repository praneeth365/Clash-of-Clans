class Troops:
    def __init__(self,start_time,timer,health,x,y,alive,attack,current_attack,damage,speed,destination_x,destination_y,moving,attack_complete,num_heal,num_rage):
        self.start_time=start_time
        self.timer=timer
        self.health=health
        self.x=x
        self.y=y
        self.alive=alive
        self.attack=attack
        self.current_attack=current_attack
        self.damage=damage
        self.speed=speed
        self.destination_x=destination_x
        self.destination_y=destination_y
        self.moving=moving
        self.attack_complete=attack_complete
        self.num_heal=num_heal
        self.num_rage=num_rage
        self.name="barbarian"

    def update_health(self,damage):
        self.health=self.health-damage
        if(self.health<=0):
            self.alive=False   
                 
