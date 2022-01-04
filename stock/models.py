from django.db import models




class ArticuloFarmacia(models.Model):
    nombreArticulo=models.CharField(max_length=75)
    cantidad=models.IntegerField(null=True, blank=True)
    fecharda=models.DateField(null=True, blank=True)
    created=models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated=models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        verbose_name='ArticuloFarmacia'
        verbose_name_plural='ArticulosFarmacia'

    def __str__(self):
        return self.nombreArticulo

class ArticuloFarmaciaLiquido(models.Model):
    nombreArticulo=models.CharField(max_length=75)
    cantidad=models.IntegerField(null=True, blank=True)
    fecharda=models.DateField(null=True, blank=True)
    created=models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated=models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        verbose_name='ArticuloFarmaciaLiquido'
        verbose_name_plural='ArticulosFarmaciaLiquido'

    def __str__(self):
        return self.nombreArticulo
