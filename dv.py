from p_g_r import GetResolve
import sys
import time

#给声音片段加标签，makerfile为数据文件，数据格式为单列无空格字符串数字。zhenlv为视频的帧率，如24，25，29.97，30等等

def mktl(makerfile,zhenlv):
    
    
    
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
        
        
        
    mf = open(makerfile)
    mfd = mf.read()
    mfdb = mfd.replace("\n","\t")
    d = mfdb.split("\t")
    e = d[0:-1:3]
    f = d[1:-1:3]
    for k in e:
        tm0 = int(float(zhenlv)*float(k))
        timeline.AddMarker(tm0, "Blue", "maker", "", 1)
        time.sleep(0.1)
    for l in f:
        tm1 = int(float(zhenlv)*float(l))
        timeline.AddMarker(tm1, "Blue", "maker", "", 1)
        time.sleep(0.1)
    print(d[-2])
    mf.close()
    
'''
    i = 0
    for line in mfd:
        t = line.strip("\n")
        tm = t.split("\t")
        tm0 = int(30*float(tm[0]))
        tm1 = int(30*float(tm[1]))
        timeline.AddMarker(tm0, "Blue", "maker", "", 1)
        time.sleep(0.1)
        timeline.AddMarker(tm1, "Blue", "maker", "", 1)
        time.sleep(0.1)
        i = i + 1
    print(i)
'''
#检查当前时间线有多少片段，根据片段数量除2加1后进行标签添加

def itn():
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
    print(timelineVideoTrackCount)
    print(len(itemsIntrack))

print("mktl(makerfile,zhenlv):给声音片段加标签，makerfile为数据文件，")
print()
print("数据格式为Audacity导出的标签文件")
print()
print("zhenlv为视频的帧率，如24，25，29.97，30等")
print()
print("itn():检查当前时间线有多少片段")
print()
print("根据片段数量除2加1后进行标签添加")
print()
