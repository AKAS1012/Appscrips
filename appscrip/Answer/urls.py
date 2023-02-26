from django.urls import path

from .views import NameListAV, NameDetail, CricketerListAV, CricketerDetail, ColorListAV, ColorDetailAV

urlpatterns = [
	path('name/', NameListAV.as_view(), name='name_list'),
	path('name/<int:pk>', NameDetail.as_view()),
	path('cricketer/', CricketerListAV.as_view(), name='cricketer_list'),
	path('cricketer/<int:pk>', CricketerDetail.as_view()),
	path('color/', ColorListAV.as_view(), name='color_list'),
	path('color/<int:pk>', ColorDetailAV.as_view()),

]
