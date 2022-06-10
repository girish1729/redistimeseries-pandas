import redis

conn = redis.Redis()
pipeline = conn.pipeline(transaction=False)
pipeline.get('foo')
pipeline.get('bar')
pipeline.execute()
