from django.core.management.base import BaseCommand
from dz2.models import Сustomer
class Command(BaseCommand):
    help = "Create user."
    def handle(self, *args, **kwargs):
        customer = Сustomer(name='John', email='john@example.com',
                        phone='+71231231212', adress = 'Электросталь, ул. Ленина, 23д. 5кв.', 
                        date = 12/12/2000)
        customer.save()
        self.stdout.write(f'{customer}')