from rest_framework import generics
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserSerializer

class UserLoginView(generics.GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data

        refresh = RefreshToken.for_user(user)
        response = {
            'refresh' : str(refresh),
            'access' : str(refresh.access_token)
        }

        return Response(response)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protected_view(request):
    # 보호된 뷰 로직을 여기에 작성하세요
    return Response({'message': 'This is a protected view.'})

# from rest_framework.response import Response
# from .models import Book
# from .serializers import BookSerializer
# from rest_framework import viewsets
# from rest_framework.decorators import action

# class BookViewSet(viewsets.ModelViewSet):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

#     @action(detail=True, methods=['post'])
#     def mark_as_read(self, request, pk=None):
#         book = self.get_object()
#         book.mark_as_read()
#         return Response({'status' : 'book marked as read'})

# from rest_framework.decorators import api_view , permission_classes
# from rest_framework.permissions import AllowAny
# from rest_framework import viewsets

# @api_view(['POST'])
# @permission_classes([AllowAny])
# def create_book(request):
#     serializer = BookSerializer(data = request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=201)
#     return Response(serializer.errors, status=400)


# from rest_framework.generics import ListAPIView

# class BookListView(ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

# from rest_framework import viewsets
# from rest_framework.decorators import action
# from .models import Book
# from .serializers import BookSerializer
# from rest_framework.response import Response

# class BookViewSet(viewsets.ViewSet):
#     def list(self, request):
#         queryset = Book.objects.all()
#         serializer = BookSerializer(queryset, many=True)
#         return Response(serializer.data)
    
#     def retrieve(self, request, pk=None):
#         book = Book.objects.get(pk=pk)
#         serializer = BookSerializer(book)
#         return Response(serializer.data)
    
#     def mark_as_read(self, request, pk=None):
#         book = Book.objects.get(pk=pk)
#         book.mark_as_read()
#         return Response({'status' : 'book marked as read'})


# from rest_framework import viewsets
# from rest_framework.decorators import action

# class MyViewSet(viewsets.ViewSet):
#     # 기본 CRUD 작업
#     def list(self, request):
#         # 리소스 목록 반환
#         pass
#     def create(self, request):
#         # 새로운 리소스 생성
#         pass
#     def retrieve(self, request, pk=None):
#         # 특정 ID의 리소스를 반환
#         pass
#     def destroy(self, request, pk=None):
#         # 특정 ID의 리소스 삭제
#         pass
    
#     # @action 데코레이터를 사용한 사용자 정의 작업

#     @action(detail=False, methods=['GET'])
#     def my_custom_action(self, request):
#         # 사용자 정의 작업의 구현
#         # 이 작업은 특정 리소스에 대해 동작하지 않음( detail=False )
#         # GET 요청에 응답함 (methods=['GET'])
#         pass