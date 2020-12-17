# 取得达芬奇影片中的所有视频1通道的片段，用于制作字幕文件
from p_g_r import GetResolve
import sys
import datetime
def zm(x):
    resolve = GetResolve()
    projectManager = resolve.GetProjectManager()
    project = projectManager.GetCurrentProject()
    timeline = project.GetCurrentTimeline()
    if not timeline:
        if project.GetTimelineCount() > 0:
            timeline = project.GetTimelineByIndex(1)
            project.SetCurrentTimeline(timeline)
    if not timeline:
        print("Current project has no timelines")
        sys.exit()
    timelineVideoTrackCount = timeline.GetTrackCount("video")
    itemsIntrack = timeline.GetItemsInTrack("video", 1)
    itemlist = timeline.GetItemListInTrack("video", 1)
    print()
    print("当前时间线视频通道数：",timelineVideoTrackCount)
    print()
    print("第一视频通道片段数：",len(itemsIntrack))
    print()
    i = len(itemsIntrack)
    srt = []
    for r in range(0,i):
        iS = itemlist[r].GetStart()
        iE = itemlist[r].GetEnd()
        iSt = datetime.timedelta(seconds=iS/x)
        iEt = datetime.timedelta(seconds=iE/x)
        srt.append([r+1,"huanhang",str(iSt),"jiantou",str(iEt),"huanhang","Subtitle"])
    print(srt)

#   datetime.timedelta(seconds=90267.0 / 25)
#   01:   00:   10,   679
#   小时：分钟：秒钟，微秒        
print()
print("zm(x):x为视频帧率一般为24，25，30等")
print()
print("返回时间线的视频通道数量及片段数量")
print()
print("返回每个片段的开始结束帧数列表")
print()
print()
print()
print("将列表考入到Notepad++，进行格式转换")
print()
print("{, 'huanhang', '}替换为{\\n}")
print()
print("{', 'jiantou', '}替换为{ --> }")
print()
print("{'], [}替换为{\\n\\n}")
print()
print("{'}替换为{}")
print()
print("如果帧数为整数如25，{0000}替换为{0}")
print()
print("如果帧数不为整数如29.97，正则表达式{(\d\d\d)\d\d\d}替换为{\\1}")
print()
print("如果帧数为整数如25，正则表达式{(\d:\d\d:\d\d)$}替换{\\1.000}")
print()
print("如果帧数为整数如25，正则表达式{(\d:\d\d:\d\d) }替换{\\1.000 }")
print()
print("去除最前最后的{[[}和{]]}")
print()
print("保存为.srt文件")
