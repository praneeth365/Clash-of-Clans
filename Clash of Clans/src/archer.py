class Archer:
    def __init__(self,health,damage,x,y,alive,attack,attack_complete,destination_x,destination_y,range):
        self.health=health
        self.damage=damage
        self.x=x
        self.y=y
        self.alive=alive
        self.attack=attack
        self.attack_complete=attack_complete
        self.destination_x=destination_x
        self.destination_y=destination_y
        self.range=range
        self.name="archer"

    def update_health(self,damage):
        self.health=self.health-damage
        if(self.health<=0):
            self.alive=False    

