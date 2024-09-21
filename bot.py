import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def theme(ctx, num: int = None):
    # If no theme is provided, prompt the user to choose
    if num is None:
        await ctx.send('Выберите одну из двух тем: 1, 2, 3')
        return

    if num == 1:
        await water_pollution(ctx)
    elif num == 2:
        await deforestation(ctx)
    elif num == 3:
        await warming(ctx)
    else:
        await ctx.send('Неверная тема. Выберите из: 1, 2, 3')


async def water_pollution(ctx):
    await ctx.send('Загрязнение вод: корпорации выбрасывают химикаты и нефть в водоёмы, вместо того что бы оккуратно утилизировать отходы и следить за оборудыванием')
    img_name = random.choice(os.listdir('waterpollution'))
    with open(f'waterpollution/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
    await ctx.send('Решение: корпорации не хотят терять свои доходы, но государтсво может на них надавить.')

async def deforestation(ctx):
    await ctx.send('Вырубка лесов пагубно сказывается на нас, по скольку мы дышим кислородом, которые вырабатывают деревья')
    img_name = random.choice(os.listdir('les'))
    with open(f'les/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
    await ctx.send('Решение: использовать менее органическое топливо')

async def warming(ctx):
    await ctx.send('раньше все думали что будет глобальное похолодание, но к нашему несчястью наши же производства перевесили чашу весов в сторону глобального потеления...')
    img_name = random.choice(os.listdir('warming'))
    with open(f'warming/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
    await ctx.send('Решение: Многие факторы влияют на повышение температуры, даже сельскохозяйственные животные (в особенности коровы), но всё же в основном причина это выхлопные газы и дым заводов, фильтры дорогие но эта планета нам дороже')

bot.run("Token")