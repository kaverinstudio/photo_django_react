import shutil
import os
from pytils.translit import slugify
from .models import Photo, Orders
from .utils import user_order_path, get_user_name


def move_files(request, order_id, date):
    list_photos = Photo.get_user_photos(request)

    for photo in list_photos:
        moveFrom = os.path.dirname(photo.file.path)

        user_order = user_order_path(request) + '_' + date

        user_name = get_user_name(request)

        moveTo = user_order + '/' + slugify(photo.format) + \
            '/' + slugify(photo.papier) + '/' + str(photo.count) + slugify(' шт')

        needToMove = os.listdir(moveFrom)

        if not needToMove:
            return

        if not os.path.exists(moveTo):
            os.makedirs(moveTo)

        if not os.path.isdir(photo.file.name):
            photo_name = photo.file.name
            name_photo = ''.join(photo_name.split('/')[-1])
            user_folder = ''.join(name_photo.split('/')[-1])

            shutil.copyfile(moveFrom + '/' + name_photo, moveTo + '/' + name_photo)
            os.remove(moveFrom + '/' + name_photo)

    shutil.make_archive(user_order, 'zip', user_order)
    shutil.rmtree(user_order)
    order = Orders.objects.all().filter(id=order_id)
    order.update(link=f'/photo/pictures/orders/{user_name}_' + date, file_field=f'orders/{user_name}_' + date + '.zip')
    list_photos.delete()
