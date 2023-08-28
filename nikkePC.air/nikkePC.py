# -*- encoding=utf8 -*-
__author__ = "25026"

from airtest.core.api import *
import time
import random

auto_setup(__file__,devices=["Windows:///?title_re=NIKKE.*"])

buff_num=0

def outpost():
    pos=wait(Template(r"tpl1676694430396.png", record_pos=(-0.215, 0.103), resolution=(1349, 759)))
    touch((pos[0]+50,pos[1]+100))
    time.sleep(1)
    touch(Template(r"tpl1676695148158.png", record_pos=(0.063, 0.187), resolution=(1349, 759)))
    wait(Template(r"tpl1676694098706.png", record_pos=(-0.001, -0.094), resolution=(1349, 759)))
    time.sleep(2)
    try:
        touch(Template(r"tpl1676694106295.png", record_pos=(-0.0, 0.089), resolution=(1349, 759)))
        time.sleep(2)
        touch(Template(r"tpl1676694106295.png", record_pos=(-0.0, 0.089), resolution=(1349, 759)))
    except:
        print("go on")
    pos=wait(Template(r"tpl1676694430396.png", record_pos=(-0.215, 0.103), resolution=(1349, 759)))
    touch((pos[0]+50,pos[1]+100))
    time.sleep(1)
    touch(Template(r"tpl1676695298773.png", record_pos=(-0.062, 0.187), resolution=(1349, 759)))
    time.sleep(1)
    touch(Template(r"tpl1676695327384.png", record_pos=(0.047, 0.143), resolution=(1349, 759)))
    time.sleep(1)
    touch(Template(r"tpl1676695367359.png", record_pos=(-0.0, 0.09), resolution=(1349, 759)))
    time.sleep(1)
    touch(Template(r"tpl1676695389681.png", record_pos=(-0.077, 0.142), resolution=(1349, 759)))
    time.sleep(1)
    touch(Template(r"tpl1676695413310.png", record_pos=(0.126, -0.201), resolution=(1349, 759)))

def daily_shop():
    wait(Template(r"tpl1676695610324.png", record_pos=(-0.218, 0.103), resolution=(1349, 759)))
    touch(Template(r"tpl1676695610324.png", record_pos=(-0.218, 0.103), resolution=(1349, 759)))
    time.sleep(3)
    pos=exists(Template(r"tpl1676696675871.png", record_pos=(-0.379, -0.026), resolution=(1351, 760)))
    touch((pos[0]+25,pos[1]+100))
    time.sleep(1)
    touch(Template(r"tpl1676696880629.png", record_pos=(0.048, 0.195), resolution=(1350, 760)))
    time.sleep(2)
    touch(Template(r"tpl1676696913124.png", record_pos=(0.001, 0.09), resolution=(1350, 760)))
    time.sleep(1)
    touch(Template(r"tpl1676696944784.png", record_pos=(-0.478, 0.073), resolution=(1351, 760)))
    time.sleep(1)
    pos=exists(Template(r"tpl1676696675871.png", record_pos=(-0.379, -0.026), resolution=(1351, 760)))
    touch((pos[0]+30,pos[1]+100))
    time.sleep(1)
    touch(Template(r"tpl1676697133602.png", record_pos=(0.044, 0.183), resolution=(1351, 760)))
    time.sleep(2)
    touch(Template(r"tpl1676696913124.png", record_pos=(0.001, 0.09), resolution=(1350, 760)))
    time.sleep(2)
    touch((pos[0]+125,pos[1]+100))
    time.sleep(1)
    touch(Template(r"tpl1676697133602.png", record_pos=(0.044, 0.183), resolution=(1351, 760)))
    time.sleep(2)
    touch(Template(r"tpl1676696913124.png", record_pos=(0.001, 0.09), resolution=(1350, 760)))
    time.sleep(2)
    touch((pos[0]+240,pos[1]+100))
    time.sleep(1)
    touch(Template(r"tpl1676697133602.png", record_pos=(0.044, 0.183), resolution=(1351, 760)))
    time.sleep(2)
    touch(Template(r"tpl1676696913124.png", record_pos=(0.001, 0.09), resolution=(1350, 760)))
    time.sleep(2)
    touch(Template(r"tpl1676697190399.png", record_pos=(-0.413, 0.249), resolution=(1351, 760)))

