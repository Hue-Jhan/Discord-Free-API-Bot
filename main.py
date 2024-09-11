from typing import Final
import os, json, requests, discord, urllib.parse
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import get_response
from discord.ext import tasks, commands
from prodiapy import Prodia
from io import BytesIO
from PIL import Image
import random
import asyncio
import aiohttp
import time

load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

# Setup
intents: Intents = discord.Intents.all()
intents.message_content = True  # NOQA
intents.members = True  # ignore if it gives u warnings
client = commands.Bot(command_prefix="!", intents=intents)
url_prodia = "https://api.prodia.com/v1/sd/generate"


# startup
@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running!')
    await client.change_presence(status=discord.Status.idle)


@client.command()
async def h(ctx):
    em = discord.Embed(title='HELP PAGE', color=discord.Color.yellow())
    em.set_author(name='COMMANDS LIST')
    em.add_field(name='!dog', value='Gives u a random dog image', inline=False)
    em.add_field(name='!achiev (string)', value='Type something and it gives u a minecraft achievemnt image of that', inline=False)
    em.add_field(name='!drake (string) (string)', value='Type something and it gives u a drake meme image of that', inline=False)
    em.add_field(name='!supreme (string)', value='Type something and it gives u a supreme image of that', inline=False)
    em.add_field(name='!ph (string) (string)', value='Type something and it gives u a pornhub image of that', inline=False)
    em.add_field(name='!meme (memename) (string) (string)', value='Choose the meme, what to type and it will give u the pic', inline=False)
    em.add_field(name='!joke', value='Gives u a random unfunny joke', inline=False)
    em.add_field(name='!urban (string) (number)', value='Type something and it gives u the first 3 urban definitions of that, you can specify with (number) the exact result you want', inline=False)
    em.add_field(name='!insult', value='Gives u a random insult', inline=False)
    em.add_field(name='!ai', value='Type something and its gonna generate an image of that', inline=False)
    await ctx.send(embed=em)


@client.command()
async def dog(ctx):
    try:
        r = requests.get("https://dog.ceo/api/breeds/image/random")
        res = r.json()
        if r.status_code == 200 and res['status'] == 'success':
            em = discord.Embed(title='Random Dog Image', color=discord.Color.blurple())
            em.set_image(url=res['message'])
            await ctx.send(embed=em)
        else:
            await ctx.send("Failed to fetch a dog image.")
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")


@client.command()
async def achiev(ctx, input: str):
    try:
        res = requests.get(f"https://api.alexflipnote.dev/achievement?text={input}")
        if res.status_code == 200:
            content_type = res.headers['Content-Type']
            if 'image' in content_type:
                image = Image.open(BytesIO(res.content))
                with BytesIO() as image_binary:
                    image.save(image_binary, 'PNG')
                    image_binary.seek(0)
                    await ctx.send(file=discord.File(fp=image_binary, filename='achiev_meme.png'))
            else:
                r = res.json()
                await ctx.send(f"API returned an error: {r}")
        else:
            await ctx.send("Failed to fetch a drake meme")
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")


@client.command()
async def drake(ctx, input1: str, input2: str):
    try:
        res = requests.get(f"https://frenchnoodles.xyz/api/endpoints/drake/?text1={input1}&text2={input2}")
        # r = res.json()
        # image = Image.open(BytesIO(r.content))
        if res.status_code == 200:
            content_type = res.headers['Content-Type']
            if 'image' in content_type:
                image = Image.open(BytesIO(res.content))
                with BytesIO() as image_binary:
                    image.save(image_binary, 'PNG')
                    image_binary.seek(0)
                    await ctx.send(file=discord.File(fp=image_binary, filename='drake_meme.png'))
            else:
                r = res.json()
                await ctx.send(f"API returned an error: {r}")
        else:
            await ctx.send("Failed to fetch a drake meme")
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")


@client.command()
async def supreme(ctx, input: str):
    try:
        res = requests.get(f"https://api.alexflipnote.dev/supreme?text={input}")
        # r = res.json()
        # image = Image.open(BytesIO(r.content))
        if res.status_code == 200:
            content_type = res.headers['Content-Type']
            if 'image' in content_type:
                image = Image.open(BytesIO(res.content))
                with BytesIO() as image_binary:
                    image.save(image_binary, 'PNG')
                    image_binary.seek(0)
                    await ctx.send(file=discord.File(fp=image_binary, filename='supremepic.png'))
            else:
                r = res.json()
                await ctx.send(f"API returned an error: {r}")
        else:
            await ctx.send("Failed to fetch the supreme pic")
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")


@client.command()
async def ph(ctx, input1: str, input2:str):
    try:
        res = requests.get(f"https://api.alexflipnote.dev/pornhub?text={input1}&text2={input2}")
        # r = res.json()
        # image = Image.open(BytesIO(r.content))
        if res.status_code == 200:
            content_type = res.headers['Content-Type']
            if 'image' in content_type:
                image = Image.open(BytesIO(res.content))
                with BytesIO() as image_binary:
                    image.save(image_binary, 'PNG')
                    image_binary.seek(0)
                    await ctx.send(file=discord.File(fp=image_binary, filename='phpic.png'))
            else:
                r = res.json()
                await ctx.send(f"API returned an error: {r}")
        else:
            await ctx.send("Failed to fetch the ph pic")
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")


