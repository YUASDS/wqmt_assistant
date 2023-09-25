from utils.functions import *
import wqmt as wq
import pywebio as pw
import utils.log as log
import utils.adb as adb

if __name__ == "__main__":
    adb.connect()
    pw.output.put_text("请提前在Config.yaml中配置好mumu的ip地址和端口")
    pw.output.put_text("建议按照12小时间隔，早晚各一次。晚上执行的时候请在17点之后，以便领取体力")

    options = ["早一次", "晚一次", "自选", "单刷肉鸽"]
    selected_options = pw.input.actions("嗯……", options)
    if cfg.log_switch == "close":
        pw.output.put_text(f"config.yaml中已经关闭日志输出，之后本窗口可以关闭")
    if "早一次" in selected_options:
        wq.morning()
        log.logit(f"完成所有任务").text()
    if "晚一次" in selected_options:
        wq.night()
        log.logit(f"完成所有任务").text()
    if "自选" in selected_options:
        log.logit(f"打开自选界面").text()
        agree = wq.select_jobs()
        if "启动" in agree:
            wq.starttohome()
        if "签到" in agree:
            wq.dailycheckin()
        if "公会" in agree:
            wq.guild()
        if "邮件" in agree:
            wq.getmail()
        if "采购中心-每日免费体力" in agree:
            wq.purchase()
        if "基建收菜" in agree:
            wq.construction()
        if "管理局" in agree:
            wq.Bureau()
        if "好友" in agree:
            wq.friends()
        if "监察密令" in agree:
            wq.supervision()
        if "副本-锈河记忆" in agree:
            wq.raidriver()
        if "副本-11-6" in agree:
            wq.raid11()
        if "副本-深井" in agree:
            wq.raiddark()
        log.logit("完成所有任务").text()
    if "单刷肉鸽" in selected_options:
        wq.starttohome()
        wq.rouge()
