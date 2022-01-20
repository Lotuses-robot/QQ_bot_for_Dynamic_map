from os import path

import nonebot
import bot_config


nonebot.init(bot_config)

nonebot.load_plugins(path.join(path.dirname(__file__), 'bot_plugins'), 'bot_plugins')

if __name__ == '__main__':
    nonebot.run()
