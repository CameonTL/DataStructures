# This program allowed user inputs to be handled by an external class

from pets import Pets

def main():
  name = input('Enter your pet\'s name: ')
  animalType = input('Enter what kind of animal your pet is: ')
  age = int(input('Enter your pet\'s age: '))
  
  animalInfo = Pets(name, animalType, age)
  
  print('Here is the information you entered about your pet:')
  print(animalInfo)
  
main()
