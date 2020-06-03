import subprocess

result = subprocess.Popen(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1', '-sexagesimal', '/home/callbarian/C3D/videos/Duluth_Arson/Duluth_Arson.mp4'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
out = result.communicate()
print(out)
