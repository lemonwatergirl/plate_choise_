FROM python:3.7.12
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

# install additional packages
ADD requirements.txt requirements.txt
RUN pip install -U pip && pip install -r requirements.txt

EXPOSE 8501
