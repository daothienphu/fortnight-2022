import os
import time
os.system("convert -size 460x460 xc:   +noise Random   img_2.png")
time.sleep(1)
os.system('convert flag.png img_2.png -fx "(((255*u)&(255*(1-v)))|((255*(1-u))&(255*v)))/255" img_1.png')