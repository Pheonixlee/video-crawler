# video-crawler
赘婿之吉星高照爬取
第一次学会m3u8解析
不懂的人我来解释下，要看是什么网站的请看代码中的headers的referer.
首先运行video_crawler.py,运行的方式可以是pycharm运行,也可以Win+R,打开cmd,写上你下载去的path(cd path)
写上python video_clawler.py
运行后会出现一个dir,里面有1370个ts文件
要把他们合并起来的话，首先你们要改代码，create_filenames.py里运行后复制到filenames.txt,也可以把我的filenames.txt内的换成你的ts视频路径，接下来右键bat文件，点击编辑
复制ffmpeg的那段话，更改路径。到cmd,改路径写上这段话，即可合并视频，虽然不是无水印的，因为iqiyi是在有点难度，嘤嘤嘤。
我不会的难点：create_filenames.py写了with open():
                                        f.write()
下去之后出现的不是print出来的样子，做了好久做不出，难受。我不是系统学习的啊，所以基础都不稳。
