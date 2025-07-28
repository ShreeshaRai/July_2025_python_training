from add import add,sub,mul
from module import checksum
from module2 import Person
result=add(4,5)
print(result)
result1=sub(4,5)
print(result1)
result2=mul(4,5)
print(result2)
try:
    checksum(1150)
except exception as e:
    print(e)
person=Person()
person.printname("sample")
