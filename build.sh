#!/bin/bash

if [ "$#" -ne 3 ]; then
  echo "Missing Arguments. Try ./build.sh <USER> <API_KEY> <COMPILER>"
  exit 1
fi

user=$1
api_key=$2
compiler=$3

docker build -t is-builder-$compiler -f "Dockerfile.$compiler" .

docker run -ti --network=host                                 \
  -e CONAN_UPLOAD=https://api.bintray.com/conan/labviros/is   \
  -e CONAN_USERNAME=is                                        \
  -e CONAN_LOGIN_USERNAME=$user                               \
  -e CONAN_PASSWORD=$api_key                                  \
  -e CONAN_CHANNEL=stable                                     \
  -v `pwd`:/packages                                          \
  -w /packages                                                \
  is-builder-$compiler                                        \
  /bin/bash create_packages.bash 
