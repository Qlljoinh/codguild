import disnake
from disnake.ext import commands
import os

class TalentsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="talent", description="find the talent for the hero")
    async def talents(self, inter: disnake.ApplicationCommandInteraction, hero: str = commands.Param(choices=["liliya", "velyn", "kinnara", "madelin", "garwood", "niko", "emrys", "bakshi", "thea", "waldir", "kregg", "nika", "indis", "atey", "guangyin", "bahar", "aluin", "eliana", "alistar", "nernin", "tarra", "kella", "ordo", "teodor", "freygar"])):
                # Проверка, что команда вызвана в правильном канале
        allowed_channel_id = 1316108781209522206  # ID канала, где разрешено использовать команду
        if inter.channel.id != allowed_channel_id:
            await inter.response.send_message(f"This command allowed only in <#{allowed_channel_id}>.", ephemeral=True)
            return
        # Получаем язык пользователя
        language_cog = self.bot.get_cog("LanguageCog")
        if language_cog is None:
            await inter.response.send_message("LanguageCog не загружен.")
            return

        user_language = language_cog.get_user_language(inter.author.id)

        # Путь к файлу с сообщением
        message_path = os.path.abspath(os.path.join("resources", "message", "talent", f"{hero}_{user_language}.txt"))
        # Путь к изображению
        image_path = os.path.abspath(os.path.join("resources", "img", "talent", f"{hero}.txt"))

        # Проверка наличия файла с сообщением
        if not os.path.exists(message_path):
            await inter.response.send_message(f"Файл с сообщением для {hero} на языке {user_language} не найден. Путь: {message_path}")
            return

        # Проверка наличия изображения
        if not os.path.exists(image_path):
            await inter.response.send_message(f"Изображение для {hero} не найдено. Путь: {image_path}")
            return

        # Чтение содержимого файла с сообщением
        with open(message_path, "r", encoding="utf-8") as file:
            message_content = file.read()

        # Создание Embed
        embed = disnake.Embed(title=f"Talant for: {hero}", description=message_content, color=disnake.Color.blue())
        with open(image_path, "r", encoding="utf-8") as file:
            image_link = file.read()
        embed.set_image(url = image_link) # * доделал функцию для изображений. Теперь это просто гиперссылки на изображения в облаках discord.
        
        # Отправка Embed с изображением
        await inter.response.send_message(embed=embed, delete_after = 1*30*60)

def setup(bot):
    bot.add_cog(TalentsCog(bot))