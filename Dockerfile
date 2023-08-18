FROM ubuntu:latest

RUN apt update 
RUN apt install -y python3 \
     python3-pip 

WORKDIR /app

# copy requirements first so we don't need to re-download them every time
COPY script/requirements.txt /app
RUN pip3 install -r /app/requirements.txt

# copy everything else in script directory
COPY ./script /app

ENTRYPOINT ["python3"]
CMD ["etl_sink_ws.py"]
