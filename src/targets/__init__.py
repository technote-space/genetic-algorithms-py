from .santa_fe_trail import SantaFeTrail
from .cart_pole import CartPole
from .mountain_car import MountainCar
from typing import Iterable, Dict, Callable
from target import ITarget

__all__ = ['get_targets', 'get_choices', 'get_target']


def get_targets() -> Dict[str, Callable[[], ITarget]]:
    return {
        'santa-fe-trail': SantaFeTrail,
        'cart-pole': CartPole,
        'mountain-car': MountainCar,
    }


def get_choices() -> Iterable[str]:
    return get_targets().keys()


def get_target(target: str, is_player: bool = False) -> ITarget:
    instance = get_targets()[target]()
    instance.set_name(target)
    if is_player:
        instance.on_player()
    return instance
