from django.db import models


class City(models.Model):
    city_name = models.CharField(max_length=50, blank=None, null=None)

    def __str__(self):
        return f"{self.city_name}"

    class Meta:
        verbose_name_plural = "Города"


class Street(models.Model):
    street_name = models.CharField(max_length=100, null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='city')

    def __str__(self):
        return f"{self.street_name}"

    class Meta:
        verbose_name_plural = "Улицы"


class Shop(models.Model):
    shop_name = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    street = models.ForeignKey(Street, on_delete=models.SET_NULL, null=True)
    house_number = models.IntegerField()
    open = models.TimeField()
    close = models.TimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.shop_name}"

    class Meta:
        verbose_name_plural = "Магазины"
