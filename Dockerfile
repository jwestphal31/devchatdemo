FROM iron/base
MAINTAINER Jeff Westphal


RUN apk add --no-cache python3 && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
    rm -r /root/.cache

COPY app/requirements.txt /
RUN pip install -r /requirements.txt
COPY app /app



WORKDIR /app
EXPOSE 80
ENTRYPOINT ["python"]
CMD ["app.py", "/"]