def email():
    wait(Template(r"tpl1676697278788.png", record_pos=(-0.216, 0.104), resolution=(1351, 760)))
    touch(Template(r"tpl1676697289666.png", record_pos=(0.459, -0.263), resolution=(1351, 760)))
    time.sleep(2)
    touch(Template(r"tpl1676697310541.png", record_pos=(0.071, 0.195), resolution=(1351, 760)))
    time.sleep(3)
    touch(Template(r"tpl1676696913124.png", record_pos=(0.001, 0.09), resolution=(1350, 760)))
    time.sleep(2)
    touch(Template(r"tpl1676697338309.png", record_pos=(0.123, -0.207), resolution=(1351, 760)))

def friendship():
    wait(Template(r"tpl1676697416503.png", record_pos=(-0.215, 0.104), resolution=(1351, 760)))
    touch(Template(r"tpl1676697435984.png", record_pos=(0.473, -0.142), resolution=(1351, 760)))
    time.sleep(5)
    touch(Template(r"tpl1676697467823.png", record_pos=(0.083, 0.195), resolution=(1351, 760)))
    time.sleep(1)
    touch(Template(r"tpl1676697508039.png", record_pos=(0.008, 0.07), resolution=(1351, 760)))
    time.sleep(1)
    touch(Template(r"tpl1676697521844.png", record_pos=(0.124, -0.212), resolution=(1351, 760)))

def daily_exploration():
    wait(Template(r"tpl1676697573430.png", record_pos=(-0.217, 0.104), resolution=(1351, 760)))
    touch(Template(r"tpl1676697595612.png", record_pos=(-0.202, 0.152), resolution=(1351, 760)))
    time.sleep(10)
    touch(Template(r"tpl1676697639058.png", record_pos=(0.023, 0.255), resolution=(1351, 760)))
    time.sleep(2)
    touch(Template(r"tpl1676697686675.png", record_pos=(0.088, 0.19), resolution=(1351, 760)))
    time.sleep(2)
    touch(Template(r"tpl1676697727753.png", record_pos=(0.0, 0.09), resolution=(1351, 760)))
    time.sleep(1)
    touch(Template(r"tpl1676697750647.png", record_pos=(0.13, -0.207), resolution=(1351, 760)))
    time.sleep(3)
    touch(Template(r"tpl1676697770311.png", record_pos=(0.022, 0.253), resolution=(1351, 760)))
    time.sleep(2)
    touch(Template(r"tpl1676697798275.png", record_pos=(-0.0, 0.19), resolution=(1351, 760)))
    time.sleep(1)
    touch(Template(r"tpl1676697821280.png", record_pos=(0.037, 0.192), resolution=(1351, 760)))
    time.sleep(1)
    touch(Template(r"tpl1676697868456.png", record_pos=(0.13, -0.206), resolution=(1351, 760)))
    time.sleep(3)
    touch(Template(r"tpl1676697884861.png", record_pos=(-0.414, 0.249), resolution=(1351, 760)))
    time.sleep(5)

