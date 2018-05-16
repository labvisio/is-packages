from conans import ConanFile, CMake, tools


class IswireConan(ConanFile):
    name = "is-wire"
    version = "1.1.0"
    license = ""
    url = "https://github.com/labviros/is-packages"
    description = ""
    settings = "os", "compiler", "build_type", "arch"
    options = {"fPIC": [True, False]}
    default_options = "fPIC=True", "spdlog:fmt_external=False"
    generators = "cmake"
    requires = ("spdlog/[>=0.15]@bincrafters/stable", "prometheus-cpp/[>=0.4]@is/stable",
                "is-msgs/[>=1.1]@is/stable", "protobuf/[>=3.0]@bincrafters/stable",
                "SimpleAmqpClient/[>=2.0]@is/stable", "boost/[>=1.65]@conan/stable",
                "opentracing-cpp/[>=1.0]@is/stable")

    def configure(self):
        #self.options["spdlog"].fPIC = True
        self.options["prometheus-cpp"].fPIC = True
        self.options["is-msgs"].fPIC = True
        self.options["protobuf"].fPIC = True
        self.options["SimpleAmqpClient"].fPIC = True
        self.options["SimpleAmqpClient"].with_openssl = False
        self.options["boost"].fPIC = True
        self.options["opentracing-cpp"].fPIC = True

    def source(self):
        self.run("git clone https://github.com/labviros/is-wire")
        self.run("cd is-wire && git checkout v1.1.0")
        tools.replace_in_file(
            "is-wire/CMakeLists.txt", "project(is-wire)", '''project(is-wire)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()''')

    def build(self):
        cmake = CMake(self)
        cmake.definitions["enable_tests"] = "OFF"
        cmake.definitions["CMAKE_POSITION_INDEPENDENT_CODE"] = self.options.fPIC
        cmake.configure(source_folder="is-wire")
        cmake.build()
        cmake.install()

    def package(self):
        pass

    def package_info(self):
        self.cpp_info.libs = ["is-wire-rpc", "is-wire-core"]
