class Queen:
    def __init__(self,health,x,y,alive,attack,current_attack,damage,start_attack,last_move):
        self.health=health
        self.x=x
        self.y=y
        self.alive=alive
        self.attack=attack
        self.current_attack=current_attack
        self.damage=damage
        self.start_attack=start_attack
        self.last_move=last_move
        self.name="queen"

    def update_coordinates(self,move):
        self.last_move=move
        if(move=="w"):
            self.y+=2
        elif(move=="s"):
            self.y=self.y-2
        elif(move=="a"):
            self.x=self.x-2
        elif(move=="d"):
            self.x=self.x+2

    def update_health(self,damage):
        self.health=self.health-damage
        if(self.health<=0):
            self.alive=False            
