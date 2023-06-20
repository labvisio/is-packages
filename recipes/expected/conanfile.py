import os

from conan import ConanFile
from conan.tools.files import copy, get
from conan.tools.layout import basic_layout

class ExpectedConan(ConanFile):
    name = "expected"
    version = "0.3.0"
    license = "CC0-1.0"
    url = "https://github.com/labviros/is-packages"
    homepage = "https://github.com/TartanLlama/expected"
    description = "Single header implementation of std::expected with functional-style extensions."
    settings = "os", "compiler", "build_type", "arch"
    package_type = "header-library"
    # no_copy_source = T

    def source(self):
        get(self, **self.conan_data["sources"][self.version],
            destination=self.source_folder, strip_root=True)

    def layout(self):
        basic_layout(self, src_folder="src")

    def build(self):
        pass

    def package(self):
        copy(self, "COPYING", src=self.source_folder, dst=os.path.join(self.package_folder, "licenses"))
        copy(self, "*", src=os.path.join(self.source_folder, "tl"), dst=os.path.join(self.package_folder, "include/tl"))

    def package_info(self):
        self.cpp_info.set_property("pkg_config_name", "expected")
        self.cpp_info.set_property("cmake_file_name", "expected")
        self.cpp_info.set_property("cmake_target_name", "expected::expected")
        self.cpp_info.components["expected"].libs = ["tl"]
        # self.cpp_info.bindirs = []
        # self.cpp_info.frameworkdirs = []
        # self.cpp_info.libdirs = []
        # self.cpp_info.resdirs = []
