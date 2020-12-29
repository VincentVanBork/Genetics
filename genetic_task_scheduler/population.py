from chromosome import Chromosome


class Population():
    """
    mutability how often mutations happen
    adaptability how much chromosome must be damaged to die (9-49) length of the chromosome
    survivability how many chromosomes are picked from the population as offspring (least 0-Npop) e.g. 5 with lowest time
    """
    def __init__(self, df, size=100, mutability=5, surivability=0, adaptability=10) -> None:
        super().__init__()
        self.chromosomes:list[Chromosome] = []
        self.mutability = mutability
        self.surivability = surivability
        # self.next_generation = []
        for i in range(size):
            self.chromosomes.append(Chromosome(df))
        self.fitness:list[int] = []
        self.adaptability = adaptability
        self.size = size 
        self.best = float('inf')
    
    def mutate_generation(self):
        for chromosome in self.chromosomes:
            chromosome.mutate(self.mutability)

    def next_generation(self):
        # assert len(self.chromosomes) >=0
        # print(self.fitness)
        # self.fitness = [chromosome.fitness() for chromosome in self.chromosomes]
        # self.fitness.sort()
        # print(self.fitness)
        # self.chromosomes = self.fitness[:self.adaptability]    
        # self.best = self.chromosomes[0]

    def repopulate_generation(self):
        while len(self.chromosomes) < self.size:
            for chromosome in self.chromosomes:
                print("CHROM", chromosome)
                self.chromosomes.append(chromosome.copy())