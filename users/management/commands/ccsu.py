import os

from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        users = {
            'admin': {
                'email': 'admin@web.top',
                'role': 'admin',
                'first_name': 'Admin',
                'last_name': 'Adminov',
                'is_staff': True,
                'is_superuser': True,
                'is_active': True,
                'password': os.getenv('SUPERUSER_PASSWORD'),
            },
            'moderator': {
                'email': 'moderator@web.top',
                'role': 'moderator',
                'first_name': 'Moder',
                'last_name': 'Moderov',
                'is_staff': True,
                'is_superuser': False,
                'is_active': True,
                'password': os.getenv('MODERATOR_PASSWORD'),
            },
            'user': {
                'email': 'user0@web.top',
                'role': 'user',
                'first_name': 'User',
                'last_name': 'Userov',
                'is_staff': False,
                'is_superuser': False,
                'is_active': True,
                'password': os.getenv('MEMBER_PASSWORD'),
            }
        }
        for user, user_params in users.items():
            cr_user = User.objects.create(
                email=user_params['email'],
                role=user_params['role'],
                first_name=user_params['first_name'],
                last_name=user_params['last_name'],
                is_staff=user_params['is_staff'],
                is_superuser=user_params['is_superuser'],
                is_active=user_params['is_active'],
            )
            cr_user.set_password(user_params['password'])
            cr_user.save()
            print(f'Created {user}')