from conans import ConanFile, CMake, tools


class IsmsgsConan(ConanFile):
    name = "is-msgs"
    version = "1.1.2"
    license = ""
    url = "https://github.com/labviros/is-packages"
    description = ""
    settings = "os", "compiler", "build_type", "arch"
    options = {"fPIC": [True, False]}
    default_options = "fPIC=True", "spdlog:fmt_external=False"
    generators = "cmake"
    requires = "protobuf/[>=3.0]@bincrafters/stable"
    build_requires = "spdlog/[>0.15]@bincrafters/stable"

    def source(self):
        self.run("git clone https://github.com/labviros/is-msgs")
        self.run("cd is-msgs && git checkout v1.1.2")
        tools.replace_in_file(
            "is-msgs/CMakeLists.txt", 'set(module "msgs")', '''set(module "msgs")
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()''')

    def build(self):
        cmake = CMake(self)
        cmake.definitions["CMAKE_POSITION_INDEPENDENT_CODE"] = self.options.fPIC
        cmake.definitions["enable_tests"] = "OFF"
        cmake.configure(source_folder="is-msgs")
        cmake.build()
        cmake.install()

    def package(self):
        pass

    def package_info(self):
        self.cpp_info.libs = ["is-msgs"]
