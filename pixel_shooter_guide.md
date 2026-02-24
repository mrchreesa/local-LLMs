# 🎮 Building a Pixel Shooter Game with PyGame  
### University of West London – Coding Club by ATAL Society  
### Second Edition: *Games with PyGame*

---

## 🔧 Project Overview
Creating a **Pixel Shooter** game in PyGame is the perfect 4-hour Vibe Coding Club project—simple mechanics, retro pixel charm, and endless room for creative tweaks.  
We’ll build a **top-down shooter** where the player moves and shoots enemies for points.

### Core Mechanics
- **Player:** A pixel ship at the bottom that moves left/right and shoots upward.
- **Enemies:** Red pixel blobs spawn from the top and drift downward.
- **Bullets:** Blue pixels shoot upward from the player.
- **Win/Lose:** Score points by shooting enemies; game over if enemies reach the bottom or collide with the player.
- **Pixel Art Style:** Use rectangles for visuals (no images required initially).

Total code: ~150 lines.

---

## 📚 Prerequisites (10–15 mins setup)

### Basic Requirements
- **Python basics:** variables, loops, functions, conditionals.
- **Installed Python (3.8+)** and **VS Code** (recommended editor).

### Step 1: Create a Virtual Environment
```bash
python -m venv pygame_env
```
Activate it:
- **Windows:** `pygame_env\Scripts\activate`
- **macOS/Linux:** `source pygame_env/bin/activate`

Deactivate later with `deactivate`.

### Step 2: Install PyGame
```bash
pip install pygame
```
Test setup with:
```python
import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.quit()
print("Pygame ready!")
```
Run: `python test.py` – if it prints without errors, you're ready!

---

## 🕹️ Game Concept Overview
- **Screen:** 800x600 pixels.
- **Controls:** Arrow keys / A-D to move, Space to shoot.
- **Player speed:** 5 px/frame.
- **Bullets:** Fast upward (10 px/frame), auto-despawn off-screen.
- **Enemies:** Spawn every 60 frames, move down (2 px/frame).
- **Collisions:** Bullet-enemy = score +1. Enemy hits player/bottom = game over.

---

## ⚙️ Step-by-Step Breakdown

### Step 1: Initialize & Basic Window (10 mins)
Create the game loop: handle events, update, draw, and cap FPS.

```python
import pygame, random, sys

WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PLAYER_COLOR = (0, 255, 0)
BULLET_COLOR = (0, 0, 255)
ENEMY_COLOR = (255, 0, 0)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pixel Shooter - Vibe Coding Club")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
```
✅ Test: Black window opens and closes.

---

### Step 2: Add Player (10 mins)
```python
player = pygame.Rect(WIDTH//2 - 20, HEIGHT - 50, 40, 20)
player_speed = 5

keys = pygame.key.get_pressed()
if keys[pygame.K_LEFT] or keys[pygame.K_a]:
    player.x -= player_speed
if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
    player.x += player_speed
player.x = max(0, min(WIDTH - player.width, player.x))

pygame.draw.rect(screen, PLAYER_COLOR, player)
```
✅ Test: Green ship moves left/right.

---

### Step 3: Shooting Bullets (15 mins)
```python
bullets = []
shoot_cooldown = 0

if keys[pygame.K_SPACE] and shoot_cooldown <= 0:
    bullets.append(pygame.Rect(player.centerx - 2, player.top - 5, 4, 10))
    shoot_cooldown = 10
shoot_cooldown = max(0, shoot_cooldown - 1)

for bullet in bullets[:]:
    bullet.y -= 10
    if bullet.top < 0:
        bullets.remove(bullet)

for bullet in bullets:
    pygame.draw.rect(screen, BULLET_COLOR, bullet)
```
✅ Test: Bullets shoot upward and disappear off-screen.

---

### Step 4: Enemies & Spawning (15 mins)
```python
enemies = []
spawn_timer = 0
score = 0

spawn_timer += 1
if spawn_timer > 60:
    enemies.append(pygame.Rect(random.randint(0, WIDTH-30), -30, 30, 30))
    spawn_timer = 0

for enemy in enemies[:]:
    enemy.y += 2
    if enemy.top > HEIGHT:
        enemies.remove(enemy)

for enemy in enemies:
    pygame.draw.rect(screen, ENEMY_COLOR, enemy)
```
✅ Test: Red squares fall from the top.

---

### Step 5: Collisions & Scoring (15 mins)
```python
for bullet in bullets[:]:
    for enemy in enemies[:]:
        if bullet.colliderect(enemy):
            bullets.remove(bullet)
            enemies.remove(enemy)
            score += 1
            break

for enemy in enemies[:]:
    if enemy.colliderect(player) or enemy.top > HEIGHT - 50:
        running = False

score_text = font.render(f"Score: {score}", True, WHITE)
screen.blit(score_text, (10, 10))
```
✅ Test: Hitting enemies adds score; collision = game over.

---

