from rest_framework import generics
from .models import SampleData
from .serializers import SampleDataSerializer

# Create/List_all
class SampleDataList(generics.ListCreateAPIView):
    queryset = SampleData.objects.all()
    serializer_class = SampleDataSerializer

#Retrieve/Delete One
class SampleDataDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SampleData.objects.all()
    serializer_class = SampleDataSerializer
