from abc import ABC, abstractmethod
class Vechile(ABC):
  @abstractmethod
  def can_fit_in_spot(self, spot):
      pass

class Motocycle(vehicle):
class Bus(vehicle):
  def can_fit_in_spot(self, spot):
    return True if spot.size == LARGE else False
class Car(vehicle):
class ParkingLot(vehicle):
class Level():
  def __init__(self,levl)
class parkingSpot():
  def __init__(self,spot_number,spot_size,is_available = False,vehicle):
    self.spot_number = spot_number
    self.spot_type = spot_size
    self.is_available = is_available
    self.vehicle = vehicle
  def is_available(self):
    return self.is_available
  
  

    
