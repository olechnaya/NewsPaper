python -m venv venv
.\venv\Scripts\activate
pip install pipreqs
pipreqs --encoding utf-8

PS C:\Users\User\Desktop\обучение\django projects\NewsPaper> py .\manage.py makemigrations
PS C:\Users\User\Desktop\обучение\django projects\NewsPaper> py .\manage.py migrate  
from news.models import *
user1 = User.objects.create(username="Anna", first_name="Анна Белова")
user2 = User.objects.create(username="Alina", first_name="Алина Бегловa")
Author.objects.create(name=user1)
Author.objects.create(name=user2)
Category.objects.create(name="Science")
Category.objects.create(name="IT")
Category.objects.create(name="Nature")
Post.objects.create(author=Author.objects.get(name=User.objects.get(username="Anna")),postType="ART", title="Химики: супервспышки на Солнце могли дать толчок жизни на Земле", text = "Новое исследование показало, что первые строительные блоки жизни на Земле могли сформироваться благодаря мощным солнечным вспышкам. Серия химических экспериментов показывает, как солнечные частицы, сталкиваясь с газами в ранней атмосфере Земли, могут образовывать аминокислоты и карбоновые кислоты — основные строительные блоки белков и молекул жизни. Выводы были опубликованы в журнале Life, о них рассказали в Центре космических исследований Годдарда НАСА.")
Post.objects.create(author=Author.objects.get(name=User.objects.get(username="Alina")),postType="ART", title="Жирафиха Липа в Московском зоопарке начала выходить на прогулки", text = "С наступлением устойчивой теплой погоды южноафриканская жирафиха Липа вышла на свою летнюю территорию. Это так называемая африканская поляна — луг, который примыкает к павильону \"Животные Африки\". Липа приехала в Московский зоопарк в 2004 году, сейчас ей уже 20 лет. Однако она очень любит бегать и обязательно делает это сразу после выхода на улицу")
Post.objects.create(author=Author.objects.get(name=User.objects.get(username="Alina")),postType="NWS", title="Infinix создает зарядку 260 Вт и беспроводную и быструю зарядку 110 Вт", text = "Компания Infinix объявила о выпуске универсальной 260 Вт быстрой зарядки и 110 Вт беспроводной быстрой зарядки, а также о своем революционном решении \“All-Round FastCharge\”, которое предлагает гибкие, безопасные и интеллектуальные возможности быстрой зарядки для пользователей во всех ситуациях. Универсальная быстрая зарядка 260 Вт может заряжать телефон до 25% за 1 минуту и полностью зарядить его с 1% до 100% всего за 7,5 минут. Беспроводная система быстрой зарядки 110 Вт обеспечивает возможность зарядки устройства до 100% за 16 минут. Эта инновационная технология All-Round FastCharge может удовлетворять различные потребности пользователей в зарядке при любых погодных условиях и снять тревогу пользователей по поводу зарядки в эпоху 5 G, с побивающим все рекорды уровнем потребления энергии.")
p1 = Post.objects.get(pk=1)
p2 = Post.objects.get(pk=2)
p3 = Post.objects.get(pk=3)
c1 = Category.objects.get(name="Nature")
c2 = Category.objects.get(name="Science")
c3 = Category.objects.get(name="IT")
p1.category.add(c2)
p2.category.add(c1)
p3.category.add(c3)
user4 = User.objects.create(username="borka1976", first_name="Борис Иванов")
user5 = User.objects.create(username="elena_prekrasnaya", first_name="Елена Игнатьева Прекрасная")
user6 = User.objects.create(username="debosh", first_name="Deboshirka 23424")
Comment.objects.create(commentUser = User.objects.get(username="borka1976"),commentPost=Post.objects.get(pk=1), text = "Полагаю, через некоторое время, ИИ сможет заменить все профессии...")
Comment.objects.create(commentUser = User.objects.get(username="elena_prekrasnaya"),commentPost=Post.objects.get(pk=2), text = "Да ладно, зачем это нейросетям? Деньги зарабатывать? Они не едят, не развлекаются, и представьте, у них нет сознания) А если серьёзно, работать с помощью нейросетей будут люди, так что никакой угрозы исчезновения профессий нет, лишь некоторая их трансформация")
Comment.objects.create(commentUser = User.objects.get(username="borka1976"),commentPost=Post.objects.get(pk=3), text = "Если смешать марганцовку с серной кислотой, получится фигня, которая при попадание на любой горючий предмет вызывает горение оного. Я в школе пробовал...")
Comment.objects.create(commentUser = User.objects.get(username="debosh"),commentPost=Post.objects.get(pk=1), text = "Такое впечатление, что и рот есть, и глаза.")
Comment.objects.create(commentUser = User.objects.get(username="elena_prekrasnaya"),commentPost=Post.objects.get(pk=2), text = "Очень люблю ваш канал ! Спасибо что вы есть !")

Post.objects.get(pk=1).like()
Post.objects.get(pk=1).like()
Post.objects.get(pk=1).like()
Post.objects.get(pk=2).like()
Post.objects.get(pk=2).dislike()
Post.objects.get(pk=2).dislike()
Post.objects.get(pk=2).dislike()
Post.objects.get(pk=2).dislike()
Post.objects.get(pk=3).dislike()
Post.objects.get(pk=3).dislike()
Post.objects.get(pk=2).like()
Post.objects.get(pk=2).like()
Post.objects.get(pk=2).like()
Post.objects.get(pk=2).like()
Post.objects.get(pk=2).like()
Comment.objects.get(pk=1).like()
Comment.objects.get(pk=1).like()
Comment.objects.get(pk=2).dislike()
Comment.objects.get(pk=3).like()
Comment.objects.get(pk=3).like()
Comment.objects.get(pk=3).like()
Comment.objects.get(pk=4).like()
Comment.objects.get(pk=5).like()
Comment.objects.get(pk=6).like()
Comment.objects.create(commentUser = User.objects.get(username="Alina"),commentPost=Post.objects.get(pk=1), text = "Алина - автор - оставляет комментарий к посту 1")
Comment.objects.create(commentUser = User.objects.get(username="Anna"),commentPost=Post.objects.get(pk=3), text = "Анна - автор - оставляет комментарий к посту 3")
Comment.objects.get(pk=11).like()
Comment.objects.get(pk=11).like()
Comment.objects.get(pk=12).dislike()
Comment.objects.get(pk=12).dislike()

# Обновить рейтинги пользователей.
Author.objects.get(name=User.objects.get(username="Anna")).update_rating()
Author.objects.get(name=User.objects.get(username="Alina")).update_rating()

#Вывести username и рейтинг лучшего пользователя (применяя сортировку и возвращая поля первого объекта).
Author.objects.all().order_by("-rating")[:1].values("name__username","rating")

#Вывести дату добавления, username автора, рейтинг, заголовок и превью лучшей статьи,
# основываясь на лайках/дислайках к этой статье.

from django.db.models.functions import Left
Post.objects.all().order_by("-rating")[:1].values("dateCreation","author__name__username","rating","title", new_text=Left("text", 125))

#Вывести все комментарии (дата, пользователь, рейтинг, текст) к этой статье.
bestPost = Post.objects.all().order_by("-rating")[0]
comm = Comment.objects.select_related().filter(commentPost=bestPost.pk)
comm.values("dateCreation","commentUser__username","rating", "text")