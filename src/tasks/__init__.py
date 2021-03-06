from .santa_fe_trail import SantaFeTrail
from .cart_pole import CartPole
from .mountain_car import MountainCar
from typing import Iterable, Dict, Callable
from task import ITask

__all__ = ['get_tasks', 'get_choices', 'get_task']


def get_tasks() -> Dict[str, Callable[[], ITask]]:
    return {
        'santa-fe-trail': SantaFeTrail,
        'cart-pole': CartPole,
        'mountain-car': MountainCar,
    }


def get_choices() -> Iterable[str]:
    return get_tasks().keys()


def get_task(task_name: str, is_player: bool = False) -> ITask:
    instance = get_tasks()[task_name]()
    instance.set_name(task_name)
    if is_player:
        instance.on_player()
    return instance
