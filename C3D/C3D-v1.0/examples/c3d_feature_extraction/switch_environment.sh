#!/bin/bash
#conda /home/callbarian/bin/miniconda3/bin/deactivate c3d_py36
eval $(conda shell.bash hook)

conda deactivate
python --version
conda activate Anomaly_py36
python --version


