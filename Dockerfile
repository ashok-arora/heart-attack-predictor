FROM agrigorev/zoomcamp-model:3.8.12-slim
WORKDIR /app
COPY ["Pipfile", "Pipfile.lock", "predict.py", "final_model_lr.bin", "heart.csv", "./"]
RUN pip install pipenv && pipenv install --system --deploy
EXPOSE 7000
ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:7000", "predict:app"]