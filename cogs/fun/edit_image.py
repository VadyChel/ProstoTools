import discord
from discord.ext import commands


class FunEditImage(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.FOOTER = self.client.config.FOOTER_TEXT

    @commands.command(
        name="color-view",
        aliases=["colorview"],
        usage="color-view [Цвет]",
        description="**Цвет в изображении**",
        help="**Примеры использования:**\n1. {Prefix}color-view #444444\n\n**Пример 1:** Покажет изображении в указаном цвете"
    )
    @commands.cooldown(1, 60, commands.BucketType.member)
    async def colorview(self, ctx, color: str):
        if color.startswith("#"):
            hex = color[1:]
            if len(hex) == 6:
                emb = discord.Embed(
                    description=f"Цвет `{color}` в изображении",
                    colour=discord.Color.green()
                )
                emb.set_image(url=f"https://some-random-api.ml/canvas/colorviewer?hex={hex}")
                emb.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
                emb.set_footer(text=self.FOOTER, icon_url=self.client.user.avatar_url)
                await ctx.send(embed=emb)
            else:
                emb = discord.Embed(
                    title="Ошибка!",
                    description=f"**Указан не правильный формат цвета!**",
                    colour=discord.Color.green(),
                )
                emb.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
                emb.set_footer(text=self.FOOTER, icon_url=self.client.user.avatar_url)
                await ctx.send(embed=emb)
                await ctx.message.add_reaction("❌")
                return
        else:
            emb = discord.Embed(
                title="Ошибка!",
                description=f"**Указан не правильный формат цвета!**",
                colour=discord.Color.green(),
            )
            emb.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
            emb.set_footer(text=self.FOOTER, icon_url=self.client.user.avatar_url)
            await ctx.send(embed=emb)
            await ctx.message.add_reaction("❌")
            return

    @commands.command(
        description="**Добавляет к аватарке радужный эффект**",
        usage="gay |@Участник|",
        help="**Примеры использования:**\n1. {Prefix}gay\n2. {Prefix}gay @Участник\n3. {Prefix}gay 660110922865704980\n\n**Пример 1:** Добавит к вашей аватарке радужный эффект\n**Пример 2:** Добавит к аватарке указаного участника радужный эффект\n**Пример 3:** Добавит к аватарке участника с указаным id радужный эффект"
    )
    @commands.cooldown(1, 60, commands.BucketType.member)
    async def gay(self, ctx, member: discord.Member = None):
        if member is None:
            member = ctx.author

        emb = discord.Embed(title="Радужный эффект", colour=discord.Color.green())
        emb.set_image(url=f"https://some-random-api.ml/canvas/gay/?avatar={member.avatar_url_as(format='png')}")
        emb.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        emb.set_footer(text=self.FOOTER, icon_url=self.client.user.avatar_url)
        await ctx.send(embed=emb)

    @commands.command(
        description="**Добавляет к аватарке эффект стекла**",
        usage="glass |@Участник|",
        help="**Примеры использования:**\n1. {Prefix}glass\n2. {Prefix}glass @Участник\n3. {Prefix}glass 660110922865704980\n\n**Пример 1:** Добавит к вашей аватарке эффект стекла\n**Пример 2:** Добавит к аватарке указаного участника эффект стекла\n**Пример 3:** Добавит к аватарке участника с указаным id эффект стекла"
    )
    @commands.cooldown(1, 60, commands.BucketType.member)
    async def glass(self, ctx, member: discord.Member = None):
        if member is None:
            member = ctx.author

        emb = discord.Embed(title="Эффект стекла", colour=discord.Color.green())
        emb.set_image(url=f"https://some-random-api.ml/canvas/glass/?avatar={member.avatar_url_as(format='png')}")
        emb.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        emb.set_footer(text=self.FOOTER, icon_url=self.client.user.avatar_url)
        await ctx.send(embed=emb)

    @commands.command(
        description="**Добавляет к аватарке эффект смерти в GTA**",
        usage="wasted |@Участник|",
        help="**Примеры использования:**\n1. {Prefix}wasted\n2. {Prefix}wasted @Участник\n3. {Prefix}wasted 660110922865704980\n\n**Пример 1:** Добавит к вашей аватарке эффект смерти в GTA\n**Пример 2:** Добавит к аватарке указаного участника эффект смерти в GTA\n**Пример 3:** Добавит к аватарке участника с указаным id эффект смерти в GTA"
    )
    @commands.cooldown(1, 60, commands.BucketType.member)
    async def wasted(self, ctx, member: discord.Member = None):
        if member is None:
            member = ctx.author

        emb = discord.Embed(title="Эффект смерти в GTA", colour=discord.Color.green())
        emb.set_image(url=f"https://some-random-api.ml/canvas/wasted/?avatar={member.avatar_url_as(format='png')}")
        emb.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        emb.set_footer(text=self.FOOTER, icon_url=self.client.user.avatar_url)
        await ctx.send(embed=emb)

    @commands.command(
        description="**Добавляет к аватарке указаный эффект**",
        usage="filter [Фильтер] |@Участник|",
        help="**Примеры использования:**\n1. {Prefix}filter threshold\n2. {Prefix}filter threshold @Участник\n3. {Prefix}filter threshold 660110922865704980\n\n**Пример 1:** Добавит к вашей аватарке эффект threshold\n**Пример 2:** Добавит к аватарке указаного участника эффект threshold\n**Пример 3:** Добавит к аватарке участника с указаным id эффект threshold"
    )
    @commands.cooldown(1, 60, commands.BucketType.member)
    async def filter(self, ctx, filter:str, member: discord.Member = None):
        if member is None:
            member = ctx.author

        filters = (
            "greyscale",
            "invert",
            "brightness",
            "threshold",
            "sepia",
            "red",
            "green",
            "blue",
            "blurple",
            "pixelate",
            "blur"
        )
        if filter.lower() not in filters:
            emb = discord.Embed(
                title="Ошибка!",
                description=f"**Укажите один из этих фильтров: {', '.join(filters)}!**",
                colour=discord.Color.green(),
            )
            emb.set_author(
                name=self.client.user.name, icon_url=self.client.user.avatar_url
            )
            emb.set_footer(text=self.FOOTER, icon_url=self.client.user.avatar_url)
            await ctx.send(embed=emb)
            await ctx.message.add_reaction("❌")
            return

        emb = discord.Embed(title=f"Эффект {filter}", colour=discord.Color.green())
        emb.set_image(url=f"https://some-random-api.ml/canvas/{filter}/?avatar={member.avatar_url_as(format='png')}")
        emb.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        emb.set_footer(text=self.FOOTER, icon_url=self.client.user.avatar_url)
        await ctx.send(embed=emb)


def setup(client):
    client.add_cog(FunEditImage(client))