import random
import colorama
from colorama import Fore


number = random.randrange(1,100)
guess = int(input(Fore.LIGHTCYAN_EX + str('guess my number from 1 to 100!')))
while guess<number or guess>number:
  if guess>number:
    print(Fore.RED + str('too high!'))
    guess = int(input(Fore.LIGHTCYAN_EX + str('guess again!')))
  elif guess<number:
    print(Fore.LIGHTYELLOW_EX + str('too low!'))
    guess = int(input(Fore.LIGHTCYAN_EX + str('guess again!')))
else:
    print(Fore.LIGHTGREEN_EX + str('you got it!'))
