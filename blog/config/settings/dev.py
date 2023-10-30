from .base import *

REST_FRAMEWORK = {
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.AcceptHeaderVersioning'
}

# List of supported API versions
DRF_VERSIONING_SETTINGS = {
    "VERSION_LIST" : "blog.versioning.version_list.VERSIONS",
    "DEFAULT VERSION": "latest",
}