


def user_social(backend, user, response, *args, **kwargs):


	user.username = kwargs['details']['fullname']
	user.login_type = "facebook"
	user.save()
