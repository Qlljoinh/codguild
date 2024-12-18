import disnake
from disnake.ext import commands
import os

class TowerHallCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="tower_hall", description="see the conditions for raising the town hall")
    async def talents(self, inter: disnake.ApplicationCommandInteraction):
                # Проверка, что команда вызвана в правильном канале
        allowed_channel_id = 1316108781209522206  # ID канала, где разрешено использовать команду
        if inter.channel.id != allowed_channel_id:
            await inter.response.send_message(f"This command allowed only in <#{allowed_channel_id}>.", ephemeral=True)
            return
        # Получаем язык пользователя
        language_cog = self.bot.get_cog("LanguageCog")
        if language_cog is None:
            await inter.response.send_message("LanguageCog not loaded...")
            return

        user_language = language_cog.get_user_language(inter.author.id)

        # Путь к файлу с сообщением
        message_path = os.path.abspath(os.path.join("resources", "message", "tower", f"tower_{user_language}.txt"))


        # Проверка наличия файла с сообщением
        if not os.path.exists(message_path):
            await inter.response.send_message(f"Файл с сообщением для tower на языке {user_language} не найден. Путь: {message_path}")
            return


        # Чтение содержимого файла с сообщением
        with open(message_path, "r", encoding="utf-8") as file:
            message_content = file.read()

        # Создание Embed
        embed = disnake.Embed(title=f"Info about Tower Hall", description=message_content, color=disnake.Color.blue())

        
        await inter.response.send_message(embed=embed, delete_after = 1*30*60)

def setup(bot):
    bot.add_cog(TowerHallCog(bot))