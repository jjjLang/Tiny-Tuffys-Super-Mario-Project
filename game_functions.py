# import pygame
import sys
from fireball import Fireball
# from mario import Mario
from Block import Block
from pipe import Pipe
from enemy import *
# from item import Item
from pole import Pole
from flag import Flag


def mario_move(mario, settings, screen, fireball):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # mario.is_idle = False
                mario.is_facing_left = False
                mario.moving_left = False
                mario.is_facing_right = True
                mario.moving_right = True
                mario.go_down = False
            elif event.key == pygame.K_LEFT:
                # mario.is_idle = False
                mario.is_facing_right = False
                mario.moving_right = False
                mario.is_facing_left = True
                mario.moving_left = True
                mario.go_down = False
            elif event.key == pygame.K_SPACE:
                # check_mario_ground(settings, screen, mario, ground)
                #  mario.is_idle = False
                if not mario.falling:
                    mario.moving_left = False
                    mario.moving_right = False
                    mario.jump = True
                    mario.go_down = False
                    mario.last_y_position = mario.rect.y

                # if not mario.mario_bounce:
                #     mario.last_y_position = mario.rect.y

                if event.key == pygame.K_RIGHT:
                    mario.moving_left = False
                    mario.moving_right = True
                    mario.jump = True
                    mario.go_down = False
            elif event.key == pygame.K_LSHIFT or pygame.K_RSHIFT:
                mario.sprint = True
            if event.key == pygame.K_DOWN:
                if mario.is_big:
                    # mario.is_idle = False
                    mario.moving_right = False
                    mario.moving_left = False
                    mario.crouch = True
                elif not mario.is_big:
                    mario.moving_right = False
                    mario.moving_left = False
                    mario.jump = False
                    mario.crouch = False
            if mario.is_fire:
                if event.key == pygame.K_LSHIFT or pygame.K_RSHIFT:
                    mario.throw_fire = True
                    if len(fireball) < settings.fireballs_allowed:
                        new_fireball = Fireball(settings, screen, mario)
                        fireball.add(new_fireball)
            elif event.key == pygame.K_q:
                sys.exit()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                # mario.is_idle = True
                mario.moving_right = False
            elif event.key == pygame.K_LEFT:
                # mario.is_idle = True
                mario.moving_left = False
            elif event.key == pygame.K_SPACE:
                # mario.is_idle = True
                mario.jump = False
                mario.falling = True
            elif event.key == pygame.K_LSHIFT or pygame.K_RSHIFT:
                mario.sprint = False
            if mario.is_fire:
                if event.key == pygame.K_LSHIFT or pygame.K_RSHIFT:
                    mario.throw_fire = False
            if mario.is_big:
                if event.key == pygame.K_DOWN:
                    mario.crouch = False


# def check_mario_ground(settings, screen, mario, ground):
#     ground_check = mario.rect.colliderect(ground.rect)
#     mario.touch_ground = ground_check


# will finish this after we figure out how the platforms will work
# def check_mario_plat(settings, screen, mario, ground):
#     pass


# Griffin's code
def create_block(settings, screen, blocks):
    while settings.current_block < settings.number_of_blocks[settings.current_level]:
        block = Block(settings.block_positions[settings.current_level][settings.current_block], screen,
                      settings.block_types[settings.current_level][settings.current_block],
                      settings.block_items[settings.current_level][settings.current_block])
        settings.current_block += 1

        block.x = block.pos[0]
        block.y = block.pos[1]
        blocks.add(block)


# def create_item(settings, screen, blocks, items):
# for b in blocks:
#     if b.item_type == 1:
#         item = Item(1)
#     pass


def create_pipe(settings, screen, pipes):
    while settings.current_pipe < settings.number_of_pipes[settings.current_level]:
        pipe = Pipe(settings.pipe_positions[settings.current_level][settings.current_pipe], screen,
                    settings.pipe_sizes[settings.current_level][settings.current_pipe])
        settings.current_pipe += 1

        pipe.x = pipe.pos[0]
        pipe.y = pipe.pos[1]
        pipes.add(pipe)


