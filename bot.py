# coding: utf-8
import discord 
from discord import app_commands

class MyClient(discord.Client):
    def __init__(self, user_id):
        intents = discord.Intents.all()
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self) #全てのコマンドを管理するCommandTree型オブジェクトを生成
        self.user_id = user_id

    #ボットをセットアップするdiscord.Clientが持つ空のメソッド、オーバーライドすることでログイン時にon_ready()より精密に実行する
    async def setup_hook(self):
        self.channel = self.create_dm(self.get_user(self.user_id))
        self.channel.send(content="起動しました。")
