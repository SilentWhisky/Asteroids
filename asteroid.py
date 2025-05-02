import random
from circleshape import*
from constants import*

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            new_split_one = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            new_split_two = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            new_split_one.velocity = self.velocity.rotate(random_angle) * 1.2
            new_split_two.velocity = self.velocity.rotate(-random_angle) * 1.2