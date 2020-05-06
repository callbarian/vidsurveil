import os
from os import path
import time
import cutWithSlide

def prepare_video(video_directory):
    
    #stream = os.popen("cd /home/callbarian/C3D/videos")

    for file in os.listdir(video_directory):
        name , extension = path.splitext(file)
        
        dir_path = video_directory +'/'+ name
        
        os.popen('mkdir ' + dir_path)

        os.popen('mv ' + video_directory +'/'+ file+ ' ' + dir_path)

def split_video(video_directory,move_directory,count):
    success = 0   
    for file in os.listdir(video_directory):
        for file2 in os.listdir(video_directory +'/'+ file):
            name , extension = path.splitext(file2)
        
            save_path = video_directory +'/'+ name + '/' + name
            file_path= video_directory +'/'+ name + '/' + file2
            cutWithSlide.cut(file_path,save_path)
            time.sleep(count)
            print("deliberately delaying to prevent crash")
            #with delaying few seconds, the below command will be executed before ffmpeg finish its job. Or it could get into the next loop and start another ffmpeg process, and it will lead to a crash.

            os.popen('rm ' + file_path)
            break 
    success = 1
    return success
            
       
def run():
    video_directory = "/home/callbarian/C3D/videos"
    #input video directory
    move_directory = "/home/callbarian/C3D/move_videos"
    #video directory that will copy your input video after processing
    prepare_video(video_directory)
    time.sleep(2)
    count = 8
    #seconds to delay to prevent crash. need more time if the video is longer than 30minutes
    success = split_video(video_directory,move_directory,count)
    if success:
        print("video splition succeeded")
    time.sleep(1)
    #os.popen("python /home/callbarian/C3D/C3D-v1.0/examples/c3d_feature_extraction/extract_C3D_feature.py") 

run()
#os.popen("python extract_C3D_feature.py")
#os.popen("conda deactivate")
#os.popen("conda activate Anomaly_py36")
#os.popen("python /home/callbarian/AnomalyDetectionCVPR2018-master/Demo_GUI.py")
#os.popen("source deactivate c3d_py36")
