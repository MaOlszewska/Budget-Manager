from .views import ExpenseList, ExpenseDetail, ExpenseAdd, ExpenseUpdate, ExpenseDelete, UserLoginView,UserRegister
from django.urls import path
from django.contrib.auth.views import LogoutView

from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', ExpenseList.as_view(), name = 'expenses'),
    path('expense/<int:pk>/', ExpenseDetail.as_view(), name = 'expense'),
    path('add-expense/', ExpenseAdd.as_view(), name = 'add-expense'),
    path('update-expense/<int:pk>/', ExpenseUpdate.as_view(), name = 'update-expense'),
    path('delete-expense/<int:pk>/', ExpenseDelete.as_view(), name = 'delete-expense'),
    path('login/', UserLoginView.as_view(), name = 'login'),
    path('logout/', LogoutView.as_view(next_page='login'), name = 'logout'),
    path('register/', UserRegister.as_view(), name='register'),
    path('piechart/',views.barchart,name='piechart')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

