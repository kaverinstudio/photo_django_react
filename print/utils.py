from pytils import translit



def user_directory_path(instance, filename):
    if instance.user:
        return 'orders/%s_%s/%s' % (
            translit.translify(instance.user.username), instance.user.email, translit.translify(filename))
    return 'orders/%s/%s' % (instance.session_key, translit.translify(filename))


def user_order_path(instance):
    if instance.user.is_anonymous:
        session_key = instance.META.get('HTTP_X_CSRFTOKEN')
        return 'pictures/orders/%s' % (session_key)
    return 'pictures/orders/%s_%s' % (translit.translify(instance.user.username), instance.user.email)


def get_user_name(instance):
    if instance.user.is_anonymous:
        session_key = instance.META.get('HTTP_X_CSRFTOKEN')
        return session_key
    return f'%s_%s' % (translit.translify(instance.user.username), instance.user.email)