def create_enemy(settings, screen, enemies):
    while settings.current_enemies < settings.number_of_enemies[settings.current_level]:
        if settings.enemy_species[settings.current_level][settings.current_enemies] == 0:
            enemy = Goomba(screen, settings.enemy_positions[settings.current_level][settings.current_enemies],
                           settings.enemy_types[settings.current_level][settings.current_enemies])
        elif settings.enemy_species[settings.current_level][settings.current_enemies] == 1:
            enemy = KoopaTroopa(screen, settings.enemy_positions[settings.current_level][settings.current_enemies],
                                settings.enemy_types[settings.current_level][settings.current_enemies],
                                settings.enemy_path[settings.current_level][settings.current_enemies])
        elif settings.enemy_species[settings.current_level][settings.current_enemies] == 2:
            enemy = PiranhaPlant(screen, settings.enemy_positions[settings.current_level][settings.current_enemies],
                                 settings.enemy_types[settings.current_level][settings.current_enemies],
                                 settings.enemy_path[settings.current_level][settings.current_enemies])
        elif settings.enemy_species[settings.current_level][settings.current_enemies] == 3:
            enemy = KoopaParatroopa(screen, settings.enemy_positions[settings.current_level][settings.current_enemies],
                                    settings.enemy_types[settings.current_level][settings.current_enemies],
                                    settings.enemy_path[settings.current_level][settings.current_enemies])
        elif settings.enemy_species[settings.current_level][settings.current_enemies] == 4:
            enemy = Blooper(screen, settings.enemy_positions[settings.current_level][settings.current_enemies])
        elif settings.enemy_species[settings.current_level][settings.current_enemies] == 5:
            enemy = CheepCheep(screen, settings.enemy_positions[settings.current_level][settings.current_enemies])
        elif settings.enemy_species[settings.current_level][settings.current_enemies] == 6:
            enemy = Podoboo(screen, settings.enemy_positions[settings.current_level][settings.current_enemies],
                            settings.enemy_path[settings.current_level][settings.current_enemies])
        elif settings.enemy_species[settings.current_level][settings.current_enemies] == 7:
            enemy = FireBar(screen, settings.enemy_positions[settings.current_level][settings.current_enemies],
                            settings.radius[settings.current_enemies])  # fix
        elif settings.enemy_species[settings.current_level][settings.current_enemies] == 8:
            enemy = FakeBowser(screen, settings.enemy_positions[settings.current_level][settings.current_enemies],
                               settings.enemy_types[settings.current_level][settings.current_enemies])
        else:
            enemy = Goomba(screen, (500, 200), 0)  # default
        enemies.add(enemy)
        settings.current_enemies += 1


def check_collision(settings, scoreboard, enemies, mario, blocks, pipes, flags):
    check_enemy_mario_collision(settings, scoreboard, enemies, mario)
    check_enemy_object_collision(enemies, blocks)
    check_enemy_object_collision(enemies, pipes)
    check_mario_pipes_collision(mario, pipes)
    check_mario_block_collision(mario, blocks)
    check_mario_flag_collision(mario, flags)


def check_mario_flag_collision(mario, flags):
    for flag in flags:
        if mario.rect.colliderect(flag):
            mario.flag = True


def check_mario_block_collision(mario, blocks):
    for block in blocks:
        collision = pygame.sprite.spritecollide(mario, blocks, False)
        if collision:
            if block.rect.collidepoint(mario.rect.bottomleft) or \
                    block.rect.collidepoint(mario.rect.midbottom) or \
                    block.rect.collidepoint(mario.rect.bottomright):
                mario.falling = False
                mario.grounded = True
            elif mario.falling or mario.rect.collidepoint(block.rect.left, block.rect.top - 10) or \
                    mario.rect.collidepoint(block.rect.midleft) or \
                    mario.rect.collidepoint(block.rect.left, block.rect.bottom):
                mario.moving_right = False
                mario.sprint = False
            elif mario.falling or mario.rect.collidepoint(block.rect.right, block.rect.top - 10) or \
                    mario.rect.collidepoint(block.rect.midright) or \
                    mario.rect.collidepoint(block.rect.right, block.rect.bottom):
                mario.moving_left = False
                mario.sprint = False
            if mario.rect.collidepoint(block.rect.bottomleft) or \
                    mario.rect.collidepoint(block.rect.midbottom) or \
                    mario.rect.collidepoint(block.rect.bottomright):
                if block.type == 1:
                    block.bump = True
                if block.type == 3:
                    block.emptied = True
                mario.jump = False
                mario.mario_bounce = False
                mario.falling = True


