from discord.ext import commands
import os
import datetime

client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print("Bot is ready")

@client.command()
async def save(ctx):
    # change channelid and authorid
    # if ctx.message.channel.id == channelid and ctx.message.author.id == authorid:
    if ctx.message.author.id == authorid: 
        channel = ctx.message.channel.id
        print("Fetching all messages... Can take a while")
        messages = [msg for msg in await ctx.channel.history(limit=None, oldest_first=False).flatten() if msg.attachments]
        for messages_list_item in messages:
            try:
                messages_list_item_str = str(messages_list_item)
                # print(messages_list_item_str)
                message_id_temp = messages_list_item_str.split(' channel')[0]
                message_id_final = message_id_temp.replace("<Message id=", "")
                user_id_temp = messages_list_item_str.split('author=<User id=')[1]
                user_id_final = user_id_temp.split(' name=',1)[0]
                user_name_temp = messages_list_item_str.split("name='")[2]
                user_name_final = user_name_temp.split("' discriminator=")[0]
                channel_name_temp = messages_list_item_str.split("name='")[1]
                channel_name_final = channel_name_temp.split("' position=")[0]
                # print(message_id_final)
                # print(user_id_final)
                # print(user_name_final)
            except IndexError:
                xdddd = "amogus"
            id_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            for id_list_item in id_list:
                try:
                    message2 = await ctx.message.channel.fetch_message(message_id_final)
                    url = message2.attachments[id_list_item].url
                    media_files_list = [".jpg", ".jpeg", ".png", ".gif", ".webp", ".mp4", ".mov", ".webm", ".mp3", ".ogg", ".wav"]
                    if url.endswith(media_files_list[0]) or url.endswith(media_files_list[1]) or url.endswith(media_files_list[2]) or url.endswith(media_files_list[3]) or url.endswith(media_files_list[4]) or url.endswith(media_files_list[5]) or url.endswith(media_files_list[6]) or url.endswith(media_files_list[7]) or url.endswith(media_files_list[8]) or url.endswith(media_files_list[9]) or url.endswith(media_files_list[10]) or url.endswith(media_files_list[11]):
                        fileTimeTemp = str(message2.created_at)
                        fileTimeTemp2 = fileTimeTemp.replace(" ", "_")
                        fileTimeTemp3 = fileTimeTemp2.replace(":", "-")
                        fileTime = fileTimeTemp3.split('.')[0]
                        fileName = url.rsplit('/', 1)[-1]
                        fileNameFinal = channel_name_final + "_" + fileTime + "_" + user_name_final + "_" + fileName
                        # fileNameFinal = fileTime + "__" + fileName
                        print(datetime.datetime.now().strftime('[%Y-%m-%d %H:%M:%S]'),"Saving file: " + fileNameFinal)
                        await message2.attachments[id_list_item].save(fileNameFinal)
                        # if user_id_final == 'id':
                            # some action
                except IndexError:
                    xdddd = "amogus"              
        print("All files saved")
        print(" ")

client.run("token")