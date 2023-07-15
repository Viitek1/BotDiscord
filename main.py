import discord
from discord.ext import commands
from discord.utils import get

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
#intents.typing = True
#intents.presences = True

bot = commands.Bot(command_prefix='.', intents=intents)
@bot.command()
async def completa(ctx, arg, date, hora):
    
    emoji_Maca = discord.utils.get(ctx.guild.emojis, id=1129135625979822140)
    emoji_Incubo = discord.utils.get(ctx.guild.emojis, id=1129133199830827209)
    emoji_ArcanoElevado = discord.utils.get(ctx.guild.emojis, id=1129135605402579005)
    emoji_ArcanoSilence = discord.utils.get(ctx.guild.emojis, id=1129135608250499192)
    emoji_MainHeal = discord.utils.get(ctx.guild.emojis, id=1129135614168670229)
    emoji_Corrompido = discord.utils.get(ctx.guild.emojis, id=1129135616576196688)
    emoji_Bruxo = discord.utils.get(ctx.guild.emojis, id=1129135609999532183)
    emoji_Fire = discord.utils.get(ctx.guild.emojis, id=1129135619801620551)
    emoji_Frost = discord.utils.get(ctx.guild.emojis, id=1129135622783778856)
    emoji_Raiz = discord.utils.get(ctx.guild.emojis, id=1129135631809921104)
    emoji_QuebraReinos = discord.utils.get(ctx.guild.emojis, id=1129135628064391168)
    emoji_CacaEspirito = discord.utils.get(ctx.guild.emojis, id=1129135612453195877)
    emoji_Entalhada = discord.utils.get(ctx.guild.emojis, id=1129135618203590778)
    emoji_Xbow = discord.utils.get(ctx.guild.emojis, id=1129135634330681446)
    
    emojis = [emoji_Maca,  emoji_Incubo, emoji_ArcanoElevado, emoji_ArcanoSilence, emoji_MainHeal, emoji_Corrompido, emoji_Bruxo, emoji_Fire, emoji_Frost,
            emoji_Raiz, emoji_QuebraReinos, emoji_CacaEspirito, emoji_Entalhada, emoji_Xbow]

    global ip
    ip = int(arg)
    global msg_embed
    msg_embed = discord.Embed(
        title=f"Avalon    Data: {date}   Horario: {hora} " ,
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
        f"1X Scout(OBRIGATORIO COMPARTILHAR TELA!!!)\n\n",)
    
    embed_main = msg_embed.add_field(name = f'{emoji_Maca}Main Tank ()', value="", inline = True)
    msg_embed.add_field(name = f'{emoji_Incubo}OFF Tank ()', value="", inline = True)
    msg_embed.add_field(name = f'{emoji_ArcanoElevado}Arcano Elevado()', value="", inline = True)

    global msg
    msg =  await ctx.send(embed = msg_embed)
    
    global msg_id 
    msg_id = msg.id
    #for i in emojis:
    await msg.add_reaction(emoji_Maca)
    users = []
    role = discord.utils.find(lambda r: r.name == "Avalon", msg.guild.roles)
    @bot.event
    async def on_reaction_add(reaction, user):
        msg = reaction.message
        if reaction.emoji in emojis and msg.id == msg_id: #and user == msg_user:
            funcao =  reaction.emoji.id
            name = user.name
            await user.add_roles(role)
            

           
            
            match funcao:
                case 1129135625979822140:
                    #users.append(user.name + '\n') funciona
                    users.append(user.name)
                    usernames = ""
                    print(users)
                    for user in users:
                        usernames += user 
                    msg_embed1 = embed_main.set_field_at(0, name = f'{emoji_Maca}Main Tank ({len(users)})', value=usernames, inline = True )
                    await msg.edit(embed=msg_embed1)
                case 1129133199830827209:
                    '''offTank = name
                    mainTank = mainTank
                    arcanoElevado = arcanoElevado

                    msg_embed1 = msg_embed.clear_fields()
                    msg_embed1.add_field(name = f'{emoji_Maca}Main Tank ({len([mainTank])})', value=mainTank, inline = True)
                    msg_embed1.add_field(name=f"{emoji_Incubo}OFFTank ({len([offTank])})", value=offTank, inline=True)
                    msg_embed1.add_field(name=f"{emoji_ArcanoElevado}Arcano Elevado ({len([arcanoElevado])})", value=arcanoElevado, inline=True)

                    await msg.edit(embed=msg_embed1)'''

                case 1129135605402579005:
                    '''arcanoElevado = name
                    mainTank = mainTank
                    offTank = offTank

                    msg_embed1 = msg_embed.clear_fields()
                    msg_embed1.add_field(name = f'{emoji_Maca}Main Tank ({len([mainTank])})', value=mainTank, inline = True)
                    msg_embed1.add_field(name=f"{emoji_Incubo}OFFTank ({len([offTank])})", value=offTank, inline=True)
                    msg_embed1.add_field(name=f"{emoji_ArcanoElevado}Arcano Elevado ({len([arcanoElevado])})", value=arcanoElevado, inline=True)

                    await msg.edit(embed=msg_embed1)'''
                case 1129135608250499192:
                    arcanoSilence = name
                case 1129135614168670229:
                    mainTank = name
                case 1129135616576196688:
                    mainTank = name
                case 1129135609999532183:
                    mainTank = name
                case 1129135619801620551:
                    mainTank = name
                case 1129135622783778856:
                    mainTank = name
                case 1129135631809921104:
                    mainTank = name
                case 1129135628064391168:
                    mainTank = name
                case 1129135612453195877:
                    mainTank = name
                case 1129135618203590778:
                    mainTank = name
            


    @bot.event
    async def on_reaction_remove(reaction, user):  
        nome = user.name
        msg = reaction.message
        if reaction.emoji in emojis and msg.id == msg_id: #and user == msg_user:
            await user.remove_roles(role)
            users.remove(user.name)
            usernames = ""

            for user in users:
                usernames -= user 
            msg_embed1 = embed_main.set_field_at(0, name = f'{emoji_Maca}Main Tank ({len(users)})', value=usernames, inline = True )
            await msg.edit(embed=msg_embed1)
        
    

@bot.command()
async def clear(ctx, amount : int):
    if amount == 0:
        await ctx.channel.purge(limit=10)
    else:
        await ctx.channel.purge(limit=amount)


    



#test

bot.run('MTA5MTcxMjg1MzA4NzYxNzA4NA.G2utZU.MWFA98IqJfw3krtPEwgjsmfjWrbExkpEIJ7Tp4')




