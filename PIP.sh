#! /bin/bash

if [ $# != 1 ];
then
    echo '***************PIP*********************'
    echo "Usage: $0 package_name"
    echo "Example: $0 numpy"
    echo '***************************************'
else
    echo "Do Install"
    pip install $1 -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com
fi
