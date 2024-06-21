from .models import Queue  

class UniqueQueue:
    def add(self, item):
        Queue.objects.create(item=item)

    def length(self):
        return Queue.objects.count()

    def last_added(self):
        try:
            return Queue.objects.latest('created_at').item
        except Queue.DoesNotExist:
            return None
