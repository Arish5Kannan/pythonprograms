print("********STONE PAPER SCISSOR**********")
print("Welcome to the Game........")
print("Choices are:  1.s(stone) 2.p(paper) 3.sc(scissor)")
s = input("Do you want to start(say yes or no)?: ")
count = 0
if s=='yes' or s=='YES':
    while(True):
      f = input("Enter your choice(s/sc/p): ")
      if(f=='s' or f=='sc'):
          print("Machine choice(s/sc/p): p ")
          print("Machine won 1 point")
          h = 'p'
      elif f=='p' or f=='s':
          print("Machine choice(s/sc/p): sc ")
          print("Machine won 1 point")
          h = 'sc'
      else:
          print("Machine choice(s/sc/p): s ")
          print("Machine won 1 point")
          h = 's'
      if f=='p' and h=='sc' or f=='s' and h=='p':
          count += 1
      else:
          print("Sorry, Game over")
          print(f"Your score :{count}")
          print("Congratulations!!!")
          break
else:
    print("************Try when you have intrest*********")


