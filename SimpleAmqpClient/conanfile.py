from conans import ConanFile, CMake, tools


class SimpleamqpclientConan(ConanFile):
    name = "SimpleAmqpClient"
    version = "2.5.0"
    license = ""
    url = ""
    description = ""
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = "shared=False", "fPIC=True"
    generators = "cmake"
    requires = "rabbitmq-c/0.9.0@is/stable", "boost/1.67.0@conan/stable"

    def configure(self):
        if self.options.shared:
            self.options["boost"].fPIC = True
            self.options["rabbitmq-c"].fPIC = True

    def source(self):
        self.run("git clone https://github.com/alanxz/SimpleAmqpClient")
        self.run("cd SimpleAmqpClient && git checkout 6323892d3e8701489fb945f45aa877a7e2a0ce31")
        tools.replace_in_file("SimpleAmqpClient/CMakeLists.txt", "PROJECT(SimpleAmqpClient)",
                              '''PROJECT(SimpleAmqpClient)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()''')

    def build(self):
        cmake = CMake(self)
        if not self.options.shared:
            cmake.definitions["CMAKE_POSITION_INDEPENDENT_CODE"] = self.options.fPIC

        cmake.definitions["ENABLE_TESTING"] = "OFF"
        cmake.configure(source_folder="SimpleAmqpClient")
        cmake.build()
        cmake.install()

    def package(self):
        pass

    def package_info(self):
        self.cpp_info.libs = ["SimpleAmqpClient"]
