from conans import ConanFile, CMake, tools
import os


class AriaConan(ConanFile):
    name = "aria"
    version = "2.9.4"
    license = ""
    url = "https://github.com/labviros/is-packages"
    description = ""
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": False}
    source_subfolder = "source_subfolder"

    def source(self):
        tools.get(
            "http://robots.mobilerobots.com/ARIA/download/current/ARIA-src-{}.tar.gz".format(self.version))
        extracted_dir = "ARIA-src-" + self.version
        os.rename(extracted_dir, self.source_subfolder)

        tools.replace_in_file(
            os.path.join(self.source_subfolder, "Makefile"),
            "STATIC_TARGETS:=lib/libAria.a examples/demoStatic$(binsuffix)",
            "STATIC_TARGETS:=lib/libAria.a",
        )
        tools.replace_in_file(
            os.path.join(self.source_subfolder, "Makefile"),
            "TARGETS:=lib/libAria.$(sosuffix) examples/demo$(binsuffix)",
            "TARGETS:=lib/libAria.$(sosuffix)",
        )

    def build(self):
        if self.options.shared:
            self.run("cd {} && make all".format(self.source_subfolder))
        else:
            self.run("cd {} && make static".format(self.source_subfolder))

    def package(self):
        self.copy("*.a", "lib", "", keep_path=False)
        self.copy("*.so", "lib", "", keep_path=False)
        self.copy("{}/include/*.h".format(self.source_subfolder),
                  "include/Aria", "", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["Aria"]
        if not self.options.shared:
            self.cpp_info.libs.extend(["pthread", "dl"])

