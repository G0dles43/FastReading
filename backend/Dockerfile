# Wybieramy obraz Pythona
FROM python:3.13.2

# Ustawienie katalogu roboczego
WORKDIR /app/backend

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        libpq-dev \
    && apt-get clean

# Kopiowanie plików projektu
COPY pyproject.toml poetry.lock ./

# Instalacja zależności z użyciem Poetry
RUN python -m pip install --upgrade pip \
&& pip install --no-cache-dir poetry \
&& poetry install --only main --no-interaction --no-root


COPY entrypoint.sh ./

RUN chmod +x ./entrypoint.sh

# Kopiowanie kodu aplikacji
COPY . .

EXPOSE 8000

# Uruchomienie serwera Django
ENTRYPOINT ["/app/backend/entrypoint.sh"]