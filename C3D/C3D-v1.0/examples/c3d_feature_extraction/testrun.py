import subprocess

result = subprocess.Popen(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1', '-sexagesimal', '/home/callbarian/C3D/videos/Duluth_Arson.mp4'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
out = result.communicate()
print(out)
time = out[0].decode().split(':')
hour = int(time[0])
minute = int(time[1])
seconds = int(time[2].split('.')[0])
print(hour)
print(minute)
print(seconds)

