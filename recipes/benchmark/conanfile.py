import os

from conan import ConanFile
from conan.tools.files import copy, get, rmdir
from conan.tools.cmake import CMake, CMakeToolchain, cmake_layout


class Benchmark(ConanFile):
    name = 'benchmark'
    version = '1.4.1'
    license = 'Apache-2.0'
    url = 'https://github.com/labvisio/is-packages'
    homepage = 'https://github.com/google/benchmark'
    description = 'A microbenchmark support library'
    settings = 'os', 'compiler', 'build_type', 'arch'
    options = {
        'shared': [True, False],
        'fPIC': [True, False],
    }
    default_options = {
        'shared': False,
        'fPIC': True,
    }

    def configure(self):
        if self.options.shared:
            self.options.rm_safe('fPIC')

    def layout(self):
        cmake_layout(conanfile=self, src_folder='src')

    def source(self):
        get(
            conanfile=self,
            url=self.conan_data['sources'][self.version]['url'],
            sha256=self.conan_data['sources'][self.version]['sha256'],
            destination=self.source_folder,
            strip_root=True,
        )

    def generate(self):
        tc = CMakeToolchain(self)
        tc.variables['BENCHMARK_ENABLE_TESTING'] = 'OFF'
        tc.variables['BENCHMARK_ENABLE_GTEST_TESTS'] = 'OFF'
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        copy(
            conanfile=self,
            pattern='LICENSE',
            src=self.source_folder,
            dst=os.path.join(self.package_folder, 'licenses'),
        )
        cmake = CMake(self)
        cmake.install()
        rmdir(
            conanfile=self,
            path=os.path.join(self.package_folder, "lib", "pkgconfig"),
        )
        rmdir(
            conanfile=self,
            path=os.path.join(self.package_folder, "lib", "cmake"),
        )
        rmdir(
            conanfile=self,
            path=os.path.join(self.package_folder, "share"),
        )

    def package_info(self):
        self.cpp_info.set_property('cmake_file_name', 'benchmark')
        self.cpp_info.set_property('cmake_target_name', 'benchmark::benchmark')
        self.cpp_info.set_property('pkg_config_name', 'benchmark')
        self.cpp_info.components['benchmark'].libs = ['benchmark', 'benchmark_main']
        self.cpp_info.components['benchmark'].system_libs.extend(['pthread', 'rt', 'm'])
