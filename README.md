Youtube-dl_demo 
===
Youtube-dl是一個可以下載Youtube、以及其他數百個網站影片的工具，這個repository只是簡單地把Youtube-dl用python再包裝一層，使我們可以用更簡單的方式去設定參數。

但是也因為Youtube-dl可以調整的參數實在太多，因此這邊的參數只有調整某些部分。

> PS.這邊只有實作出下載音樂的部分，可將程式掛在常駐伺服器或是打包後放在工作排程的電腦上

## Index
- [Youtube-dl_demo](#youtube-dl_demo)
  - [Index](#index)
  - [Guide](#guide)
  - [How to Use](#how-to-use)


Guide
---
1. clone this repository

```
git clone https://github.com/a607ernie/youtube-dl_demo.git
```

2. modify the config.json

```
{
    "url" : "https://www.youtube.com/playlist?list=xxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    "output_folder" : "D:\\USER\\MUSIC",
    "ffmpeg_path": "D:\\USER\\ffmpeg\\bin",
    "start" : 1,
    "end" : 15
}
# url : Youtube的音樂歌單，須設定為公開
# output_folder : 音樂下載好要存放的地方
# ffmpeg_path : 因為可能會下載到.webm或其他不是mp3格式的音樂，因此需要轉檔工具
# start 、 end : 程式開始抓取位置、結束位置，從最新(歌單的最上方)的影片開始算
```

3. install youtube-dl
```
pip install youtube-dl
```

4. 下載[ffmpeg](https://ffmpeg.org/download.html)

下載好後，config這邊的```ffmpeg_path```要指定ffmpeg資料夾中的```bin```位置

5. 執行程式

```
python music.py
```


How to Use
---

上面測試步驟沒問題後，接著可以把這個程式做成常駐程式
1. linux service
2. ```pyinstaller```打包成EXE後，掛在windows工作排程上



