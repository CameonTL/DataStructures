# This program determines if a user input is a palindrome using a stack class

from stacks import Stack

def main():
  again = ''
  while again == '':
    word2 = ''
    s = Stack()
    word = input('Enter a word to test if it is a palindrome: ')
    for item in word:
      s.push(item)
    while not s.isEmpty():
      word2 += s.pop()
    if word == word2:
      print('This word is a palindrome.')
    else:
      print('This word is not a palindrome.')
    again = input('Press the enter key to test another word.')
    
main()
