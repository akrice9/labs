import random

question = input("Ask a question: ")
number = random.randrange(1,7)
if number<2:
  print("yes, definitely")
if 1<number<3:
  print("As I see it")
if 2<number<4:
  print("Ask again later")
if 3<number<5:
  print("Cannot predict now")
if 4<number<6:
  print("Don't count on it")
if 5<number<7:
  print("Very doubtful")
if 6<number:
  print("Definitely not")