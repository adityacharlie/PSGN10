from django.contrib.auth.models import AbstractUser


class Customer(AbstractUser):

    class Meta:
        verbose_name = 'customer'
        verbose_name_plural = 'customers'

    def get_full_name(self):
        return ' '.join((self.first_name, self.last_name)) if self.first_name or self.last_name else self.email
