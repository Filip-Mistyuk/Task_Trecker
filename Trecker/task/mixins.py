from django.core.exceptions import PermissionDenied

class UserIsOwnerMixin():
    def dispatch(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.user != self.request.user:
            raise PermissionDenied
        else: 
            return super().dispatch(request, *args, **kwargs)