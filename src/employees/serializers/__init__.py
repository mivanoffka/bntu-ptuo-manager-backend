from .employee_version_serializer import EmployeeVersionSerializer
from .employee_serializer import EmployeeSerializer

from .common import GenderSerializer
from .bntu import BntuPositionSerializer
from .trade_union import TradeUnionPositionSerializer, WorkingGroupSerializer
from .other import (
    CommentSerializer,
    RelativeSerializer,
    RewardSerializer,
    RelativeTypeSerializer,
)
from .contacts import (
    PhoneNumberSerializer,
    EmailSerializer,
    AddressSerializer,
    PhoneNumberTypeSerializer,
)
from .education import (
    EducationalInstitutionSerializer,
    AcademicDegreeSerializer,
    EducationLevelSerializer,
)

from .generic import EnumeratedSerializer, TreeNodeSerializer

from .tree_serializer import (
    BntuDepartmentOptionSerializer,
    TreeSerializer,
    TradeUnionDepartmentOptionSerializer,
)