def daily_tower():
    wait(Template(r"tpl1676698007008.png", record_pos=(-0.216, 0.103), resolution=(1351, 760)))
    touch(Template(r"tpl1676698017827.png", record_pos=(0.199, 0.097), resolution=(1351, 760)))
    time.sleep(3)
    touch(Template(r"tpl1676698056540.png", record_pos=(0.094, -0.095), resolution=(1351, 760)))
    time.sleep(2)
    touch(Template(r"tpl1676698094906.png", record_pos=(0.092, -0.051), resolution=(1351, 760)))
    time.sleep(2)
    pos=exists(Template(r"tpl1676698538658.png", record_pos=(0.006, -0.261), resolution=(1351, 760)))
    touch((pos[0],pos[1]+300))
    time.sleep(2)
    touch(Template(r"tpl1676698234345.png", record_pos=(0.091, 0.249), resolution=(1336, 760)))
    time.sleep(10)
    touch(Template(r"tpl1676698754093.png", record_pos=(0.485, -0.264), resolution=(1351, 760)))
    time.sleep(1)
    touch(Template(r"tpl1676698346100.png", record_pos=(-0.065, 0.236), resolution=(1351, 760)))
    time.sleep(3)
    touch(Template(r"tpl1676698371751.png", record_pos=(-0.456, 0.241), resolution=(1351, 760)))
    time.sleep(10)
    touch(Template(r"tpl1676698413078.png", record_pos=(-0.414, 0.249), resolution=(1351, 760)))
    time.sleep(3)

def daily_jjc():
    wait(Template(r"tpl1676698007008.png", record_pos=(-0.216, 0.103), resolution=(1351, 760)))
    touch(Template(r"tpl1676698017827.png", record_pos=(0.199, 0.097), resolution=(1351, 760)))        
    time.sleep(2)
    touch(Template(r"tpl1676699010565.png", record_pos=(0.075, 0.064), resolution=(1351, 760)),times=3)
    time.sleep(3)
    touch(Template(r"tpl1676699034767.png", record_pos=(-0.107, 0.021), resolution=(1351, 760)),times=3)
    time.sleep(2)
    for i in range(3):
        touch(Template(r"tpl1681439457236.png", record_pos=(0.102, 0.026), resolution=(1333, 750)))
        time.sleep(2)
        touch(Template(r"tpl1676699251714.png", record_pos=(-0.001, 0.178), resolution=(1351, 760)),times=3)
        wait(Template(r"tpl1676699288948.png", record_pos=(-0.002, 0.135), resolution=(1351, 760)),timeout=60)
        touch((1000,300),times=5)
        time.sleep(5)
    touch(Template(r"tpl1676699686196.png", record_pos=(-0.413, 0.25), resolution=(1351, 760)))
    time.sleep(8)

