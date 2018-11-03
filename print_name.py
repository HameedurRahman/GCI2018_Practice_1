a=str(input("\nEnter your name: "))

def reverse(a): 
  str = "" 
  for i in a: 
    str = i + str
  return str

print("Hello",a,", please to meet you! Did you know that your name backwards is ",(reverse(a)))


