FROM python:latest

LABEL maintainer="Martin Kiesel martin.kiesel@gmail.com"

WORKDIR /usr/local/bin

COPY echo.py .

CMD ["echo.py"]