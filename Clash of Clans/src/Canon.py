class Canons:
    def __init__(self,x,y,health,damage,alive,range):
        self.x=x
        self.y=y
        self.health=health
        self.damage=damage
        self.alive=alive
        self.range=range   
        self.name="canon"
    def update_health(self,damage):
        self.health=self.health-damage
        if(self.health<=0):
            self.alive=False
                                        