### Step 6: Game Over Screen (5 mins)
Show score and restart prompt.
```python
screen.fill(BLACK)
game_over_text = font.render(f"Game Over! Final Score: {score}", True, WHITE)
screen.blit(game_over_text, (WIDTH//2 - 200, HEIGHT//2))
restart_text = font.render("Press R to Restart or Q to Quit", True, WHITE)
screen.blit(restart_text, (WIDTH//2 - 250, HEIGHT//2 + 40))
pygame.display.flip()
```
✅ Optional: Wrap code in `main()` for easier restart.

---

## 🛠️ Full Runnable Game (~150 lines)

*(Full code kept identical to tested version – see full block in previous edition.)*

---

## 💡 Enhancements & Expansions (30–60 mins)
Once the core game works, add polish and new features.

### Level 1: Quick Wins
- **Sound effects:**
  ```python
  shoot_sound = pygame.mixer.Sound('pew.wav')
  shoot_sound.play()
  ```
- **High score:** Save/load using `pickle`.
- **Starfield background:** Animated stars scrolling down.

### Level 2: Gameplay Tweaks
- **Enemy waves:** Faster spawns as score rises.
- **Power-ups:** Random drops for double-shoot or shields.
- **Lives system:** Player has 3 lives before game over.

### Level 3: Visual Polish
- **Particle explosions:** Small fading pixels when enemies are hit.
- **Sprite art:** Replace rectangles with actual images!

---

## 🎨 Working with Sprites (Expanded)
### Why Sprites?
Using images instead of colored rectangles instantly upgrades your visuals. You can animate ships, bullets, or explosions for a professional look.

### Step 1: Load Sprite Images
```python
player_img = pygame.image.load('ship.png').convert_alpha()
bullet_img = pygame.image.load('bullet_blue.png').convert_alpha()
enemy_img = pygame.image.load('enemy_red.png').convert_alpha()

player_img = pygame.transform.scale(player_img, (40, 20))
enemy_img  = pygame.transform.scale(enemy_img, (30, 30))
bullet_img = pygame.transform.scale(bullet_img, (4, 10))
```
### Step 2: Replace Draw Calls
```python
screen.blit(player_img, player)
for bullet in bullets:
    screen.blit(bullet_img, bullet)
for enemy in enemies:
    screen.blit(enemy_img, enemy)
```
### Step 3: Add Explosions (Optional)
```python
explosion_imgs = [pygame.image.load(f'explode_{i}.png').convert_alpha() for i in range(5)]
explosions = []

# On hit:
explosions.append({'pos': enemy.copy(), 'frame': 0, 'life': 10})

# Update & draw:
for ex in explosions[:]:
    ex['life'] -= 1
    if ex['life'] <= 0:
        explosions.remove(ex)
    else:
        ex['frame'] = (ex['frame'] + 1) % len(explosion_imgs)
        screen.blit(explosion_imgs[ex['frame']], ex['pos'])
```

---

## 🖌️ Recommended Sprite Packs

### 1. [2D Space Shooter Pack (CC0)](https://opengameart.org/content/2d-space-shooter-pack)
- **Free & No Attribution Required.**
- Ships, aliens, bullets, explosions, and backgrounds.
- Perfect for replacing your basic rectangles.

### 2. [Space Shooter Redux by Kenney](https://opengameart.org/content/space-shooter-redux)
- Hundreds of sprites (ships, power-ups, UI icons).
- Clean, colorful aesthetic.

### 3. [Arcade Space Shooter Assets](https://opengameart.org/content/arcade-space-shooter-game-assets)
- Retro pixel look, ideal for your minimalist vibe.

### 4. [Handpainted 2D Space Shooter Spritesheet](https://opengameart.org/content/handpainted-2d-space-shooter-spritesheet)
- Detailed yet small-scale graphics.

---

## 🕵️ Debugging Tips
| Issue | Fix |
|-------|-----|
| `No module named pygame` | Activate venv, run `pip install pygame` |
| Bullets not disappearing | Use `for bullet in bullets[:]` when removing |
| Lag or slowdown | Limit framerate with `clock.tick(FPS)` |
| Black screen | Add `pygame.display.flip()` |
| Score not updating | Ensure `screen.fill()` happens *before* drawing text |

**Pro Tip:** Print lengths of lists (`len(bullets)`, `len(enemies)`) to check buildup.

---

## 🔬 Showcase-Ready Ideas
- **Scrolling background** with stars or nebula.
- **Different enemy types** (speed, color, score value).
- **Menu screen** with title + difficulty select.
- **PyInstaller export:**
  ```bash
  pip install pyinstaller
  pyinstaller --onefile pixel_shooter.py
  ```
  Share your `.exe` with friends!

---

## 🎤 Final Vibe
Your game is ready to shine at the next Coding Club showcase!  
Fast, retro, customizable—a great intro to PyGame fundamentals.

Experiment, remix, and make it yours.  
**Happy coding, Space Pilot!** 🚀

