import numpy as np 

class Sort:
    def __init__(self,size):
        self.size = size
        self.cities = np.empty(self.size, dtype=Object)
        self.last_position = -1
    
    def list(self):
        if self.last_position == -1:
            print("Vetor vazio.")
        else:
            for index in range(self.last_position + 1):
                print(f"{index} -> {self.cities[index].label}")
                print(f"\t Heurística:  {self.cities[index].target_distance}")
                print(f"\t KM:  {self.cities[index].cost}")
                print(f"\t Star:  {self.cities[index].star_distance}\n")

    def insert(self, value):
        if self.last_position == (self.size - 1):
            print("Capacidade máxima atingida.")
            return
        
        position = 0
        for position in range(self.last_position + 1):
            if self.array[position].star_distance > value.star_distance:
                break
            
            if position == self.last_position:
                position += 1
        
        last_position = self.last_position
        while last_position >= position:
            next_position = last_position + 1
            self.array[next_position] = self.array[last_position]
            last_position -= 1
        self.array[position] = value
        self.last_position += 1