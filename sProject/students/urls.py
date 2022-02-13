from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'students'
urlpatterns = [
    path('', views.index ),
    path('reg/', views.regStudent, name='reg'),
    path('regCon/', views.regConStudent, name='regCon'),
    path('all/',views.readStudentAll, name='stuAll'),
    path('upload/',views.upload,name="upload"),
    path('upload_create/',views.upload_create,name="upload_create"),
    path('profile/',views.profile,name="profile"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)