import discord
from discord.ext import commands
 
from discord_buttons_plugin import *

client = commands.Bot(command_prefix='!')
buttons = ButtonsClient(client) 
client.remove_command('help')

@client.event
async def on_ready():
    print('Connected to bot: {}'.format(client.user.name))
    print('Bot ID: {}'.format(client.user.id))

@buttons.click
async def homeroom(ctx):
    embed = discord.Embed(title="( :signal_strength: ตารางเรียนวันจันทร์:satellite: )", description=":shield:TUK | TEAM:shield:", color=0xffff66)
    embed.add_field(name="HOMEROOM", value="HOMEROOM zoomlink: ", inline=False)
    await ctx.message.edit(embed = embed)
    await ctx.reply()

@buttons.click
async def monday(ctx):
    embed = discord.Embed(title="( :signal_strength: ตารางเรียนวันจันทร์:satellite: )", description=":shield:TUK | TEAM:shield:", color=0xffff66)
    embed.add_field(name="คาบแรก 8.30-9.00", value="Eng. Main Basic zoomlink: ", inline=False)
    embed.add_field(name="คาบสอง 9.15-9.45", value="Eng. Main Basic zoomlink: ", inline=False)
    embed.add_field(name="คาบสาม 10.05-10.35", value="Ent. Phy zoomlink: ", inline=False)
    embed.add_field(name="คาบสี 10.50-11.20", value="Ent. Chem zoomlink: ", inline=False)
    embed.add_field(name="คาบห้า 11.35-12.05", value="PE zoomlink: ตามหาลิ้งเอง", inline=False)
    embed.add_field(name="เบรคแดกข้าวเที่ยง, 12.05-13.00", value="แดกอย่าให้กูไล่", inline=False)
    embed.add_field(name="คาบหก 13.00-13.30", value="History zoomlink: ", inline=False)
    embed.add_field(name="คาบเจ็ด 13.45-14.15", value="Thai zoomlink: ", inline=False)
    embed.add_field(name="คาบแปด 14.30-15.00", value="Computer zoomlink: ", inline=False)
    await ctx.message.edit(embed = embed)
    await ctx.reply()

@buttons.click
async def tuesday(ctx):
    embed = discord.Embed(title="( :signal_strength: ตารางเรียนวันอังคาร:satellite: )", description=":shield:TUK | TEAM:shield:", color=0xffccff)
    embed.add_field(name="คาบแรก 8.30-9.00", value="Math zoomlink: ", inline=False)
    embed.add_field(name="คาบสอง 9.15-9.45", value="Eng. Main Basic zoomlink: ", inline=False)
    embed.add_field(name="คาบสาม 10.05-10.35", value="Ent. bio zoomlink: ", inline=False)
    embed.add_field(name="คาบสี 10.50-11.20", value="Religion zoomlink: ", inline=False)
    embed.add_field(name="คาบห้า 11.35-12.05", value="Thai zoomlink: ", inline=False)
    embed.add_field(name="เบรคแดกข้าวเที่ยง, 12.05-13.00", value="แดกอย่าให้กูไล่", inline=False)
    embed.add_field(name="คาบหก 13.00-13.30", value="Physics zoomlink: ", inline=False)
    embed.add_field(name="คาบเจ็ด 13.45-14.15", value="Physics zoomlink: ", inline=False)
    embed.add_field(name="คาบแปด 14.30-15.00", value="Art zoomlink: ", inline=False)
    await ctx.message.edit(embed = embed)
    await ctx.reply()
    

@buttons.click
async def wednesday(ctx):
    embed = discord.Embed(title="( :signal_strength: ตารางเรียนพุธ:satellite: )", description=":shield:TUK | TEAM:shield:", color=0x00ff00)
    embed.add_field(name="คาบแรก 8.30-9.00", value="Ent. Phy zoomlink: ", inline=False)
    embed.add_field(name="คาบสอง 9.15-9.45", value="Ent. Math zoomlink: ", inline=False)
    embed.add_field(name="คาบสาม 10.05-10.35", value="Math zoomlink: ", inline=False)
    embed.add_field(name="คาบสี 10.50-11.20", value="Ent. bio zoomlink: ", inline=False)
    embed.add_field(name="คาบห้า 11.35-12.05", value="Eng. Main Basic zoomlink: ", inline=False)
    embed.add_field(name="เบรคแดกข้าวเที่ยง, 12.05-13.00", value="แดกอย่าให้กูไล่", inline=False)
    embed.add_field(name="คาบหก 13.00-13.30", value="Computer zoomlink: ", inline=False)
    embed.add_field(name="คาบเจ็ด 13.45-14.15", value="Social zoomlink: ", inline=False)
    embed.add_field(name="คาบแปด 14.30-15.00", value="Thai zoomlink: ", inline=False)
    await ctx.message.edit(embed = embed)
    await ctx.reply()
    

