from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from .models import Item
from .serializers import ItemSerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all().order_by('-date_posted')
    serializer_class = ItemSerializer
    # Accept all content types: multipart for image uploads, JSON for edits
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def create(self, request, *args, **kwargs):
        # Debugging: print incoming payload to server console so we can inspect
        try:
            print('--- Item create called ---')
            print('Request data:', dict(request.data))
            # request.FILES is a dict-like object
            print('Files:', {k: getattr(v, 'name', str(v)) for k, v in request.FILES.items()})
        except Exception as e:
            print('Error printing request contents:', e)
        return super().create(request, *args, **kwargs)