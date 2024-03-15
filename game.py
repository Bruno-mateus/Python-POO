import random


#encapsulation
class Character:
    #constructor
    def __init__(self,name,life,level,special=0):
       #values privates and set
        self.__name = name
        self.__life = life
        self.__level = level
        self.__special= special
        #getters
    def get_name(self):
            return self.__name
        
    def get_life(self):
            return self.__life
        
    def get_level(self):
            return self.__level
    def get_special(self):
        return self.__special
        
    def hud(self):
            return f"Nome: {self.__name}\nNivel: {self.__level}\nVida: {round(self.__life,2)}\nSpecial: {self.__special}"
        
    def damage(self,damage):
        self.__life -= damage
        if self.__life < 0:
           self.__life=0
           
    def attack(self,target):
        attack = self.__level*0.78
        target.damage(damage=attack)
        print(f'O {self.get_name()} atacou o {target.get_name()} e causo {round(attack,2)} de dano')
        
    def super_attack(self, target):
        if self.__special == 3:
            attack = self.get_level() * 3.7
            target.damage(attack)
            print(f"{self.get_name()} usou o super ataque {self.get_ability()} e causou {round(attack,2)} de dano no {target.get_name()}")
        else:
            print(f"Você não conseguiu dar o ataque {self.get_ability()} por falta de energia, perdeu a vez...")
            
    def bar_special(self,super_atack=False):
         if self.__special <3:
             self.__special+=1
         if super_atack == True:
            self.__special=0
         
        
class Hero(Character):
    def __init__(self,name,life,level,ability):
        #init constructor
        super().__init__(name,life,level)
        #Start the parent class constructor.
        self.__ability = ability
        #getter
    def get_ability(self):
       return self.__ability
    def hud(self):
        return f"{super().hud()}\nHabilidade: {self.get_ability()}"
   
class Enemy(Character):
    def __init__(self,name,life,level,type,ability):
        super().__init__(name,life,level)
        self.__type = type
        self.__ability = ability
        
    def GetType(self):
        return self.__type
    def hud(self):
        return  f"{super().hud()}\nTipo: {self.GetType()}"
    def get_ability(self):
        return self.__ability
            


class Game:
    def __init__(self):
        self.enemy = Enemy('Morcego',70,3,"Voador","Furcao vendaval")
        self.hero = Hero('Bob',100,5,"Bola de fogo")
        
    def init_battle(self):
        print("Iniciando a batalha")
        while self.hero.get_life() > 0 and self.enemy.get_life() > 0:
            print("\nDetalhe dos persongens:\n")
            print(f"{self.hero.hud()}\n")
            print(f"{self.enemy.hud()}\n")
            print("Pressione enter para atacar ....")
            choice=input("Escolha:\n 1. Ataque normal, 2. Ataque especialz\n")            
            print(choice)
            if choice == '1':
                self.hero.attack(self.enemy)
                self.hero.bar_special()
            elif choice == '2':
                self.hero.super_attack(self.enemy)
                self.hero.bar_special(True)
            else:
                print("Escolha invalida, tente novamente !")
            
            if self.enemy.get_life()>0:
                attack = random.randint(1, 2)
                if attack ==1 :
                    self.enemy.attack(self.hero)
                    self.enemy.bar_special()    
                elif attack==2 and self.enemy.get_special() == 3:
                    self.enemy.super_attack(self.hero)
                    self.enemy.bar_special(True)
                           
        if self.hero.get_life() >=0:
            print(f"Parabéns {self.hero.get_name()}, você venceu o {self.enemy.get_name()}")
        else:
            print(f"Voce morreu, o {self.enemy.get_name()} venceu a batalha")
            
game = Game()

game.init_battle()