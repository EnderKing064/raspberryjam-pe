#
# Code under the MIT license by Alexander Pruss
#

import mcpi.minecraft as minecraft
import time
from math import *
from mcpi.block import *
from mcturtle import *
import code
import sys

def quit():
    sys.exit()

def inputLine(prompt):
    mc.events.clearAll()
    while True:
        chats = mc.events.pollChatPosts()
        for c in chats:
            if c.entityId == playerId:
                print(c.message)
                if c.message == 'quit':
                    return 'quit()'
                elif c.message == ' ':
                    return ''
                else:
                    return c.message
        time.sleep(0.2)

mc = minecraft.Minecraft()
playerPos = mc.player.getPos()
playerId = mc.getPlayerId()
t = Turtle(mc)

mc.postToChat("Enter python code into chat, type 'quit' to quit.")
i = code.interact(banner="", readfunc=inputLine, local=locals())