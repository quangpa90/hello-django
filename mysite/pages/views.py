from django.shortcuts import render
from django.http import HttpResponse
from untils.mock_api import MockApi
# Create your views here.
def home_page(request):
    id = request.GET.get("id")
    mock_api = MockApi()
    products = mock_api.get_products_by_category(id)
    data = {"category":"Close","my_products":products}
    return render(request, 'pages/home.html',data)
def category(request):
    return render(request, 'pages/category.html')