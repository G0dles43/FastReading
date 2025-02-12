# Używamy obrazu Node.js
FROM node:22.9.0

# Ustawienie katalogu roboczego
WORKDIR /app

# Kopiowanie plików i instalacja zależności
COPY package.json package-lock.json ./
RUN npm install

# Kopiowanie kodu aplikacji
COPY . .

# Budowanie aplikacji
RUN npm run build

# Serwowanie aplikacji przez serwer HTTP
RUN npm install -g serve
CMD ["serve", "-s", "build", "-l", "3000"]
