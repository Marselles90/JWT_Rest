from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import filters, viewsets, pagination
from django_filters.rest_framework import FilterSet, DjangoFilterBackend

from .serializers import UserSerializer
from .models import User



class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

class UserPaginatoins(pagination.PageNumberPagination):
    '''
    PageNumberPagination - обеспечивает пагинацию для модели News.
    page_size - количество элементов на странице.
    page_size_query_param - параметр для указания количества элементов на странице.
    max_page_size - максимальное количество элементов на странице.
    '''
    page_size = 12
    page_size_query_param = 'page_size'
    max_page_size = 100



class FilterUser(FilterSet):
    class Meta:
        model = User
        fields = ['username', 'is_active', 'email']
        
        
class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]
    search_fields = ['']
    pagination_class = UserPaginatoins
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = FilterUser