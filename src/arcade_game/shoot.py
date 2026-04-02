"""   
le module de tir
"""

import pyxel

class Shoot :
    """
    Une classe pour le module de tir de notre vaisseau
    """
    def __init__(self, spaceship, x, y):
        """Initialisation du tir

        :param x: L'abscisse du coin supérieur gauche
        :type x: int
        :param y: L'ordonnée du coin supérieur gauche
        :type y: int
        """
        self.spaceship = spaceship
        # position initiale du vaisseau
        self.x = x + 2
        self.y = y
        # largeur (width) et hauteur du vaisseau (height)
        self.w = 4
        self.h = 6

    # =====================================================
    # == UPDATE
    # =====================================================
    def update(self):
        """Mise à jour du vaisseau (30FPS)
        """
        self._move()
        self.draw()
        
    def _move(self):
        self.y -= 4

    # =====================================================
    # == DRAW
    # =====================================================
    def draw(self):
        """
        Dessin du tir
        """
        pyxel.blt(self.x, self.y, 0, 10, 1, self.w, self.h)
