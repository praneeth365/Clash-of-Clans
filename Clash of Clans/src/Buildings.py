class Buildings:
    def __init__(self,health,alive):
        self.health=health
        self.alive=alive

    def update_health(self,damage):
        self.health=self.health-damage
        if(self.health<=0):
            self.alive=False



class Hut(Buildings):
  def __init__(self,health, alive,x,y):
    super().__init__(health,alive)
    self.name="Hut"
    self.x=x
    self.y=y

class TownHall(Buildings):
  def __init__(self,health, alive):
    super().__init__(health,alive)
    self.name="Town Hall"

class WizardTower(Buildings):
  def __init__(self,health,alive,x,y,range,damage):
    super().__init__(health,alive)
    self.name="Wizard Tower" 
    self.x=x
    self.y=y
    self.range=range
    self.damage=damage   
