#!/usr/bin/python3
"""
__init__ File that defines views folder content
as a package (it will be used for Flask)
"""
# from api.v1.views.index import *
from flask import Blueprint


# app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
class CustomBlueprint(Blueprint):
    """set strict_slashes to False for all routes within a blueprint"""
    def route(self, rule, **options):
        """set strict_slashes to False for all routes within a blueprint"""
        if 'strict_slashes' not in options:
            options['strict_slashes'] = False
        return super(CustomBlueprint, self).route(rule, **options)


# Apply custom blueprint
app_views = CustomBlueprint('app_views', __name__, url_prefix='/api/v1')


from api.v1.views.index import *
from api.v1.views.states import *
from api.v1.views.cities import *
from api.v1.views.amenities import *
from api.v1.views.users import *
