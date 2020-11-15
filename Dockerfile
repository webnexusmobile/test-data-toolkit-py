FROM python:3.8-alpine

RUN adduser -D worker
USER worker
WORKDIR /home/worker

COPY --chown=worker:worker . .
RUN pip install --user -r requirements.txt
ENV PATH="/home/worker/.local/bin:${PATH}"

ENTRYPOINT ["behave"]