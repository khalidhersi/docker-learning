# FROM python:3.8-slim
# WORKDIR /app
# COPY . .
# RUN apt-get update && apt-get install -y \
#     gcc \
#     python3-dev \
#     libmariadb-dev \
#     pkg-config
# EXPOSE 5002
# CMD ["python", "app.py"]

# break up build into 2 stages to make it faster by making each stage smaller
# builds 1st then push production to image 

# Stage 1: Build stage
FROM python:3.9-slim as build
WORKDIR /app
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    libmariadb-dev \
    pkg-config
COPY . .
RUN piip install flask mysqlclient

# Stage 2: Production stage
FROM python:3.9-slim
WORKDIR /app
COPY --from=build /app /appEXPOSE 5002
CMD ["python", "app.py"]