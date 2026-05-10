import pygame
import math
import sys
import ctypes
import pyautogui
from pygame.locals import *

print("1. 1280x720")
print("2. 1366x768")
print("3. 1600x900")
print("4. 1680x1050")
print("5. 1920x1080")
print("6. 2560x1440")
choice = input("Choose your game resolution : ")

res_vars = {
    "1280x720": {"v": 1.272, "r": 19.9, "ph": 145, "length": 200},
    "1366x768": {"v": 1.317, "r": 20.0, "ph": 145, "length": 200},
    "1600x900": {"v": 1.424, "r": 22.8, "ph": 150, "length": 220},
    "1680x1050": {"v": 1.46, "r": 26.0, "ph": 145, "length": 300},
    "1920x1080": {"v": 1.559, "r": 28.0, "ph": 165, "length": 300},
    "2560x1440": {"v": 1.8, "r": 37.0, "ph": 240, "length": 350},
}

res_map = {
    "1": "1280x720",
    "2": "1366x768",
    "3": "1600x900",
    "4": "1680x1050",
    "5": "1920x1080",
    "6": "2560x1440",
}

resolution = res_map.get(choice, "1366x768")  # default to 1366x768
vars = res_vars[resolution]

wt, ht = 1920, 1080

pygame.init()
screen = pygame.display.set_mode((wt, ht), pygame.NOFRAME)
pygame.display.set_caption("Aimbot")
clock = pygame.time.Clock()
FPS = 60

# makes the window transparent
hwnd = pygame.display.get_wm_info()['window']
ctypes.windll.user32.SetWindowLongW(hwnd, -20,
    ctypes.windll.user32.GetWindowLongW(hwnd, -20) | 0x80000 | 0x20)
ctypes.windll.user32.SetLayeredWindowAttributes(hwnd, 0 + (0 << 8) + (0 << 16), 0, 0x1)

white = (255, 255, 255)
x = wt // 2
y = ht // 2
angle = 85
degree = 85
power = 100
g = 9.8
v = vars["v"]
r = vars["r"]
wind = 0
ww = 1.0 / 80.0
ph = vars["ph"]
length = vars["length"]
font = pygame.font.SysFont("Arial", 20)

def draw_labels():
    power_label = font.render(f"Power: {power}", True, white)
    degree_label = font.render(f"Angle: {degree}°", True, white)
    wind_label = font.render(f"Wind: {wind}", True, white)

    screen.blit(power_label, (wt - 140, ht - 140))
    screen.blit(degree_label, (wt - 140, ht - 120))
    screen.blit(wind_label, (wt - 140, ht - 100))

def draw_scene():
    pygame.draw.circle(screen, (15, 219, 18), (x, y), 4)
    angle_rad = math.radians(angle)
    for t in [i * 0.05 for i in range(1000)]:
        px = x + power * v * t * math.cos(angle_rad) + 0.5 * wind * ww * t * t
        py = y - power * v * t * math.sin(angle_rad) + 0.5 * g * t * t
        if py <= ht - ph:
            pygame.draw.circle(screen, white,
                (int(px + r * math.cos(angle_rad)), int(py - r * math.sin(angle_rad))), 1)

running = True
while running:
    screen.fill((0, 0, 0))
    draw_scene()
    draw_labels()

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            elif event.key == K_w: # move crosshair up
                y -= 1
            elif event.key == K_s: # move crosshair down
                y += 1
            elif event.key == K_a: # move crosshair left
                x -= 1
            elif event.key == K_d: # move crosshair right
                x += 1
            elif event.key == K_q: # quit
                running = False
            elif event.key == K_l: # adjust angle right
                angle -= 1
                degree = angle
            elif event.key == K_j: # adjust angle left (TODO: fix angle values)
                angle += 1
                degree = angle
            elif event.key == K_i: # increase power
                power = min(power + 1, 100)
            elif event.key == K_k: # decrease power
                power = max(power - 1, 0)
            elif event.key == K_e: # move crosshair to current mouse pos
                mx, my = pyautogui.position()
                x = mx
                y = my
            elif event.key == K_z: # reset everything
                x, y = wt // 2, ht // 2
                angle = degree = 85
                power = 100
                wind = 0
            elif event.key == K_f:  # increase wind
                wind += 1
            elif event.key == K_v:  # decrease wind
                wind -= 1

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()