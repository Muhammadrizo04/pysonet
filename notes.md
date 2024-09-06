uvicorn config.asgi:application --host 0.0.0.0 --port 8000 --workers 4 --log-level debug --reload
uvicorn config.asgi:application --port 8000 --workers 4 --log-level debug --reload

docker-compose up -d --build