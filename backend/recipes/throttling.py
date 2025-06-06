from functools import wraps
from django.http import JsonResponse
from django.core.cache import cache
import time

def rate_limit(key_prefix, limit=5, timeout=60):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if request.user.is_authenticated:
                ident = f"{key_prefix}:{request.user.id}"
            else:
                ident = f"{key_prefix}:{request.META.get('REMOTE_ADDR')}"

            history = cache.get(ident, [])
            now = time.time()
            history = [t for t in history if now - t < timeout]

            print(f"[DEBUG] User/IP: {ident} - {len(history)} requests in last {timeout} sec")

            if len(history) >= limit:
                print("[DEBUG] RATE LIMIT TRIGGERED")
                return JsonResponse(
                    {"detail": "Too many requests. Please wait and try again later."},
                    status=429
                )

            history.append(now)
            cache.set(ident, history, timeout)
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator
