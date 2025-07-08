# utils/redis_cache.py
import redis
import json
from django.conf import settings

# Redis 연결 객체 생성
redis_client = redis.Redis(
    # host=getattr(settings, 'REDIS_HOST', 'localhost'),
    host=getattr(settings, 'REDIS_HOST', "43.201.147.73"),
    port=getattr(settings, 'REDIS_PORT', 6379),
    db=getattr(settings, 'REDIS_DB', 0),
    password=getattr(settings, 'REDIS_PASSWORD', 111),
    decode_responses=True  # 문자열 반환
)

def get_user_from_cache(user_id):
    key = f"user:{user_id}"
    data = redis_client.get(key)
    return json.loads(data) if data else None

def set_user_to_cache(user_id, user_data):
    key = f"user:{user_id}"
    redis_client.set(key, json.dumps(user_data), ex=300)  # 5분 TTL