from django.db.models.signals import post_migrate
from django.dispatch import receiver
from base.models import Position , BankNames , IdentityChoice , Language

@receiver(post_migrate)
def create_default_Entries(sender , **kwargs):
        if sender.name == 'base':
            Position.objects.create(position_name = 'Manager' , level = 'm4' )
            Position.objects.create(position_name = 'Agent' , level = 't1' )
            Position.objects.create(position_name = 'Leader' , level = 't4' )
            BankNames.objects.create(name = 'ICICI')
            BankNames.objects.create(name = 'HDFC')
            BankNames.objects.create(name = 'SBI')
            IdentityChoice.objects.create(name = 'AADHAR CARD')
            IdentityChoice.objects.create(name = 'PAN CARD')
            IdentityChoice.objects.create(name = 'PASSPORT')
            Language.objects.create(code = 'hi' ,name = 'Hindi')
            Language.objects.create(code = 'en' ,name = 'english')
            Language.objects.create(code = 'ru' ,name = 'Russian')
            Language.objects.create(code = 'ar' ,name = 'Arabic')