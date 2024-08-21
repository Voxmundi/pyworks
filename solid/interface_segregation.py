from abc import ABC, abstractmethod

class Worker(ABC):

    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def eat(self):
        pass


class HumanWorker(Worker):

    def work(self):
        print ("Human is working")
    
    def eat(self):
        print ("Human is Eating")


class RobotWorker(Worker):

    def work(self):
        print ("Robot working")
    
    def eat(self):
        raise NotImplementedError("Robots can't Eat")
    
# human = HumanWorker()
# robot = RobotWorker()

# human.work()
# human.eat()

# robot.work()
# robot.eat()


class Workable(ABC):

    @abstractmethod
    def work(self):
        pass

class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass

class HumanWorker(Workable,Eatable):

    def work(self):
        print ('Human Works')
    
    def eat(self):
        print ("Human Eat")
   
class RobotWorker(Workable):

    def work(self):
        print ("Robot Works")




h = HumanWorker()

h.work()
h.eat()

r = RobotWorker()
r.work()

