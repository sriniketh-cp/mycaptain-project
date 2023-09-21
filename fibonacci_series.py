class Fibonacci:
  def __init__(self, fMax):
    self.f1 = 0
    self.f2 = 1
    self.fSum = 0
    self.fMax = fMax

  def generate_fibonacci_series(self):
    print("The Fibonacci series is:")
    while self.fSum < self.fMax:
      print(self.fSum)
      self.fSum = self.f1 + self.f2
      self.f1 = self.f2
      self.f2 = self.fSum

if __name__ == '__main__':
  f = Fibonacci(100)
  f.generate_fibonacci_series()
