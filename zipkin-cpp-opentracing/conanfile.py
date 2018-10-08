from conans import ConanFile, CMake, tools


class ZipkincppopentracingConan(ConanFile):
    name = "zipkin-cpp-opentracing"
    version = "0.3.1"
    license = ""
    url = "https://github.com/labviros/is-packages"
    description = ""
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = "shared=False", "fPIC=True"
    generators = "cmake"
    requires = ("libcurl/7.61.1@bincrafters/stable", "opentracing-cpp/1.4.0@is/stable")

    def configure(self):
        if self.options.shared:
            self.options["libcurl"].fPIC = True
            self.options["opentracing-cpp"].fPIC = True

    def source(self):
        self.run("git clone https://github.com/rnburn/zipkin-cpp-opentracing")
        self.run("cd zipkin-cpp-opentracing && git checkout v0.3.1")
        tools.replace_in_file(
            "zipkin-cpp-opentracing/CMakeLists.txt", "project(zipkin-opentracing)",
            '''project(zipkin-opentracing)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()''')

    def build(self):
        cmake = CMake(self)
        cmake.definitions["BUILD_TESTING"] = "OFF"
        if not self.options.shared:
            cmake.definitions["CMAKE_POSITION_INDEPENDENT_CODE"] = self.options.fPIC
        cmake.configure(source_folder="zipkin-cpp-opentracing")
        cmake.build()
        cmake.install()

    def package(self):
        pass

    def package_info(self):
        self.cpp_info.libs = ["zipkin_opentracing", "zipkin"]
