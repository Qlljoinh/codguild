import disnake
from disnake.ext import commands
import json

class LanguageCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.user_languages = self.load_languages()  # Загрузка языковых настроек из файла

    def load_languages(self):
        try:
            with open("user_languages.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_languages(self):
        with open("user_languages.json", "w") as file:
            json.dump(self.user_languages, file)

    @commands.slash_command(name="setlang", description="Изменить язык интерфейса бота для себя")
    async def setlang(self, inter: disnake.ApplicationCommandInteraction, language: str = commands.Param(choices=["Russian", "English"])):
        if language.lower() not in ["english", "russian"]:
            await inter.response.send_message("Доступные языки: English, Russian", delete_after = 15)
            return

        self.user_languages[str(inter.author.id)] = language.lower()
        self.save_languages()  # Сохранение языковых настроек в файл
        await inter.response.send_message(f"Язык интерфейса изменен на {language.capitalize()}")

    @commands.Cog.listener()
    async def on_slash_command_error(self, inter: disnake.ApplicationCommandInteraction, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await inter.response.send_message("Пожалуйста, укажите язык.", delete_after = 10)

    def get_user_language(self, user_id):
        return self.user_languages.get(str(user_id), "english")

def setup(bot):
    bot.add_cog(LanguageCog(bot))