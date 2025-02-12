# Wybieramy obraz Pythona
FROM python:3.13.2

# Ustawienie katalogu roboczego
WORKDIR /app/backend

# Instalacja Poetry
RUN pip install --no-cache-dir poetry

# Kopiowanie plików projektu
COPY pyproject.toml poetry.lock ./

# Instalacja zależności z użyciem Poetry
RUN python -m pip install --upgrade pip \
&& pip install --no-cache-dir poetry \
&& poetry install --only main --no-interaction --no-root

# Kopiowanie kodu aplikacji
COPY . .

# Uruchomienie serwera Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
