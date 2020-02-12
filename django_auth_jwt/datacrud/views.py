from rest_framework import generics
from .models import SampleData
from .serializers import SampleDataSerializer
from rest_framework import views, permissions, status

# Create/List_all
class SampleDataList(generics.ListCreateAPIView):

    #Allow only authenticated users
    permission_classes = [permissions.IsAuthenticated]

    queryset = SampleData.objects.all()
    serializer_class = SampleDataSerializer

#Retrieve/Delete One
class SampleDataDetail(generics.RetrieveUpdateDestroyAPIView):

    #Allow only authenticated users
    permission_classes = [permissions.IsAuthenticated]

    queryset = SampleData.objects.all()
    serializer_class = SampleDataSerializer