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
        self.kslife.set_channel(self.channel)
        await self.channel.send(content="kslifeアクセスチェック中・・・")
        #kslifeアクセスを試みる(失敗したらexitする)
        await self.kslife.testing_access()
        await self.channel.send(content="botを起動しました。")
    
    #helpコマンドでヘルプを参照するためのメソッド
    def help_embed(self) -> discord.Embed:
        embed = discord.Embed(
            title="kslife攻略コマンド",
            description="コマンド一覧を参照します。",
            color=0x00ff00,
            url="https://github.com/nekoy3/kslife-cheats"
        )
        embed.add_field(name="!help", value="このヘルプを表示します。")
        embed.add_field(name="!stop", value="botを停止します。")
        embed.set_footer(text="made by nekoy3")
        return embed

    #コマンドラインを受け取って取得する個数を取得する
    def get_count(self, args) -> int:
        if len(args) > 2:
            try:
                if 1 <= int(args[2]) <= 30:
                    return int(args[2])
                else:
                    return 10
            except ValueError:
                return 10
        else:
            return 10
    
    #メッセージ送信で処理するメソッド、基本的にここで処理をする
    async def on_message(self, msg):
        if msg.content.startswith('!'):
            #ヘルプコマンドの処理
            if msg.content.startswith('!help'):
                await self.channel.send(content="helpを参照します。", embed=self.help_embed())
            
            #停止コマンドの処理
            elif msg.content.startswith('!stop'):
                await self.channel.send(content="See you next again")
                self.kslife.exit_chrome()
                await self.close()
            
            #情報取得コマンドの処理
            elif msg.content.startswith('!get'):
                msg_args = msg.content.split(" ")
                ermsg = "[!get] 引数\nml : 授業連絡を早い順10件取得します。\nak : 授業アンケートを早い順10件取得します。\n第二引数絵個数を1~30で取得できます。"
                try:
                    msg_args[1]
                except IndexError:
                    await self.channel.send(content=ermsg)
                
                #引数の値個の情報を取得する->c個
                c = self.get_count(msg_args)
                
                if msg_args[1] == "ml":
                    pass
                elif msg_args[1] == "ak":
                    pass
                else:
                    await self.channel.send(content=ermsg)
                    return

            else:
                await self.channel.send(content="コマンドが異なります。\"!help\"で参照してください。")
        else:
            return
