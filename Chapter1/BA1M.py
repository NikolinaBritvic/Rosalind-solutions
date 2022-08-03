# Implement NumberToPattern

def NumberToPattern(number,k):
  rez=""
  D={0:"A",1:"C",2:"G",3:"T"}
  for i in range(k):
    rez+=str(D[number%4])
    number=number//4
  return rez

number=int(input("Number: "))
k=int(input("k: "))
print(NumberToPattern(number,k))
