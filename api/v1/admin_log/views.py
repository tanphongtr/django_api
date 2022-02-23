from rest_framework import generics
from django.contrib.admin.models import LogEntry
from django.contrib.auth.models import User
from .serializers import AdminLogSerializer
# from constance.admin import get_values

from constance import settings, LazyConfig
config = LazyConfig()

def get_values():
    """
    Get dictionary of values from the backend
    :return:
    """

    # First load a mapping between config name and default value
    default_initial = ((name, options[0])
                       for name, options in settings.CONFIG.items())

    # Then update the mapping with actually values from the backend
    initial = dict(default_initial, **dict(config._backend.mget(settings.CONFIG)))
    
    return initial
class AdminLogAPIView(generics.ListAPIView):
    
    queryset = LogEntry.objects.all()
    serializer_class = AdminLogSerializer
    filename = 'my_export.xlsx'

    def get(self, request, *args, **kwargs):
        print(get_values(), '='*10)
        return super().get(request, *args, **kwargs)