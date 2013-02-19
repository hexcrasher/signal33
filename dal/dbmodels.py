#the objects in this file are just wrappers for my models
#i want to keep the models lite so we'll create dbmodels

from models.addressmodel import AddressModel
from models.usermodel import UserLogOnModel, UserModel, UserRegisterModel

class AddressDBModel(AddressModel):

    def __index__(self):
        super(AddressDBModel, self).__init__()


class UserLogOnDBModel(UserLogOnModel):

    def __index__(self):
        super(UserLogOnDBModel, self).__init__()

class UserDBModel(UserModel):

    def __index__(self):
        super(UserDBModel, self).__init__()

class UserRegisterDBModel(UserRegisterModel):

    def __index__(self):
        super(UserRegisterDBModel, self).__init__()