from conans import ConanFile, CMake, tools


class IswireConan(ConanFile):
    name = "is-wire"
    version = "1.1.0"
    license = "<Put the package license here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Iswire here>"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    generators = "cmake"
    requires = (
        "protobuf/3.5.2@picoreti/testing",
        "SimpleAmqpClient/2.5.0@picoreti/testing",
        "boost/1.67.0@conan/stable",
        "is-msgs/1.1.0@picoreti/testing",
        "opentracing-cpp/1.4.0@picoreti/testing",
        "prometheus-cpp/0.4.1@picoreti/testing",
        "gtest/1.8.0@bincrafters/stable",
        "spdlog/0.16.3@bincrafters/stable"
    )
    
    default_options = "shared=False", "spdlog:fmt_external=False"

    def source(self):
        self.run("git clone https://github.com/labviros/is-wire")
        self.run("cd is-wire && git checkout bb5c60facc362a00c4eb7d5482eaa2ca2c6aea0f")
        tools.replace_in_file("is-wire/CMakeLists.txt", "project(is-wire)",
                              '''project(is-wire)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()''')

    def build(self):
        cmake = CMake(self)
        cmake.definitions["enable_tests"] = "OFF"
        cmake.configure(source_folder="is-wire")
        cmake.build()
        cmake.install()

    def package(self):
        pass

    def package_info(self):
        self.cpp_info.libs = ["is-wire"]
