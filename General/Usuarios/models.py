from django.contrib.auth.models import User
from django.db.models.signals import post_save

def actualizar_id(sender, instance, created, **kwargs):
    if created:
        cantidad = User.objects.count()
        print(cantidad)
        user = User.objects.get(id = instance.id)
        if cantidad == 1:
            user.is_superuser=True
        else:
            user.is_staff=True
        user.save()

post_save.connect(actualizar_id, sender= User)