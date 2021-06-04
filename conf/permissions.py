from rest_framework.permissions import BasePermission


class ApiBasePermission(BasePermission):
    def __init__(self, perm_id):
        self.perm_id = perm_id
        super(ApiBasePermission, self).__init__()

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        if request.user.is_superuser is True:
            return True
        else:
            for perm in self.perm_id:
                if request.user.role.permission.filter(pk=perm).exists():
                    return True
            return False
