from django.db import models

class EmailType(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Тип имейла'
        verbose_name_plural = 'Типы имейлов'
        
class EmailSendingFact(models.Model):
    type = models.ForeignKey(EmailType, on_delete=models.CASCADE)
    order = models.ForeignKey('print.Orders', null=True, blank=True, default=None, on_delete=models.CASCADE)
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    class Meta:
        verbose_name = 'Имейл заказа фотографий'
        verbose_name_plural = 'Имейлы заказов фотографий'
