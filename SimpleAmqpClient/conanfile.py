from conans import ConanFile, CMake, tools


class SimpleamqpclientConan(ConanFile):
    name = "SimpleAmqpClient"
    version = "2.5.0"
    license = ""
    url = "https://github.com/labviros/is-packages"
    description = ""
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False], "with_openssl": [True, False]}
    default_options = "shared=True", "fPIC=True", "with_openssl=False"
    generators = "cmake"
    requires = ("rabbitmq-c/0.9.0@is/stable", "boost/1.66.0@conan/stable")

    def configure(self):
        self.options["boost"].shared = self.options.shared 
        self.options["rabbitmq-c"].shared = self.options.shared 
        self.options["rabbitmq-c"].with_openssl = self.options.with_openssl

    def source(self):
        self.run("git clone https://github.com/alanxz/SimpleAmqpClient")
        self.run("cd SimpleAmqpClient && git checkout 6323892d3e8701489fb945f45aa877a7e2a0ce31")
        tools.replace_in_file(
            "SimpleAmqpClient/CMakeLists.txt", "PROJECT(SimpleAmqpClient)",
            '''PROJECT(SimpleAmqpClient)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()''')

    def build(self):
        cmake = CMake(self)
        if not self.options.shared:
            cmake.definitions["CMAKE_POSITION_INDEPENDENT_CODE"] = self.options.fPIC
        cmake.definitions["ENABLE_SSL_SUPPORT"] = self.options.with_openssl
        cmake.definitions["ENABLE_TESTING"] = "OFF"
        cmake.configure(source_folder="SimpleAmqpClient")
        cmake.build()
        cmake.install()

    def package(self):
        pass

    def package_info(self):
        self.cpp_info.libs = ["SimpleAmqpClient"]
