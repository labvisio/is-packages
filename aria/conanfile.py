from conans import ConanFile, CMake, tools
import os


class AriaConan(ConanFile):
    name = "aria"
    version = "2.9.4"
    license = ""
    url = "https://github.com/labviros/is-packages"
    description = ""
    settings = "os", "compiler", "build_type", "arch"

    source_subfolder = "source_subfolder"

    def source(self):
        tools.get(
            "http://robots.mobilerobots.com/ARIA/download/current/ARIA-src-{}.tar.gz".format(self.version))
        extracted_dir = "ARIA-src-" + self.version
        os.rename(extracted_dir, self.source_subfolder)

    def build(self):
        self.run("cd {} && make allLibs".format(self.source_subfolder))

    def package(self):
        self.copy("*.a", "lib", "", keep_path=False)
        self.copy("*.so", "lib", "", keep_path=False)
        self.copy("{}/include/*.h".format(self.source_subfolder),
                  "include/Aria", "", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["Aria",  "ArNetworking"]
