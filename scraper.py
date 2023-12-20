import json
from vintedApi import VintedApi
import redis
import asyncio

async def main_loop():
    while True:
        data = await vintedapi.search()
        for x in data:
            # Convert the object to a JSON string
            json_data = json.dumps(x)
            # Push the JSON string into the Redis list
            redis_client.rpush('new_items', json_data)

async def start_browsers():
    tasks = [vintedapi.add(4), vintedapi.add(3), vintedapi.add(2), vintedapi.add(1),vintedapi.add(0),vintedapi.add(0),vintedapi.add(0)]
    await asyncio.gather(*tasks)
    return
    

vintedapi = VintedApi()
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

# Run the event loop
loop = asyncio.get_event_loop()
loop.run_until_complete(start_browsers())
input("Press Enter after setting up VPNs")
vintedapi.getAuth() #asyncio.gather
input("Press Enter after getting all auth")
loop.run_until_complete(main_loop())
