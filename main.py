from utils.functions import *
import wqmt as wq
import pywebio as pw
import utils.log as log
import utils.adb as adb


def start_options():
    while True:
        button_clicked = pw.input.actions("请选择操作", ["直接开始", "配置"])

        if button_clicked == "配置":
            wq.select_sever()
            jobs = wq.select_jobs()
            fight = wq.select_fights()
            last_action = wq.select_last_action()

        elif button_clicked == "直接开始":
            jobs = cfg.config["saved_selections"]
            fight = cfg.config["fights"]
            last_action = cfg.config["last_action"]

        if "启动" in jobs:
            wq.starttohome()
        if "签到" in jobs:
            wq.dailycheckin()
        if "公会" in jobs:
            wq.guild()
        if "邮件" in jobs:
            wq.getmail()
        if "采购中心-每日免费体力" in jobs:
            wq.purchase()
        if "基建收菜" in jobs:
            wq.construction()
        if "管理局" in jobs:
            wq.Bureau()
        if "好友" in jobs:
            wq.friends()
        if "副本-锈河记忆" in jobs:
            wq.raidriver("storm")
        if "副本-深井" in jobs:
            wq.raiddark()
        if "无" not in jobs:
            if "副本-11-6" in fight:
                wq.raid11()
            if "狄斯币" in fight:
                wq.raidriver("gold")
            if "狂厄结晶" in fight:
                wq.raidriver("crystal")
        if "监察密令" in jobs:
            wq.supervision()
        if "肉鸽" in jobs:
            wq.rouge()
        log.logit("完成所有任务").text()
        if "退出无期迷途" in last_action:
            wq.wqmtclose()
            log.logit("退出完成").text()


if __name__ == "__main__":
    adb.connect()
    pw.output.put_text("建议按照12小时间隔，早晚各一次。晚上执行的时候请在17点之后，以便领取体力")
    # pw.input.
    if cfg.log_switch == "close":
        pw.output.put_text("config.yaml中已经关闭日志输出，之后本窗口可以关闭")

    start_options()
