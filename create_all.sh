#!/bin/bash

(cd rabbitmq-c && conan create . picoreti/testing)
(cd SimpleAmqpClient && conan create . picoreti/testing)
(cd protobuf && conan create . picoreti/testing)
(cd prometheus-cpp && conan create . picoreti/testing)
(cd opentracing-cpp && conan create . picoreti/testing)
(cd is-msgs && conan create . picoreti/testing)
(cd is-wire && conan create . picoreti/testing)