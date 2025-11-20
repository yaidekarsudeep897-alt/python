#iterators
list=[24,17,41]
it=iter(list)
print(next(it))
print(next(it))
print(next(it))

class CountDown():
    def __init__(self,start):
        self.start=start

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start<=0:
            raise StopIteration
        num=self.start
        self.start-=1
        return num
    
cd=CountDown(5)
for i in cd:
    print(i)

#Genarator
def simple_gen():
    yield 1
    yield 2
    yield 3

g=simple_gen()
for i in g:
    print(i)

def simple_gen(x):
    for i in range(x):
        yield i
g=simple_gen(5)
c=0
for i in g:
    if c>2:
        break
    print(i)
    c+=1