#!/bin/bash

if [ "$#" -ne 4 ]; then
  echo "Missing Arguments. Try ./build.sh <REMOTE> <USER> <PASSWORD> <GCC_VERSION>"
  exit 1
fi

remote=$1
user=$2
password=$3
gcc_version=$4

docker build \
  -t is-builder-gcc$GCC_VERSION \
  --build-arg IS_CONAN=$remote \
  --build-arg GCC_VERSION=$gcc_version \
  .

docker run -ti --network=host \
  -e CONAN_LOGIN_USERNAME_IS=$user \
  -e CONAN_PASSWORD_IS=$password \
  is-builder-gcc$gcc_version
