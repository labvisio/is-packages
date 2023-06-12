import os

from conan import ConanFile
from conan.tools.files import copy, get, rmdir
from conan.tools.cmake import CMake, CMakeDeps, CMakeToolchain, cmake_layout


class ZipkincppopentracingConan(ConanFile):
    name = "zipkin-cpp-opentracing"
    version = "0.3.1"
    license = "Apache-2.0"
    url = "https://github.com/labvisio/is-packages"
    homepage = "https://github.com/rnburn/zipkin-cpp-opentracing"
    description = "OpenTracing Tracer implementation for Zipkin in C++"
    settings = "os", "compiler", "build_type", "arch"
    options = {
        "shared": [True],
        "fPIC": [True, False],
    }
    default_options = {
        "shared": True,
        "fPIC": True,
    }

    def configure(self):
        if self.options.shared:
            self.options.rm_safe("fPIC")
        self.options["libcurl"].shared = self.options.shared
        self.options["opentracing-cpp"].shared = self.options.shared

    def requirements(self):
        self.requires("libcurl/7.76.0")
        self.requires("opentracing-cpp/1.4.0@is/stable")

    def layout(self):
        cmake_layout(self, src_folder="src")

    def source(self):
        get(self, **self.conan_data["sources"][self.version],
            destination=self.source_folder, strip_root=True)

    def generate(self):
        tc = CMakeToolchain(self)
        tc.variables["BUILD_SHARED_LIBS"] = self.options.shared
        tc.variables["BUILD_STATIC_LIBS"] = not self.options.shared
        tc.variables["BUILD_TESTING"] = False
        tc.generate()
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
        target = "zipkin-cpp-opentracing"
        self.cpp_info.set_property("pkg_config_name", target)
        self.cpp_info.set_property("cmake_file_name", target)
        self.cpp_info.set_property("cmake_target_name", f"zipkin-cpp-opentracing::{target}")
        self.cpp_info.components["zipkin-cpp-opentracing"].libs = ["zipkin", "zipkin_opentracing"]
        self.cpp_info.components["zipkin-cpp-opentracing"].requires = [
            "opentracing-cpp::opentracing-cpp",
            "libcurl::libcurl",
        ]
