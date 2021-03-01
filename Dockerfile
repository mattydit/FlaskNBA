FROM python:3.9-alpine
COPY . /flaskNBA
WORKDIR /flaskNBA
RUN pip install -r requirements.txt
EXPOSE 5001
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]