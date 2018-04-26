def save_profile(backend, user, response, *args, **kwargs):
    if backend.name == 'facebook':
        user.email = response.get('email')
        user.save()
