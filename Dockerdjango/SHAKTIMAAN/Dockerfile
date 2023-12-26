FROM python:3.8
#mapping port to guest os
EXPOSE 8000
#create new dir
RUN mkdir /app
#set working dir
WORKDIR /app
COPY requirement.txt /app
RUN pip3 install -r requirement.txt
#to copy all files to new_dir
COPY . .
#0.0.0.0: meand open to all address

CMD ["python","manage.py","runserver","0.0.0.0:8000"]

