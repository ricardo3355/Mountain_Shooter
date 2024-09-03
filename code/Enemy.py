#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import ENTITY_SPEED, ENTITY_SHOT_DELAY, WIN_HEIGHT
from code.EnemyShot import EnemyShot
from code.Entity import Entity
import pygame


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

    def move(self):
        if self.name == 'Enemy3':
            # Move horizontally from right to left
            self.rect.centerx -= ENTITY_SPEED[self.name]
            # Vertical movement logic for Enemy3
            if self.rect.top <= 0:  # Hits the top border
                # Increase speed downwards
                self.vertical_speed = abs(self.vertical_speed) * 2
            elif self.rect.bottom >= WIN_HEIGHT:  # Hits the bottom border
                self.vertical_speed = -abs(self.vertical_speed)  # Move upwards
            self.rect.centery += self.vertical_speed
        else:
            self.rect.centerx -= ENTITY_SPEED[self.name]

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))


class Enemy3(Enemy):
    def __init__(self, position: tuple):
        super().__init__('Enemy3', position)
        self.speed_y = 2
        self.direction_y = 1  # 1 for moving down, -1 for moving up
        self.shoot_asset = pygame.image.load('./asset/Enemy3shot.png')

    def move(self):
        self.rect.x -= 0.9  # Move horizontal

        # Move vertical with up and down pattern
        self.rect.y += self.speed_y * self.direction_y
        if self.rect.bottom > WIN_HEIGHT:
            self.direction_y = -1  # Move up
        if self.rect.top < 0:
            self.direction_y = 3  # Move down

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))
        pass
