from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Customer(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=False, null=True)
    last_name = models.CharField(max_length=100, blank=False, null=True)
    email = models.EmailField()

    def __str__(self):
        return self.first_name + " " + self.last_name + " - " + self.email


class Book(models.Model):
    LEVELS = (
        ('PRIMARY', 'PRIMARY'),
        ('SENIOR', 'SENIOR')
    )

    title = models.CharField(max_length=100, blank=False, null=False)
    subject = models.CharField(max_length=100, blank=False, null=False)
    class_number = models.CharField(max_length=10, blank=False, null=False)
    level = models.CharField(max_length=100, choices=LEVELS)
    cost = models.PositiveBigIntegerField(null=False)
    teachers_guide = models.PositiveBigIntegerField(null=False)

    def __str__(self):
        return (self.title + " - " + self.level + " "
                + self.class_number + " - Cost: " +
                str(self.cost) + " Ugx. - Teachers guide: "
                + str(self.teachers_guide) + " Ugx."
                )


class Order(models.Model):
    name = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_no = models.PositiveBigIntegerField()
    address = models.CharField(max_length=500, blank=False, null=False)
    phone_number = models.PositiveBigIntegerField()
    order_item = models.ForeignKey(Book, on_delete=models.RESTRICT)
    quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return ("Order_no: " + str(self.order_no) +
                " - Name: " + self.name.first_name + " " + self.name.last_name +
                " - Order: " + self.order_item.title +
                " - Quantity: " + str(self.quantity) +
                " - Address" + self.address +
                " - Telephone: "+str(self.phone_number)
                )
