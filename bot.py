# coding: utf-8
import discord 
from discord import app_commands

class MyClient(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self) #全てのコマンドを管理するCommandTree型オブジェクトを生成

    async def setup_hook(self):
        for id in mybot.cfg.guild_id_list:
            guild=discord.Object(id=id)
            self.tree.copy_global_to(guild=guild)
            await self.tree.sync(__