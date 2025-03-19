from django.contrib import admin
from .models import (
    Employee,
    Name,
    Gender,
    BntuDepartment,
    BntuPosition,
    Address,
    PhoneNumber,
    PhoneNumberType,
    Email,
    TradeUnionDepartment,
    TradeUnionPosition,
    WorkingGroup,
    Comment,
    Reward,
    Relative,
    RelativeType,
)


def register():

    # region Common
    admin.site.register(Name),
    # endregion

    # region BNTU
    admin.site.register(BntuPosition),
    admin.site.register(BntuDepartment),
    # endregion

    # region Contacts
    admin.site.register(PhoneNumber),
    admin.site.register(Address),
    admin.site.register(Email),
    # endregion

    # region Trade Union
    admin.site.register(TradeUnionPosition),
    admin.site.register(TradeUnionDepartment),
    admin.site.register(WorkingGroup),
    # endregion

    # region Other
    admin.site.register(Reward),
    admin.site.register(Relative),

    # endregion


register()
