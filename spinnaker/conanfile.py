from conans import ConanFile, tools

class SpinnakerConan(ConanFile):
    name = "spinnaker"
    version = "1.10.0.31"
    license = ""
    url = ""
    description = ""
    settings = "os", "compiler", "build_type", "arch"
    exports = 'artifacts/*'

    def system_requirements(self):
        pack_names = ['libavcodec-ffmpeg56', 'libavformat-ffmpeg56', 'libswscale-ffmpeg3', \
                      'libswresample-ffmpeg1', 'libavutil-ffmpeg54', 'libusb-1.0-0' ]
        installer = tools.SystemPackageTool()
        installer.update()  # Update the package database
        installer.install(" ".join(pack_names))  # Install the package

    def build(self):
        tools.untargz('artifacts/spinnaker.tar.gz')

    def package(self):
        self.copy("*", dst="lib", src="lib", symlinks=True)
        self.copy("*", dst="include", src="include", keep_path=True)

    def package_info(self):
        self.cpp_info.libs = [ 'GCBase_gcc540_v3_0',      \
                               'GenApi_gcc540_v3_0',      \
                               'log4cpp_gcc540_v3_0',     \
                               'Log_gcc540_v3_0',         \
                               'MathParser_gcc540_v3_0',  \
                               'NodeMapData_gcc540_v3_0', \
                               'Spinnaker_C',             \
                               'Spinnaker',               \
                               'XmlParser_gcc540_v3_0',   \
                               'ptgreyvideoencoder' ]
