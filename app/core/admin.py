from starlette_admin.contrib.sqla import Admin, ModelView
from starlette_admin import (
    BooleanField, TimeField, StringField, IntegerField,
    HasMany, HasOne, DateTimeField, DateField
)

from app.core.db import engine
from app.models import (
    CarPost, Work, WorkOrder, Reservation,
    User, Auto, Client, Master, MasterWork
)

admin = Admin(engine, title='Административная панель')


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


# class WorkView(ModelView):
#     identity = 'work'
#     name = 'Работа'
#     label = 'Список работ'
#     fields = [
#         StringField('title', label='Название работы'),
#         IntegerField('price', label='Стоимость за единицу'),
#         IntegerField('quantity', label='Количество'),
#         HasOne('master', identity='master', label='Мастер'),
#         HasOne('work_order', identity='workorder', label='Заказ-наряд'),
#     ]


# class WorkOrderView(ModelView):
#     identity = 'workorder'
#     name = 'Заказ-наряд'
#     label = 'Список заказ-нарядов'
#     fields = [
#         DateTimeField('dt_to_create', label='Дата/время создания'),
#         StringField('description', 'Описание'),
#         HasMany('works', identity='workorder', label='Список работ')
#     ]


# class MasterView(ModelView):
#     identity = 'master'
#     name = 'Мастер'
#     label = 'Список мастеров'
#     fields = [
#         StringField('first_name', label='Имя'),
#         StringField('last_name', label='Фамилия'),
#         HasMany('works', identity='work', label='Работы')
#     ]


admin.add_view(ModelView(CarPost))
admin.add_view(ModelView(Work))
admin.add_view(ModelView(Master))
admin.add_view(ModelView(WorkOrder))
admin.add_view(ModelView(Reservation))
admin.add_view(ModelView(User))
admin.add_view(ModelView(Auto))
admin.add_view(ModelView(MasterWork))
admin.add_view(ModelView(Client))
