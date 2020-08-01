from . import views
from django.urls import path
from django.conf import settings 
from django.conf.urls.static import static 

urlpatterns = [

  path('', views.home_view, name='home'),
  path('search-result', views.search_view, name='search'),
  path('<int:question_id>', views.detail_view, name='detail-view'),
  path('<int:question_id>/liked', views.like_view, name='liked'),
]

if settings.DEBUG: 
       urlpatterns += static(settings.MEDIA_URL, 
                             document_root=settings.MEDIA_ROOT) 
#
