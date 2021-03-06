from django.urls   import path
from product.views import PostView, ProductView, ProductDetailView, MenuView, BestProductView
urlpatterns = [
        path('/post', PostView.as_view()),
        path('/menu', MenuView.as_view()),
        path('/products_info', ProductView.as_view()),
        path('/<int:product_id>', ProductDetailView.as_view()),
        path('/best', BestProductView.as_view()),
]