def check_mario_pipes_collision(mario, pipes):
    for pipe in pipes:
        collision = pygame.sprite.spritecollide(mario, pipes, False)
        mario.colliding = collision
        if collision:
            if mario.rect.collidepoint(pipe.rect.left, pipe.rect.top + 10) or \
                    mario.rect.collidepoint(pipe.rect.left, pipe.rect.top + 20) or \
                    mario.rect.collidepoint(pipe.rect.left, pipe.rect.top + 30) or \
                    mario.rect.collidepoint(pipe.rect.midleft) or \
                    mario.rect.collidepoint(pipe.rect.left, pipe.rect.bottom - 30) or \
                    mario.rect.collidepoint(pipe.rect.left, pipe.rect.bottom - 20) or \
                    mario.rect.collidepoint(pipe.rect.left, pipe.rect.bottom - 10):
                mario.moving_right = False
                mario.sprint = False
                mario.rect.x -= 2
            elif mario.rect.collidepoint(pipe.rect.right, pipe.rect.top + 10) or \
                    mario.rect.collidepoint(pipe.rect.right, pipe.rect.top + 20) or \
                    mario.rect.collidepoint(pipe.rect.right, pipe.rect.top + 30) or \
                    mario.rect.collidepoint(pipe.rect.midright) or \
                    mario.rect.collidepoint(pipe.rect.right, pipe.rect.bottom - 30) or \
                    mario.rect.collidepoint(pipe.rect.right, pipe.rect.bottom - 20) or \
                    mario.rect.collidepoint(pipe.rect.right, pipe.rect.bottom - 10):
                mario.moving_left = False
                mario.sprint = False
                mario.rect.x += 2
            # if mario.rect.collidepoint(pipe.rect.bottomleft) or \
            #         mario.rect.collidepoint(pipe.rect.midbottom) or \
            #         mario.rect.collidepoint(pipe.rect.bottomright):
            #     # options for blocks, doesn't effect pipes bc pipes don't have attribute 'type'
            #     if pipe.type == 1:
            #         pipe.bump = True
            #     if pipe.type == 3:
            #         pipe.emptied = True
            #     mario.jump = False
            #     mario.mario_bounce = False
            #     mario.falling = True
            #     print("BOTTOM")
            if pipe.rect.collidepoint(mario.rect.bottomleft) or \
                    pipe.rect.collidepoint(mario.rect.midbottom) or \
                    pipe.rect.collidepoint(mario.rect.bottomright):
                mario.falling = False
                mario.grounded = True
                mario.dropping = False
        else:
            mario.grounded = False
            mario.dropping = True


def check_enemy_object_collision(enemies, obstacles):
    collision = pygame.sprite.groupcollide(obstacles, enemies, False, False)
    for enemy in enemies:
        for obstacle in obstacles:
            if collision:
                if obstacle.rect.collidepoint(enemy.rect.topright) or \
                        obstacle.rect.collidepoint(enemy.rect.midright) or \
                        obstacle.rect.collidepoint(enemy.rect.topleft) or \
                        obstacle.rect.collidepoint(enemy.rect.midleft):
                    enemy.vel_x *= -1
                if obstacle.rect.collidepoint(enemy.rect.bottomleft) or \
                        obstacle.rect.collidepoint(enemy.rect.bottomright) or \
                        obstacle.rect.collidepoint(enemy.rect.midbottom):
                    enemy.falling = False
                    enemy.on_ground = True


def check_enemy_mario_collision(settings, scoreboard, enemies, mario):
    for enemy in enemies:
        collision = pygame.sprite.spritecollide(mario, enemies, False)
        if collision:
            # checks if mario collides with any of the top 3 points of enemy
            if (mario.falling or mario.dropping) and (mario.rect.collidepoint(enemy.rect.left + 3, enemy.rect.top) or
                                                      mario.rect.collidepoint(enemy.rect.midtop) or
                                                      mario.rect.collidepoint(enemy.rect.right - 3, enemy.rect.top)):
                settings.stomp.play()
                if enemy.group_type == 1:
                    enemy.rect.y += 16
                mario.mario_bounce = True
                mario.jump = False
                enemy.dead = True
                mario.death = False
                scoreboard.enemy_killed('brown_guy')
            # checks if goomba collides with mario's left top and right
            elif enemy.rect.collidepoint(mario.rect.topright) or enemy.rect.collidepoint(mario.rect.midright) or \
                    enemy.rect.collidepoint(mario.rect.bottomright) or enemy.rect.collidepoint(mario.rect.topleft) \
                    or enemy.rect.collidepoint(mario.rect.midleft) or enemy.rect.collidepoint(mario.rect.bottomleft) \
                    or enemy.rect.collidepoint(mario.rect.midtop):  # and not mario.mario_bounce:
                mario.death = True
                for enemy_ in enemies:  # this loop stops all the enemies
                    enemy_.killed_mario = True
            elif (mario.mario_bounce or mario.jump) and collision:  # and not mario.mario_bounce:
                mario.death = True
                enemy.killed_mario = True
            if enemy.enemy_rect.y > settings.screen_width:
                enemies.remove(enemy)
            if enemy.stepped_on and enemy.count == 5:
                enemies.remove(enemy)


