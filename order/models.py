from django.db import models
from django.contrib.auth.models import User

# Create your models here.


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
    item_title = models.CharField(
        max_length=500, blank=False, null=False, default="")
    class_no = models.CharField(
        max_length=500, blank=False, null=False, default="")
    level = models.CharField(max_length=500, default="")
    order_quantity = models.PositiveIntegerField()
    teachers_quantity = models.PositiveIntegerField(default=0)
    cleared = models.BooleanField(default=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (
            " - Order: " + self.item_title +
            " - class: " + self.level + self.class_no +
            " - Quantity: " + str(self.order_quantity) +
            " - Teachers guide quantity: " + str(self.teachers_quantity)
        )
