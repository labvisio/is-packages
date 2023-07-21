import os

from conan import ConanFile
from conan.tools.scm import Git
from conan.tools.files import copy, rmdir
from conan.tools.cmake import CMake, CMakeDeps, CMakeToolchain, cmake_layout


class SimpleAmqpClient(ConanFile):
    name = "simpleamqpclient"
    version = "2.5.0"
    license = "MIT"
    url = "https://github.com/labvisio/is-packages"
    homepage = "https://github.com/alanxz/SimpleAmqpClient"
    description = "Simple C++ Interface to rabbitmq-c"
    settings = "os", "compiler", "build_type", "arch"
    package_type = "library"
    options = {
        "shared": [True, False],
        "fPIC": [True, False],
        "with_openssl": [True, False],
    }
    default_options = {
        "shared": True,
        "fPIC": True,
        "with_openssl": False,
    }

    def requirements(self):
        self.requires("rabbitmq-c/0.9.0@is/stable")
        self.requires("boost/1.80.0", transitive_headers=True)

    def configure(self):
        if self.options.shared:
            self.options.rm_safe("fPIC")
        self.options["boost"].shared = self.options.shared
        self.options["rabbitmq-c"].shared = self.options.shared
        self.options["rabbitmq-c"].with_openssl = self.options.with_openssl

    def layout(self):
        cmake_layout(conanfile=self, src_folder="src")

    def source(self):
        git = Git(self)
        git.clone(url="https://github.com/alanxz/SimpleAmqpClient", target=".")
        git.run("checkout 6323892d3e8701489fb945f45aa877a7e2a0ce31")

    def generate(self):
        tc = CMakeToolchain(self)
        tc.variables["ENABLE_SSL_SUPPORT"] = self.options.with_openssl
        tc.variables["ENABLE_TESTING"] = "OFF"
        tc.generate()
        deps = CMakeDeps(self)
        deps.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        copy(
            conanfile=self,
            pattern="LICENSE-MIT",
            src=self.source_folder,
            dst=os.path.join(self.package_folder, "licenses"),
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

    def package_info(self):
        self.cpp_info.set_property("pkg_config_name", "SimpleAmqpClient")
        self.cpp_info.set_property("cmake_file_name", "SimpleAmqpClient")
        self.cpp_info.set_property("cmake_target_name", "SimpleAmqpClient::SimpleAmqpClient")
        self.cpp_info.components["SimpleAmqpClient"].libs = ["SimpleAmqpClient"]
        self.cpp_info.components["SimpleAmqpClient"].requires = [
            "rabbitmq-c::rabbitmq-c", "boost::boost"
        ]
