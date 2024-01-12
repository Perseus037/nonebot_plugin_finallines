import random
import json
import os

from nonebot import on_command
from nonebot.adapters.onebot.v11 import Bot, Event
from nonebot.plugin import PluginMetadata

__version__ = "0.1.0.post1"
__plugin_meta__ = PluginMetadata(
    name="最终台词",
    description="来一句劲道的最终台词吧",
    usage="使用命令：最终台词",
    homepage="https://github.com/Perseus037/nonebot_plugin_finallines",
    type="application",
    config=None,
    supported_adapters={"~onebot.v11"},
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
async def handle_first_receive(bot: Bot, event: Event):
    user_id = int(event.get_user_id())
    user_info = await bot.get_stranger_info(user_id=user_id)
    nickname = user_info.get("nickname", "你")

    # 从台词列表中随机选择一句并发送
    final_word = random.choice(final_words)
    reply = f"{nickname}的最终台词是：{final_word}"

    await final_words_cmd.finish(reply)
