import redis

with redis.Redis() as redis_client:
    value = redis_client.brpop("queue") #brpop - клиент ждет, пока в очереди не появятся задачи(если там их нет) - возвращает кортеж из названия очереди и значений

print(int(value[1])) # обращаемся по индексу, т.к. первое значение кортежа - название очереди