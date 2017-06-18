PWD=`pwd`
if [ ! -e libs/python ]; then
    mkdir -p libs/python
    PYTHONPATH=$PWD/libs/python
    PYTHONUSERBASE=$PYTHONPATH sh pipInstall.sh
fi
