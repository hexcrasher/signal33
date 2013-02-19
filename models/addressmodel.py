from models.modelbase import ModelBase

class AddressModel(ModelBase):

    def __init__(self):
        super(AddressModel, self).__init__()
        self.street = None
        self.street2 = None
        self.city = None
        self.state = None
        self.zip = None

