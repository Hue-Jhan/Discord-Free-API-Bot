# Discord-Free-API-Bot
Discord Bot with free simple api and AI functions, with built in responses, help command, triggers and more. Made in python.

HOW TO USE: Simply create a discord bot, upload this codes to your PyCharm specified folder. You will need to make an .env file and specify your bot AuthToken by typing DISCORD_TOKEN=xxxxxxxxxxxxxxxxxxxx

# 💻 API FUNCTIONS
<img align="right" src="https://github.com/Hue-Jhan/Discord-Free-API-Bot/blob/main/media/apibot%20h.png" width="350" />

The API functions i added are quite simple, i wanted to add some image altering ones but every api uses different kind of classes n stuff so i got bored, also theres `Jayx` and `NotSoBot` for advanced image altering. I added a prodia api command that uses the prodia stable diffusion model, allowing you to generate images based on a given prompt. 

Here are the functions i added:

- **!h**: Lists all the commands, do not confuse it with !help;
- **!ai (string)**: Generates an image based on your prompt (Prodia ai api), [API](https://app.prodia.com/api)
- **!dog**: Gives u a random dog image, [API](https://dog.ceo/api/breeds/image/random)  <!-- <img align="center" src="https://github.com/Hue-Jhan/Discord-Free-API-Bot/blob/main/media/apibot%20dog.png" width="100" /> --> 
- **!achiev (string)**: Type something and it gives u a minecraft achievemnt image of that, [API](https://api.alexflipnote.dev/achievement?text=xd).
- **!drake (string) (string)**: Type something and it gives u a drake meme image of that, [API](https://frenchnoodles.xyz/api/endpoints/drake/?text1=bals&text2=balz).
- **!supreme (string)**: Type something and it gives u a supreme image of that, [API](https://api.alexflipnote.dev/supreme?text=sium)
- **!ph (string) (string)**: Type something and it gives u a pronhub image of that, [API](https://api.alexflipnote.dev/pornhub?text=xd&text2=lel)
- **!meme (memename) (string) (string)**: Choose the meme, what to type and it will give u the pic, [API](https://api.memegen.link/images/)
- **!joke**: Gives u a random unfunny joke, [API](https://official-joke-api.appspot.com/jokes/random)
- **!urban (string) (number)**: Type something and it gives u the first 3 urban definitions of that, you can specify with (number) the exact result you want, [API](https://api.urbandictionary.com/v0/define?term=kek)
- **!insult (string)**: Gives u a random insult, [API](https://evilinsult.com/generate_insult.php?lang=en&type=json)

You can find examples of this commmands being executed in `media` folder, here are some examples:

<img align="left" src="https://github.com/Hue-Jhan/Discord-Free-API-Bot/blob/main/media/apibot%20achiev.png" width="100" />
<img align="left" src="https://github.com/Hue-Jhan/Discord-Free-API-Bot/blob/main/media/apibot%20supreme.png" width="100" />
<img align="left" src="https://github.com/Hue-Jhan/Discord-Free-API-Bot/blob/main/media/apibot%20ph.png" width="100" />
<img align="left" src="https://github.com/Hue-Jhan/Discord-Free-API-Bot/blob/main/media/apibot%20meme.png" width="100" />
<img align="left" src="https://github.com/Hue-Jhan/Discord-Free-API-Bot/blob/main/media/apibot%20urban.png" width="100" />
<img align="left" src="https://github.com/Hue-Jhan/Discord-Free-API-Bot/blob/main/media/apibot%20dog.png" width="100" />

---

---

---

---
<p>   </p>
<p>   </p>
<p>   </p>

# 🔧 Other Functions

- The bot possesses triggers you can customize in the `responses.py` folder (WARNING NSFW CONTENT).
You can customize the bot command to receive personal messages instead of receiving the answer in the channel where you asked it.
The triggers include a rolling dice function and a random age function

- The bot has also a customizable status
