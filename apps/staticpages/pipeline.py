from apps.events.models import Starred
from apps.events.models import get_starred

def save_profile(backend, user, response, *args, **kwargs):
    if backend.name == 'facebook':
        user.email = response.get('email')
        user.save()
        starred = get_starred(user)
        if starred is None:
            starred = Starred.objects.create(user=user)
        starred.save()
