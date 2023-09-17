
![img](https://github.com/walklty/wqmt_assistant/blob/dev/Target/Snipaste_2023-09-09_05-17-32.png?raw=true)


# 主要更新内容

📅202309xx 我跟ChatGPT说，你看人家代码都有个class什么的，你也这样给我改改。

改了一些寻找图片的循环逻辑，增加了一些图像识别步骤。

重写了log的逻辑，固定了一个滚动窗口输出内容，重点内容会有单独的提示。

增加了监察密令的每日领取

📅20230909 增加了肉鸽刷界石的步骤。进去退出来竟然有20界石……个人感觉有点bug

请在游戏主界面启动。请先通关一次。

使用这个功能前建议在config.yaml中把 log_switch: close


# 前言

## 废话
![author](https://img.shields.io/badge/author-ChatGPT3.5-blue)

本项目由ChatGPT 3.5编写，Codeium复审代码，用于无期迷途每日收菜

程序完全自用，只在MUMU12上使用，只在720P下开发，本人啥也不懂，有问题问AI。

为了减少报错，程序相当低效和冗余，有问题问AI。

## 介绍

程序使用Python语言，PyWebIO提供简单的选项和log查看， OpenCV识别图像。

功能包括：

- 从登录界面进入主界面，干掉活动提示、工会战提示、月卡到期提示

- 收取邮件，公会捐赠，采购部免费日礼包，戳好友

- 管理局派遣，领取中午晚上的体力

- 扫荡锈河记忆副本第一个

- 扫荡副本11-6， 扫荡深井

缺点包括：

- 我是个躺平的闲鱼，不缺材料，因此没有换副本刷不同材料的需求

- 自用方式为每天早晚点一次，因此不考虑特殊情况比如明明没有体力你却让软件去刷11-6这种

# 使用方法

## 方法1 - Python

安装相关依赖

```
pip install -r requirements.txt
```

先打开模拟器，然后如下启动程序

```
start.bat
```

## 方法2

先打开模拟器，然后双击main.exe

# 挖坑

- [x] 面板展开检测 -- 避免因为面板折叠找不到好友菜单在哪

- [x] 限制log小数点

- [x] APP启动检测 : 现在程序会先检查wqmt启动没有，如果没有则会启动

- [x] 副本界面检查（切换副本第一页、第二页界面）

- [ ] 多个副本供选择（什么时候我有刷其他本的动力了）

- [x] 自带ADB

- [x] OCR识别 -- 实装了，但是没有任何地方用得到，所以没有把识别程序放进去，那玩意体积200多MB呢

- [ ] 兑换采购部商品（手动触发）

- [x] 默认随机xy & 随机延迟 -- 会在一个15X15的范围内以正态分布的方式随机生成点击位置

- [ ] 活动大厅收菜

- [ ] 副本后的升级检测

- [x] 加入log功能 -- 会记录到log文件夹下，间隔7天删除

