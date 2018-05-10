from conans import ConanFile, CMake, tools


class OpentracingcppConan(ConanFile):
    name = "opentracing-cpp"
    version = "1.4.0"
    license = "<Put the package license here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Opentracingcpp here>"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"

    def source(self):
        self.run("git clone https://github.com/opentracing/opentracing-cpp")
        self.run("cd opentracing-cpp && git checkout v1.4.0")
        tools.replace_in_file("opentracing-cpp/CMakeLists.txt", "project(opentracing-cpp)",
                              '''project(opentracing-cpp)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()''')

    def build(self):
        cmake = CMake(self)
        cmake.definitions["BUILD_TESTING"] = "OFF"
        cmake.configure(source_folder="opentracing-cpp")
        cmake.build()
        cmake.install()

    def package(self):
        pass

    def package_info(self):
        self.cpp_info.libs = ["opentracing"]
