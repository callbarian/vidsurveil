import os
from os import path


def prepare_video():
    
    #stream = os.popen("cd /home/callbarian/C3D/videos")

    for file in os.listdir("/home/callbarian/C3D/videos"):
        name , extension = path.splitext(file)
        #print(file)
        #print(name)
        dir_path = '/home/callbarian/C3D/videos/' + name
        
        os.popen('mkdir ' + dir_path)

        #print('mv ' + '/home/callbarian/C3D/videos/' +file1+ ' ' + copy_path)
        os.popen('mv ' + '/home/callbarian/C3D/videos/' +file+ ' ' + dir_path)

def split_video():
       
    for file in os.listdir("/home/callbarian/C3D/videos"):
        name , extension = path.splitext(file)
        #print(name) 
    
        #file_dir = file_dir + ".mp4"
        save_path = "/home/callbarian/C3D/videos/" + name + '/' + name
        file_path= "/home/callbarian/C3D/videos/" + name + '/' + file
        os.popen('ffmpeg -i ' + file_path + ' -c copy -map 0 -f segment -segment_time 30 -reset_timestamps 1 -segment_format_options movflags=+faststart ' + save_path + '%03d.mp4')
        os.popen('mv ' + file_path + ' /home/callbarian/C3D/move_videos')
       
def main():
    #prepare_video()
    split_video()

main()
#os.popen("python extract_C3D_feature.py")
#os.popen("conda deactivate")
#os.popen("conda activate Anomaly_py36")
#os.popen("python /home/callbarian/AnomalyDetectionCVPR2018-master/Demo_GUI.py")
#os.popen("source deactivate c3d_py36")
