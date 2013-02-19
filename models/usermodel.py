from models.modelbase import ModelBase
from models.addressmodel import AddressModel

class UserModel(ModelBase):

    def __init__(self):
        super(UserModel, self).__init__()
        self.user_name = None
        self.email_address = None
        self.first_name = None
        self.last_name = None



class UserRegisterModel(UserModel, AddressModel):

    def __init__(self):
        super(UserRegisterModel, self).__init__()
        self.password = None
        self.confirm_email_address = None
        self.confirm_password = None

class UserLogOnModel(UserModel):

    def __init__(self):
        super(UserLogOnModel, self).__init__()