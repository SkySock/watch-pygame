import pygame
import datetime
import math


class Watch(pygame.sprite.Sprite):
    def __init__(self, radius=250):
        super().__init__()
        self.radius = radius
        self.image = pygame.Surface([self.radius * 2, self.radius * 2])
        self.rect = self.image.get_rect()
        self.center = [self.radius, self.radius]

    def draw_watch(self):
        pygame.draw.circle(self.image, (255, 255, 255), (self.radius, self.radius), self.radius, 3)
        self.draw_risks(6, 0.05)
        self.draw_risks(30, 0.1)
        self.draw_digits()

    def draw_arrows(self, time):
        second_angle = (time.second * 1000000 + time.microsecond) * (360 / (60 * 1000000))
        
        minute_angle = (time.minute * 60 + time.second) * 0.1
        hour_angle = (time.hour * 3600 + time.minute * 60 + time.second) * (360 / (12*60*60))
        pygame.draw.aaline(self.image, (255, 255, 255), self.center,
                           self.get_coords_from_angle(hour_angle, int(self.radius * 0.5)), 2
                           )
        pygame.draw.aaline(self.image, (255, 255, 255), self.center,
                           self.get_coords_from_angle(minute_angle, int(self.radius * 0.75)), 2
                           )
        pygame.draw.aaline(self.image, (255, 0, 0), self.center,
                           self.get_coords_from_angle(second_angle, int(self.radius * 0.85)), 2
                           )

    def update(self, *args, **kwargs) -> None:
        time = datetime.datetime.now()
        self.image.fill((0, 0, 0))
        self.draw_watch()
        self.draw_arrows(time)

    def get_coords_from_angle(self, angle, radius):
        angle = math.radians(angle - 90)

        sin, cos = math.sin(angle), math.cos(angle)
        return [self.center[0] + cos * radius, self.center[1] + sin * radius]

    def draw_risks(self, step, ratio):
        for angle in range(0 - 90, 360 - 90, step):
            angle = math.radians(angle)
            inner_rad = int(self.radius * (1 - ratio))
            sin, cos = math.sin(angle), math.cos(angle)
            pygame.draw.aaline(self.image, (255, 255, 255),
                               [self.center[0] + cos * inner_rad, self.center[1] + sin * inner_rad],
                               [self.center[0] + cos * (self.radius-2), self.center[1] + sin * (self.radius-2)],
                               3)

    def draw_digits(self):
        font = pygame.font.SysFont(None, 32)
        radius = self.radius * 0.8
        for digit in range(1, 13):
            angle = math.radians(digit * 30 - 90)
            sin, cos = math.sin(angle), math.cos(angle)
            img = font.render(str(digit), True, (255, 255, 255))
            self.image.blit(img, (round(self.center[0] + cos * radius - 8), round(self.center[1] + sin * radius - 8)))