nikke_dictionary={
    '拉普拉斯': Template(r"tpl1676701278570.png", record_pos=(-0.206, -0.086), resolution=(1351, 760)),
    '尼夫': Template(r"tpl1676701399310.png", record_pos=(0.091, -0.087), resolution=(1351, 760)),
    '麦斯威尔': Template(r"tpl1676701426962.png", record_pos=(0.39, -0.087), resolution=(1351, 760)),
    '舒格': Template(r"tpl1676701966550.png", record_pos=(-0.211, -0.023), resolution=(1351, 760)),
    '普琳玛': Template(r"tpl1676702014593.png", record_pos=(0.089, -0.022), resolution=(1351, 760)),
    '丽塔': Template(r"tpl1676702057744.png", record_pos=(0.388, -0.021), resolution=(1351, 760)),
    '伊莎贝尔': Template(r"tpl1676702081004.png", record_pos=(-0.208, 0.041), resolution=(1351, 760)),
    '西格娜': Template(r"tpl1676702112713.png", record_pos=(0.088, 0.042), resolution=(1351, 760)),
    '波莉': Template(r"tpl1676702145696.png", record_pos=(0.388, -0.053), resolution=(1351, 760)),
    '米兰达': Template(r"tpl1676702180722.png", record_pos=(-0.211, 0.011), resolution=(1351, 760)),
    '迪赛尔': Template(r"tpl1676702203191.png", record_pos=(0.089, 0.011), resolution=(1351, 760)),
    '克拉乌': Template(r"tpl1676702233524.png", record_pos=(0.39, 0.011), resolution=(1351, 760)),
    '梅里': Template(r"tpl1676702257614.png", record_pos=(-0.21, 0.076), resolution=(1351, 760)),
    '佩珀': Template(r"tpl1676702318573.png", record_pos=(0.088, 0.076), resolution=(1351, 760)),
    '米尔克': Template(r"tpl1676702348226.png", record_pos=(0.39, 0.033), resolution=(1351, 760)),
    '尤尔夏': Template(r"tpl1676702382331.png", record_pos=(-0.209, 0.098), resolution=(1351, 760)),
    '艾德米': Template(r"tpl1676702410016.png", record_pos=(0.091, 0.098), resolution=(1351, 760)),
    '吉萝婷': Template(r"tpl1676702454832.png", record_pos=(0.392, -0.015), resolution=(1351, 760)),
    '梅登': Template(r"tpl1676702476583.png", record_pos=(-0.208, 0.048), resolution=(1351, 760)),
    '鲁德米拉': Template(r"tpl1676702503936.png", record_pos=(0.091, 0.05), resolution=(1351, 760)),
    '杨': Template(r"tpl1676702525661.png", record_pos=(0.387, 0.05), resolution=(1351, 760)),
    '朵拉': Template(r"tpl1676702547231.png", record_pos=(-0.208, 0.113), resolution=(1351, 760)),
    '长发公主': Template(r"tpl1676702569785.png", record_pos=(0.088, 0.113), resolution=(1351, 760)),
    '诺雅': Template(r"tpl1676702590384.png", record_pos=(0.388, 0.058), resolution=(1351, 760)),
    '神罚': Template(r"tpl1676702620682.png", record_pos=(-0.208, 0.123), resolution=(1351, 760)),
    '索达': Template(r"tpl1676702660317.png", record_pos=(0.09, 0.124), resolution=(1351, 760)),
    '诺伊斯': Template(r"tpl1676702689134.png", record_pos=(0.39, 0.052), resolution=(1351, 760)),
    '沃伦姆': Template(r"tpl1676702720791.png", record_pos=(-0.205, 0.116), resolution=(1351, 760)),
    '圣诞露菲': Template(r"tpl1676702750915.png", record_pos=(0.091, 0.117), resolution=(1351, 760)),
    '拉毗': Template(r"tpl1676702785089.png", record_pos=(0.39, -0.032), resolution=(1351, 760)),
    '尼恩': Template(r"tpl1676702996943.png", record_pos=(-0.214, -0.069), resolution=(1351, 760)),

    '德尔塔': Template(r"tpl1676703008886.png", record_pos=(0.094, -0.07), resolution=(1351, 760)),

    '阿妮斯': Template(r"tpl1676703018992.png", record_pos=(0.386, -0.069), resolution=(1351, 760)),

    '米哈拉': Template(r"tpl1676703026984.png", record_pos=(-0.21, -0.005), resolution=(1351, 760)),

    '贝洛塔': Template(r"tpl1676703042675.png", record_pos=(0.091, -0.004), resolution=(1351, 760)),

    '米卡': Template(r"tpl1676703051300.png", record_pos=(0.387, -0.004), resolution=(1351, 760)),

    'N102': Template(r"tpl1676703059882.png", record_pos=(-0.209, 0.059), resolution=(1351, 760)),

    '艾瑟尔': Template(r"tpl1676703068847.png", record_pos=(0.089, 0.059), resolution=(1351, 760)),

    '艾可希雅': Template(r"tpl1676703077672.png", record_pos=(0.39, 0.06), resolution=(1351, 760)),

    '爱丽丝': Template(r"tpl1676703091206.png", record_pos=(-0.208, 0.124), resolution=(1351, 760)),

    '艾玛': Template(r"tpl1676703099124.png", record_pos=(0.091, 0.124), resolution=(1351, 760)),

    '普丽瓦蒂': Template(r"tpl1676703118487.png", record_pos=(0.393, 0.025), resolution=(1351, 760)),

    '尤莉亚': Template(r"tpl1676703125631.png", record_pos=(-0.208, 0.09), resolution=(1351, 760)),

    '布丽德': Template(r"tpl1676703132049.png", record_pos=(0.091, 0.091), resolution=(1351, 760)),

    '德雷克': Template(r"tpl1676703141676.png", record_pos=(0.389, 0.09), resolution=(1351, 760)),

    '艾菲涅尔': Template(r"tpl1676703150798.png", record_pos=(-0.204, 0.154), resolution=(1351, 760)),

    '红莲': Template(r"tpl1676703157335.png", record_pos=(0.092, 0.155), resolution=(1351, 760)),

    '阿莉亚': Template(r"tpl1676703167803.png", record_pos=(0.39, 0.154), resolution=(1351, 760)),
    '桑迪': Template(r"tpl1678148218237.png", record_pos=(-0.229, 0.177), resolution=(1353, 790)),
    '玛奇玛': Template(r"tpl1678148285038.png", record_pos=(-0.236, 0.075), resolution=(1342, 790)),
    '帕瓦': Template(r"tpl1678148354009.png", record_pos=(0.075, 0.075), resolution=(1342, 790))
}

