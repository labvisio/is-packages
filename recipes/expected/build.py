import subprocess


def main():
    options_build_type = ["Debug", "Release"]
    for build_type in options_build_type:
        command = f"""
            conan create . --user is --channel stable \
                -s compiler=gcc \
                -s compiler.version=11 \
                -s compiler.libcxx=libstdc++11 \
                -s build_type={build_type} \
                -b missing
        """
        subprocess.call(['bash', '-c', command])


if __name__ == "__main__":
    main()
