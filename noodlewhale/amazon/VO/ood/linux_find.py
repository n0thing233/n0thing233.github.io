from abc import ABC, abstractmethod
class File:
  def __init__(self,
               name = None,
               creation_timestamp = None,
               size = None,
               isdir = None,
               children = None):
      self.filename = filename
      self.creation_timestamp = creation_timestamp
      self.size = size
      self.isdir = isdir
      self.children = []

class filter(ABC):
  @abstractmethod
  def apply(self,file)：
      pass
class sizeFilter(filter):
  def apply(self,file,size):
      if file.size >= size:
          return True
      else:
          return False
class suffixFilter(filter):
   def apply(self,file,suffix):
       return file.endswith(suffix)

class findcommand:
  def findWithFilter(self,file,filter):
      res = []
      if  not file.isdir:
        raise Exception("file not directory!")
      for i in file.children:
        if i.isdir:
          res += findWithFilter(i,filter)
        elif filter.apply(i):
          res += file
      return res
