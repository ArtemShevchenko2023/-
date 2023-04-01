#pgzero
import random

#автор Шевченко Артём
WIDTH = 600 # Ширина окна
HEIGHT = 400 # Высота окна
TITLE = "Epilepsyk" # Заголовок окна игры
FPS = 60 # Количество кадров в секунду
ship = Actor("kor", (300, 400))
space = Actor("fo")
type1 = Actor("kor", (100, 200))
type2 = Actor("korab2", (300, 200))
type3 = Actor("korab3", (500, 200))
planets = [Actor("pla", (random.randint(0, 600), -100)), Actor("pla2", (random.randint(0, 600), -100))]
enemies = []
meteors = []
bullets = []
mode = 'learn'
count = 0
qq = 1
for i in range(2):
    x = random.randint(0, 600)
    y = random.randint(-450, -50)
    enemy = Actor("ene", (x, y))
    enemy.speed = random.randint(5, 8)
    enemies.append(enemy)

for i in range(1):
    x = random.randint(0, 600)
    y = random.randint(-450, -50)
    meteor = Actor("met", (x, y))
    meteor.speed = random.randint(2, 10)
    meteors.append(meteor)

def draw():
    if mode == 'learn':
        space.draw()
        screen.draw.text("Привет!", center = (100, 50), color = "green", fontsize = 40)
        screen.draw.text("В этой игре управление мышкой!", center = (280, 100), color = "green", fontsize = 35)
        screen.draw.text("ЛКМ - стрельба", center = (200, 150), color = "green", fontsize = 40)
        screen.draw.text("Уклоняйся от врагов или", center = (250, 200), color = "green", fontsize = 40)
        screen.draw.text("устраняй их стрельбой!", center = (250, 250), color = "green", fontsize = 40)
        screen.draw.text("Нажми на Enter и", center = (250, 300), color = "green", fontsize = 40)
        screen.draw.text("перейди в меню!", center = (200, 350), color = "green", fontsize = 40)
    if mode == 'menu':
        space.draw()
        type1.draw()
        type2.draw()
        type3.draw()
        screen.draw.text("Choose your ship", center = (300, 100), color = "green", fontsize = 36)
    if mode == 'game':
        space.draw()
        planets[0].draw()
        for i in range(len(meteors)):
            meteors[i].draw()
        for i in range(len(enemies)):
            enemies[i].draw()
        for i in range(len(bullets)):
            bullets[i].draw()
        ship.draw()
        screen.draw.text(count, center = (20, 20), color = "green", fontsize = 20)
    if mode == 'end':
        space.draw()
        screen.draw.text("Нажми на пробел!", center = (300, 100), color = "green", fontsize = 36)
        screen.draw.text("Проигрышей:", center = (300, 150), color = "green", fontsize = 36)
        screen.draw.text(qq, center = (450, 150), color = "green", fontsize = 36)
        screen.draw.text("Game Over!", center = (300, 200), color = "green", fontsize = 36)
        screen.draw.text(count, center = (300, 250), color = "green", fontsize = 50)
    if mode == 'win':
        space.draw()
#автор Шевченко Артём
def on_mouse_move(pos):
    ship.pos = pos
def on_mouse_down(button, pos):
    global mode
    if mode == 'game' and button == mouse.LEFT:
        bullet = Actor("sas")
        bullet.pos = ship.pos
        bullets.append(bullet)
    if mode == 'menu':
        if type1.collidepoint(pos):
            ship.image = "kor"
            mode = 'game'
        if type2.collidepoint(pos):
            ship.image = "korab2"
            mode = 'game'
        if type3.collidepoint(pos):
            ship.image = "korab3"
            mode = 'game'
def new_enemy():
    x = random.randint(0, 400)
    y = -50
    enemy = Actor("ene", (x, y))
    enemy.speed = random.randint(5, 8)
    enemies.append(enemy)
