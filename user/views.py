from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .serializers import CustomTokenObtainPairSerializer, CustomTokenRefreshSerializer, UserSerializer
from .models import User
from shared.permissions import DenyAccess, IsCustomer


class ObtainJWTTokenPair(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class RefreshJWTToken(TokenRefreshView):
    serializer_class = CustomTokenRefreshSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
   
    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [permissions.AllowAny]
        elif self.action == 'get_auth_user':
            permission_classes = [permissions.IsAuthenticated]    
        elif IsCustomer:
            permission_classes = [DenyAccess]
        else:
            permission_classes = [permissions.IsAuthenticated]

        return [permission() for permission in permission_classes]

    @action(methods=['get'], url_path='me', detail=False)
    def get_auth_user(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)    
    

    
