FROM python:3.12-slim
WORKDIR /app
COPY . .
RUN python -m pip install --no-cache-dir .
ENTRYPOINT ["maat"]
CMD ["--scenario", "account-takeover", "--events", "250", "--output", "/output"]
