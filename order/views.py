from django.shortcuts import render
from .models import Book, Order
from .serializers import BookSerializer, OrderSerializer
from rest_framework import generics
from django.http import HttpResponse
from django.core.mail import send_mail
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookGetEditDelView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class OrderListView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderEditView(generics.RetrieveUpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDeleteView(generics.RetrieveDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


@csrf_exempt
@api_view(['POST'])
def SendEmail(request):
    mess = ""

    if request.method == "POST":
        orders = request.data.get('orders')
        name = request.data.get("name")
        address = request.data.get("address")
        tel = request.data.get("tel")
        email = request.data.get("email")
        comment = request.data.get("comment")

        for order in orders:
            order_object = Order.objects.get(
                item_title=order["item_title"], cleared=False)
            order_object.cleared = True
            order_object.save()

            m = "Book title: " + \
                order["item_title"] + "\nClass: " + \
                order["level"] + " " + order["class_no"] + "\n" + \
                "No of Books: " + str(order["order_quantity"]) + "\n" + \
                "No of Teachers Guide: " + \
                str(order["teachers_quantity"]) + \
                "\n" + "-------------------\n"

            mess += m
        mess += "Name: " + name + "\n" + "Telephone: " + \
            tel + "\n" + "Email: " + email + "\n" + "Delivery Location: " + \
                address + "\n" + "Comment: " + "\n" + comment + "\n"

        send_mail(
            'BOOK ORDER',
            mess,
            email,
            ['publishing@newvision.co.ug'],
            fail_silently=False,
        )
    return HttpResponse("hello")
