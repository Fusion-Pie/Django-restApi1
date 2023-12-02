from .serialize import GangInfoSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import GangInfo

context = {}

# Create your views here.
@api_view(['GET'])
def gangList(request):
    # Serving Full gang info
    gangInfo = GangInfo.objects.all()
    serializer = GangInfoSerializer(gangInfo, many = True)
    context['status'] = status.HTTP_200_OK
    context['data'] = serializer.data
    return Response(context)
    
@api_view(['GET'])
def gangInfo(request, id):
    # Serving the particular gang member
    try:
        gangMem = GangInfo.objects.get(id = id)
        serializer = GangInfoSerializer(gangMem)
        context['status'] = status.HTTP_200_OK
        context['data'] = serializer.data
    except:
        context['status'] = status.HTTP_204_NO_CONTENT
        context['data'] = 'No Gang Member'

    return Response(context)

@api_view(['POST'])
def gangAddMember(request):
    # Added member in the gang
    serializer = GangInfoSerializer(data = request.data)
    
    # If data is valid
    if serializer.is_valid():
        serializer.save()
        context['status'] = status.HTTP_201_CREATED
        context['data'] = serializer.data
    else:
        context['status'] = status.HTTP_400_BAD_REQUEST
        context['data'] = {}
    
    return Response(context)

@api_view(['PUT'])
def updateGangMember(request):
    # Updating the already present member
    try:
        gangMem = GangInfo.objects.get(id= request.data['id'])
        
        serializer = GangInfoSerializer(instance=gangMem, data=request.data)

        if serializer.is_valid():
            serializer.save()

        context['status'] = status.HTTP_200_OK
        context['data'] = serializer.data

    except:
        context['status'] = status.HTTP_204_NO_CONTENT
        context['data'] = 'No memeber found to update'

    return Response(context)


@api_view(['DELETE'])
def deleteGangMember(request, id):
    try:
        gangMem = GangInfo.objects.get(id=id)
        gangMem.delete()       

        context['status'] = status.HTTP_200_OK
        context['data'] = 'Member Deleted'

        return Response(context) 
    except:
        context['status'] = status.HTTP_204_NO_CONTENT
        context['data'] = 'No Member found to delete'

        return Response(context)