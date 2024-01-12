<div align="center"> 
  
  <img src="https://github.com/Perseus037/data/blob/master/king%20power.png?raw=true" alt="我的王之力啊！" width="280" height="280">

# nonebot-plugin-finallines


_✨一个发送劲道的最终台词的nonebot2插件✨_

<img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="python">
<a href="https://pdm.fming.dev">
  <img src="https://img.shields.io/badge/pdm-managed-blueviolet" alt="pdm-managed">
</a>
<!-- <a href="https://wakatime.com/badge/user/b61b0f9a-f40b-4c82-bc51-0a75c67bfccf/project/f4778875-45a4-4688-8e1b-b8c844440abb">
  <img src="https://wakatime.com/badge/user/b61b0f9a-f40b-4c82-bc51-0a75c67bfccf/project/f4778875-45a4-4688-8e1b-b8c844440abb.svg" alt="wakatime">
</a> -->

<br />

<a href="./LICENSE">
  <img src="https://img.shields.io/github/license/lgc-NB2Dev/nonebot-plugin-uma.svg" alt="license">
</a>
<a href="https://pypi.python.org/pypi/nonebot-plugin-finallines">
  <img src="https://img.shields.io/pypi/v/nonebot-plugin-finallines.svg" alt="pypi">
</a>
<a href="https://pypi.org/project/nonebot-plugin-finallines/">
  <img src="https://img.shields.io/pypi/dm/nonebot-plugin-finallines.svg" alt="pypi download">
</a>


</div>

## 💬 前言

我的王之力啊！！！

## 📖 介绍

一个简单有趣的的nonebot2插件，输入指令后会回复一句劲道的最终台词，大部分出自或致敬游戏，动漫，小说的知名作品，小部分是自己编着玩的。

前置插件：nonebot_plugin_saa,nonebot_plugin_userinfo,使用前请确认这两个插件已经正确安装并成功加载。

使用nonebot_plugin_saa于nonebot_plugin_userinfo实现多适配器支持，支持的适配器：~onebot.v11, ~onebot.v12, ~QQ Guild,  WeChat, ~Kaiheila, Telegram, Feishu, Red

灵感来源：https://cn.shindanmaker.com/1191352 

玩的开心w

## 💿 安装

<!--
<details open>
<summary>[推荐] 使用 nb-cli 安装</summary>
在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装

```bash
nb plugin install nonebot-plugin-finallines
```
-->

</details>

<details open>
<summary>使用包管理器安装</summary>
在 nonebot2 项目的插件目录下, 打开命令行, 根据你使用的包管理器, 输入相应的安装命令

<details open>
<summary>pip</summary>

```bash
pip install nonebot-plugin-finallines
```

</details>
<details>
<summary>pdm</summary>

```bash
pdm add nonebot-plugin-finallines
```

</details>
<details>
<summary>poetry</summary>

```bash
poetry add nonebot-plugin-finallines
```

</details>
<details>
<summary>conda</summary>

```bash
conda install nonebot-plugin-longtu
```

</details>

打开 nonebot2 项目根目录下的 `pyproject.toml` 文件, 在 `[tool.nonebot]` 部分的 `plugins` 项里追加写入

```toml
[tool.nonebot]
plugins = [
    # ...
    "nonebot_plugin_finallines"
]
```

</details>

## ⚙️ 配置

暂无

## 🎉 使用

现有指令列表：

最终台词：向发送指令的人回应一句属于你的最终台词


## 📞 制作者

### 黑纸折扇 [Perseus037] (https://github.com/Perseus037)

- QQ: 1209228678

## 🙏 感谢

-  [linky233] 的idea
-  [student_2333](https://github.com/lgc2333) 的无私帮助
-  [nonebot-plugin-send-anything-anywhere](https://github.com/MountainDash/nonebot-plugin-send-anything-anywhere) 处理不同 adapter 消息的适配和发送
-  [nonebot-plugin-userinfo](https://github.com/noneplugin/nonebot-plugin-userinfo) 实现不同 adpter 获取用户信息

## 📝 更新日志
### 0.1.0.post2

- 实现多适配器支持

### 0.1.0.post1

- 增加了50余条台词加入语料库
