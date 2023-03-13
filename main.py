from telethon import TelegramClient
from os import path
from time import sleep
import aiocron
from telethon.tl.types import PeerUser

config = {
    "apiID" : 123,
    "apiHash" : "",
    "botToken" : "",
    "directory" : r"./salam/lala.txt",
    "adminUserId" : 123, # int
    "timeSleep" : 120 # min
}
class CheckFile:
    def __init__(self) -> None:
        self.directory = config["directory"]
    async def check_file(self):
        if not path.exists(self.directory):
            text = "file zekr shode yaft nashod :|"
            for char in text:
                sleep(0.1)
                print(char, end= "", flush= True)
            exit()
        return True

client = TelegramClient(
    session= "bot",
    api_id= config["apiID"],
    api_hash= config["apiHash"]
)

client.start(bot_token= config["botToken"])

@aiocron.crontab("*/{} * * * *".format(config["timeSleep"]))
async def main():
    CheckFile.check_file()
    await client.send_file(PeerUser(config["adminUserId"]), config["directory"], caption= 'تقدیم با عشق')

client.run_until_disconnected()