class Task:
    def __init__(self, resources, time_weights) -> None:
        super().__init__()
        self.resources = resources 
        self.time_weights = time_weights