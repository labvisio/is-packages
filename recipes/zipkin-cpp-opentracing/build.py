import subprocess


def main():
    command = """
        conan create . --user is --channel stable \
            -s compiler=gcc \
            -s compiler.version=11 \
            -s compiler.libcxx=libstdc++11 \
            -s build_type=Release \
            -b missing \
            -o:h zipkin-cpp-opentracing/*:shared=True \
    """
    subprocess.call(['bash', '-c', command])
    command = """
        conan create . --user is --channel stable \
            -s compiler=gcc \
            -s compiler.version=11 \
            -s compiler.libcxx=libstdc++11 \
            -s build_type=Debug \
            -b missing \
            -o:h zipkin-cpp-opentracing/*:shared=True \
    """
    subprocess.call(['bash', '-c', command])


if __name__ == "__main__":
    main()
