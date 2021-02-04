from modules.scheduler.scheduler import Scheduler
from discord.ext import commands
import random
import datetime


class PingCog(commands.Cog, name="Ping"):
	"""A command which simply acknowledges the user's ping"""

	def __init__(self, bot: commands.Bot):
		self.bot = bot

	@commands.command(name="ping")
	async def ping(self, ctx: commands.Context):
		"""A command which simply acknowledges the user's ping.

		Usage:
		```
		++ping
		```
		"""

		# log in console that a ping was received
		print("Received ping")

		with open("modules/ping/responses.txt") as responses:
			await ctx.send(random.choice(responses.readlines()))

	@Scheduler.schedule()
	def on_test(self):
		print("test", datetime.datetime.now())


# This function will be called when this extension is loaded. It is necessary to add these functions to the bot.
def setup(bot: commands.Bot):
	bot.add_cog(PingCog(bot))