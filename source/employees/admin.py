from django.contrib import admin

from .utils.enumeration import Enumerated


from .models import (
    Employee,
    Name,
    BntuDepartment,
    BntuPosition,
    Address,
    PhoneNumber,
    Email,
    TradeUnionDepartment,
    TradeUnionPosition,
    Reward,
    Relative,
    EducationalInstitution,
    WorkingGroup,
    PhoneNumberType,
    RelativeType,
    Comment,
    Gender,
    AcademicDegree,
    EducationLevel,
    TradeUnionDepartmentOption,
    WorkingGroupOption,
)


def register():
    # region Common
    admin.site.register(Name),
    admin.site.register(Gender)
    # endregion

    # region BNTU
    admin.site.register(BntuPosition),
    admin.site.register(BntuDepartment),
    # endregion

    # region Contacts
    admin.site.register(PhoneNumber),
    admin.site.register(Address),
    admin.site.register(Email),
    admin.site.register(PhoneNumberType)
    # endregion

    # region Trade Union
    admin.site.register(TradeUnionPosition),
    admin.site.register(TradeUnionDepartment),
    admin.site.register(WorkingGroup),
    admin.site.register(TradeUnionDepartmentOption),
    admin.site.register(WorkingGroupOption),
    # endregion

    # region Education

    admin.site.register(EducationalInstitution)
    admin.site.register(EducationLevel)
    admin.site.register(AcademicDegree)

    # endregion

    # region Other
    admin.site.register(Reward),
    admin.site.register(Relative),
    admin.site.register(RelativeType),
    admin.site.register(Comment)

    # endregion

    admin.site.register(Employee)


register()
