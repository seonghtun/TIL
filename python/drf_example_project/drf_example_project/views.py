from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

@api_view(['GET','POST'])
@permission_classes([AllowAny])

def hello_rest_api(request):
    data = {'massage' : 'Hello rest api!'}
    return Response(data)