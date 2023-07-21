import os

from conan import ConanFile
from conan.tools.files import copy, get
from conan.tools.layout import basic_layout


class Expected(ConanFile):
    name = 'expected'
    version = '0.3.0'
    license = 'CC0-1.0'
    url = 'https://github.com/labviros/is-packages'
    homepage = 'https://github.com/TartanLlama/expected'
    description = 'Single header implementation of std::expected'
    settings = 'os', 'compiler', 'build_type', 'arch'
    package_type = 'header-library'

    def source(self):
        get(
            conanfile=self,
            url=self.conan_data['sources'][self.version]['url'],
            sha256=self.conan_data['sources'][self.version]['sha256'],
            destination=self.source_folder,
            strip_root=True,
        )

    def layout(self):
        basic_layout(conanfile=self, src_folder='src')

    def package(self):
        copy(
            conanfile=self,
            pattern="COPYING",
            src=self.source_folder,
            dst=os.path.join(self.package_folder, "licenses"),
        )
        copy(
            conanfile=self,
            pattern="*",
            src=os.path.join(self.source_folder, "tl"),
            dst=os.path.join(self.package_folder, "include/tl"),
        )

    def package_info(self):
        self.cpp_info.set_property("pkg_config_name", "expected")
        self.cpp_info.set_property("cmake_file_name", "expected")
        self.cpp_info.set_property("cmake_target_name", "expected::expected")
        self.cpp_info.components["expected"].libs = ["tl"]
