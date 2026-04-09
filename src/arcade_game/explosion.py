"""
                                 )                    
 (                            ( /(                    
 )\ )       )     )      (    )\())   )      (   (    
(()/(    ( /(    (      ))\  ((_)\   /((    ))\  )(   
 /(_))_  )(_))   )\  ' /((_)   ((_) (_))\  /((_)(()\  
(_)) __|((_)_  _((_)) (_))    / _ \ _)((_)(_))   ((_) 
  | (_ |/ _` || '  \()/ -_)  | (_) |\ V / / -_) | '_| 
   \___|\__,_||_|_|_| \___|   \___/  \_/  \___| |_| 
"""

import pyxel

class Explosion:
    """
    Une classe pour le module d'explosion
    """
    def __init__(self, x, y, radius):
        """Initialisation de l'explosion

        :param x: L'abscisse du coin supérieur gauche
        :type x: int
        :param y: L'ordonnée du coin supérieur gauche
        :type y: int
        :param radius: Le radius de l'explosion
        :type radius: int
        """
        # position initiale du vaisseau
        self.x = x
        self.y = y
        
        self.radius = radius

    # =====================================================
    # == UPDATE
    # =====================================================
    def update(self):
        """Mise à jour de l'explosion
        """
        self.radius += 1
        
    # =====================================================
    # == DRAW
    # =====================================================
    def draw(self):
        """
        Dessin d'une explosion
        """
        pyxel.circb(self.x+4, self.y+4, 2*(self.radius//4), 8+self.radius%3)