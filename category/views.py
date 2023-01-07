from rest_framework import viewsets, permissions
from .models import Category
from .serializers import CategorySerializer

# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