def zixun(pos):
    try:
        wait(pos,timeout=5)
    except:
        swipe((700,500),(700,300))
        if zixun(pos)==1:
            return 1
    touch(pos)
    time.sleep(1)
    touch(Template(r"tpl1676699976798.png", record_pos=(0.063, 0.185), resolution=(1351, 760)))
    touch(Template(r"tpl1676699995492.png", record_pos=(0.055, 0.07), resolution=(1351, 760)),times=2)
    time.sleep(2)
    touch(Template(r"tpl1676700011844.png", record_pos=(0.346, -0.269), resolution=(1351, 760)))
    wait(Template(r"tpl1680231041506.png", record_pos=(-0.125, 0.094), resolution=(1284, 722)))
    touch(Template(r"tpl1680231041506.png", record_pos=(-0.125, 0.094), resolution=(1284, 722)),times=2)
    touch(Template(r"tpl1676706696499.png", record_pos=(0.46, -0.269), resolution=(1351, 760)))
    try:
        wait(Template(r"tpl1676701852641.png", record_pos=(-0.007, 0.215), resolution=(1351, 760)),timeout=5)
        touch(Template(r"tpl1676701852641.png", record_pos=(-0.007, 0.215), resolution=(1351, 760)))
    except:
        print("go on")
    time.sleep(2)
    touch(Template(r"tpl1676701902237.png", record_pos=(-0.47, 0.251), resolution=(1351, 760)))
    time.sleep(2)
    return 1
        
def daily_zixun():
    wait(Template(r"tpl1676697278788.png", record_pos=(-0.216, 0.104), resolution=(1351, 760)))
    touch(Template(r"tpl1676699868210.png", record_pos=(-0.111, 0.242), resolution=(1351, 760)))
    time.sleep(2)
    touch(Template(r"tpl1676699895403.png", record_pos=(0.355, -0.215), resolution=(1351, 760)))
    time.sleep(1)
#     zixun(nikke_dictionary['尼夫'])
    zixun(nikke_dictionary['麦斯威尔'])
#     zixun(nikke_dictionary['波莉'])
#     zixun(nikke_dictionary['梅登'])
#     zixun(nikke_dictionary['朵拉'])
#     zixun(nikke_dictionary['诺伊斯'])
#     zixun(nikke_dictionary['德雷克'])
#     zixun(nikke_dictionary['红莲'])
#     zixun(nikke_dictionary['普丽瓦蒂'])
    time.sleep(3)
    touch(Template(r"tpl1676707437390.png", record_pos=(-0.413, 0.252), resolution=(1351, 760)))
    time.sleep(5)
    
