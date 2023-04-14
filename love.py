import random
import time
from termcolor import colored, cprint

# Définir les emojis de couleurs
colors = ["🟥", "🟦", "🟩", "⬛"]
WIDTH, HEIGHT = 12, 12
HEART_EMOJI = "❤️ "

while True:
    start_time = time.time()
    elapsed_time = 0
    sleep_duration = 0.05

    # Boucle pour mettre à jour le carré pendant 5 secondes
    while elapsed_time < 5:
        # Mettre à jour le carré avec des couleurs aléatoires
        square = [[random.choice(colors) for j in range(WIDTH)] for i in range(HEIGHT)]
        # Déplacer le curseur en haut à gauche du carré
        cprint("\033[1;1H", end="")
        # Afficher le carré avec les couleurs
        for row in square:
            for col in row:
                cprint(col, end=" ")
            print()
        # Pause pour que l'utilisateur puisse voir les changements
        time.sleep(sleep_duration)

        # Augmenter la durée de la pause pour ralentir progressivement
        sleep_duration += 0.02

        # Calculer le temps écoulé
        elapsed_time = time.time() - start_time

    # Placer l'emoji cœur au milieu du carré
    middle_x, middle_y = WIDTH // 2, HEIGHT // 2

    # Remplacer progressivement les carrés par des carrés noirs
    for step in range(middle_x + 1):
        cprint("\033[1;1H", end="")

        # Progression depuis le haut gauche
        for i in range(step + 1):
            for j in range(WIDTH):
                if j <= (middle_x + step) and i < HEIGHT:
                    square[i][j] = "⬛"

        # Progression depuis le bas droit
        for i in range(HEIGHT - step - 1, HEIGHT):
            for j in range(WIDTH):
                if j >= (middle_x - step) and i >= 0:
                    square[i][j] = "⬛"

        # Afficher l'emoji cœur quand les progressions se rencontrent
        if step == middle_x:
            square[middle_y][middle_x] = HEART_EMOJI

        # Afficher le carré avec les changements
        for row in square:
            for col in row:
                cprint(col, end=" ")
            print()

        # Pause pour que l'utilisateur puisse voir les changements
        time.sleep(0.1)





    # Attendre 3 secondes avant de recommencer
    time.sleep(3)
