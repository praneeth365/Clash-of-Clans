class Ballons:
    def __init__(self,damage,health,x,y,alive,attack,attack_complete,timer,start_time,destination_x,destination_y):
        self.damage=damage
        self.health=health
        self.x=x
        self.y=y
        self.alive=alive
        self.attack=attack
        self.attack_complete=attack_complete
        self.timer=timer
        self.start_time=start_time
        self.destination_x=destination_x
        self.destination_y=destination_y
        self.name="ballon"


    def update_health(self,damage):
        self.health=self.health-damage
        if(self.health<=0):
            self.alive=False