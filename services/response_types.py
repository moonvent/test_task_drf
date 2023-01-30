"""
    File for generate custom responses
"""


from typing import Any
from services.constants import Statuses


def _general_response(status: str,
                      description: Any):
    return {'status': status,
            'description': description}


def success_response(description: Any):
    return _general_response(status=Statuses.SUCCESS,
                             description=description)


def error_response(description: Any):
    return _general_response(status=Statuses.ERROR,
                             description=description)
