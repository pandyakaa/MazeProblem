# A simple implementation of Priority Queue 
# using Queue. 

# Digunakan untuk memudahkan pada saat melakukan algoritma A*
# SOURCE : https://www.geeksforgeeks.org/priority-queue-in-python/, accessed on Wednesday, 27/03/2019 21.43 

class PriorityQueue(object): 
    def __init__(self): 
        self.queue = [] 
  
    def __str__(self): 
        return ' '.join([str(i) for i in self.queue]) 
  
    # for checking if the queue is empty 
    def isEmpty(self): 
        return len(self.queue) == [] 
  
    # for inserting an element in the queue 
    def insert(self, data): 
        self.queue.append(data) 
  
    # for popping an element based on Priority 
    def delete(self): 
        try: 
            min = 0
            for i in range(len(self.queue)): 
                if self.queue[i].f < self.queue[min].f: 
                    min = i 
            item = self.queue[min] 
            del self.queue[min] 
            return item 
        except IndexError: 
            print() 
            exit() 