
class CustomerMixin(object):
    def is_customer(self):
        return hasattr(self, 'customer')
