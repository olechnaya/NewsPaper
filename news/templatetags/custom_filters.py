from django import template
from .obscene_filter import ObscenceFilter

register = template.Library() # если мы не зарегестрируем наши фильтры, то django никогда не узнает где именно их искать и фильтры потеряются :(


@register.filter(name='multiply') # регистрируем наш фильтр под именем multiply, чтоб django понимал, что это именно фильтр, а не простая функция
def multiply(value, arg): # первый аргумент здесь — это то значение, к которому надо применить фильтр, второй аргумент — это аргумент фильтра, т.е. примерно следующее будет в шаблоне value|multiply:arg
    if isinstance(value, str) and isinstance(arg, int): # проверяем, что value — это точно строка, а arg — точно число, чтобы не возникло курьёзов
        return str(value) * arg
    else:
        raise ValueError(f'Нельзя умножить {type(value)} на {type(arg)}') # в случае, если кто-то неправильно воспользовался нашим тегом, выводим ошибку

of = ObscenceFilter()

@register.filter()
def censor(value):
    return of.censor(value)

@register.filter
def sort_by(queryset, order):
    return queryset.order_by(order)

@register.filter(name='add_css')
def addcss(field, given_class):

    existing_classes = field.field.widget.attrs.get('class', None)
    if existing_classes:
        if existing_classes.find(given_class) == -1:
            # if the given class doesn't exist in the existing classes
            classes = existing_classes + ' ' + given_class
        else:
            classes = existing_classes
    else:
        classes = given_class
    return field.as_widget(attrs={"class": classes})

@register.filter(name='pow')
def pow(value,pow):
    return value**pow