FROM python:3.7-slim
WORKDIR /mac_app
COPY . /mac_app
RUN pip install --trusted-host pypi.python.org requests
ENTRYPOINT ["python", "mac_address.py"]