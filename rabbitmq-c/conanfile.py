from conans import ConanFile, CMake, tools

class RabbitMQConan(ConanFile):
    name = "rabbitmq-c"
    version = "0.9.0"
    license = ""
    url = ""
    description = ""
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "with_ssl": [True, False]}
    default_options = "shared=False", "with_ssl=True"
    generators = "cmake"

    def requirements(self):
        if self.options.with_ssl == True:
            self.requires("OpenSSL/1.0.2o@conan/stable")
    
    def source(self):
        self.run("git clone https://github.com/alanxz/rabbitmq-c")
        self.run("cd rabbitmq-c && git checkout v0.9.0")

    def build(self):
        cmake = CMake(self)
        cmake.definitions["ENABLE_SSL_SUPPORT"] = "ON" if self.options.with_ssl == True else "OFF"
        cmake.definitions["BUILD_EXAMPLES"] = "OFF"
        cmake.definitions["BUILD_TESTS"] = "OFF"
        cmake.configure(source_folder="rabbitmq-c")
        cmake.build()
        #cmake.install()

    def package(self):
        self.copy("*.h", dst="include", src="rabbitmq-c/librabbitmq")
        self.copy("*rabbitmq.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["rabbitmq"]
