from datetime import datetime
from collections import OrderedDict

class Lrucache:

  def __init__(self,capacity):
    try:
      self.d=OrderedDict()
      self.capapcity=int(capacity)
    except ValueError:
      print("Capacity Should be on int value.")

  def set(self,value):
    try:
      if int(value) in self.d:
        self.cache.pop(value)
      self.d[value]=datetime.now()
      if self.get_size()>self.capapcity:
        self.d.popitem(last=False)
    except ValueError:
      print("Value Should be on int value.")

  def printcache(self):
    print(self.d.keys())

  def get(self):
    value=self.d.popitem()[0]
    print(value)
    self.d[value]=datetime.now()

  def get_size(self):
    return len(self.d)





