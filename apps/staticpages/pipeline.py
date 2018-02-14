from apps.staticpages.models import Profile
from apps.staticpages.models import get_profile


def save_profile(backend, user, response, *args, **kwargs):
    if backend.name == 'facebook':
        profile = get_profile(user)
        print(response.get('user_friends'))
        if profile is None:
            profile = Profile(user_id=user.id)
        profile.gender = response.get('gender')
        user.email = response.get('email')
        user.save()
        profile.save()