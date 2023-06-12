import subprocess


def main():
    command = """
        conan create . --user is --channel stable \
            -s compiler=gcc \
            -s compiler.version=11 \
            -s compiler.libcxx=libstdc++11 \
            -s build_type=Debug \
            -b missing \
    """
    subprocess.call(['bash', '-c', command])
    command = """
        conan create . --user is --channel stable \
            -s compiler=gcc \
            -s compiler.version=11 \
            -s compiler.libcxx=libstdc++11 \
            -s build_type=Release \
            -b missing \
    """
    subprocess.call(['bash', '-c', command])


if __name__ == "__main__":
    main()
