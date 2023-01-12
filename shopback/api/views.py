from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Products, Categories
from .serializer import ProductsSerializer, CategoriesSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView


# Create your views here.
class ProductsListAPI(ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer


class ProductsRetrieveAPI(RetrieveAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer


class CategoriesListAPI(ListAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer


class CategoriesRetrieveAPI(RetrieveAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer


class CategoryProductsListAPI(APIView):
    def get(self, request, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({'error': 'Method GET not allowed'})
        products = Products.objects.filter(category_id=pk)
        if len(products) < 1:
            return Response({'error': 'Products not found'})
        return Response({'products': ProductsSerializer(products, many=True).data})
