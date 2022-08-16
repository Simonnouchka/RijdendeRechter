from datetime import datetime

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from discord import Embed, File
from discord.ext.commands import Bot as BotBase
from discord.ext.commands import CommandNotFound

from ..db import db

PREFIX = "+"
OWNER_IDS = [730711658934042625]


class Bot(BotBase):
    def __init__(self):
        self.PREFIX = PREFIX
        self.ready = False
        self.guild = None
        self.scheduler = AsyncIOScheduler()

        db.autosave(self.scheduler)
        super().__init__(command_prefix=PREFIX, owner_ids=OWNER_IDS)

    def run(self, version):
        self.VERSION = version

        with open("./lib/bot/token.0", "r", encoding="utf-8") as tf:
            self.TOKEN = tf.read()

        print("running bot...")
        super().run(self.TOKEN, reconnect=True)

    async def on_connect(self):
        print("bot connected")

    async def on_disconnect(self):
        print("bot disconnected")

    async def on_error(self, err, *args, **kwargs):
        if err == "on_command_error":
            await args[0].send("Something went wrong.")

        channel = self.get_channel(868538789574869017)
        await channel.send("An error occured.")
        raise

    async def on_command_error(self, ctx, exc):
        if isinstance(exc, CommandNotFound):
            pass

        else:
            raise exc.original

    async def on_ready(self):
        if not self.ready:
            self.ready = True
            self.guild = self.get_guild(868538789574869014)
            self.scheduler.start()

            channel = self.get_channel(1009080597630697473)
            await channel.send("Now online!")

            print("bot ready")

        else:
            print("bot reconnected")

    async def on_message(self, message):
        pass


bot = Bot()
