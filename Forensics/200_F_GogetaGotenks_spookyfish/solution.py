import os
os.system('convert img_1.png img_2.png -fx "(((255*u)&(255*(1-v)))|((255*(1-u))&(255*v)))/255" the_flag.png')