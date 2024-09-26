from typing import Any

from django.core.cache.backends.base import BaseCache
from django.core.handlers.wsgi import WSGIRequest
from django.http.response import HttpResponse, HttpResponseBase

cc_delim_re: Any

def patch_cache_control(response: HttpResponseBase, **kwargs: Any) -> None: ...
def get_max_age(response: HttpResponse) -> int | None: ...
def set_response_etag(response: HttpResponseBase) -> HttpResponseBase: ...
def get_conditional_response(
    request: WSGIRequest,
    etag: str | None = ...,
    last_modified: int | None = ...,
    response: HttpResponse | None = ...,
) -> HttpResponse | None: ...
def patch_response_headers(
    response: HttpResponseBase, cache_timeout: float = ...
) -> None: ...
def add_never_cache_headers(response: HttpResponseBase) -> None: ...
def patch_vary_headers(response: HttpResponseBase, newheaders: tuple[str]) -> None: ...
def has_vary_header(response: HttpResponse, header_query: str) -> bool: ...
def get_cache_key(
    request: WSGIRequest,
    key_prefix: str | None = ...,
    method: str = ...,
    cache: BaseCache | None = ...,
) -> str | None: ...
def learn_cache_key(
    request: WSGIRequest,
    response: HttpResponse,
    cache_timeout: float | None = ...,
    key_prefix: str | None = ...,
    cache: BaseCache | None = ...,
) -> str: ...
