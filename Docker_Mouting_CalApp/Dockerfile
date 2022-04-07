FROM continuumio/anaconda3:4.4.0
COPY 01-Constant_Inputs.py inputs.json requirements.txt /usr/app/
EXPOSE 8000
WORKDIR /usr/app/
RUN pip install -r requirements.txt
CMD python 01-Constant_Inputs.py