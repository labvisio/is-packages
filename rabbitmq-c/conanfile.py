from conans import ConanFile, CMake, tools


class RabbitMQConan(ConanFile):
    name = "rabbitmq-c"
    version = "0.9.0"
    license = ""
    url = "https://github.com/labviros/is-packages"
    description = ""
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False], "with_openssl": [True, False]}
    default_options = "shared=False", "fPIC=True", "with_openssl=False"
    generators = "cmake"

    def requirements(self):
        if self.options.with_openssl:
            self.requires("OpenSSL/1.0.2n@conan/stable")

    def source(self):
        self.run("git clone https://github.com/alanxz/rabbitmq-c")
        self.run("cd rabbitmq-c && git checkout v0.9.0")

    def build(self):
        cmake = CMake(self)
        cmake.definitions["ENABLE_SSL_SUPPORT"] = "ON" if self.options.with_openssl else "OFF"
        cmake.definitions["BUILD_STATIC_LIBS"] = "OFF" if self.options.shared else "ON"
        if not self.options.shared:
            cmake.definitions["CMAKE_POSITION_INDEPENDENT_CODE"] = self.options.fPIC
        cmake.definitions["BUILD_EXAMPLES"] = "OFF"
        cmake.definitions["BUILD_TESTS"] = "OFF"
        cmake.configure(source_folder="rabbitmq-c")
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include", src="rabbitmq-c/librabbitmq")
        self.copy("*rabbitmq.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["rabbitmq"]

    def configure(self):
        del self.settings.compiler.libcxx