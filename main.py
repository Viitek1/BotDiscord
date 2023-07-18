import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='.', intents=intents)

emojis = {
    "Maca": 1129135625979822140,
    "Incubo": 1129133199830827209,
    "ArcanoElevado": 1129135605402579005,
    "ArcanoSilence": 1129135608250499192,
    "MainHeal": 1129135614168670229,
    "Corrompido": 1129135616576196688,
    "Bruxo": 1129135609999532183,
    "Fire": 1129135619801620551,
    "Frost": 1129135622783778856,
    "Raiz": 1129135631809921104,
    "QuebraReinos": 1129135628064391168,
    "CacaEspirito": 1129135612453195877,
    "Entalhada": 1129135618203590778,
    "Xbow": 1129135634330681446
}

roles = {
    "Avalon": None
}

def find_roles(msg):
    role = discord.utils.find(lambda r: r.name == "Avalon", msg.guild.roles)
    return role

@bot.command()
async def completa(ctx, min_ip, date, hora):
    ip = int(min_ip)

    body_text = discord.Embed(
        title=f"Avalon    Data: {date}   Horario: {hora} ",
        description=f"-IP MINIMO DPS: {ip} ARMA E OFFHANGE + IP GERAL: {ip - 300}\n"
        f"-IP MINIMO SUPORTES: {ip - 300}\n\n"
        f"SAIDA DE FORT\n"
        f"CLASSES\n"
        f"1X MAIN TANK({ip})\n"
        f"1X OFFTANK({ip})\n"
        f"1X ARCANO ELEVADO({ip-300})\n"
        f"1X 1H ARCANO({ip})\n"
        f"1X Main Healer({ip})\n"
        f"1X PT Healer({ip})\n"
        f"1X Bruxo({ip - 300})\n"
        f"1X Fire({ip})\n"
        f"2X Frost({ip})\n"
        f"3X Raiz Ferrea({ip - 300})\n"
        f"1X Quebra Reinos({ip - 300})\n"
        f"1X Caça-Espirito({ip})\n"
        f"1X Oculto({ip - 300})\n"
        f"4X Xbow({ip})\n"
        f"1X Scout(OBRIGATORIO COMPARTILHAR TELA!!!)\n\n",
    )

    embed_main = body_text.add_field(name='Main Tank ()', value="", inline=True)
    body_text.add_field(name='OFF Tank ()', value="", inline=True)
    body_text.add_field(name='Arcano Elevado()', value="", inline=True)

    msg = await ctx.send(embed=embed_main)
    global msg_id
    msg_id = msg.id

    for emoji_name, emoji_id in emojis.items():
        emoji = discord.utils.get(ctx.guild.emojis, id=emoji_id)
        await msg.add_reaction(emoji)
    
    roles["Avalon"] = find_roles(msg)


@bot.event
async def on_reaction_add(reaction, user):
    # message = reaction.message
    # emoji_id = reaction.emoji.id

    # if emoji_id in emojis.values() and message.id == msg_id:
    #     name = user.name
    #     await user.add_roles(roles["Avalon"])

    #     if emoji_id == emojis["Maca"]:
    #         users = [user.name]
    #         usernames = "\n".join(users)
    #         msg_embed1 = embed_main.set_field_at(
    #             0, name=f'Main Tank ({len(users)})', value=usernames, inline=True)
    #         await message.edit(embed=msg_embed1)
    print();

# @bot.event
# async def on_reaction_remove(reaction, user):
#     msg = reaction.message
#     emoji_id = reaction.emoji.id

#     if emoji_id in emojis.values() and msg.id == msg_id:
#         await user.remove_roles(roles["Avalon"])
#         users.remove(user.name)
#         usernames = "\n".join(users)
#         msg_embed1 = embed_main.set_field_at(
#             0, name=f'Main Tank ({len(users)})', value=usernames, inline=True)
#         await msg.edit(embed=msg_embed1)

# @bot.command()
# async def clear(ctx, amount: int):
#     if amount == 0:
#         await ctx.channel.purge(limit=10)
#     else:
#         await ctx.channel.purge(limit=amount)

bot.run('hash')
