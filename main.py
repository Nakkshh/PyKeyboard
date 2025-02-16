import pygame
import sys

# Initialize Pygame
pygame.init()
pygame.mixer.set_num_channels(20)  # Allow multiple sounds to play simultaneously

# Set up display
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PyKeyboard")

WHITE, BLACK, GRAY, BLUE = (255, 255, 255), (0, 0, 0), (169, 169, 169), (0, 100, 255)

# Define white and black keys with labels
white_keys = [
    (pygame.K_a, "C4"), (pygame.K_s, "D4"), (pygame.K_d, "E4"),
    (pygame.K_f, "F4"), (pygame.K_g, "G4"), (pygame.K_h, "A4"),
    (pygame.K_j, "B4"), (pygame.K_k, "C5")
]

black_keys = [
    (pygame.K_w, "C#4", 70), (pygame.K_e, "D#4", 170),
    (pygame.K_t, "F#4", 370), (pygame.K_y, "G#4", 470), (pygame.K_u, "A#4", 570)
]

# Load sounds
sounds = {key: pygame.mixer.Sound(f"sounds/sounds_wav/{note}.wav") for key, note in white_keys}
sounds.update({key: pygame.mixer.Sound(f"sounds/sounds_wav/{note}.wav") for key, note, _ in black_keys})

# Adjust volume
for sound in sounds.values():
    sound.set_volume(0.8)  # Reduce distortion

# Track pressed keys and sustain mode
pressed_keys = {}
sustain_mode = False

# Font for labels
font = pygame.font.Font(None, 30)

running = True
while running:
    screen.fill(WHITE)

    # Draw white keys
    for i, (key, note) in enumerate(white_keys):
        color = BLUE if pressed_keys.get(key, False) else WHITE
        pygame.draw.rect(screen, color, (i * 100, 0, 100, HEIGHT))
        pygame.draw.rect(screen, BLACK, (i * 100, 0, 100, HEIGHT), 2)

        # Draw key labels
        label = font.render(note, True, BLACK)
        screen.blit(label, (i * 100 + 35, HEIGHT - 40))

    # Draw black keys
    for key, note, x_pos in black_keys:
        color = GRAY if pressed_keys.get(key, False) else BLACK
        pygame.draw.rect(screen, color, (x_pos, 0, 60, 250))

        # Draw key labels (move higher for visibility)
        label = font.render(note, True, WHITE)
        screen.blit(label, (x_pos + 10, 140))

    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LSHIFT:  # Sustain mode toggle
                sustain_mode = not sustain_mode
            elif event.key in sounds:
                sounds[event.key].stop()  # 🔹 Stop previous sound before playing again
                sounds[event.key].play()  # 🔹 Ensure the key plays every time it's pressed
                pressed_keys[event.key] = True
        elif event.type == pygame.KEYUP:
            if event.key in pressed_keys and not sustain_mode:
                pressed_keys[event.key] = False

    pygame.display.flip()

pygame.quit()
sys.exit()
