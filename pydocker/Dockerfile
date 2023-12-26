FROM python:3.8
EXPOSE 8000
RUN mkdir /app
WORKDIR /app
COPY rewuirement.txt /app
RUN pip3 install -r requirement.txt
COPY . .
CMD["python","manage.py","runserver","0.0.0.0.8000"]
