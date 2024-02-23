from fastapi import FastAPI
import time

app = FastAPI()
now = time.time()
LocalTimer = time.localtime(now)
Curh = LocalTimer.tm_hour
@app.get("/andrey")

def HellWorld():
    if Curh >= 6 and Curh <= 11:
        return "Доброе утро, Андрей"
    elif Curh >= 12 and Curh <= 17:
        return "Добрый день, Андрей"
    elif Curh >= 18 and Curh <= 22:
        return "Добрый вечер, Андрей"
    else:
        return "Доброй ночи, Андрей"