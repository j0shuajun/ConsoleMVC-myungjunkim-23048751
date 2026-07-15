"""In-memory sample storage. No console input/output belongs here."""


class Sample:
    def __init__(self, sample_id, name, average_production_time, yield_rate):
        self.sample_id = sample_id
        self.name = name
        self.average_production_time = average_production_time
        self.yield_rate = yield_rate


class SampleModel:
    def __init__(self):
        self._samples = []

    def add(self, sample):
        self._samples.append(sample)

    def list_all(self):
        return list(self._samples)

    def find(self, sample_id):
        for sample in self._samples:
            if sample.sample_id == sample_id:
                return sample
        return None
