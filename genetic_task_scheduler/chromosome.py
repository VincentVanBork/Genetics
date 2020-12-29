import random
#TODO check __call__ in python
import pandas as pd

def check_overlapping(x, y):
    return [False if ((x.start == x.stop) or (oth.start == oth.stop)) else ((x.start < oth.stop  and x.stop > oth.start) or (x.stop  > oth.start and oth.stop > x.start)) for oth in y]

class Gene:
    def __init__(self, resources, time_weights, start_time) -> None:
        super().__init__()
        self.resources:list = resources 
        self.time_weights:list = time_weights
        self.start_time:int = start_time
        self.finish = sum([time for time in self.time_weights])
    
    def sequence_time(self, protein):
        return self.start_time , self.start_time + self.time_weights.get(protein)

class Chromosome():
    def __init__(self, tasks:pd.DataFrame) -> None:
        super().__init__()
        self.genes = []
        self.damage = 0
        
        for i in range(50):
            self.genes.append(Gene(tasks[f"R.{i}"].to_list(), tasks[f"T.{i}"].to_list()))
        
        self.max_time = sum([gene.finish for gene in self.genes])
        self.current_time = self.max_time 

    def check_integrity(self, max_num_overlaps):
        """
        if any tasks for some resource overlap dies
        """
        for protein in range(11):
            ranges = []
            for gene in self.genes:
                start_time, end_time = gene.sequence_time(protein)
                ranges.append(range(start_time, end_time+1))

            for index, sth in ranges:
                damages = check_overlapping(sth, ranges[:index] + ranges[index+1:])
                if any(damages):
                    self.damage +=1

        if self.damage > max_num_overlaps:
            return False
        else:
            return True

    def mutate(self, number_of_mutations):
        """
        exchange places at random
        """
        mutations = []
        for i in range(number_of_mutations+1):
            old_gene = random.choice(self.genes)
            try:
                mutations.index(old_gene)
                
            except ValueError:
                old_gene = random.choice(self.genes)
            finally:
                old_gene.start_time = random.choice(range(self.max_time - old_gene.finish))

    def fitness(self):
        """
        calculate how much time tasks take in this chromosome
        """
        #TODO idk how yet
        return self.current_time
