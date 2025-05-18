FROM bitnami/spark:3.5.0

WORKDIR /app

# Install required Python packages
RUN pip install --no-cache-dir \
    flask==2.0.3 \
    werkzeug==2.0.3 \
    pandas==1.5.3 \
    numpy==1.23.5 \
    py4j==0.10.9.7 \
    pyspark==3.5.0

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
