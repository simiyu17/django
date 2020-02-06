from rest_framework import generics
from .models import Employee
from .serializers import EmployeeSerializer

# Create/List_all
class EmployeeList(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

#Retrieve/Delete One
class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
