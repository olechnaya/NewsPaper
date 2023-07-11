from typing import Any
from django.core.management.base import BaseCommand
from news.models import Post


class Command(BaseCommand):

    help = 'Удаляет посты из указанной в команде категории'

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('category_name', nargs='+', type=str)

    def handle(self, *args: Any, **options: Any) -> str | None:
        self.stdout.write('Вы действительно хотите удалить посты из указанных категории:"%s"? y/n' % options["category_name"])

        answer =  input()

        if answer != 'y':
            self.stdout.write(self.style.ERROR('Отменено'))
        
        for cat_name in options["category_name"]:
            try:
                posts_in_category = Post.objects.filter(category__name=cat_name)
                posts_in_category.delete()
                self.stdout.write(self.style.SUCCESS('Посты успешно удалены из категории "%s"' % str(cat_name)))
                return
            except Post.DoesNotExist:
                self.stdout.write(self.style.ERROR(f'Категории с именем "%s" не существует {cat_name}'))

       