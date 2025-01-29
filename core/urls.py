from django.contrib import admin
from django.urls import path

from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('talabalar/', talabalar_view, name='talabalar'),
    path('talabalar/<int:talaba_id>/', talaba_details_view),
    path('talabalar/<int:talaba_id>/delete/', talaba_delete_view),
    path('talabalar/<int:talaba_id>/update/', talaba_update_view),
    path('mualliflar/', mualliflar_view, name='mualliflar'),
    path('mualliflar/<int:pk>/delete-confirm/', muallif_delete_confirm_view),
    path('mualliflar/<int:pk>/delete/', muallif_delete_view),
    path('mualliflar/<int:pk>/update/', muallif_update_view),
    path('kitoblar/', kitoblar_view, name='kitoblar'),
    path('kitoblar/<int:pk>/update/', kitob_update_view),
    path("kitob-qo'shish/", kitob_qoshish_view, name='kitob_qoshish'),
    path('recordlar/', recordlar_view, name='recordlar'),
    path('recordlar/<int:pk>/update/', record_update_view),
]
