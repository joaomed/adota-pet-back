from pickle import GET
from xmlrpc.client import ResponseError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_200_OK

from .serializers import PetSerializer
from .models import Pet


class PetList(APIView):
    def get(self, request, format=None):
        pets = Pet.objects.all()
        serializer = PetSerializer(pets, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

    def post(self, request, format=None):
        serializer = PetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(
            {
                "message": "Houveram erros de validação",
                "erros": serializer.errors,
            },
            status=HTTP_400_BAD_REQUEST,
        )
