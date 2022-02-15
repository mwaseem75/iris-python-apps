#!/bin/bash

cd ${SRC_PATH}/src/Python/flask

/usr/irissys/bin/irispython /opt/irisapp/src/Python/flask/app.py  &

/home/irisowner/.local/bin/jupyter-notebook --no-browser --port=8888 --ip 0.0.0.0 --notebook-dir=/irisdev/app/src/Notebooks --NotebookApp.token='' --NotebookApp.password='' &

exit 1
