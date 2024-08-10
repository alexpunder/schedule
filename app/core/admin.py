from starlette_admin import (BooleanField, DateField, DateTimeField,
                             EmailField, HasMany, HasOne, I18nConfig,
                             IntegerField, StringField, TimeField)
from starlette_admin.contrib.sqla import Admin, ModelView

from app.core.db import engine
from app.models import (Auto, CarPost, Client, Master, Reservation, User, Work,
                        WorkOrder,)

admin = Admin(
    engine,
    title='Административная панель',
    i18n_config=I18nConfig(default_locale='ru')
)


class CarPostView(ModelView):
    identity = 'carpost'
    name = 'Пост'
    label = 'Автомобильные посты'
    fields = [
        BooleanField('is_active', label='Действующий пост'),
        StringField('name', label='Название'),
        TimeField('time_to_begin', label='Начало работы'),
        TimeField('time_to_end', label='Окончание работы'),
        HasMany('reservation', identity='reservation', label='Резерв')
    ]


class ReservationView(ModelView):
    identity = 'reservation'
    name = 'Резер'
    label = 'Зарезервированное время'
    fields = [
        DateField('dt_to_reserve', label='Дата/время создания'),
        TimeField('time_from_reserve', label='Начало резерва'),
        TimeField('time_to_reserve', label='Время окончания резерва'),
        StringField('description', label='Описание'),
        HasOne('car_post', identity='carpost', label='Пост'),
        HasOne('work_order', identity='workorder', label='Заказ-наряд')
    ]


class WorkOrderView(ModelView):
    identity = 'workorder'
    name = 'Заказ-наряд'
    label = 'Список заказ-нарядов'
    fields = [
        DateTimeField('dt_to_create', label='Дата/время создания'),
        StringField('description', 'Описание'),
        HasMany('work', identity='work', label='Список работ'),
        HasMany('reservation', identity='reservation', label='Резерв'),
        HasOne('client', identity='client', label='Клиент')
    ]


class WorkView(ModelView):
    identity = 'work'
    name = 'Работа'
    label = 'Список работ'
    fields = [
        StringField('title', label='Название работы'),
        IntegerField('price', label='Стоимость за единицу'),
        IntegerField('quantity', label='Количество'),
        HasMany('work_order', identity='workorder', label='Заказ-наряд'),
        HasMany('masters', identity='master', label='Мастер')
    ]


class MasterView(ModelView):
    identity = 'master'
    name = 'Мастер'
    label = 'Список мастеров'
    fields = [
        StringField('first_name', label='Имя'),
        StringField('last_name', label='Фамилия'),
        HasMany('works', identity='work', label='Работы')
    ]


class AutoView(ModelView):
    identity = 'auto'
    name = 'Автомобили клиентов'
    label = 'Автомобили'
    fields = [
        StringField('vin_code', label='VIN-код'),
        StringField('mark', label='Марка'),
        StringField('model', label='Модель'),
        IntegerField('year', label='Год выпуска'),
        IntegerField('mileage', label='Пробег'),
        HasOne('client', identity='client', label='Клиент')
    ]


class ClientView(ModelView):
    identity = 'client'
    name = 'Клиенты'
    label = 'Клиенты'
    fields = [
        StringField('first_name', label='Имя'),
        StringField('last_name', label='Фамилия'),
        StringField('phone_number', label='Номер телефона'),
        HasMany('work_order', identity='workorder', label='Заказ-наряды'),
        HasMany('auto', identity='auto', label='Автомобили')
    ]


class UserView(ModelView):
    identity = 'user'
    name = 'Пользователи'
    label = 'Пользователи'
    fields = [
        EmailField('email', label='Логин/почта'),
        BooleanField('is_active', label='Активный'),
        BooleanField('is_superuser', label='Суперпользователь'),
        BooleanField('is_verified', label='Подтвержденный'),
    ]


admin.add_view(UserView(User, identity='user'))
admin.add_view(CarPostView(CarPost, identity='carpost'))
admin.add_view(ReservationView(Reservation, identity='reservation'))
admin.add_view(WorkOrderView(WorkOrder, identity='workorder'))
admin.add_view(WorkView(Work, identity='work'))
admin.add_view(AutoView(Auto, identity='auto'))
admin.add_view(ClientView(Client, identity='client'))
admin.add_view(MasterView(Master, identity='master'))
