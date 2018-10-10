#!/bin/bash

set -e

cd rabbitmq-c && python build.py && cd ..
cd SimpleAmqpClient && python build.py && cd ..
cd prometheus-cpp && python build.py && cd ..
cd opentracing-cpp && python build.py && cd ..
cd zipkin-cpp-opentracing && python build.py && cd ..
cd spinnaker && python build.py && cd ..
cd flycapture2 && python build.py && cd ..
cd armadillo && python build.py && cd ..
cd benchmark && python build.py && cd ..

git clone https://github.com/labviros/is-msgs \
  && cd is-msgs \
  && git checkout v1.1.8 \
  && python package.py \
  && cd ..

git clone https://github.com/labviros/is-wire \
  && cd is-wire \
  && git checkout v1.1.4 \
  && python package.py \
  && cd ..

cd opencv && python build.py && cd ..