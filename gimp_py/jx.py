# -*- coding: utf-8 -*-

#!/usr/bin/env python2

from gimpfu import *

def jxtx():
    jxtx = gimp.image_list()[0] #获取打开的第一个图像
    qxc = pdb.gimp_layer_group_new(jxtx) #生成去瑕疵图层组
    pdb.gimp_item_set_name(qxc, '去瑕疵') #更改图层组名称
    pdb.gimp_image_insert_layer(jxtx, qxc, None, 0) #插入图层组

    tk = pdb.gimp_image_width(jxtx) #取得图像宽度
    tg = pdb.gimp_image_height(jxtx) #取得图像高度

    lbqxc = pdb.gimp_layer_new(jxtx, tk, tg, 1, '脸部杂质--修复H', 100, 0) #生成脸部瑕疵图层
    tfqxc = pdb.gimp_layer_new(jxtx, tk, tg, 1, '头发杂质--修复H', 100, 0)

    pdb.gimp_image_insert_layer(jxtx, lbqxc, qxc, 0) #在图层组插入图层
    pdb.gimp_image_insert_layer(jxtx, tfqxc, qxc, 0)

    qxc1 = pdb.gimp_layer_group_new(jxtx) #生成去图层组
    pdb.gimp_item_set_name(qxc1, '锐化眼眉发鼻唇--盖印--高反差--叠加') #更改图层组名称
    pdb.gimp_image_insert_layer(jxtx, qxc1, None, 0) #插入图层组

    qxc2 = pdb.gimp_layer_group_new(jxtx) #生成去图层组
    pdb.gimp_item_set_name(qxc2, '锐化皱纹--盖印--高反差--叠加') #更改图层组名称
    pdb.gimp_image_insert_layer(jxtx, qxc2, None, 0) #插入图层组

    qxc3 = pdb.gimp_layer_group_new(jxtx) #生成去图层组
    pdb.gimp_item_set_name(qxc3, '修亮眼球--盖印--相加') #更改图层组名称
    pdb.gimp_image_insert_layer(jxtx, qxc3, None, 0) #插入图层组

    qxc4 = pdb.gimp_layer_group_new(jxtx) #生成去图层组
    pdb.gimp_item_set_name(qxc4, '加对比--盖印--去色红减黄加--柔光--不透50') #更改图层组名称
    pdb.gimp_image_insert_layer(jxtx, qxc4, None, 0) #插入图层组

    qxc5 = pdb.gimp_layer_group_new(jxtx) #生成去图层组
    pdb.gimp_item_set_name(qxc5, '周边加深--盖印--相乘--画四周') #更改图层组名称
    pdb.gimp_image_insert_layer(jxtx, qxc5, None, 0) #插入图层组

    qxc6 = pdb.gimp_layer_group_new(jxtx) #生成去图层组
    pdb.gimp_item_set_name(qxc6, '暗影加强--盖印--相乘--不透50') #更改图层组名称
    pdb.gimp_image_insert_layer(jxtx, qxc6, None, 0) #插入图层组

    qxc7 = pdb.gimp_layer_group_new(jxtx) #生成去图层组
    pdb.gimp_item_set_name(qxc7, '亮处加强--盖印--滤色--不透15') #更改图层组名称
    pdb.gimp_image_insert_layer(jxtx, qxc7, None, 0) #插入图层组

    qxc8 = pdb.gimp_layer_group_new(jxtx) #生成去图层组
    pdb.gimp_item_set_name(qxc8, '皮肤加红--盖印--加红饱和') #更改图层组名称
    pdb.gimp_image_insert_layer(jxtx, qxc8, None, 0) #插入图层组

    qxc9 = pdb.gimp_layer_group_new(jxtx) #生成去图层组
    pdb.gimp_item_set_name(qxc9, '黑白--盖印--去色红减黄加') #更改图层组名称
    pdb.gimp_image_insert_layer(jxtx, qxc9, None, 0) #插入图层组

