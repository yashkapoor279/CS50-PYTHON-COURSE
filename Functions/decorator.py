#function defined inside a main function without changing the main function is called a decorator


def myd(func):
  def wrapper():
    print("Ghayal hu isiliye ghaatak hu")
    func()
    print("hawa hawa")
  return wrapper

@myd
def lyari():
  print("Slmkum lyari")

lyari()