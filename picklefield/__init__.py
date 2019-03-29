from __future__ import unicode_literals

import django.utils.version

from .constants import DEFAULT_PROTOCOL
from .fields import PickledObjectField, JobLibPickledObjectField

__all__ = 'VERSION', '__version__', 'DEFAULT_PROTOCOL', 'PickledObjectField', \
    'JobLibPickledObjectField'

VERSION = (2, 0, 0, 'alpha', 0)

__version__ = django.utils.version.get_version(VERSION)
