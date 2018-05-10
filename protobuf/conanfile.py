from conans import ConanFile, CMake, tools


class ProtobufConan(ConanFile):
    name = "protobuf"
    version = "3.5.2"
    license = "<Put the package license here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Protobuf here>"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"
    requires = "zlib/1.2.11@conan/stable"

    def source(self):
        self.run("git clone https://github.com/google/protobuf")
        self.run("cd protobuf && git checkout v3.5.2")
        tools.replace_in_file("protobuf/cmake/CMakeLists.txt", "project(protobuf C CXX)",
                              '''project(protobuf C CXX)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()''')

    def build(self):
        cmake = CMake(self)
        cmake.definitions["protobuf_BUILD_TESTS"] = "OFF"
        cmake.configure(source_folder="protobuf/cmake")
        cmake.build()
        cmake.install()

    def package(self):
        pass

    def package_info(self):
        self.cpp_info.libs = ["protobuf"]
