from time import sleep
import functools
import signal

class TimeoutException(RuntimeError):
    def __init__(self, message=None):
        super().__init__(message)


def handler(signum, frame):
    raise TimeoutException("Timed out")


def timeout(seconds):
  def decorator(func):
      if(seconds is None or seconds <= 0):
        return func
      @functools.wraps(func)
      def wrapper(*args, **argv):
          signal.signal(signal.SIGALRM, handler)
          signal.setitimer(signal.ITIMER_REAL, seconds)
          result = func(*args, **argv)
          signal.signal(signal.SIG_DFL)
          return result
      return wrapper
  return decorator


# @timeout(seconds=0.5)
# def func1():
#     sleep(0.1)


# try:
#     func1()
# except TimeoutException as e:
#     print(e)


@timeout(seconds= )
def func2():
    sleep(0.3)

def main():
  try:
      func2()
  except TimeoutException as e:
      print(e)

if __name__ == "__main__":
  main()