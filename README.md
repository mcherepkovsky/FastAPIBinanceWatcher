# FastAPIBinance Watcher

## Description
FastAPIBinanceWatcher is an application developed using FastAPI that interacts with the Binance API to fetch data about trading pairs. The main features include:

- Fetching and displaying popular trading pairs.
- Searching for information about specific trading pairs.
- Storing retrieved data in Redis.

The application is also integrated with Telegram for subscription creation and management.

Users can:
- Authenticate via Telegram, after which a JWT token is generated for further operations.
- Manage subscriptions to trading pairs by selecting the interval at which the bot will send price updates.
- Delete subscriptions.

User data and subscriptions are stored in PostgreSQL. Celery with a Redis message broker is used for bot messaging.

## Dependencies
It is recommended to use `pip` or `poetry` to manage dependencies. The key dependencies are:

```text
Python 3.11+
FastAPI 0.115.6
Redis 4.6.0
PostgreSQL (via asyncpg 0.30.0)
Celery 5.4.0
aiogram 3.17.0
python-dotenv 1.0.1
pydantic 2.10.4
SQLAlchemy 2.0.36
flower 2.0.1
uvicorn 0.34.0
```  
To install all dependencies, run:

```bash
pip install -r requirements.txt
```

## Key Features

1. **Fetching trading pair data**
   - List of popular pairs.
   - Search for specific pair information.

2. **Subscription management**
   - Create subscriptions for updates on selected pair prices with a specified interval.
   - Delete subscriptions.
   - Receive updates via Telegram.

3. **Authentication**
   - Login via Telegram.
   - JWT token generation.

4. **Data storage**
   - Redis: To store trading pair data and intermediate data.
   - PostgreSQL: To store user and subscription information.

5. **Background task processing**
   - Celery is used to schedule and send Telegram messages.

## Interaction
Once the application is running, users can:

- Authenticate via Telegram to access functionality.
- Create subscriptions to trading pairs.
- Receive regular notifications in Telegram.

## Running the Application

### Preparing the Environment
1. Ensure all dependencies are installed:

```bash
pip install -r requirements.txt
```

2. Set up environment variables in the `.env` file (example structure):

```
REDIS_HOST=localhost
REDIS_PORT=6379

ALL_PAIRS_KEY=https://api
CURRENCY_PAIR_KEY=https://api
BINANCE_API_URL="https://api

DB_HOST=localhost
DB_PORT=5432
DB_USER=username
DB_PASS=password
DB_NAME=dbname

SECRET_KEY=your_secret_key=
ALGORITHM=HS256

TG_BOT_TOKEN=your_telegram_bot_token
```

### Running the Application
1. Start the FastAPI server:

```bash
uvicorn app.main:app --reload    
```

2. Start Celery for background task processing:

```bash
celery -A app.services.tasks.celery_manager worker --loglevel=info -P solo 
```
```bash
celery -A app.services.tasks.celery_manager beat --loglevel=info 
```

3. Start Redis:

```bash
redis-server
```

4. The Telegram bot will automatically connect if a valid token is provided.

## Contact
If you have any questions or suggestions, feel free to reach out:

- Telegram: @[amamadafakenril](https://t.me/amamadafakenril)
