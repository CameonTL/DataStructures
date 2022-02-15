# This program plays a game where three coins are flipped and their value is added to the balance if they land heads

from coin import Coin

def main():
  myCoin = Coin()
  
  QUARTER = 0.25
  DIME = 0.1
  NICKEL = 0.05
  balance = 0
  
  enter = ''
  while enter == '' and balance < 1.00:
    thisRnd = 0
    print('Flipping coins...')
    myCoin.toss()
    quart = myCoin.get_sideup()
    print('The quarter was', quart)
    if quart == 'Heads':
      balance += QUARTER
      thisRnd += QUARTER
    myCoin.toss()
    nick = myCoin.get_sideup()
    print('The nickel was', nick)
    if nick == 'Heads':
      balance += NICKEL
      thisRnd += NICKEL
    myCoin.toss()
    dim = myCoin.get_sideup()
    print('The dime was', dim)
    if dim == 'Heads':
      balance += DIME
      thisRnd += DIME
    print('You have earned $', format(thisRnd, '.2f'), 'this round.')
    print('Your balance is', format(balance, '.2f'))
    enter = input('Press the enter key to continue')
  if balance == 1.0:
    print('You win!')
  elif balance > 1.0:
    print('Your balance went over $1.00. You lost.')
