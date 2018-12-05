
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from users import views as user_views
from transactions import views as transaction_views
from Save import views as save_views
from budget import views as budget_views
from csvreader import views as csv_views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', include('Save.urls')),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('newtransaction/', transaction_views.TransactionCreateView.as_view(), name='transaction-create'),
    path('transactiondetail/<int:pk>/', transaction_views.TransactionDetailView.as_view(), name='transaction-detail'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('admin/', admin.site.urls),
    path('progress/', save_views.progress, name='save-progress'),
    path('budget/', budget_views.BudgetCreateView.as_view(), name='budget-create'),
    path('editbudget/<int:pk>/', budget_views.BudgetUpdateView.as_view(), name='budget-edit'),
    path('transactions/',save_views.transactions, name='save-transactions'),
    path('transactionedit/<int:pk>/',transaction_views.TransactionUpdateView.as_view(), name='transaction-edit'),
    path('transactiondelete/<int:pk>/', transaction_views.TransactionDeleteView.as_view(), name='transaction-delete'),
    path('transactiondelete/<int:pk>/', transaction_views.TransactionDeleteView.as_view(), name='transaction-delete'),
    path('uploadfile/', transaction_views.transaction_upload, name='upload-transaction'),
]
