# Example of rotating off axis, check background and clipping
import numpy as np
import pixelhouse as ph

pal = ph.palette(6)

# C = ph.Canvas(400, 400, bg=pal[2])
C = ph.Animation(400, 400, bg=pal[2])

lg = ph.gradient.linear([pal[0], pal[1]])

theta = np.linspace(0, 2 * np.pi)
C += ph.text("pixelhouse", gradient=lg)
C += ph.transform.rotate(theta, x=-3)


C.show()
