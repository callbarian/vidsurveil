# This Python file uses the following encoding: utf-8
import subprocess
import sys
import PyQt5
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic

click = '/Users/iseongmin/Downloads/qt_projects/project_python_qt/file_dialog.ui'

class vidsurveil(QtWidgets.QmainWindow:
    def __init__(self):
        QDialog.__init__(self, None)
        uic.loadUi(click, self)

        self.label_2.clicked.connect(self.select_Files)
        self.label_3.clicked.connect(self.prepare_videos)

        pass  # call __init__(self) of the custom base class here

    def select_Files(self):
        fname = QFileDialog.getOpenFileName(self)
        self.label.setText(fname[0])
        result = subprocess.Popen(['cp', fname[0], '/home/callbarian/C3D/videos'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        out = result.communicate()
        result_message = out[0].decode()

        #if no error message is returned, then the string should be empty
        if not result_message.strip():
            msg = QMessageBox()
            msg.setWindowTitle("Move Success")
            msg.setText("Files has been successfully moved!")
            msg.setStandardButtons(QMessageBox.Ok)
            x = msg.exec_()

    def prepare_videos(self):
        result = subprocess.Popen(['python', '/home/callbarian/C3D/C3D-v1.0/examples/c3d_feature_extraction/run_feature_extraction.py'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        out= result.communicate()

    def extract_features(self):
        result = subprocess.Popen(['source', '/home/callbarian/C3D/C3D-v1.0/examples/switch_environment.sh'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        out = result.communicate()
        result_message = out[0].decode()
        #if(result_message.split('::')[1]) is 'Anaconda, Inc.':
        #    msg = QMessageBox()
        #    msg.setWindowTitle("C3D to Anomaly")
        #    msg.setText("switch environment successfully")
        #    msg.setStandardButtons(QMessageBox.Ok)
        #    x = msg.exec_()

        result = subprocess.Popen(['python', '/home/callbarian/AnomalyDetectionCVPR2018-master/Demo_GUI.py'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        out = result.communicate()

if __name__ == "__main__":
    app = QApplication([])
    window = vidsurveil()
    # window.show()
    sys.exit(app.exec_())
