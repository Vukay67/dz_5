from django.db import models

# class НазваниеМодели(models.Model):
#   поля...

# CharField - текстовое поле, можно передать ограничение по длине
# TextField - большое текстовое поле, можно передать ограничение по длине
# IntegerField - числовое поле(от -бесконечности до +бесконечности)
# PositiveIntegerField - положительное числовое поле (от 0 и выше)

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    description = models.TextField(max_length=2000)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} ({self.price} сом) (На складе: {self.quantity})"
    
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=10000)
    likes = models.PositiveIntegerField()

    def __str__(self):
        return f"Загаловок: {self.title} ||| Количество лайков: {self.likes}"