def power(n, pow):
  return n**pow
def triangle(height):
  for i in range(1,height):
    print('*' * i)
  return 0

if __name__ == '__main__':
  print(f'In the main function execution\nAuthor : Ravisankar')
  print(power(10, 3))
  triangle(5)
