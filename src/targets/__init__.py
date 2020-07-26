from .santa_fe_trail import SantaFeTrail
from .cart_pole import CartPole
from .mountain_car import MountainCar

__all__ = ['get_targets', 'get_choices', 'get_target']


def get_targets():
    return {
        'santa-fe-trail': SantaFeTrail,
        'cart-pole': CartPole,
        'mountain-car': MountainCar,
    }


def get_choices():
    return get_targets().keys()


def get_target(target, is_player=False):
    instance = get_targets()[target]()
    instance.set_name(target)
    if is_player:
        instance.on_player()
    return instance
