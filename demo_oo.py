class Mesure:

    def __init__(self, ip, batch, serie):
        self.ip = ip
        self._batch = batch
        self.serie = serie

    @property
    def batch(self):
        return self._batch

    @batch.setter
    def batch(self, value):
        if value.startswith("B"):
            self._batch = value
        else:
            raise ValueError("Bad Batch")


    def acquire(self):
        pass

    def save(self, path):
        pass

    def search(self, batch):
        pass

if __name__ == '__main__':
    mesure = Mesure("0.0.0.0", 123, 456)
    mesure.batch = "C789"
    print(mesure.batch)