a=str(input("\nEnter your name: "))

def reverse(a): 
  b = "" 
  for i in a: 
    b = i + b
  return b

print("Hello",a,", pleased to meet you! Did you know that your name backwards is ",(reverse(a)))



