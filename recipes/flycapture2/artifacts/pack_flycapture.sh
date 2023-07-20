#!/bin/bash
#
# Before run this script, put in this directory the *.tar.gz file 
# containing the latest flycapture library for Ubuntu 16.04 64 bits. 
# This library can be found at https://www.ptgrey.com/Support
#

set -e

FLYCAPTURE_FILE=`find . -name 'flycapture2-*'`
if [ -z $FLYCAPTURE_FILE ]; then
  echo '>> flycapture2-*.tar.gz not found! Please, read this script to find out where to download it.'
  exit 0
fi
FLYCAPTURE_FILE_ARR=(${FLYCAPTURE_FILE//-/ })
FLYCAPTURE_VERSION=${FLYCAPTURE_FILE_ARR[1]}

CURRENT_DIR=`pwd`
rm -rf tmp
mkdir -p tmp/
tar xf flycapture2-*.tgz -C tmp/ --wildcards --no-anchored 'lib*'
cd tmp/flycapture2-*
debs=(`ls | grep -i .deb`)
for deb in ${debs[@]}; do
    dpkg -x $deb .
done

cd usr/
rm -rf share/

cd lib/
rm -f libflycapture-c.so libflycapture-c.so.2
rm -f libflycapture.so libflycapture.so.2
rm -f libflycapturegui-c.so libflycapturegui-c.so.2
rm -f libflycapturegui.so libflycapturegui.so.2
rm -f libflycapturevideo-c.so libflycapturevideo-c.so.2
rm -f libflycapturevideo.so libflycapturevideo.so.2
rm -f libmultisync-c.so libmultisync-c.so.2
rm -f libmultisync.so libmultisync.so.2

mv libflycapture-c.so.$FLYCAPTURE_VERSION libflycapture-c.so
mv libflycapture.so.$FLYCAPTURE_VERSION libflycapture.so 
mv libflycapturegui-c.so.$FLYCAPTURE_VERSION libflycapturegui-c.so
mv libflycapturegui.so.$FLYCAPTURE_VERSION libflycapturegui.so
mv libflycapturevideo-c.so.$FLYCAPTURE_VERSION libflycapturevideo-c.so
mv libflycapturevideo.so.$FLYCAPTURE_VERSION libflycapturevideo.so
mv libmultisync-c.so.$FLYCAPTURE_VERSION libmultisync-c.so
mv libmultisync.so.$FLYCAPTURE_VERSION libmultisync.so

ln -s libflycapture-c.so libflycapture-c.so.2
ln -s libflycapture.so libflycapture.so.2
ln -s libflycapturegui-c.so libflycapturegui-c.so.2
ln -s libflycapturegui.so libflycapturegui.so.2
ln -s libflycapturevideo-c.so libflycapturevideo-c.so.2
ln -s libflycapturevideo.so libflycapturevideo.so.2
ln -s libmultisync-c.so libmultisync-c.so.2
ln -s libmultisync.so libmultisync.so.2

ln -s libflycapture-c.so libflycapture-c.so.$FLYCAPTURE_VERSION
ln -s libflycapture.so libflycapture.so.$FLYCAPTURE_VERSION
ln -s libflycapturegui-c.so libflycapturegui-c.so.$FLYCAPTURE_VERSION
ln -s libflycapturegui.so libflycapturegui.so.$FLYCAPTURE_VERSION
ln -s libflycapturevideo-c.so libflycapturevideo-c.so.$FLYCAPTURE_VERSION
ln -s libflycapturevideo.so libflycapturevideo.so.$FLYCAPTURE_VERSION
ln -s libmultisync-c.so libmultisync-c.so.$FLYCAPTURE_VERSION
ln -s libmultisync.so libmultisync.so.$FLYCAPTURE_VERSION

cd ..

tar cf - include/ lib/ | gzip -9 -> $CURRENT_DIR/flycapture2.tar.gz
cd $CURRENT_DIR
rm -rf tmp/