def enter_moni():
    wait(Template(r"tpl1676707579208.png", record_pos=(-0.215, 0.104), resolution=(1351, 760)))
    touch(Template(r"tpl1676707586455.png", record_pos=(0.201, 0.097), resolution=(1351, 760)))
    time.sleep(2)
    touch(Template(r"tpl1676707608394.png", record_pos=(-0.094, 0.001), resolution=(1351, 760)))
    time.sleep(3)
    touch(Template(r"tpl1676707621503.png", record_pos=(0.0, 0.051), resolution=(1351, 760)))
    time.sleep(1)
    touch(Template(r"tpl1676707635667.png", record_pos=(-0.0, -0.002), resolution=(1351, 760)))
    time.sleep(1)
    loc=wait(Template(r"tpl1676707635667.png", record_pos=(-0.0, -0.002), resolution=(1351, 760)))
    touch((loc[0]+20,loc[1]+135),times=3)
    time.sleep(1)
    touch(Template(r"tpl1676707657509.png", record_pos=(0.0, 0.193), resolution=(1351, 760)))

def single_room():
    try:
        touch(Template(r"tpl1679110872782.png", record_pos=(-0.119, 0.045), resolution=(1465, 824)),times=3)
        time.sleep(1)
        touch(Template(r"tpl1679110926962.png", record_pos=(0.084, 0.239), resolution=(1465, 824)))
        time.sleep(30)
        wait(Template(r"tpl1679111019424.png", record_pos=(-0.002, 0.213), resolution=(1465, 824)),timeout=90)
        time.sleep(1)
        touch(Template(r"tpl1679111019424.png", record_pos=(-0.002, 0.213), resolution=(1465, 824)),times=2)
        time.sleep(3)
        try:
            touch(Template(r"tpl1679111140861.png", record_pos=(-0.096, -0.084), resolution=(1465, 824)))
        except:
            try:
                touch(Template(r"tpl1679111163455.png", record_pos=(-0.099, 0.082), resolution=(1465, 824)))
            except:
                print("go on")
        time.sleep(1)
        touch(Template(r"tpl1679111210106.png", record_pos=(0.057, 0.192), resolution=(1465, 824)))
    except:
        print("sth wrong")
    
def final():
    try:
        loc=wait(Template(r"tpl1679111567929.png", record_pos=(0.045, 0.067), resolution=(1465, 824)))
        time.sleep(1)
        touch(loc,times=2)
        time.sleep(1)
        touch(Template(r"tpl1679111650586.png", record_pos=(-0.092, 0.185), resolution=(1465, 824)))
        time.sleep(2)
        touch(Template(r"tpl1679111671393.png", record_pos=(0.047, 0.244), resolution=(1465, 824)))
        time.sleep(1)
        touch(Template(r"tpl1679111742516.png", record_pos=(-0.006, 0.184), resolution=(1465, 824)))
    except:
        touch(Template(r"tpl1679112838949.png", record_pos=(-0.099, -0.056), resolution=(1465, 824)))
        time.sleep(1)
        touch(Template(r"tpl1679111671393.png", record_pos=(0.047, 0.244), resolution=(1465, 824)))
        time.sleep(1)
        touch(Template(r"tpl1679111742516.png", record_pos=(-0.006, 0.184), resolution=(1465, 824)))
    try:
        time.sleep(1)
        touch(Template(r"tpl1679111763072.png", record_pos=(-0.001, 0.066), resolution=(1465, 824)))
        time.sleep(1)
        touch(Template(r"tpl1679111775502.png", record_pos=(0.086, 0.24), resolution=(1465, 824)))
        time.sleep(30)
        wait(Template(r"tpl1679111019424.png", record_pos=(-0.002, 0.213), resolution=(1465, 824)),timeout=90)
        time.sleep(1)
        touch(Template(r"tpl1679111019424.png", record_pos=(-0.002, 0.213), resolution=(1465, 824)))
        time.sleep(3)
        touch(Template(r"tpl1679111855003.png", record_pos=(-0.001, 0.119), resolution=(1465, 824)))
        time.sleep(1)
        touch(Template(r"tpl1679111871425.png", record_pos=(-0.008, 0.07), resolution=(1465, 824)))
        time.sleep(1)
        touch(Template(r"tpl1679111889464.png", record_pos=(-0.006, 0.165), resolution=(1465, 824)))
        time.sleep(1)
        touch(Template(r"tpl1679111909022.png", record_pos=(0.058, 0.218), resolution=(1465, 824)))
        time.sleep(1)
        loc=wait(Template(r"tpl1679111937832.png", record_pos=(-0.001, -0.117), resolution=(1465, 824)))
        touch((loc[0]+70,loc[1]+260))
        time.sleep(3)
        touch(Template(r"tpl1679111968514.png", record_pos=(-0.414, 0.248), resolution=(1465, 824)))
    except:
        print("sth wrong")
