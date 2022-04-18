from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from super_types.models import Super_Types
from .models import Supers
from .serializers import SupersSerializer


@api_view(['GET', 'POST'])
def supers_list(request):
    if request.method == 'GET':
        type_param = request.query_params.get('type')
        supers = Supers.objects.all()
        super_types = Super_Types.objects.all()
        custom_response = {}

        if type_param:
            supers = supers.filter(super_type__type=type_param)
            serializer = SupersSerializer(supers, many=True)
            return Response(serializer.data)
        
        for super_type in super_types:
            heroes = Supers.objects.filter(super_type_id=1)
            heroes_serializer = SupersSerializer(heroes, many=True)
            villians = Supers.objects.filter(super_type_id=2)
            villians_serializer = SupersSerializer(villians, many=True)
            custom_response = {
                'heroes': heroes_serializer.data,
                'villians': villians_serializer.data
            }
        return Response(custom_response)



    elif request.method == 'POST':
        serializer = SupersSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def supers_details(request, pk):
    supers = get_object_or_404(Supers, pk=pk)
    if request.method == 'GET':
        serializer = SupersSerializer(supers)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SupersSerializer(supers, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        supers.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
