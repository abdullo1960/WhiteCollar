from django.urls import path
from myapp.views import homePageView, pricePageView, aboutPageView, blogPageView, contactPageView, add_servicesPageView

app_name = "myapp"

urlpatterns = [
    path('', homePageView, name="home"),
    path('about/', aboutPageView, name="about"),
    path('blog/', blogPageView, name="blog"),
    path('contact/', contactPageView, name="contact"),
    path('price/', pricePageView, name="price"),
    path('services/', add_servicesPageView, name="services"),
]