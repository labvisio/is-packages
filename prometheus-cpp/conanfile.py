from conans import ConanFile, CMake, tools


class PrometheuscppConan(ConanFile):
    name = "prometheus-cpp"
    version = "0.4.1"
    license = "<Put the package license here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Prometheuscpp here>"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"
    requires = "protobuf/3.5.2@picoreti/testing", "zlib/1.2.11@conan/stable"

    def source(self):
        self.run("git clone https://github.com/jupp0r/prometheus-cpp")
        self.run("cd prometheus-cpp && git checkout v0.4.1 && git submodule update --init")
        tools.replace_in_file("prometheus-cpp/CMakeLists.txt", "project(prometheus-cpp)",
                              '''project(prometheus-cpp)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()''')

    def build(self):
        cmake = CMake(self)
        cmake.definitions[""] = "OFF"
        cmake.configure(source_folder="prometheus-cpp")
        cmake.build()
        cmake.install()

    def package(self):
        pass

    def package_info(self):
        self.cpp_info.libs = ["prometheus-cpp"]

