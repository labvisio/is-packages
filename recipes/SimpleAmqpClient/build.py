import subprocess


def main():
    options_ssl = [True, False]
    options_shared = [True, False]
    options_build_type = ["Debug", "Release"]
    for shared in options_shared:
        for ssl in options_ssl:
            for build_type in options_build_type:
                command = f"""
                    conan create . --user is --channel stable \
                        -s compiler=gcc \
                        -s compiler.version=11 \
                        -s compiler.libcxx=libstdc++11 \
                        -s build_type={build_type} \
                        -b missing \
                        -o:h simpleamqpclient/*:shared={shared} \
                        -o:h simpleamqpclient/*:with_openssl={ssl}
                """
                subprocess.call(['bash', '-c', command])

if __name__ == "__main__":
    main()
