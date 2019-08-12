import math
position =[0,0]
direction = []
magnitude = []
i = 0
while True:
   dir_steps= input()
   if not dir_steps:
       break
   try:
       dire, steps = dir_steps.split(' ')
       steps = int(steps)
       if dire == 'up':
           position[0] += steps
       elif dire == 'down':
           position[0] -= steps
       elif dire == 'left':
           position[1] += steps
       elif dire == 'right':
           position[1] -= steps
   except ValueError:
       print("Except block")
print (int(math.sqrt(position[1]**2+position[0]**2)))