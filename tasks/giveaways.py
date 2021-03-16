import time as tm
from discord.ext import commands, tasks


class TasksGiveaways(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.giveaways_loop.start()

    @tasks.loop(minutes=1)
    async def giveaways_loop(self):
        await self.client.wait_until_ready()
        data = await self.client.database.get_giveaways()
        for setting in data:
            if tm.time() >= setting[6]:
                await self.client.utils.end_giveaway(setting)


def setup(client):
    client.add_cog(TasksGiveaways(client))
