# This Python file uses the following encoding: utf-8
import subprocess
import os
import sys
import PyQt5
import functools
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic

def clickable(widget):

    class Filter(QObject):

        clicked = pyqtSignal()
         
        def eventFilter(self, obj, event):
            
            if obj == widget:
                if event.type() == QEvent.MouseButtonRelease:
                    if obj.rect().contains(event.pos()):
                        self.clicked.emit()
                        # The developer can opt for .emit(obj) to get the object within the slot.
                        return True
           
            return False
    
    filter = Filter(widget)
    widget.installEventFilter(filter)
    return filter.clicked

click = '/home/callbarian/vidsurveil/project_python_qt/file_dialog.ui'
#click = '/Users/iseongmin/Downloads/gui/application.ui'
class vidsurveil(QDialog):
    def __init__(self):
        #super().__init__()
        QDialog.__init__(self, None)
        #QDialog.__init__(self, None)
        uic.loadUi(click, self)

        #self.pushButton.clicked.connect(self.select_Files)
        #self.pushButton_2.clicked.connect(self.prepare_videos)
        #self.label_3.mousePressEvent = functools.partial(self.select_Files, self.label_3)
        #self.label_4.mousePressEvent = functools.partial(self.prepare_videos, self.label_4)
        #self.label_5.mousePressEvent = functools.partial(self.extract_features, self.label_5)
        #self.label_2.clicked.connect(self.select_Files)
        #self.label_3.clicked.connect(self.prepare_videos)
        #self.label_5.clicked.connect(self.extract_features)
        #pass  # call __init__(self) of the custom base class here
        clickable(self.label_2).connect(self.logo)
        clickable(self.label_3).connect(self.select_Files)
        clickable(self.label_4).connect(self.prepare_videos)
        clickable(self.label_5).connect(self.extract_features)

        #layout = QGridLayout(self)
        #layout.addWidget(self.label_2)
        layout2 = self.verticalLayout_22
        layout3 = self.verticalLayout_3
        layout4 = self.verticalLayout_4
        layout5 = self.verticalLayout_5
        
        layout2.addWidget(self.label_2)
        layout3.addWidget(self.label_3)
        layout4.addWidget(self.label_4)
        layout5.addWidget(self.label_5)
        
        

    def logo(self):
        print("")

    def select_Files(self):
        fname = QFileDialog.getOpenFileName(self)

        #label.setText(fname[0])
        result = subprocess.Popen(['cp', fname[0], '/home/callbarian/C3D/videos'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        #result = subprocess.Popen(['cp', fname[0], '/Users/iseongmin/Downloads/qt_projects/project_python_qt'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        out = result.communicate()
        result_message = out[0].decode()

        #if no error message is returned, then the string should be empty
        if fname[0]:
            if not result_message.strip():
                msg = QMessageBox()
                msg.setWindowTitle("Move Success")
                msg.setText("Files has been successfully moved!")
                msg.setStandardButtons(QMessageBox.Ok)
                x = msg.exec_()
        
    def prepare_videos(self):
        print("preparing videos.......")
        result = subprocess(['python', '/home/callbarian/C3D/C3D-v1.0/examples/c3d_feature_extraction/run_feature_extraction.py'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        #result = subprocess.Popen(['python', '/Users/iseongmin/Downloads/qt_projects/application/application.py'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        
        out= result.communicate()
        print(out[0])

    def extract_features(self):
        print("extracting........")
        os.system('sh ' + '/home/callbarian/C3D/C3D-v1.0/examples/c3d_feature_extraction/feature_extraction.sh')
        #result = subprocess.Popen(['sh','/home/callbarian/C3D/C3D-v1.0/examples/c3d_feature_extraction/call_environment.sh','/home/callbarian/bin/miniconda3/envs/c3d_py36/bin/python','/home/callbarian/C3D/C3D-v1.0/examples/c3d_feature_extraction/extract_C3D_feature.py'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)


        #result = subprocess.Popen(['python', '/home/callbarian/C3D/C3D-v1.0/examples/c3d_feature_extraction/extract_C3D_feature.py'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        #(out, err) = result.communicate()
        #print(out)
        #result.wait()
        #os.popen('python ' + '/home/callbarian/C3D/C3D-v1.0/examples/c3d_feature_extraction/extract_C3D_feature.py')
        #print("this is after feature extraction....")
        #result_message = out[0]


        #result = subprocess.Popen(['sh','/home/callbarian/C3D/C3D-v1.0/examples/c3d_feature_extraction/call_environment.sh','/home/callbarian/bin/miniconda3/envs/Anomaly_py36/bin/python','/home/callbarian/AnomalyDetectionCVPR2018-master/Demo_GUI.py'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        #(out,err) = result.communicate()
        #print(out)
        #result.wait()
        
         #result_message = out[0].decode()
#        if(result_message.split('::')[1]) is 'Anaconda, Inc.':
#            msg = QMessageBox()
#            msg.setWindowTitle("C3D to Anomaly")
#            msg.setText("switch environment successfully")
#            msg.setStandardButtons(QMessageBox.Ok)
#            x = msg.exec_()

        #result = subprocess.Popen(['python', '/home/callbarian/AnomalyDetectionCVPR2018-master/Demo_GUI.py'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
       # out = result.communicate()

if __name__ == "__main__":
    app = QApplication([])
    window = vidsurveil()
    window.show()
    sys.exit(app.exec_())
