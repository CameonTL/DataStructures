class Pets:
  def __init__(self, name, animalType, age):
    self.name = name
    self.animalType = animalType
    self.age = age
    
  def setName(self, name):
    self.name = name
    
  def setAnimalType(self, animalType):
    self.animalType = animalType
    
  def setAge(self, age):
    self.age = age
    
  def getName(self):
    return self.name
  
  def getAnimalType(self):
    return self.animalType
  
  def getAge(self):
    return self.age
  
  def __str__(self):
    msg = 'Pet\'s name: ' + self.getName()
    msg += '\nAnimal type: ' + self.getAnimalType()
    msg += '\nPet\'s age: ' + str(self.getAge())
    return msg
