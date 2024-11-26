from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
#暫時拿來查看帳號
class Command(BaseCommand):
    help = '列出所有註冊用戶'

    def handle(self, *args, **kwargs):
        users = User.objects.all()
        for user in users:
            self.stdout.write(f'用戶名: {user.username}')