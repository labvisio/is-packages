import os, sys
import platform

import subprocess


def main():
    command = """
        conan create . --user is --channel stable \
            -s compiler=gcc \
            -s compiler.version=11 \
            -s compiler.libcxx=libstdc++11 \
            -s build_type=Release \
            -b missing \
            -o:h rabbitmq-c/*:ssl=False \
            -o:h rabbitmq-c/*:shared=False
    """
    subprocess.call(['bash', '-c', command])
    command = """
        conan create . --user is --channel stable \
            -s compiler=gcc \
            -s compiler.version=11 \
            -s compiler.libcxx=libstdc++11 \
            -s build_type=Release \
            -b missing \
            -o:h rabbitmq-c/*:ssl=False \
            -o:h rabbitmq-c/*:shared=True
    """
    command = """
        conan create . --user is --channel stable \
            -s compiler=gcc \
            -s compiler.version=11 \
            -s compiler.libcxx=libstdc++11 \
            -s build_type=Release \
            -b missing \
            -o:h rabbitmq-c/*:ssl=True \
            -o:h rabbitmq-c/*:shared=False
    """
    subprocess.call(['bash', '-c', command])
    command = """
        conan create . --user is --channel stable \
            -s compiler=gcc \
            -s compiler.version=11 \
            -s compiler.libcxx=libstdc++11 \
            -s build_type=Release \
            -b missing \
            -o:h rabbitmq-c/*:ssl=True \
            -o:h rabbitmq-c/*:shared=True
    """
    subprocess.call(['bash', '-c', command])
    

if __name__ == "__main__":
    main()
