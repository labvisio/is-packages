from conans import ConanFile, CMake, tools


class BenchmarkConan(ConanFile):
    name = "benchmark"
    version = "1.4.1"
    license = "Apache2"
    url = "https://github.com/google/benchmark"
    description = "A microbenchmark support library"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = "shared=False", "fPIC=True"
    generators = "cmake"

    def source(self):
        self.run("git clone https://github.com/google/benchmark")
        self.run("cd benchmark && git checkout v1.4.1")
        tools.replace_in_file(
            "benchmark/CMakeLists.txt", "project (benchmark)", '''project (benchmark)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()''')

    def build(self):
        cmake = CMake(self)
        if not self.options.shared:
            cmake.definitions["CMAKE_POSITION_INDEPENDENT_CODE"] = self.options.fPIC
        cmake.definitions["BENCHMARK_ENABLE_GTEST_TESTS"] = "OFF"
        cmake.configure(source_folder="benchmark")
        cmake.build()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["benchmark", "benchmark_main", "pthread"]