def daily_moni():
    try:
        enter_moni()
        for i in range(5):
            single_room()
        final()
    except:
        print("sth wrong")
def daily_zhaomu():
    wait(Template(r"tpl1676707579208.png", record_pos=(-0.215, 0.104), resolution=(1351, 760)))
    touch(Template(r"tpl1676861667173.png", record_pos=(0.111, 0.242), resolution=(1381, 777)))
    touch(Template(r"tpl1676862348252.png", record_pos=(-0.481, 0.013), resolution=(1381, 777)))
    time.sleep(3)
    touch(Template(r"tpl1676861736951.png", record_pos=(-0.071, 0.181), resolution=(1381, 777)))
    time.sleep(8)
    wait(Template(r"tpl1676861805519.png", record_pos=(0.467, -0.268), resolution=(1381, 777)))
    touch(Template(r"tpl1676861805519.png", record_pos=(0.467, -0.268), resolution=(1381, 777)))
    time.sleep(3)
    touch(Template(r"tpl1676861826846.png", record_pos=(-0.065, 0.226), resolution=(1381, 777)))
    time.sleep(2)
    touch(Template(r"tpl1676861848464.png", record_pos=(0.002, 0.244), resolution=(1381, 777)))

def outpost_again():
    wait(Template(r"tpl1676951630467.png", record_pos=(-0.215, 0.104), resolution=(1381, 777)))
    touch(Template(r"tpl1676951672662.png", record_pos=(-0.231, 0.187), resolution=(1381, 777)))
    time.sleep(1)
    touch(Template(r"tpl1676695148158.png", record_pos=(0.063, 0.187), resolution=(1349, 759)))
    wait(Template(r"tpl1676694098706.png", record_pos=(-0.001, -0.094), resolution=(1349, 759)))
    time.sleep(2)
    touch(Template(r"tpl1676694106295.png", record_pos=(-0.0, 0.089), resolution=(1349, 759)))
    
def daily_mission_award():
    wait(Template(r"tpl1676951851738.png", record_pos=(-0.217, 0.104), resolution=(1381, 777)))
    touch(Template(r"tpl1676951862748.png", record_pos=(0.37, -0.226), resolution=(1381, 777)))
    time.sleep(1)
    touch(Template(r"tpl1676951884335.png", record_pos=(0.094, 0.225), resolution=(1381, 777)))
    time.sleep(3)
    touch(Template(r"tpl1676951884335.png", record_pos=(0.094, 0.225), resolution=(1381, 777)))
    time.sleep(3)
    touch(Template(r"tpl1676951953575.png", record_pos=(-0.0, 0.091), resolution=(1381, 777)))
    time.sleep(2)
    touch(Template(r"tpl1676951977172.png", record_pos=(0.131, -0.242), resolution=(1381, 777)))

    
if __name__=="__main__":
    email()
    outpost()
    daily_shop()
    friendship()
    daily_exploration()
    daily_tower()
#     daily_jjc()
#     daily_zixun()
    daily_zhaomu()
    outpost_again()
    daily_mission_award()
#     daily_moni()