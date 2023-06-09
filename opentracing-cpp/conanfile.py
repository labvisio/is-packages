import os

from conan import ConanFile
from conan.tools.files import copy, get, rmdir
from conan.tools.cmake import CMake, CMakeDeps, CMakeToolchain, cmake_layout

class OpenTracingCppConan(ConanFile):
    name = "opentracing-cpp"
    version = "1.4.0"
    license = ""
    url = "https://github.com/labvisio/is-packages"
    description = ""
    settings = "os", "compiler", "build_type", "arch"
    options = {
        "shared": [True, False],
        "fPIC": [True, False],
    }
    default_options = {
        "shared" : True,
        "fPIC": True,
    }

    def layout(self):
        cmake_layout(self, src_folder="src")

    def source(self):
        get(self, **self.conan_data["sources"][self.version],
            destination=self.source_folder, strip_root=True)

    def generate(self):
        cmake = CMakeToolchain(self)
        cmake.variables["BUILD_TESTING"] = "OFF"
        cmake.variables["ENABLE_LINTING"] = "OFF"
        cmake.variables["BUILD_SHARED_LIBS"] = self.options.shared
        cmake.variables["BUILD_STATIC_LIBS"] = not self.options.shared
        if not self.options.shared:
            cmake.variables["CMAKE_POSITION_INDEPENDENT_CODE"] = self.options.fPIC
        cmake.generate()
        deps = CMakeDeps(self)
        deps.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        copy(self, "LICENSE", src=self.source_folder, dst=os.path.join(self.package_folder, "licenses"))
        cmake = CMake(self)
        cmake.install()
        rmdir(self, os.path.join(self.package_folder, "lib", "pkgconfig"))
        rmdir(self, os.path.join(self.package_folder, "lib", "cmake"))


    def package_info(self):
        self.cpp_info.set_property("cmake_file_name", "opentracing")
        self.cpp_info.components["opentracing"].set_property("cmake_file_name", "opentracing")
        self.cpp_info.components["opentracing"].set_property("cmake_target_name", "opentracing::opentracing")
        self.cpp_info.components["opentracing"].set_property("pkg_config_name", "opentracing")
        self.cpp_info.components["opentracing"].libs = ["opentracing"]


