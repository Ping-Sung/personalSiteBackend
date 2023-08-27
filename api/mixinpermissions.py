from rest_framework.permissions import IsAdminUser

from .permissions import IsStaffEditorPermissions

class StaffEditorPermissionsMinxin:
    permission_classes = [IsStaffEditorPermissions, IsAdminUser]