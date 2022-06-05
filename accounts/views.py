from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import DriverRegistrationSerializer
from .models import DriverRegistrations


@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def register_driver(request):
    if request.method == 'POST':
        serializer = DriverRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        print(request.user)
        driver_registrations = DriverRegistrations.objects.all()
        serializer = DriverRegistrationSerializer(driver_registrations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