@client.command()
async def meme(ctx, input0: str, input1: str, input2:str):
    try:
        res = requests.get(f"https://api.memegen.link/images/{input0}/{input1}/{input2}")
        # r = res.json()
        # image = Image.open(BytesIO(r.content))
        if res.status_code == 200:
            content_type = res.headers['Content-Type']
            if 'image' in content_type:
                image = Image.open(BytesIO(res.content))
                with BytesIO() as image_binary:
                    image.save(image_binary, 'PNG')
                    image_binary.seek(0)
                    await ctx.send(file=discord.File(fp=image_binary, filename='memepic.png'))
            else:
                r = res.json()
                await ctx.send(f"API returned an error: {r}")
        else:
            await ctx.send("Failed to fetch the meme pic")
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")


@client.command()
async def insult(ctx):
    try:
        r = requests.get("https://evilinsult.com/generate_insult.php?lang=en&type=json")
        res = r.json()
        if r.status_code == 200:
            em = discord.Embed(title='- Random Insult', color=discord.Color.blurple())
            em.add_field(name=res['insult'], value="nigga", inline=False)
            await ctx.send(embed=em)
        else:
            await ctx.send("Failed to fetch an insult")
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")


@client.command()
async def urban(ctx, *, input: str, MaxDef: int = 3):
    try:
        encoded_input = urllib.parse.quote(input)
        r = requests.get(f"https://api.urbandictionary.com/v0/define?term={encoded_input}")
        res = r.json()
        if r.status_code == 200 and 'list' in res and res['list']:
            definitions = res['list']  # [:MaxDef]
            if not definitions:
                await ctx.send(f"No definitions found for {input}")
                return
            definitions = definitions[:MaxDef]
            for entry in definitions:
                definition = entry['definition'][:1020] + '...' if len(entry['definition']) > 1024 else entry['definition']
                example = entry.get('example', 'No example available')
                example = example[:1020] + '...' if len(example) > 1024 else example
                thumbs_up = entry.get('thumbs_up', 0)
                thumbs_down = entry.get('thumbs_down', 0)
                author = entry.get('author', 'Unknown')
                em = discord.Embed(title=f'- Urban dictionary Definition of {input}', color=discord.Color.blurple(), url=entry['permalink'])
                em.add_field(name='Definition', value=definition, inline=False)
                em.add_field(name="Example", value=example, inline=False)
                em.set_footer(text=f"👍 {thumbs_up} | 👎 {thumbs_down} | Author: {author}")
                await ctx.send(embed=em)
        else:
            await ctx.send(f"No definitions found for {input}")
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")


@client.command()
async def ai(ctx, *, prompt):
    try:
        url_prodia_generate = "https://api.prodia.com/v1/sd/generate"
        payload = {
            "model": "v1-5-pruned-emaonly.safetensors [d7049739]",
            "prompt": prompt,
            "negative_prompt": "badly drawn",
            "steps": 20,
            "cfg_scale": 7,
            "seed": -1,
            "upscale": False,
            "sampler": "DPM++ 2M Karras",
            "width": 512,
            "height": 512
        }
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "X-Prodia-Key": "XXXXXXXXXXXXXXXXXXXXXXXXX"
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(url_prodia_generate, json=payload, headers=headers) as response:
                if response.status != 200:
                    await ctx.send(f"Error: Received status code {response.status}")
                    return

                response_data = await response.json()
                job_id = response_data.get("job")
                if not job_id:
                    await ctx.send("Failed to start job.")
                    return

                await ctx.send(f"Job queued, pls wait...")
                
                await poll_job_status(ctx, job_id)

    except Exception as e:
        await ctx.send(f"An error occurred: {e}")

async def poll_job_status(ctx, job_id):
        url_prodia_status = f"https://api.prodia.com/v1/job/{job_id}"
        headers = {
            "accept": "application/json",
            "X-Prodia-Key": "XXXXXXXXXXXXXXXXXXXXXXXXX7"
        }

        while True:
            await asyncio.sleep(1)

            async with aiohttp.ClientSession() as session:
                async with session.get(url_prodia_status, headers=headers) as response:
                    if response.status != 200:
                        await ctx.send(f"Error: Received status code {response.status}")
                        return

                    status_data = await response.json()
                    status = status_data.get("status")
                    if status == "succeeded":
                        image_url = status_data.get("imageUrl")
                        if image_url:
                            await send_image(ctx, image_url)
                            break
                    elif status == "failed":
                        await ctx.send("Job failed.")
                        break

async def send_image(ctx, image_url):
        embed = discord.Embed(title="Generated Image")
        embed.set_image(url=image_url)
        await ctx.send(embed=embed)


@client.command()
async def joke(ctx):
    try:
        r = requests.get("https://official-joke-api.appspot.com/jokes/random")
        res = r.json()
        if r.status_code == 200:
            em = discord.Embed(title='- Random (unfunny) joke', color=discord.Color.blurple())
            em.add_field(name=res['setup'], value=" ", inline=False)
            em.add_field(name=res['punchline'], value="", inline=False)
            await ctx.send(embed=em)
        else:
            await ctx.send("Failed to fetch a joke")
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")



@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("!"):
        print("ao")
        await client.process_commands(message)
    #    return
    else:
        username: str = str(message.author)
        user_message: str = message.content
        channel: str = str(message.channel)
        print(f'[{channel}] {username}: "{user_message}"')
        await send_message(message, user_message)


async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print('(Message was empty because intents were not enabled probably)')
        return

    if is_private := user_message[0] == '?':
        user_message = user_message[1:]

    try:
        response: str = get_response(user_message)
        if response != '0':
            await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


# entry point
def main() -> None:
    client.run(token=TOKEN)


if __name__ == '__main__':
    main()
