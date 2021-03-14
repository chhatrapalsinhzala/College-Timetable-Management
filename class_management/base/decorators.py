from staff.models import Staff
from class_management import settings
from rest_framework.response import Response



def check_permissions(role):
    def _method_wrapper(func):
        def _arguments_wrapper(request, *args, **kwargs):
            staff = None
            try:
                staff = request.request.user.staff
            except (Staff.DoesNotExist, AttributeError):
                return Response("Authentication Failure", status=401)

            role_level = settings.PERMISSION_LEVELS[role.upper()]
            staff_level = settings.PERMISSION_LEVELS[staff.get_role().upper()]

            if staff:
                if staff_level >= role_level:
                    return func(request, *args, **kwargs)
                else:
                    return Response("Permission Denied", status=403)
            else:
                return Response("Authentication Failure", status=401)

        return _arguments_wrapper
    return _method_wrapper