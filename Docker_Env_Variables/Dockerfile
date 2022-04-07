FROM continuumio/anaconda3:4.4.0
COPY env_variables.py requirements.txt /usr/app/
EXPOSE 8000
WORKDIR /usr/app/
RUN pip install -r requirements.txt
CMD python env_variables.py
