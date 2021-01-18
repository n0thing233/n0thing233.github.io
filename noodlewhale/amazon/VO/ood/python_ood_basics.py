#parent class
class parent_1():
    def __init__(self,attr_1 = None, attr_2 = None):
        self.attr_1 = attr_1
        self.attr_2 = attr_2
    def function_1(self):
        pass
#abstract class
# can't initiate
# child must implement function
from abc import ABC,abstractmethod 
class abstract_1(ABC):
    @abstractmethod
    def function_abstract(self):
        pass
    def function_non_abstract(self):
        pass
#interface class
#support multi-inheritance
#can't initiate
#child must implement function
#focus on function
class interface_1(ABC):
    @abstractmethod
    def function_interface_1(self):
        pass
    @abstractmethod
    def test(self):
        pass
    def test2(self):
        pass
class interface_2(ABC):
    @abstractmethod
    def function_interface_2(self):
        pass

#test parent
class child_1(parent_1):
    def __init__(self,attr_1 = None, attr_2 = None, attr_3 = None):
        parent_1.__init__(self,attr_1, attr_2)
        self.attr_3 = attr_3
#test abstract
class child_2(abstract_1):
    def __init__(self,attr_3 = None):
        self.attr_3 = attr_3
    def function_abstract(self):
        print("function_abstracted implemented!" )
#test interface multi-inheritance
class child_3(interface_1,interface_2):
    def __init__(self):
        pass
    def function_interface_1(self):
        print("function_interface_1 implemented!" )
    def function_interface_2(self):
        print("function_interface_2 implemented!" )
    def test(self):
        pass

a = child_1(attr_1 = 1,attr_2 = 2,attr_3 = 3)
b = child_2(attr_3 = 3)
c = child_3()
print(c.function_interface_1())
print(c.function_interface_2())
