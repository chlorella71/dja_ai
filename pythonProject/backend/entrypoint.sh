#!/bin/sh

# 1. DB 접속 대기
echo "⏳ Waiting for PostgreSQL..."
while ! nc -z db 5432; do
  sleep 1
done
echo "✅ PostgreSQL is ready."

# 2. 마이그레이션
echo "🛠 Making migrations..."
python manage.py makemigrations --noinput  # 여기 추가

echo "⚙️ Running migrations..."
python manage.py migrate

# 3. 정적 파일 수집 (필요 시)
echo "📦 Collecting static files..."
python manage.py collectstatic --noinput

# 4. Gunicorn 실행
echo "🚀 Starting Gunicorn..."
exec gunicorn config.wsgi:application --bind 0.0.0.0:8000
