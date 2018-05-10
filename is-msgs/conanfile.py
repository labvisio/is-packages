from conans import ConanFile, CMake, tools


class IsmsgsConan(ConanFile):
    name = "is-msgs"
    version = "1.1.0"
    license = "<Put the package license here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Ismsgs here>"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"
    requires = "protobuf/3.5.2@picoreti/testing"

    def source(self):
        self.run("git clone https://github.com/labviros/is-msgs")
        self.run("cd is-msgs && git checkout 2327d69291375209091b97a59c5f65f95b07b960")
        tools.replace_in_file("is-msgs/CMakeLists.txt", 'set(module "msgs")',
                              '''set(module "msgs")
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()''')

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="is-msgs")
        cmake.build()
        cmake.install()

    def package(self):
        pass

    def package_info(self):
        self.cpp_info.libs = ["is-msgs"]
