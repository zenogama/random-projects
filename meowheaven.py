def main():
    number= get_number()
    woof(number)

def get_number():
      while True:
           n=int(input('how many times do you want me to woof? '))
           if n>0:
                return n

def woof(n):
     for _ in range(n):
          print('woof')

main()