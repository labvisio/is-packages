#!/bin/bash

if [ "$#" -ne 3 ]; then
  echo "Missing Arguments. Try ./build.sh <USER> <API_KEY> <COMPILER>"
  exit 1
fi

user=$1
api_key=$2
compiler=$3

read -r -d '' build_commands <<- EOM
  set -e
  cd rabbitmq-c && python build.py && cd ..
  cd SimpleAmqpClient && python build.py && cd ..
  cd prometheus-cpp && python build.py && cd ..
  cd opentracing-cpp && python build.py && cd ..
  cd zipkin-cpp-opentracing && python build.py && cd ..
  cd Qt && python build.py && cd ..
  cd opencv && python build.py && cd ..
  cd spinnaker && python build.py && cd ..
  cd armadillo && python build.py && cd ..
  cd benchmark && python build.py && cd ..

  git clone https://github.com/labviros/is-msgs \
    && cd is-msgs \
    && git checkout modern-cmake \
    && python package.py \
    && cd ..

  git clone https://github.com/labviros/is-wire \
    && cd is-wire \
    && git checkout develop \
    && python package.py \
    && cd ..
EOM

echo $build_commands

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
  /bin/bash -c "$build_commands"

