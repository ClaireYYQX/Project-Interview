from random import random, randint
from math import sin, cos, radians
class Person:
    speed = 5
    def __init__(self, x,y, direction, infection_rate):
        self.x = x
        self.y = y
        self.direction = direction
        self.immune=random()
        self.doctor=False
        self.infected=False
       # self.timeleft=randint(20,100)
        if self.immune < infection_rate:
            self.infected = True
        elif self.immune >=0.9:
            self.doctor=True

    def move(self):
        self.x += self.speed * sin(radians(self.direction))
        if self.x < 0:
            self.x += 200
        elif self.x > 200:
            self.x += -200
        self.y += self.speed * cos(radians(self.direction))
        if self.y < 0:
            self.y += 300
        elif self.y > 300:
            self.y += -300
        return self.x, self.y
    
    def get_location(self):
        return self.x, self.y

    def get_infection(self):
        return self.infected

    def get_doctor(self):
        return self.doctor

    #def get_timeleft():
     #   return self.timeleft

class World:
    def __init__(self, width, depth, population):
        
        self.people = []
        self.infection_rate = 0.2
        population=10
        
        for i in range(population):
            x_pos = randint(0,width)
            y_pos = randint(0,depth)
            direction = randint(0,360)
            new_person = Person(x_pos, y_pos, direction, self.infection_rate)
            self.people.append(new_person)
        
    def update_world(self):
       # for person in self.people:
        #    if person.timeleft==0:
         #       self.people.pop(person)
        for person in self.people:
            person.move()
        self.get_crash()
    
    def get_people(self):
        return self.people

    def get_crash(self):
        for i in self.people:
            x1,y1=i.get_location()
           # i.timeleft-=1
            for j in self.people:
                x2,y2=j.get_location()
                if x1<=x2+3 and x1>=x2-3 and y1<=y2+3 and y1>=y2-3:
                    if i.get_doctor()==True or j.get_doctor()==True:
                        i.infected=False
                        j.infected=False
                    elif i.get_infection()== True or j.get_infection()==True:
                        i.infected=True
                        j.infected=True
