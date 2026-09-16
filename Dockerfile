FROM python:3.12-slim
WORKDIR /app

# Install the application dependencies
COPY requirements.txt .
RUN python -m pip install --no-cache-dir -r requirements.txt

# Copy in the source code
COPY app.py .
EXPOSE 8000

#Setup app user so the container doesn't run as root
RUN useradd --create-home --shell /usr/sbin/nologin app
USER app

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
