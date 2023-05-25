
from create_bot import dp
from aiogram.utils import executor
from handlers import user, commands

commands.register_commands(dp)
user.register_user(dp)
executor.start_polling(dp, skip_updates=True)