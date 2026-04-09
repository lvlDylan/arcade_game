"""   
le module d'ennemi
"""

import pyxel
import math

class Ennemy :
    """
    Une classe pour le module de tir de notre vaisseau
    """
    def __init__(self, x, y):
        """Initialisation du tir

        :param x: L'abscisse du coin supérieur gauche
        :type x: int
        :param y: L'ordonnée du coin supérieur gauche
        :type y: int
        """
        # position initiale du vaisseau
        self.x = x
        self.base_x = x
        self.y = y
        # largeur (width) et hauteur du vaisseau (height)
        self.w = 8
        self.h = 8

    # =====================================================
    # == UPDATE
    # =====================================================
    def update(self):
        """Mise à jour du vaisseau (30FPS)
        """
        self._move()
        self.draw()
        
    def _move(self):
         self.y += 0.5  # avance constante
         self.x = self.base_x + math.sin(pyxel.frame_count * 0.1) * 10

    # =====================================================
    # == DRAW
    # =====================================================
    def draw(self):
        """
        Dessin d'un ennemi
        """
        frame_count = pyxel.frame_count
        if frame_count % 15 < 5:
            pyxel.blt(self.x, self.y, 0, 0, 8, 8, 8)
        elif frame_count % 15 < 10:
            pyxel.blt(self.x, self.y, 0, 0, 16, 8, 8)
        else:
            pyxel.blt(self.x, self.y, 0, 0, 24, 8, 8)