def new():
    x = random.randint(0, 400)
    y = -50
    enemy = Actor("en", (x, y))
    enemy.speed = random.randint(8, 12)
    enemies.append(enemy)
def ne():
    x = random.randint(0, 400)
    y = -50
    enemy = Actor("e", (x, y))
    enemy.speed = random.randint(12, 14)
    enemies.append(enemy)
def enemy_ship():
    for i in range(len(enemies)):
        if enemies[i].y < 650:
            enemies[i].y = enemies[i].y + enemies[i].speed
        else:
            enemies.pop(i)
            new_enemy()
def ship_enemy():
    for i in range(len(enemies)):
        if enemies[i].y < 650:
            enemies[i].y = enemies[i].y + enemies[i].speed
        else:
            enemies.pop(i)
            new()
def ship_enem():
    for i in range(len(enemies)):
        if enemies[i].y < 650:
            enemies[i].y = enemies[i].y + enemies[i].speed
        else:
            enemies.pop(i)
            ne()
def planet():
    if planets[0].y < 550:
            planets[0].y = planets[0].y + 3
    else:
        planets[0].y = -100
        planets[0].x = random.randint(0, 600)
        first = planets.pop(0)
        planets.append(first)
def meteorites():
    for i in range(len(meteors)):
        if meteors[i].y < 450:
            meteors[i].y = meteors[i].y + meteors[i].speed
        else:
            meteors[i].x = random.randint(0, 600)
            meteors[i].y = -20
            meteors[i].speed = random.randint(8, 10)
def collisions():
    global mode
    global count
    for i in range(len(enemies)):
        if ship.colliderect(enemies[i]):
            mode = 'end'
        for j in range(len(bullets)):
            if bullets[j].colliderect(enemies[i]):
                enemies.pop(i)
                bullets.pop(j)
                count += 1
                new_enemy()
                break
def coll():
    global mode
    global count
    for i in range(len(enemies)):
        if ship.colliderect(enemies[i]):
            mode = 'end'
        for j in range(len(bullets)):
            if bullets[j].colliderect(enemies[i]):
                enemies.pop(i)
                bullets.pop(j)
                count += 1
                new()
                break
def col():
    global mode
    global count
    for i in range(len(enemies)):
        if ship.colliderect(enemies[i]):
            mode = 'end'
        for j in range(len(bullets)):
            if bullets[j].colliderect(enemies[i]):
                enemies.pop(i)
                bullets.pop(j)
                count += 1
                ne()
                break
def update(dt):
    global qq
    global count
    global mode
    global planets
    global bullets
    global meteors
    global enemies
    if mode == 'game' and count < 30:
        enemy_ship()
        collisions()
    if mode == 'game' and count >= 30:
        ship_enemy()
        coll()
    if mode == 'game' and count >= 70:
        ship_enem()
        col()
    if mode == 'game' and count >= 100:
        mode = 'win'
    if mode == 'game':
        planet()
        meteorites()
        for i in range(len(bullets)):
                if bullets[i].y < 0:
                    bullets.pop(i)
                    break
                else:
                    bullets[i].y=bullets[i].y - 10
    if mode == 'learn' and keyboard.enter:
        mode = 'menu'
    elif mode == 'end' and keyboard.space:
        mode = 'learn'
        count = 0
        planets = [Actor("pla", (random.randint(0, 600), -100)), Actor("pla2", (random.randint(0, 600), -100))]
        bullets=[]
        enemies = []
        meteors = []
        qq += 1
        for i in range(2):
            x = random.randint(0, 600)
            y = random.randint(-450, -50)
            enemy = Actor("ene", (x, y))
            enemy.speed = random.randint(5, 8)
            enemies.append(enemy)
        for i in range(1):
            x = random.randint(0, 600)
            y = random.randint(-450, -50)
            meteor = Actor("met", (x, y))
            meteor.speed = random.randint(8, 10)
            meteors.append(meteor)
#автор Шевченко Артём
