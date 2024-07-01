from math import inf

print("in true math")
print(__name__)

def divide (first, second):
    if second:
        return first/second
    return inf

if __name__ == '__main__':
   print ("in main")
