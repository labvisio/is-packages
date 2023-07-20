#!/bin/bash
#
# Before run this script, put in this directory the *.tar.gz file 
# containing the latest spinnaker library for Ubuntu 16.04. 
# This library can be found at https://www.ptgrey.com/Support
#

set -e

SPINNAKER_FILE=`find . -name 'spinnaker-*'`
if [ -z $SPINNAKER_FILE ]; then
  echo '>> spinnaker-*.tar.gz not found! Please, read this script to find out where to download it.'
    exit 0
fi
SPINNAKER_FILE_ARR=(${SPINNAKER_FILE//-/ })
SPINNAKER_VERSION=${SPINNAKER_FILE_ARR[1]}

CURRENT_DIR=`pwd`
rm -rf tmp
mkdir -p tmp/
tar xf spinnaker-*.tar.gz -C tmp/ --wildcards --no-anchored 'lib*'
cd tmp/spinnaker-*
debs=(`ls | grep -i .deb`)
for deb in ${debs[@]}; do
    dpkg -x $deb .
done

cd usr/
rm -rf share/
cd ..

cd opt/spinnaker/lib/
rm -f libSpinnaker.so libSpinnaker.so.3
rm -f libSpinnaker_C.so libSpinnaker_C.so.3
rm -f libSpinVideo.so libSpinVideo.so.3
rm -f libSpinVideo_C.so libSpinVideo_C.so.3

mv libSpinnaker.so.$SPINNAKER_VERSION libSpinnaker.so
mv libSpinnaker_C.so.$SPINNAKER_VERSION libSpinnaker_C.so
mv libSpinVideo.so.$SPINNAKER_VERSION libSpinVideo.so
mv libSpinVideo_C.so.$SPINNAKER_VERSION libSpinVideo_C.so

ln -s libSpinnaker.so libSpinnaker.so.3
ln -s libSpinnaker_C.so libSpinnaker_C.so.3
ln -s libSpinVideo.so libSpinVideo.so.3
ln -s libSpinVideo_C.so libSpinVideo_C.so.3

ln -s libSpinnaker.so libSpinnaker.so.$SPINNAKER_VERSION
ln -s libSpinnaker_C.so libSpinnaker_C.so.$SPINNAKER_VERSION
ln -s libSpinVideo.so libSpinVideo.so.$SPINNAKER_VERSION
ln -s libSpinVideo_C.so libSpinVideo_C.so.$SPINNAKER_VERSION

cd ..

tar cf - include/ lib/ | gzip -9 -> $CURRENT_DIR/spinnaker.tar.gz
cd $CURRENT_DIR
rm -rf tmp/