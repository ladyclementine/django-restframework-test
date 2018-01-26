from django.db import models

class CotacaoRequest(models.Model):
    name = models.CharField(verbose_name='Nome', max_length=200, blank=False, null=True)
    email = models.CharField(verbose_name='Email', max_length=200, blank=False, null=True)
    vehicle_type = models.CharField(verbose_name='Tipo de veículo', max_length=200, null=True, blank=True)
    board_number = models.CharField(verbose_name='Número de placa', max_length=8, blank=True, null=True)

    class Meta:
        db_table = "CotacaoRequest"
        verbose_name = "Pedido de Cotação"
        verbose_name_plural = 'Pedidos de Cotação'