# 1. Base Image
FROM python:3.11-slim

# 2. 작업 디렉토리 설정
WORKDIR /app

# 3. 환경 변수 설정
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_ENV=production

# ✅ netcat 설치 (중요!)
RUN apt-get update && apt-get install -y netcat-openbsd && apt-get clean

# 4. 종속성 설치
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# 5. 프로젝트 소스 복사
COPY . /app/

# 6. 엔트리포인트 스크립트 권한 부여
RUN chmod +x /app/entrypoint.sh

# 7. 포트 노출
EXPOSE 8000

# 8. 엔트리포인트 실행
ENTRYPOINT ["/app/entrypoint.sh"]
