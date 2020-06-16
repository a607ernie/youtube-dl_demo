import subprocess
import traceback
from datetime import date
import json
import sys
sys.path.append('.')
try:
    #read config.json
    js = ''
    with open('config.json' ,'r') as reader:
        js = json.loads(reader.read())
    #==========================================================================
    #output command
    output = '-o {output_folder}\%(title)s.%(ext)s'.format(output_folder=js['output_folder'])

    #write record
    archive='--download-archive archive.txt'

    #playlist
    playlist_start='--playlist-start %s' % js['start']
    playlist_end = '--playlist-end %s' % js['end']
    playlist_rule = "%s %s" % (playlist_start,playlist_end)
    #convert to mp3
    convert_mp3 = '--extract-audio --audio-format mp3'
    audo_quality='--audio-quality 0'

    #ffmpeg path
    ffmpeg = '--ffmpeg-location %s' % js['ffmpeg_path']
    #==========================================================================
except:
    traceback.print_exc()
    input()
    
def main():
    print("讀取設定檔...")
    print("Youtube 網址  : %s" % js['url'])
    print("輸出資料夾    : ", js['output_folder'])
    print("歌單選取範圍  : %s ~ %s" % (js['start'], js['end']))
    try:
        subprocess.call("youtube-dl {archive} {convert_mp3} {audo_quality} {playlist_rule} {output} {ffmpeg} {url}"\
                        .format(url=js['url'],output=output,playlist_rule=playlist_rule,convert_mp3=convert_mp3,
                                audo_quality=audo_quality,ffmpeg=ffmpeg,archive=archive))
    except:
        print(traceback.print_exc())
    print("\nDone. Input any key to exit.")

if __name__ == '__main__':
    main()
    input()