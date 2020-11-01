
Dog_Names ="Sweet" ,"Bob" , "Sam"
for name in Dog_Names:
    print(name)
    ''' Tree'''
def draw_tree(type, x, y):
    noStroke()
    if type == 0: # Circle Tree
       fill(84, 54 , 4)
       rect(x, y, 12, 40)

       fill(19,175,5)
       ellipse(x+6, y, 50, 50)

    elif type == 1: # Triangle Tree
      fill(84, 54, 4)
      rect(x, y, 12, 40)

      fill(19, 175, 5)
      triangle(x + 6, y - 20, x + 25, y + 30, x - 15, y + 30)

    elif type == 2: # Multi Triangle Tree 
      fill(84, 54, 4)
      rect(x, y, 11, 40)

is_hot = False
is_cold = True

if is_hot:
  print("It's Hot!")
  print("Really Hot!")
else:
  print("Not Hot!")



     
    










