from enum import Enum


class ProductGroup(Enum):
    luminaire = "luminaire"
    power_tool = "power tool"
    garden_tool = "garden tool"
    paint = "paint"


class ProductStatus(Enum):
    delete = "deleted"
    update = "under update"
    active = "active"
    oos = "out of stock"


class EmployeeRoles(Enum):
    owner = "owner"
    manager = "manager"
    senior = "senior worker"
    worker = "worker"
