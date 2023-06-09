import os

from conan import ConanFile
from conan.tools.scm import Git
from conan.tools.cmake import CMake, CMakeDeps, CMakeToolchain, cmake_layout
from conan.tools.files import copy, rmdir, apply_conandata_patches, export_conandata_patches


class PrometheusCppConan(ConanFile):
    name = "prometheus-cpp"
    version = "0.4.1"
    license = ""
    url = "https://github.com/labvisio/is-packages"
    description = ""
    settings = "os", "compiler", "build_type", "arch"
    options = {
        "shared": [True, False],
        "fPIC": [True, False],
    }
    default_options = {
        "shared": True,
        "fPIC": True,
    }

    def export_sources(self):
        export_conandata_patches(self)

    def requirements(self):
        self.requires("zlib/1.2.13")

    def source(self):
        git = Git(self)
        git.clone(url="https://github.com/jupp0r/prometheus-cpp", target=".")
        git.run("checkout v0.4.1")
        git.run("submodule update --init")
        apply_conandata_patches(self)

    def layout(self):
        cmake_layout(self, src_folder="src")

    def generate(self):
        tc = CMakeToolchain(self, generator="Ninja")
        tc.generate()
        deps = CMakeDeps(self)
        deps.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        copy(self,
             pattern="LICENSE",
             dst=os.path.join(self.package_folder, "licenses"),
             src=self.source_folder)
        cmake = CMake(self)
        cmake.install()
        rmdir(self, os.path.join(self.package_folder, "lib", "cmake"))
        rmdir(self, os.path.join(self.package_folder, "lib", "pkgconfig"))

    def package_info(self):
        self.cpp_info.set_property("cmake_file_name", "prometheus-cpp")
        self.cpp_info.components["prometheus-cpp"].set_property("cmake_file_name", "prometheus-cpp")
        self.cpp_info.components["prometheus-cpp"].set_property("cmake_target_name", "prometheus-cpp::prometheus-cpp")
        self.cpp_info.components["prometheus-cpp"].set_property("pkg_config_name", "prometheus-cpp")
        self.cpp_info.components["prometheus-cpp"].libs = ["prometheus-cpp"]
        if self.settings.os in ["Linux", "FreeBSD"]:
            self.cpp_info.components["prometheus-cpp"].system_libs = ["pthread", "rt"]
        self.cpp_info.components["prometheus-cpp"].requires =["zlib::zlib"]
