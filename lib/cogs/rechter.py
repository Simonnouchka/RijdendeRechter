from discord.ext.commands import Cog
from discord.ext.commands import command
from discord import embeds

class Rechter(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command(name="report", aliases=["rep"])
    async def report(self, ctx):
        await ctx.message.delete()
        message = await ctx.channel.fetch_message(ctx.message.reference.message_id)
        await message.reply(f"{ctx.message.author.mention} heeft {message.author.mention} aangeklaagd voor de volgende uitspraak: \"{message.content}\" \n Binnen 3-4 werkdagen zal er een rechtzaak plaatsvinden.")

    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.cogs_ready.ready_up("rechter")


def setup(bot):
    bot.add_cog(Rechter(bot))
