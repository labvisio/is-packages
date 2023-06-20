from conans import ConanFile, tools

class FlyCapture2Conan(ConanFile):
    name = "flycapture2"
    version = "2.12.3.31"
    license = ""
    url = ""
    description = ""
    settings = "os", "compiler", "build_type", "arch"
    exports = 'artifacts/*'

    def system_requirements(self):
        pack_names = [
          'libraw1394-11',             \
          'libavcodec-ffmpeg56',       \
          'libavformat-ffmpeg56',      \
          'libswscale-ffmpeg3',        \
          'libswresample-ffmpeg1',     \
          'libavutil-ffmpeg54',        \
          'libgtkmm-2.4-dev',          \
          'libglademm-2.4-dev',        \
          'libgtkglextmm-x11-1.2-dev', \
          'libusb-1.0-0'
        ]
        installer = tools.SystemPackageTool()
        installer.update()  # Update the package database
        installer.install(" ".join(pack_names))  # Install the package

    def build(self):
        tools.untargz('artifacts/flycapture2.tar.gz')

    def package(self):
        self.copy("*", dst="lib", src="lib", symlinks=True)
        self.copy("*", dst="include", src="include", keep_path=True)

    def package_info(self):
        self.cpp_info.libs = [
          'flycapture',      \
          'flycapturegui',   \
          'multisync',       \
          'ptgreyvideoencoder'
        ]
