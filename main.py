# Klasikinis zaidimas Pong

import simplegui
import random

# Kintamieji
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 10
PAD_WIDTH = 8
ball_vel = [0,0]
ball_pos = [300,200]
paddle1_pos1 = [4,0]
paddle1_pos2 = [4,80]
paddle2_pos1 = [596,0]
paddle2_pos2 = [596,80]
paddle1_vel = 0
paddle2_vel = 0
score1 = 0
score2 = 0


# Spawn ball
def spawn_ball(direction):
    global ball_pos, ball_vel
    ball_pos = [300,200]
    if direction == "Left":
        ball_vel[0] = random.randrange(-7, -3, 2)
        ball_vel[1] = random.randrange(-5, 5, 2)
        
    elif direction == "Right":
        ball_vel[0] = random.randrange(3,7, 2)
        ball_vel[1] = random.randrange(-5, 5, 2)
    
        
        


# Naujas zaidimas
def new_game():
    global score1, score2
    score1, score2 = 0,0
    spawn_ball("Right")
    
# Veiksmas ekrane
def draw(c):
    global score1, score2, paddle1_pos1, paddle1_pos2, paddle2_pos2, paddle2_pos2, ball_pos, ball_vel, paddle1_vel, paddle2_vel
    
    #Rezultatas
    c.draw_text(str(score1), (260, 50), 45, 'White', 'serif')
    c.draw_text(str(score2), (320, 50), 45, 'White', 'serif')
        
    # Vidurine ir sonines linijos
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # Kamuoliuko judejimas
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    # Po tasku
    if ball_pos[0] >= 600:
        spawn_ball("Left")
        score1 += 1
    if ball_pos[0] <= 0:
        score2 += 1
        spawn_ball("Right")
        
        
    # Kamuoliuko atsimusimas i virsutine bei apatine siena
    if ball_pos[1] >= 390:
        ball_vel[1] = -ball_vel[1]
        sound.play()
    elif ball_pos[1] < 10:
        ball_vel[1] = -ball_vel[1]
        sound.play()
    
    # Kamuoliuko atsimusimas i rakete    
    if ball_pos[1] in range(paddle1_pos1[1] -10, paddle1_pos2[1] +10) and ball_pos[0] <=20:
        sound.play()
        ball_vel[0] = -ball_vel[0]
        if ball_vel[0] <= 22:
            if ball_vel[0] >0:
                ball_vel[0] += ball_vel[0] * 0.1
            elif ball_vel <0:
                ball_vel[0] -= ball_vel[0] * 0.1
        if ball_pos[1] in range(paddle1_pos1[1] -10, paddle1_pos1[1] +30) and ball_vel[1] <= 0:
            ball_vel[1] -= 2
        elif ball_pos[1] in range(paddle1_pos2[1] -30, paddle1_pos2[1] +10) and ball_vel[1] >= 0:
            ball_vel[1] += 2
            
    if ball_pos[1] in range(paddle2_pos1[1] - 10, paddle2_pos2[1] +10) and ball_pos[0] >=580:
        sound.play()
        ball_vel[0] = -ball_vel[0]
        if ball_vel[0] >0:
            ball_vel[0] += ball_vel[0] * 0.1
        elif ball_vel <0:
            ball_vel[0] -= ball_vel[0] * 0.1
        if ball_pos[1] in range(paddle2_pos1[1] -10, paddle2_pos1[1] +30) and ball_vel[1] <= 0:
            ball_vel[1] -= 2
        elif ball_pos[1] in range(paddle2_pos2[1] -30, paddle2_pos2[1] +10) and ball_vel[1] >= 0:
            ball_vel[1] += 2
    
    # Zaidimo pabaiga
    if score1 == 5:
        c.draw_text('Player 1 Won!', (90, 350), 70, 'White', 'serif')
        ball_pos = [300,200]
        ball_vel = [0,0]
    if score2 == 5:
        ball_pos = [300,200]
        ball_vel = [0,0]
        c.draw_text('Player 2 Won!', (90, 350), 70, 'White', 'serif')
    
            
    # Kamuolio piesimas
    c.draw_circle(ball_pos, BALL_RADIUS, 1, 'White', 'White')
    
    # Rakeciu pozicijos
    if paddle1_pos1[1] <= 0:
       paddle1_pos1[1] = 1
       paddle1_pos2[1] = 81
    if paddle1_pos2[1] >= HEIGHT :
        paddle1_pos1[1] = 320
        paddle1_pos2[1] = 400
    if paddle2_pos1[1] <= 0:
       paddle2_pos1[1] = 1
       paddle2_pos2[1] = 81
    if paddle2_pos2[1] >= HEIGHT :
        paddle2_pos1[1] = 320
        paddle2_pos2[1] = 400
    paddle1_pos1[1] += paddle1_vel
    paddle1_pos2[1] += paddle1_vel
    paddle2_pos1[1] += paddle2_vel
    paddle2_pos2[1] += paddle2_vel
    
    # Rakeciu piesimas
    c.draw_line(paddle1_pos1,paddle1_pos2, PAD_WIDTH, "White")
    c.draw_line(paddle2_pos1,paddle2_pos2, PAD_WIDTH, "White")


# Rakeciu valdymas        
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['s']:
        paddle1_vel += 5
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel -= 5
    if key == simplegui.KEY_MAP['down']:
        paddle2_vel += 5
    if key == simplegui.KEY_MAP['up']:
        paddle2_vel -= 5
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['s']:
        paddle1_vel = 0
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel = 0
    if key == simplegui.KEY_MAP['down']:
        paddle2_vel = 0
    if key == simplegui.KEY_MAP['up']:
        paddle2_vel = 0



frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
button1 = frame.add_button('New Game', new_game)
sound = simplegui.load_sound('http://www.cs.indiana.edu/classes/a202/fall2006/notes/chap12/missile.wav')

frame.start()
