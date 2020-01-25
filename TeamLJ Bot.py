import discord

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("TeamLJ")
    await client.change_presence(status=discord.Status.idle, activity=game)



@client.event
async def on_message(message):
    if message.content.startswith("!안녕"):
        await message.channel.send("안녕하세요")
    if message.content.startswith("!trucksmp링크"):
        await message.channel.send("https://truckersmp.com/")
    if message.content.startswith("!디스코드주소"):
        await message.channel.send("```TeamLJ Discord : https://discord.gg/9zg3c3h```")


    if message.content.startswith("/채널메세지"):
        channel = message.content[7:25]
        msg = message.content[26:]
        await  client.get_channel(int(channel)).send(msg)

    if message.content.startswith("!역할설정"):
        role = ""
        rolename = message.content.split(" ")
        member = discord.utils.get(client.get_all_members(), id=rolename[1])
        for i in message.server.roles:
            if i.name == rolename[2]:
                role = i
                break
        await client.add_roles(member, role)

    if message.content.startswith("/dm"):
        author = message.guild.get_member (int(message.content[4:22]))
        msg = message.content[23:]
        await author.send(msg)

client.run("NjQ3ODA5NDQ2MTIyMzU2Nzc2.XfMXeA.ADTs3zkKEbM99cFcPFlYcp8WtKM")