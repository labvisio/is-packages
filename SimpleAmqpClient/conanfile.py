from conans import ConanFile, CMake, tools


class SimpleamqpclientConan(ConanFile):
    name = "SimpleAmqpClient"
    version = "2.5.0"
    license = "<Put the package license here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Simpleamqpclient here>"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"
    requires = "rabbitmq-c/0.9.0@picoreti/testing", "boost/1.67.0@conan/stable"

    def source(self):
        self.run("git clone https://github.com/alanxz/SimpleAmqpClient")
        self.run("cd SimpleAmqpClient && git checkout 6323892d3e8701489fb945f45aa877a7e2a0ce31")
        tools.replace_in_file("SimpleAmqpClient/CMakeLists.txt", "PROJECT(SimpleAmqpClient)",
                              '''PROJECT(SimpleAmqpClient)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()''')

    def build(self):
        cmake = CMake(self)
        cmake.definitions["ENABLE_TESTING"] = "OFF"
        cmake.configure(source_folder="SimpleAmqpClient")
        cmake.build()
        cmake.install()

    def package(self):
        pass

    def package_info(self):
        self.cpp_info.libs = ["SimpleAmqpClient"]
