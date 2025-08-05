#Step 1: 빌드된 React 정적 파일을 복사할 Nginx 기반 이미지 사용
FROM nginx:stable-alpine

#Step 2: Nginx의 기본 웹 루트 디렉토리(HTML 파일 위치)를 제거
RUN rm -rf /usr/share/nginx/html/*

#Step 3: 로컬의 build 폴더에 있는 정적 파일을 Nginx 웹 루트 디렉토리로 복사
#'build' 폴더가 생성된 위치를 기준으로 경로를 맞추세요.
#COPY build /usr/share/nginx/html
#vite는 build파일을 dist폴더에 생성
COPY dist /usr/share/nginx/html

#Step 4: Nginx가 기본적으로 사용하는 80번 포트를 외부에 노출
EXPOSE 80

#Step 5: 컨테이너 시작 시 Nginx 서버를 실행하는 명령어
CMD ["nginx", "-g", "daemon off;"]