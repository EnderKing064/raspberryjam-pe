#
# Public domain code by Alexander Pruss
#

from mcturtle import *
t = Turtle()
t.penblock(GOLD_BLOCK)
t.turtle(GIANT)
t.pendelay(0.01)
for i in range(7):
    t.go(50)
    t.left(180.-180./7)
