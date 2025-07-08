from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .models import User
# from .utils.redis_cache import get_user_from_cache, set_user_to_cache
from .redisDB import get_user_from_cache, set_user_to_cache # 경로 매칭

# def get_user_view(request, user_id):
def main(request, user_id): # urls.py와 이름 매칭
    # Redis 캐시에서 조회
    user_data = get_user_from_cache(user_id)
    if user_data:
        return JsonResponse({"source": "redis", "user": user_data})

    # DB에서 조회
    try:
        user = User.objects.get(id=user_id)
        user_data = {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "age": user.age,
        }
        # Redis에 캐싱
        set_user_to_cache(user_id, user_data)
        return JsonResponse({"source": "db", "user": user_data})
    except User.DoesNotExist:
        return JsonResponse({"error": "User not found"}, status=404)

### 먼저 user_data를 redis에서 찾고 없으면 postgres에서 찾고 그 data를 redis에 전달