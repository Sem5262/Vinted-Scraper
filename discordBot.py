import  discord, asyncio
from discord import Intents
import redis, json
from discord.ui import Button, View
import time

redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

intents = Intents.default()
intents.messages = True
intents.reactions = True          
client = discord.Client(intents=intents)

buffer_name = 'new_items'

def dequeue_all_data_from_buffer():
    result = []
    data = redis_client.lpop(buffer_name)
    
    while data is not None:
        # Decode the JSON-formatted string and load it as a Python object
        item = json.loads(data.decode('utf-8'))
        result.append(item)
        data = redis_client.lpop(buffer_name)
    
    return result

def create_star_rating(rating):
    total_stars = 5
    full_stars = round(rating * total_stars)

    stars = '★' * full_stars + '☆' * (total_stars - full_stars)
    return stars

async def sendembed(data):
    
    channel_id = 1179451002722729987 
    channel = client.get_channel(channel_id)

    embeds = [
        discord.Embed(
            title= data['title'],
            description=data['description'],
            color=discord.Color.blue(),
        )
    ]
   
    
    embeds[0].url = data['url']
    embeds[0].add_field(name="`💶` ** Price **", value=f"`{data['price_numeric']} | {data['total_item_price']} ({data['currency']})`", inline=True)
    embeds[0].add_field(name="`📏` ** Size **", value=f"`{data['size']}`", inline=True)
    embeds[0].add_field(name=f"`📍` ** Location **", value=f"`{data['country_title']}`", inline=True)
    embeds[0].add_field(name="`👕` ** Brand **", value=f"`{data['brand']}`", inline=True)
    embeds[0].add_field(name="`🌟` ** Rating **", value=f"`{create_star_rating(data['feedback_reputation'])}|({data['feedback_count']})`", inline=True)
    embeds[0].add_field(name="`🕒` ** Posted **", value=f"<t:{int(time.time())}:R>", inline=True)
    
    
    for photo in data['photos'][:9]:
        image_embed = discord.Embed()
        image_embed.url = data['url']
        image_embed.set_image(url=photo)
        embeds.append(image_embed)
        
    linkButton = Button(label="🏷️ link",url=data['url'])
    buyButton = Button(label="🛒 Buy", url=f"https://www.vinted.be/transaction/buy/new?source_screen=item&transaction%5B&transaction%5Bitem_id%5D={data['id']}")
    view = View()

    view.add_item(linkButton)
    view.add_item(buyButton)
    await channel.send(embeds=embeds, view=view)

async def main_loop():
    while True:
        items = dequeue_all_data_from_buffer()  
        await asyncio.gather(*(sendembed(item) for item in items))
        await asyncio.sleep(0.2)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user.name}')
    print("started the loop")
    asyncio.create_task(main_loop())

client.run('Your_discord_token')      