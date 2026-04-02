"""
le module principal du projet arcade_game

                  :: ::::: ::
                  :: ::::: ::
                  :: ::::: ::
                  :: ::::: ::
                  :: ::::: ::


                 .:: ::::: ::.
                .::: ::::: :::.
               .:::' ::::: ':::.
              .::::' ::::: '::::.
             .::::'  :::::  '::::.
           .:::::'   :::::   ':::::.
         .::::::'    :::::    '::::::.
    ...:::::::'      :::::      ':::::::...
    :::::::''        :::::        '':::::::
    ::::''           :::::           ''::::

      _______ _______ _______ ______  ___
     |   _   |       |   _   |   _  \|   |(R)
     |.  1   |.|   | |.  1   |.  l   |.  |
     |.  _   `-|.  |-|.  _   |.  _  <|.  |
     |:  |   | |:  | |:  |   |:  |   |:  |
     |::.|:. | |::.| |::.|:. |::.|:. |::.|
     `--- ---' `---' `--- ---`--- ---`---'

"""

import pyxel
from arcade_game.spaceship import Spaceship
from arcade_game.ennemy import Ennemy
from random import randint

class Game:
    """
    Une classe pour notre jeu
    """
    def __init__(self):
        """
        Initialisation du jeu
        """
        self.w = 128 #largeur de l'écran
        self.h = 256 #hauteur de l'écran
        self.spaceship = Spaceship(self, self.w//2, self.h-8) #instanciation du vaisseau
        self.ennemies = []
        pyxel.init(self.w, self.h, title="Arcade Game")
        # chargement des images
        pyxel.load("images.pyxres")
        # --> appel de la fonction principale
        pyxel.run(self.update, self.draw)

    # =====================================================
    # == UPDATE (30FPS)
    # =====================================================
    def update(self):
        """mise à jour des variables (30 fois par seconde)"""

        # deplacement du vaisseau
        self.spaceship.update()
        self.update_ennemies()
        for shoot in self.spaceship.shoots:
            shoot.update()
        for ennemy in self.ennemies:
            ennemy.update()
            self.is_collision(self.spaceship, ennemy)

    # =====================================================
    # == DRAW (30FPS)
    # =====================================================
    def draw(self):
        """création et positionnement des objets (30 fois par seconde)"""

        # vide la fenetre 30 fois par seconde
        pyxel.cls(0)
        
        for shoot in self.spaceship.shoots:
            shoot.draw()
        
        if pyxel.frame_count % 30 == 0:
            self.ennemies.append(Ennemy(randint(0, self.w), 0))
            
        for ennemy in self.ennemies:
            ennemy.draw()
        
        self.spaceship.draw()
        self.update_shoot()
        self.update_ennemies()
        
    def update_shoot(self):
        visible = []
        for shoot in self.spaceship.shoots:
            if shoot.y > 0:
                visible.append(shoot)
        self.spaceship.shoots = visible
    
    def update_ennemies(self):
        visible = []
        for ennemy in self.ennemies:
            if ennemy.y < self.h:
                visible.append(ennemy)
        self.ennemies = visible
    
    def is_collision(self, vaiseau, ennemy):
        if vaiseau.x == ennemy.x and vaiseau.y == ennemy.y:
            print("BANG")
        
        

# instanciation de notre classe
Game()