def scroll_eveything_left(settings, mario, enemies, blocks, pipes, poles, flags):
    # type 1 -> sprites with no path x
    # type 2 -> sprites with path x
    # type 3 -> rotating sprites
    for enemy in enemies:
        if enemy.group_type == 1:
            if (mario.moving_right or mario.sprint) and mario.rect.x == settings.start_scrolling_pos_x:
                if mario.sprint and mario.moving_right:
                    enemy.enemy_rect.x -= mario.vel_x * 4
                elif mario.sprint and not mario.moving_right:
                    enemy.enemy_rect.x -= mario.vel_x * 3
                elif not mario.sprint:
                    enemy.enemy_rect.x -= mario.vel_x
        elif enemy.group_type == 2:
            if (mario.moving_right or mario.sprint) and mario.rect.x == settings.start_scrolling_pos_x:
                if mario.sprint and mario.moving_right:
                    enemy.enemy_rect.x -= mario.vel_x * 4
                    enemy.path_left -= mario.vel_x * 4
                    enemy.path_right -= mario.vel_x * 4
                elif mario.sprint and not mario.moving_right:
                    enemy.enemy_rect.x -= mario.vel_x * 3
                    enemy.path_left -= mario.vel_x * 3
                    enemy.path_right -= mario.vel_x * 3
                elif not mario.sprint:
                    enemy.enemy_rect.x -= mario.vel_x
                    enemy.path_left -= mario.vel_x
                    enemy.path_right -= mario.vel_x
        elif enemy.group_type == 3:
            if (mario.moving_right or mario.sprint) and mario.rect.x == settings.start_scrolling_pos_x:
                if mario.sprint and mario.moving_right:
                    enemy.center_rot_x -= mario.vel_x * 4
                elif mario.sprint and not mario.moving_right:
                    enemy.enemy_rect.x -= mario.vel_x * 3
                elif not mario.sprint:
                    enemy.center_rot_x -= mario.vel_x

    for block in blocks:
        if (mario.moving_right or mario.sprint) and mario.rect.x == settings.start_scrolling_pos_x:
            if mario.sprint and mario.moving_right:
                block.x -= mario.vel_x * 4
            elif mario.sprint and not mario.moving_right:
                block.x -= mario.vel_x * 3
            elif not mario.sprint:
                block.x -= mario.vel_x

    for pipe in pipes:
        if (mario.moving_right or mario.sprint) and mario.rect.x == settings.start_scrolling_pos_x:
            if mario.sprint and mario.moving_right:
                pipe.x -= mario.vel_x * 4
            elif mario.sprint and not mario.moving_right:
                pipe.x -= mario.vel_x * 3
            elif not mario.sprint:
                pipe.x -= mario.vel_x

    for pole in poles:
        if (mario.moving_right or mario.sprint) and mario.rect.x == settings.start_scrolling_pos_x:
            if mario.sprint and mario.moving_right:
                pole.x -= mario.vel_x * 4
            elif mario.sprint and not mario.moving_right:
                pole.x -= mario.vel_x * 3
            elif not mario.sprint:
                pole.x -= mario.vel_x

    for flag in flags:
        if (mario.moving_right or mario.sprint) and mario.rect.x == settings.start_scrolling_pos_x:
            if mario.sprint and mario.moving_right:
                flag.x -= mario.vel_x * 4
            elif mario.sprint and not mario.moving_right:
                flag.x -= mario.vel_x * 3
            elif not mario.sprint:
                flag.x -= mario.vel_x


def mario_in_range(mario, enemies):
    for enemy in enemies:
        if enemy.enemy_rect.x - mario.rect.x <= 800:
            enemy.is_move = True


def create_flag(settings, screen, flags):
    flag = Flag(screen, settings.flag_positions[settings.current_level])
    flag.x = flag.pos[0]
    flag.y = flag.pos[1]

    flags.add(flag)


def create_pole(settings, screen, poles):
    pole = Pole(screen, settings.pole_positions[settings.current_level])
    pole.x = pole.pos[0]
    pole.y = pole.pos[1]

    # print(pole.pos)
    poles.add(pole)


def create_entities(settings, screen, blocks, pipes, enemies, poles, flags):
    create_block(settings, screen, blocks)
    create_pipe(settings, screen, pipes)
    create_enemy(settings, screen, enemies)
    create_pole(settings, screen, poles)
    create_flag(settings, screen, flags)


# def update_screen(settings, screen, stats, scores, mario, blocks, enemies, items, fireball):
#     blocks.draw(screen)
#     tubes.draw(screen)
#     pass

def reset_game(screen, settings, mario, enemies, blocks, pipes, poles, flags):
    if mario.rect.y >= settings.screen_height:
        mario.rect.x = 4
        mario.rect.y = 385
        settings.bg_x = 0
        enemies.empty()
        blocks.empty()
        pipes.empty()
        poles.empty()
        flags.empty()
        settings.current_enemies = 0
        settings.current_block = 0
        settings.current_pipe = 0
        create_block(settings, screen, blocks)
        create_enemy(settings, screen, enemies)
        create_pipe(settings, screen, pipes)
        create_pole(settings, screen, poles)
        create_flag(settings, screen, flags)
        mario.death = False
