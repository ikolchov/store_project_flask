from random import randint

import factory

from db import db
from models import UserModel, EmployeeModel, EmployeeRoles


class BaseFactory(factory.Factory):
    @classmethod
    def create(cls, **kwargs):
        obj = super().create(**kwargs)
        db.session.add(obj)
        db.session.flush()
        return obj


class UserModelFactory(BaseFactory):
    class Meta:
        model = UserModel

    id = factory.Sequence(lambda n:n)
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.Faker('email')
    phone = str('1234567890')
    password = factory.Faker('password')


class EmployeeModelFactory(BaseFactory):
    class Meta:
        model = EmployeeModel

    id = factory.Sequence(lambda n:n)
    username = factory.Faker('first_name')
    first_name = factory.Faker('first_name')
    mid_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    user_role = EmployeeRoles.worker
    email = factory.Faker('email')
    phone = str(randint(1000000000, 2000000000))
    password = factory.Faker('password')
