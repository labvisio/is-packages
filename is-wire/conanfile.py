from conans import ConanFile, CMake, tools


class IswireConan(ConanFile):
    name = "is-wire"
    version = "1.1.0"
    license = ""
    url = ""
    description = ""
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = "shared=False", "fPIC=True", "spdlog:fmt_external=False"
    generators = "cmake"
    requires = (
        "spdlog/0.16.3@bincrafters/stable",
        "prometheus-cpp/0.4.1@is/stable",
        "is-msgs/1.1.0@is/stable",
        "protobuf/3.5.2@bincrafters/stable",
        "SimpleAmqpClient/2.5.0@is/stable",
        "boost/1.67.0@conan/stable",
        "opentracing-cpp/1.4.0@is/stable",
        "gtest/1.8.0@bincrafters/stable"
    )

    def configure(self):
        if self.options.shared:
            #self.options["spdlog"].fPIC = True
            self.options["prometheus-cpp"].fPIC = True
            self.options["is-msgs"].fPIC = True
            self.options["protobuf"].fPIC = True
            self.options["SimpleAmqpClient"].fPIC = True
            self.options["boost"].fPIC = True
            self.options["opentracing-cpp"].fPIC = True
            #self.options["gtest"].fPIC = True
 
    def source(self):
        self.run("git clone https://github.com/labviros/is-wire")
        self.run("cd is-wire && git checkout v1.1.0")
        tools.replace_in_file("is-wire/CMakeLists.txt", "project(is-wire)",
                              '''project(is-wire)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()''')

    def build(self):
        cmake = CMake(self)
        cmake.definitions["enable_tests"] = "OFF"
        if not self.options.shared:
            cmake.definitions["CMAKE_POSITION_INDEPENDENT_CODE"] = self.options.fPIC
        cmake.configure(source_folder="is-wire")
        cmake.build()
        cmake.install()

    def package(self):
        pass

    def package_info(self):
        self.cpp_info.libs = ["is-wire-rpc", "is-wire-core"]
