from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='notes-home'),
    path('contact/', views.emailView, name='notes-contact'),
    path('mes/', views.mes, name='Marine Engineering Subjects'),
    path('iq/', views.iq, name='Interview Questions'),
    path('imuexam/', views.imuexam, name='IMU Exam'),
    path('news/', views.news, name='Maritime News'),
    path('career/', views.career, name='Career At Sea'),
    path('<int:subject_id>/docs/', views.docs, name='docs'),
    path('<int:subject_id>/<int:file_id>/docs/', views.docs, name='docs'),
    # path('email/', views.emailView, name='email'),
    path('success/', views.successView, name='success'),
    ] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
