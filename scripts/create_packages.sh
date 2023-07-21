#!/bin/bash

set -e

cd recipes/
cd rabbitmq-c && python3 build.py && cd ..
cd SimpleAmqpClient && python3 build.py && cd ..
cd prometheus-cpp && python3 build.py && cd ..
cd opentracing-cpp && python3 build.py && cd ..
cd zipkin-cpp-opentracing && python3 build.py && cd ..
cd spinnaker && python build.py && cd ..
cd flycapture2 && python build.py && cd ..
# cd armadillo && python build.py && cd ..
cd benchmark && python3 build.py && cd ..
cd expected && python3 build.py && cd ..

git clone https://github.com/labvisio/is-msgs \
  && cd is-msgs \
  && git checkout develop \
  && python package.py \
  && cd ..

git clone https://github.com/labvisio/is-wire \
  && cd is-wire \
  && git checkout develop \
  && python package.py \
  && cd ..

cd ..

# cd opencv && python build.py && cd ..