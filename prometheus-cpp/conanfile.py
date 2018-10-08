from conans import ConanFile, CMake, tools


class PrometheuscppConan(ConanFile):
    name = "prometheus-cpp"
    version = "0.4.1"
    license = ""
    url = "https://github.com/labviros/is-packages"
    description = ""
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = "shared=True", "fPIC=True"
    generators = "cmake"
    requires = "protobuf/3.6.1@bincrafters/stable", "zlib/1.2.11@conan/stable"

    def configure(self):
        if self.options.shared:
            self.options["protobuf"].shared = True
            self.options["zlib"].shared = True

    def source(self):
        self.run("git clone https://github.com/jupp0r/prometheus-cpp")
        self.run("cd prometheus-cpp && git checkout v0.4.1 && git submodule update --init")
        tools.replace_in_file(
            "prometheus-cpp/CMakeLists.txt", "project(prometheus-cpp)", '''project(prometheus-cpp)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()''')

    def build(self):
        cmake = CMake(self)
        if not self.options.shared:
            cmake.definitions["CMAKE_POSITION_INDEPENDENT_CODE"] = self.options.fPIC
        cmake.configure(source_folder="prometheus-cpp")
        cmake.build()
        cmake.install()

    def package(self):
        pass

    def package_info(self):
        self.cpp_info.libs = ["prometheus-cpp"]
