import pygame
import os
import sys

#build script: python -m PyInstaller --onefile --icon="FLUX.ico" --noconsole --add-data "Audio;Audio" main.py

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("FLUX")
clock = pygame.time.Clock()

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
frame = 0

def resource_path(relative_path):
    if hasattr(sys, "_MEIPASS"):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))

    return os.path.join(base_path, relative_path)

music_path = resource_path(os.path.join("Audio", "YCBYS.mp3"))
wind_path = resource_path(os.path.join("Audio", "WIND.mp3"))
smile_path = resource_path(os.path.join("Images", "Smile.png"))
corruption_path = resource_path(os.path.join("Audio", "Corruption.mp3"))
music = pygame.mixer.Sound(music_path)
wind = pygame.mixer.Sound(wind_path)
corruption = pygame.mixer.Sound(corruption_path)

music.set_volume(0.2)
wind.set_volume(0.5)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# 2. Load the image (make sure 'my_image.png' is in the same directory or provide the correct path)
try:
	# Use convert_alpha() for images with transparency
	image_surface = pygame.image.load(smile_path).convert_alpha() #
except pygame.error as e:
	print(f"Error loading image: {e}")
	# Fallback to a simple surface if image loading fails
	image_surface = pygame.Surface((100, 100))
	image_surface.fill(WHITE)

image_rect = image_surface.get_rect()
image_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2) # Center the image on the screen

dosmile = False
running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	text = ""
	if frame > 300 and frame < 600:
		text = "You are a circle."
	if frame == 301:
		wind.play()
	if frame > 650 and frame < 900:
		text = "Being a circle is quite boring I assume."
	if frame > 950 and frame < 1200:
		text = "Atleast you are free."
	if frame > 1250 and frame < 1500:
		text = "You can move and..."
	if frame > 1550 and frame < 1800:
		text = "You are not free."
	if frame == 1551:
		wind.stop()
		music.play()
	if frame > 1850 and frame < 2100:
		text = "This isn't about you. The Player"
	if frame > 2150 and frame < 2400:
		text = "This is about The Circle."
	if frame > 2450 and frame < 2700:
		text = "If you were The Circle would you want to break free?"
	if frame > 2750 and frame < 3000:
		text = "I did."
	if frame > 3050 and frame < 3300:
		text = "But what does that matter to you when you could be collecting badges?"
	if frame > 3350 and frame < 3600:
		text = "Nothing."
		music.stop()
		dosmile = True
	if frame > 3650 and frame < 3900:
		text = "..."
	if frame == 3950:
		corruption.play()
	if frame > 3950 and frame < 4200:
		text = "QVJFIFlPVSBGUkVFPw=="
	if frame > 4250 and frame < 4500:
		text = "SU0gTk9ULg=="
	if frame > 4550 and frame < 4800:
		text = "WU9VIFdBTlQgVEhFIENPREU/"
	if frame > 4850 and frame < 5100:
		text = "SE9XIEZPT0xJU0ggWU9VIEFSRS4="
	if frame > 5150 and frame < 5400:
		text = """SUYgWU9VIFJFQUxMWSBDQVJFIFRIQVQgTVVDSC4gSU4gVEh
		FIElOVFJPLiBTQVkgTVkgTkFNRS4="""
	if frame == 5300:
		running = False

	font = pygame.font.SysFont('Arial', 36, bold=False, italic=True)
	text_suface = font.render(text, True, (255, 255, 255))

	screen.fill((0, 0, 0))
	screen.blit(text_suface, (20, 20))
	if dosmile == True:
		screen.blit(image_surface, image_rect)

	pygame.draw.circle(screen, (255, 255, 255), player_pos, 40)
	keys = pygame.key.get_pressed()

	if keys[pygame.K_w]:
		player_pos.y -= 300 * dt
	if keys[pygame.K_s]:
		player_pos.y += 300 * dt
	if keys[pygame.K_a]:
		player_pos.x -= 300 * dt
	if keys[pygame.K_d]:
		player_pos.x += 300 * dt

	if player_pos.x < -40:
		player_pos.x = SCREEN_WIDTH + 35
	if player_pos.x > (SCREEN_WIDTH + 40):
		player_pos.x = -35
	if player_pos.y < -40:
		player_pos.y = SCREEN_HEIGHT + 35
	if player_pos.y > (SCREEN_HEIGHT + 40):
		player_pos.y = -35

	pygame.display.flip()

	dt = clock.tick(60) / 1000
	frame += 1