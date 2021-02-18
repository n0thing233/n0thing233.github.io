from abc import ABC, abstractmethod
from enum import Enum

class parkingLot(Object):
class vehicleType(Enum):
  SMALL = 1
  MEDIUM = 2
  LARGE = 3
  XLARGE = 4
class vehicle(ABC):
  def __init__(self,license = None, vehicleType = None):
      self.license = license
      self.vehicleType = vehiacleType
      self.parked
  @abstractmethod
  def can_fit_in_spot(self,):
class motocycle(vehicle):
   def __init__(self,):
      vehicle.__init__()
   def can_fit_in_spot()
class car(vehicle):
  ...
class truck(vehicle):
  ...
class bus(vehicle):
  ...
class spot(vehiacle):
  def __init__(self,):
    self.id = 
    self.is_parked = 
    self.spot_type = 
    self.parked_vehicle_license = 
class Parkinglot(Object):
  def __init__(self):
    self.num_of_spots
    self.name
    self.parking_spot = []
  def place_vehicle(self,vehicle):
     for i in self.parking_spot():
        if i.is_parked:
          continue
        else:
          if vehicle.vehicleType.value < = i.spot_type.value:
              
        
  def remove_vehicle():

  
      
  
  

    
