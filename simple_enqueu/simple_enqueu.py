
# python code for a queue  

# intialising the queue
queue = []

# handling the enqueue operation
queue.append('a')
queue.append('b')
queue.append('c')
  
print("Initial queue")
print(queue)

# handling the dequeue operation
print("\nElements dequeued from queue")
print(queue.pop(0))

# to return the data element (peek()) at the beginning of the list (head)
print('First item: ', queue[0])

# ouput the queue 
print("\nQueue after removing elements")
print(queue)


