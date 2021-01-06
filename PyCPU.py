from pynput.mouse import Button, Controller
from pynput import mouse
mouse = Controller()
import time

#Declaring variables
delay = 0.4
delay_scroll = 1.5 
start_coords = (890, 560)
center_coords = (1020, 490)
upgrade_coords = (740, 550)
again_coords = (1340, 270)
attack_coords = (1260, 490)
j = 0

#Scroll to left
def to_left():
  print('Moving to LEFT...') #Needed to scroll have a more plausible view of the stage
  mouse.position = (center_coords)
  mouse.press(Button.left)
  time.sleep(delay)
  mouse.move(500, 0)
  time.sleep(delay_scroll)
  mouse.release(Button.left)

#Start position
def start_pos():
  mouse.position = (start_coords)
  print('ROW DONE')
  time.sleep(delay)
  mouse.click(Button.left, 1)

#Move one square per 'delay'
def next_pos():
  i = 1
  while i < 6:
    print('Deploying unit:', i, mouse.position)
    mouse.click(Button.left, 1)
    mouse.move(65, 0)
    time.sleep(delay)
    i += 1

#Moves to next row
def scroll():
  print('ROW COMPLETED')
  time.sleep(delay_scroll)
  print('Change to next row...')
  mouse.position = (center_coords)
  time.sleep(delay)
  mouse.press(Button.left)
  #1.5 sec cuz delay its too fast
  time.sleep(delay_scroll)
  mouse.move(0, -200)
  #Same
  time.sleep(delay_scroll)
  mouse.release(Button.left)

#Increasing money
def upgrade():
  mouse.position = (upgrade_coords)
  print('UPGRADING (if possible)...')
  time.sleep(delay)
  mouse.click(Button.left, 1)
  time.sleep(delay)

#Push Return button
def rerun():
  mouse.position = (again_coords)
  print('RETURNING...')
  time.sleep(delay)
  mouse.click(Button.left, 1)
  time.sleep(delay_scroll)
  mouse.click(Button.left, 1)

#Push Attack button
def attack():
  mouse.position = (attack_coords)
  print('ATTACK')
  time.sleep(delay_scroll)
  mouse.click(Button.left, 1)
  time.sleep(delay)
  mouse.click(Button.left, 1)

#Move to left
to_left()
#Number of scrolls = j -1
while j < 2:
  start_pos()
  next_pos()
  upgrade()
  scroll()
  j += 1
print('WAITING 12 sec...') #Waiting for the units to destroy the base
time.sleep(12)
rerun() #Pressing again the Attack button
time.sleep(5)
attack()