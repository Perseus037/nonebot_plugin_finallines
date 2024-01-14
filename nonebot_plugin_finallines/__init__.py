import random
import json
import os

from nonebot import on_command, require
from nonebot.adapters import Bot, Event
from nonebot.plugin import PluginMetadata, inherit_supported_adapters

require("nonebot_plugin_saa")

from nonebot_plugin_saa import MessageFactory, Text
from nonebot_plugin_saa import __plugin_meta__ as saa_plugin_meta

require("nonebot_plugin_userinfo")

from nonebot_plugin_userinfo import UserInfo, EventUserInfo 

supported_adapters_finallines = inherit_supported_adapters("nonebot_plugin_saa", "nonebot_plugin_userinfo")

__version__ = "0.1.1.post2"
__plugin_meta__ = PluginMetadata(
    name="最终台词",
    description="来一句劲道的最终台词吧,支持多平台适配",
    usage="使用命令：最终台词",
    homepage="https://github.com/Perseus037/nonebot_plugin_finallines",
    type="application",
    config=None,
    supported_adapters=supported_adapters_finallines,
)

# 读取json文件
def load_final_lines():
    current_file_path = os.path.abspath(__file__)
    current_dir = os.path.dirname(current_file_path)

    final_lines_path = os.path.join(current_dir, 'final_lines.json')

    with open(final_lines_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data["final_words"]

final_words = load_final_lines()

final_words_cmd = on_command("最终台词", priority=1)

@final_words_cmd.handle()
async def handle(user_info: UserInfo = EventUserInfo()):
    nickname = user_info.user_name if user_info.user_name else "你"
    final_word = random.choice(final_words)
    reply = f"{nickname}的最终台词是：{final_word}" 

    message_builder = MessageFactory([Text(reply)])
    await message_builder.send()
