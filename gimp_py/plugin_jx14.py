# -*- coding: utf-8 -*-

# !/usr/bin/env python2

# 文件头编码“utf-8”和运行环境“python2”是不可以顺序相反的否则直接导致崩溃！

from gimpfu import *
import itertools

def plugin_main(image, layer):

    tk = layer.width # 取得图像宽度
    tg = layer.height # 取得图像高度

    note = ["脸部杂质--修复H", "头发杂质--克隆C"]

    for i in note:
        tuceng = pdb.gimp_layer_new(image, tk, tg, 1, i, 100, 0)  # 生成图层
        pdb.gimp_image_insert_layer(image, tuceng, None, 0)  # 插入图层，第三个参数None如果有图层组，可以放图层组变量如下面的图层组‘qxc’

    name = ['去瑕疵',
            '锐化眼眉发鼻唇--盖印--高反差--叠加',
            '锐化皱纹--盖印--高反差--叠加',
            '修亮眼球--盖印--滤色',
            '加对比--盖印--去色红减黄加--柔光--不透50',
            '周边加深--盖印--相乘--画四周',
            '暗影加强--盖印--相乘--不透50',
            '亮处加强--盖印--滤色--不透15',
            '皮肤加红--盖印--加红饱和',
            '黑白--盖印--去色红减黄加']

    lm = [28,23,23,31,45,30,30,31,28,28]

    for i, m in itertools.izip(name, lm):
        qxc = pdb.gimp_layer_group_new(image)  # 生成去瑕疵图层组
        pdb.gimp_item_set_name(qxc, i)  # 更改图层组名称
        pdb.gimp_layer_set_mode(qxc, m)  # 更改图层组模式
        pdb.gimp_image_insert_layer(image, qxc, None, 0)  # 插入图层组

register(
    "Beautys",
    "",
    "",
    "lhb",
    "lhb",
    "2020",
    "Beautys",
    "RGB*",
    [
        (PF_IMAGE, "image", "Input image", None),
        (PF_DRAWABLE, "drawable", "Drawable", None)
        ],
    [],
    plugin_main,
    menu = "<Image>/Filters")

main()
