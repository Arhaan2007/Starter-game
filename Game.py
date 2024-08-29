import pygame
import random
import sys

pygame.init()

screen_width, screen_height = 800, 600
fps = 60
obstacle_width, obstacle_height = 50, 50
player_width, player_height = 20, 20
obstacles_speed = 5

white = (255, 255, 255)
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)
black = (0, 0, 0)

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('dmg')
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)
large_font = pygame.font.Font(None, 72)

player = pygame.Rect(50, screen_height // 6, player_width, player_height)
obstacles = []
obstacle_timer = pygame.time.get_ticks()
score = 0
game_state = "start"

def reset_game():
    global player, obstacles, score, obstacle_timer
    player = pygame.Rect(50, screen_height // 6, player_width, player_height)
    obstacles = []
    score = 0
    obstacle_timer = pygame.time.get_ticks()

while True:
    screen.fill(white)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if game_state == "start" and event.key == pygame.K_SPACE:
                game_state = "playing"
                reset_game()
            elif game_state == "game_over" and event.key == pygame.K_SPACE:
                game_state = "start"

    if game_state == "start":
        title_text = large_font.render("Press SPACE to Start", True, blue)
        screen.blit(title_text, (screen_width//2 - title_text.get_width()//2, screen_height//2 - title_text.get_height()//2))

    elif game_state == "playing":
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and player.y > 0:
            player.y -= 5
        if keys[pygame.K_DOWN] and player.y < screen_height - player_height:
            player.y += 5

        if pygame.time.get_ticks() - obstacle_timer > 1500:
            obstacle = pygame.Rect(screen_width, random.randint(0, screen_height - obstacle_height), obstacle_width, obstacle_height)
            obstacles.append(obstacle)
            obstacle_timer = pygame.time.get_ticks()

        for obstacle in obstacles:
            obstacle.x -= obstacles_speed
            pygame.draw.rect(screen, red, obstacle)

        for obstacle in obstacles:
            if player.colliderect(obstacle):
                game_state = "game_over"

        obstacles = [obstacle for obstacle in obstacles if obstacle.x > -obstacle_width]
        score += 1
        pygame.draw.rect(screen, green, player)

        score_text = font.render(f"Score: {score}", True, blue)
        screen.blit(score_text, (10, 10))

        if score > 1000:
            if pygame.time.get_ticks() - obstacle_timer > 800:
                obstacle = pygame.Rect(screen_width, random.randint(0, screen_height - obstacle_height), obstacle_width, obstacle_height)
                obstacles.append(obstacle)
                obstacle_timer = pygame.time.get_ticks()

        if score > 1500:
            if pygame.time.get_ticks() - obstacle_timer > 400:
                obstacle = pygame.Rect(screen_width, random.randint(0, screen_height - obstacle_height), obstacle_width, obstacle_height)
                obstacles.append(obstacle)
                obstacle_timer = pygame.time.get_ticks()

        if score > 2000:
            if pygame.time.get_ticks() - obstacle_timer > 200:
                obstacle = pygame.Rect(screen_width, random.randint(0, screen_height - obstacle_height), obstacle_width, obstacle_height)
                obstacles.append(obstacle)
                obstacle_timer = pygame.time.get_ticks()

        if score > 4000:
            if pygame.time.get_ticks() - obstacle_timer > 180:
                obstacle = pygame.Rect(screen_width, random.randint(0, screen_height - obstacle_height), obstacle_width, obstacle_height)
                obstacles.append(obstacle)
                obstacle_timer = pygame.time.get_ticks()
    elif game_state == "game_over":
        game_over_text = large_font.render("Game Over", True, red)
        score_text = font.render(f"Final Score: {score}", True, blue)
        restart_text = font.render("Press SPACE to Restart", True, black)
        screen.blit(game_over_text, (screen_width//2 - game_over_text.get_width()//2, screen_height//2 - game_over_text.get_height()))
        screen.blit(score_text, (screen_width//2 - score_text.get_width()//2, screen_height//2))
        screen.blit(restart_text, (screen_width//2 - restart_text.get_width()//2, screen_height//2 + restart_text.get_height()))

    pygame.display.flip()
    clock.tick(fps)