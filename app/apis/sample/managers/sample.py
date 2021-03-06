from app.apis.sample.models.sample import Sample


class SampleManager:
    def __init__(self):
        self.Sample = Sample

    def create_entry(self, sample_data_attributes={}):
        return self.Sample.add(**sample_data_attributes)

    def get_list(self):
        return self.Sample.objects
