from telethon import TelegramClient
from os import path
from time import sleep
import aiocron
from telethon.tl.types import PeerUser
from telethon.tl.functions.messages import SendMultiMediaRequest
# SendMultiMediaRequest()


config = {
    "apiID" : 271091,
    "apiHash" : "c67b07ae46783460c54aa781f0ecf09d",
    "botToken" : "5701813060:AAEuNLXRknCSUhoZqGktpnjmyCAuqet77No",
    "directory" : r"../../etc/x-ui/x-ui.db",
    "adminUserId" : 931213973, # int
    "timeSleep" : 1 # min
}
class CheckFile:
    def __init__(self) -> None:
        self.directory = config["directory"]
    def check_file(self):
        if not path.exists(self.directory):
            text = "file zekr shode yaft nashod :|\n"
            for char in text:
                sleep(0.1)
                print(char, end= "", flush= True)
            exit()
        return True

CheckFile().check_file()


client = TelegramClient(
    session= "bot",
    api_id= config["apiID"],
    api_hash= config["apiHash"]
)

client.start(bot_token= config["botToken"])

@aiocron.crontab("*/{} * * * *".format(config["timeSleep"]))
async def main():
    CheckFile().check_file()
    await client.send_file(PeerUser(config["adminUserId"]), config["directory"], caption= 'تقدیم با عشق')

print("bot is online")
client.run_until_disconnected()
