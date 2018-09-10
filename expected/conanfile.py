from conans import ConanFile, CMake, tools


class ExpectedConan(ConanFile):
    name = "expected"
    version = "0.3.0"
    license = ""
    url = "https://github.com/labviros/is-packages"
    description = ""
    settings = "os", "compiler", "build_type", "arch"

    def source(self):
        self.run("git clone https://github.com/TartanLlama/expected")

    def package(self):
        self.copy("*.hpp", dst="include/tl/", src="expected/tl/")

    def package_id(self):
        self.info.header_only()
