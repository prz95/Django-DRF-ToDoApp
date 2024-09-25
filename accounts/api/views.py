from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import (
    RegisterSerializer,
)


class RegisterApiView(generics.GenericAPIView):
    """Creates new user with the given info and credentials"""

    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        """
        Register class
        """

        serializer = RegisterSerializer(data=request.data, many=False)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)