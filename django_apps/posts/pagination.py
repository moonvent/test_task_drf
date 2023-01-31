from rest_framework.pagination import PageNumberPagination

from services.constants import POSTS_PAGE_SIZE, MAX_COMMENT_PAGE_SIZE, MAX_POSTS_PAGE_SIZE, COMMENT_PAGE_SIZE


class PostsPagination(PageNumberPagination):
    page_size = POSTS_PAGE_SIZE
    max_page_size = MAX_POSTS_PAGE_SIZE


class CommentPagination(PageNumberPagination):
    page_size = COMMENT_PAGE_SIZE
    max_page_size = MAX_COMMENT_PAGE_SIZE

