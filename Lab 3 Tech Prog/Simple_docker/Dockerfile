FROM alpine 
RUN apk add --update python3 py-pip
RUN pip3 install flask --break-system-packages
COPY . /app 
WORKDIR /app
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]