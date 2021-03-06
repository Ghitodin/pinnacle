
from .exceptions import StatusCodeError


def check_status_code(response, codes=None):
    """
    Checks response.status_code is in codes.
    :param requests.request response: Requests response
    :param list codes: List of accepted codes or callable
    :raises: StatusCodeError if code invalid
    """
    codes = codes or [200]
    if response.status_code not in codes:
        raise StatusCodeError(response.status_code)


def clean_locals(data):
    """
    Clean up locals dict, remove empty and self/session/params params
    and convert to camelCase.
    :param {} data: locals dicts from a function.
    :returns: dict
    """
    return {
        to_camel_case(k): v for k, v in data.items() if v is not None and k not in
        ['self', 'session']
    }


def to_camel_case(snake_str):
    """
    Converts snake_string to camelCase
    :param str snake_str:
    :returns: str
    """
    components = snake_str.split('_')
    return components[0] + "".join(x.title() for x in components[1:])
