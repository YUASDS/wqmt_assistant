from utils.functions import *
import wqmt as wq
from pywebio.input import actions as pw_actions
import utils.log as log

if __name__ == '__main__':
    [log.logit(" ") for i in range(5)]
    adb_connect()
    [log.logit(" ") for i in range(2)]
    log.logit("请提前在Config.yaml中配置好mumu的ip地址和端口")
    log.logit("建议按照12小时间隔，早晚各一次。晚上执行的时候请在17点之后，以便领取体力")

    options = ['早一次', '晚一次', '自选']
    log.logit("打开options界面")
    selected_options = pw_actions("嗯……", options)
    if "早一次" in selected_options:
        wq.morning()
        log.logit("完成所有任务")
    if "晚一次" in selected_options:
        wq.night()
        log.logit("完成所有任务")
    if "自选" in selected_options:
        log.logit("打开自选界面")
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
        if "副本-锈河记忆" in agree:
            wq.raidriver()
        if "副本-11-6" in agree:
            wq.raid11()
        if "副本-深井" in agree:
            wq.raiddark()
        log.logit("完成所有任务")
