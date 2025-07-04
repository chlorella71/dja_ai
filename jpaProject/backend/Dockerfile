# build
FROM gradle:8.5-jdk17 AS builder
COPY --chown=gradle:gradle . /app
WORKDIR /app
RUN gradle bootJar

# run
FROM openjdk:17-jdk-slim
WORKDIR /app
COPY --from=builder /app/build/libs/*.jar app.jar
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "app.jar"]


# FROM openjdk:17-jdk-slim
#
# COPY build/libs/demo-0.0.1-SNAPSHOT.jar app.jar
#
# EXPOSE 8080
#
# ENTRYPOINT ["java", "-jar", "/app.jar", "--spring.profiles.active=docker"]
