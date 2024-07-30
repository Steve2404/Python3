from gen_for2 import queue

def big_queue():
    yield 0
    yield from queue(1, 2, 3, 4)
    yield 5
    
b_queue = big_queue()  
for _ in range(7):
    print(next(b_queue))
    #b_queue.send("Hello")