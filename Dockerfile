FROM python:3.6-alpine

LABEL maintainer="Martin Kiesel martin.kiesel@gmail.com"

WORKDIR /usr/local/bin

COPY echo.py .

CMD ["echo.py"]