@buttons.click
async def thursday(ctx):
    embed = discord.Embed(title="( :signal_strength: ตารางเรียนวันพฤหัสบดี:satellite: )", description=":shield:TUK | TEAM:shield:", color=0xcc6633)
    embed.add_field(name="คาบแรก 8.30-9.00", value="Math zoomlink: ", inline=False)
    embed.add_field(name="คาบสอง 9.15-9.45", value="Biology zoomlink: ", inline=False)
    embed.add_field(name="คาบสาม 10.05-10.35", value="Ent. Math zoomlink: ", inline=False)
    embed.add_field(name="คาบสี 10.50-11.20", value="Ent. bio zoomlink: ", inline=False)
    embed.add_field(name="คาบห้า 11.35-12.05", value="Earth & Space zoomlink: ", inline=False)
    embed.add_field(name="เบรคแดกข้าวเที่ยง, 12.05-13.00", value="แดกอย่าให้กูไล่", inline=False)
    embed.add_field(name="คาบหก 13.00-13.30", value="Eng. Main Basic zoomlink: ", inline=False)
    embed.add_field(name="คาบเจ็ด 13.45-14.15", value="Physics zoomlink: ", inline=False)
    embed.add_field(name="คาบแปด 14.30-15.00", value="Chemistry zoomlink: ", inline=False)
    await ctx.message.edit(embed = embed)
    await ctx.reply()
    
@buttons.click
async def friday(ctx):
    embed = discord.Embed(title="( :signal_strength: ตารางเรียนวันศุกร์:satellite: )", description=":shield:TUK | TEAM:shield:", color=0x3366cc)
    embed.add_field(name="คาบแรก 8.30-9.00", value="กายภาพ zoomlink: ", inline=False)
    embed.add_field(name="คาบสอง 9.15-9.45", value="Math zoomlink: ", inline=False)
    embed.add_field(name="คาบสาม 10.05-10.35", value="Ent. Math zoomlink: ", inline=False)
    embed.add_field(name="คาบสี 10.50-11.20", value="Guidance zoomlink: ", inline=False)
    embed.add_field(name="คาบห้า 11.35-12.05", value="Ent. Chem zoomlink: ", inline=False)
    embed.add_field(name="เบรคแดกข้าวเที่ยง, 12.05-13.00", value="แดกอย่าให้กูไล่", inline=False)
    embed.add_field(name="คาบหก 13.00-13.30", value="Chemistry zoomlink: ", inline=False)
    embed.add_field(name="คาบเจ็ด 13.45-14.15", value="Eng. Main Basic zoomlink: ", inline=False)
    embed.add_field(name="คาบแปด 14.30-15.00", value="Thai zoomlink: ", inline=False)
    await ctx.message.edit(embed = embed)
    await ctx.reply()
    
#############################################################################################################################################################

@client.command()
async def zoom(ctx):
    await buttons.send(
		content="ควยบัน",
		channel = ctx.channel.id,
		components = [
			ActionRow([
				Button(

					style = ButtonType().Primary,
					label = "homeroom",
					custom_id = "homeroom",

				),

				Button(
					style = ButtonType().Success,
					label = "monday",
					custom_id = "monday"
				),
				Button(
					style = ButtonType().Success,
					label = "tuesday",
					custom_id = "tuesday",
				)
			]),
            ActionRow([
                Button(
                    style = ButtonType().Success,
                    label = "wednesday",
                    custom_id = "wednesday"
                ),
                Button(
                    style = ButtonType().Success,
                    label = "thursday",
                    custom_id = "thursday"
                ),
                Button(
                    style = ButtonType().Success,
                    label = "friday",
                    custom_id = "friday"
                )
            ])
		]
	)




client.run("Token")    