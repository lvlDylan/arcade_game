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
from arcade_game.explosion import Explosion

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
        self.explosions = []
        self.score = 0
        
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
            if self.is_collision(self.spaceship, ennemy):
                self.spaceship.lives -= 1
        
        self.update_shoot()
        self.update_explosions()
        self.collision_shoots_ennemies(self.spaceship.shoots, self.ennemies)

            
    # =====================================================
    # == DRAW (30FPS)
    # =====================================================
    def draw(self):
        """création et positionnement des objets (30 fois par seconde)"""

        # vide la fenetre 30 fois par seconde
        pyxel.cls(0)
        
        if self.spaceship.lives > 0:
            # affichage des vies            
            pyxel.text(5,5, 'VIES:'+ str(self.spaceship.lives), 7)
            pyxel.text(5, 15, 'SCORE:'+ str(self.score), 7)
            for shoot in self.spaceship.shoots:
                shoot.draw()
            
            if pyxel.frame_count % 30 == 0:
                self.ennemies.append(Ennemy(randint(0, self.w - 8), -8))
            for ennemy in self.ennemies:
                ennemy.draw()
            
            for explosion in self.explosions:
                explosion.draw()
                    
            self.spaceship.draw()
        else:
            pyxel.text(45,64, 'GAME OVER', 7)
            pyxel.text(45, 75, 'SCORE : ' + str(self.score), 7)

        
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
    
    def update_explosions(self):
        for explosion in self.explosions:
            explosion.update()
            if explosion.radius > 12:
                self.explosions.remove(explosion)
    
    def is_collision(self, vaiseau, ennemy):
        if (max(vaiseau.x, ennemy.x) <= min(vaiseau.x + vaiseau.w, ennemy.x + ennemy.w)) and (max(vaiseau.y, ennemy.y) <= min(vaiseau.y + vaiseau.h, ennemy.y + ennemy.h)):
            self.ennemies.remove(ennemy)
            self.explosions.append(Explosion(vaiseau.x, vaiseau.y, 1))
            return True
    
    def collision_shoots_ennemies(self, shoots, ennemies):
        ennemies_to_delete = []
        shoots_to_delete = []
        for shoot in shoots:
            for ennemy in ennemies:
                if (max(shoot.x, ennemy.x) <= min(shoot.x + shoot.w, ennemy.x + ennemy.w)) and (max(shoot.y, ennemy.y) <= min(shoot.y + shoot.h, ennemy.y + ennemy.h)):
                    ennemies_to_delete.append(ennemy)
                    shoots_to_delete.append(shoot)
                    self.score += 1
                    self.explosions.append(Explosion(ennemy.x, ennemy.y, 1))
                
        for ennemy in ennemies_to_delete:
            self.ennemies.remove(ennemy)
        for shoot in shoots_to_delete:
            self.spaceship.shoots.remove(shoot)

# instanciation de notre classe
Game()