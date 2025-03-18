class Mesure:

    def __init__(self, ip, batch, serie):
        self.ip = ip
        self.batch = batch
        self.serie = serie

    def acquire(self):
        pass

    def save(self, path):
        pass

    def search(self, batch):
        pass