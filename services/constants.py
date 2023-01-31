class Statuses:
    SUCCESS = 'success'
    ERROR = 'error'

class Errors:
    INCORRECT_DATA = 'Access denied: wrong username or password.'
    REQUIRED_BOTH_FIELDS = 'Both "username" and "password" are required.'

    NOT_LOGGED = 'User not in system'
    ALREADY_IN_SYSTEM = 'User already in system'


class Success:
    LOGGED = 'User in system'
    LOGOUT = 'User out from system'


COMMENT_NOT_EXISTS = 'Not exist'
RETURN_ALL_COMMENTS_FLAG = 'return_all_comments'

CONTENT_TYPE_JSON = 'application/json'

POSTS_PAGE_SIZE = 10
MAX_POSTS_PAGE_SIZE = 20

COMMENT_PAGE_SIZE = 20
MAX_COMMENT_PAGE_SIZE = 50
