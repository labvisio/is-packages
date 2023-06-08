from conan import ConanFile
from conan.tools.cmake import CMake, CMakeDeps, CMakeToolchain, cmake_layout
from conan.tools.files import copy, get, rmdir
from conan.tools.scm import Version
import os

required_conan_version = ">=1.53.0"


class RabbitmqcConan(ConanFile):
    name = "rabbitmq-c"
    version = "0.9.0"
    license = "MIT"
    url = "https://github.com/conan-io/conan-center-index"
    homepage = "https://github.com/alanxz/rabbitmq-c"
    description = "This is a C-language AMQP client library for use with v2.0+ of the RabbitMQ broker."
    topics = ("rabbitmq", "message queue")
    package_type = "library"
    settings = "os", "arch", "compiler", "build_type"
    options = {
        "shared": [True, False],
        "fPIC": [True, False],
        "ssl": [True, False],
    }
    default_options = {
        "shared": True,
        "fPIC": True,
        "ssl": True,
    }

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def configure(self):
        if self.options.shared:
            self.options.rm_safe("fPIC")
        if self.options.ssl:
            self.options["OpenSSL"].shared = self.options.shared
        self.settings.rm_safe("compiler.libcxx")
        self.settings.rm_safe("compiler.cppstd")

    def requirements(self):
        if self.options.ssl:    
            self.requires("openssl/[>=1.1 <4]")

    def layout(self):
        cmake_layout(self, src_folder="src")

    def source(self):
        get(self, **self.conan_data["sources"][self.version],
            destination=self.source_folder, strip_root=True)

    def generate(self):
        tc = CMakeToolchain(self, generator="Ninja")
        tc.variables["BUILD_EXAMPLES"] = False
        tc.cache_variables["BUILD_SHARED_LIBS"] = "ON" if self.options.shared else "OFF"
        tc.cache_variables["BUILD_STATIC_LIBS"] = "OFF" if self.options.shared else "ON"
        if Version(self.version) < "0.12.0":
            tc.variables["BUILD_TESTS"] = False
        else:
            tc.variables["BUILD_TESTING"] = False
        tc.variables["BUILD_TOOLS"] = False
        tc.variables["BUILD_TOOLS_DOCS"] = False
        tc.variables["ENABLE_SSL_SUPPORT"] = self.options.ssl
        tc.variables["BUILD_API_DOCS"] = False
        tc.variables["RUN_SYSTEM_TESTS"] = False
        if not self.options.shared:
            tc.variables["CMAKE_POSITION_INDEPENDENT_CODE"] = self.options.fPIC
        tc.generate()

        if self.options.ssl:
            deps = CMakeDeps(self)
            deps.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        copy(self, "LICENSE-MIT", src=self.source_folder, dst=os.path.join(self.package_folder, "licenses"))
        copy(self, "LICENSE", src=self.source_folder, dst=os.path.join(self.package_folder, "licenses"))
        cmake = CMake(self)
        cmake.install()
        rmdir(self, os.path.join(self.package_folder, "lib", "pkgconfig"))
        rmdir(self, os.path.join(self.package_folder, "lib", "cmake"))

    def package_info(self):
        rabbitmq_target = "rabbitmq" if self.options.shared else "rabbitmq-static"
        # self.cpp_info.libs = [rabbitmq_target]
        self.cpp_info.set_property("pkg_config_name", rabbitmq_target)
        self.cpp_info.set_property("cmake_file_name", "rabbitmq-c")
        self.cpp_info.set_property("cmake_target_name", f"rabbitmq::{rabbitmq_target}")
        self.cpp_info.set_property("pkg_config_name", "librabbitmq")
        if not self.options.shared:
            self.cpp_info.components["rabbitmq"].defines.append("AMQP_STATIC")
        if self.options.ssl:
            self.cpp_info.components["rabbitmq"].requires.append("openssl::openssl")