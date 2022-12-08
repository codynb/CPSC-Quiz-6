#The author is Cody Brown, Quiz 6, code 2
class Ambulance:
    """The attributes are: priority, speed, and capacity"""

theAmb = Ambulance()


theAmb.priority = 1
theAmb.speed = 40 #meters per second
theAmb.capacity = 2 #number of patients inside

# p = theAmb.priority
# s = theAmb.speed
# c = theAmb.capacity


def controlled_velocity(car):
    cv = -10 * (1-car.priority) + 2.37*(car.speed/10)**3.98 + 30*(car.capacity + 1.2)
    print(cv)

controlled_velocity(theAmb)
