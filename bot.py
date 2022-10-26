# coding: utf-8
import discord 
from discord import app_commands

class MyClient(discord.Client):
    def __init__(self, user_id, kslife):
        intents = discord.Intents.all()
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self) #全てのコマンドを管理するCommandTree型オブジェクトを生成
        self.user_id = user_id
        self.kslife = kslife

    #ボットをセットアップするdiscord.Clientが持つ空のメソッド、オーバーライドすることでログイン時にon_ready()より精密に実行する
    async def setup_hook(self):
        self.channel = await self.create_dm(await self.fetch_user(self.user_id))
        await self.channel.send(content="kslifeアクセスチェック中・・・")
        #kslifeアクセスを試みる(失敗したらexitする)
        await self.kslife.testing_access(self.channel)
        await self.channel.send(content="botを起動しました。")
    
    #helpコマンドでヘルプを参照するためのメソッド
    def help_embed(self) -> discord.Embed:
        embed = discord.Embed(title="Embedのタイトル",description="Embedの概要")
        return embed
    
    #メッセージ送信で処理するメソッド、基本的にここで処理をする
    async def on_message(self, msg):
        if msg.content.startswith('!'):
            if msg.content.startswith('!help'):
                await self.channel.send(content="helpを参照します。", embed=self.help_embed())
            
            elif msg.content.startswith('!stop'):
                await self.channel.send(content="See you next again")
                self.kslife.exit_chrome()
                await self.close()

            else:
                await self.channel.send(content="コマンドが異なります。\"!help\"で参照してください。")
        else:
            return
