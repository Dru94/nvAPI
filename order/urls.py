from django.urls import path
from .views import (BookListView, BookGetEditDelView, BookCreateView,
                    OrderListView, OrderCreateView, OrderEditView, SendEmail)

urlpatterns = [
    path('', BookListView.as_view(), name="book-list"),
    path('orders', OrderListView.as_view(), name="order-list"),
    path('add-order', OrderCreateView.as_view(), name="order-create"),
    path('edit-order', OrderEditView.as_view(), name="order-edit"),
    path('send-order', SendEmail, name="send-email")

]
