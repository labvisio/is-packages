import os

from conan import ConanFile
from conan.tools.files import copy, unzip
from conan.tools.system.package_manager import Apt


class FlyCapture2Conan(ConanFile):
    name = "flycapture2"
    version = "2.13.3.31"
    license = ""
    url = ""
    description = ""
    settings = "os", "compiler", "build_type", "arch"
    exports_sources = 'artifacts/*'

    def system_requirements(self):
        pack_names = [
          'libraw1394-11',
          'libavcodec58',
          'libavformat58',
          'libswscale5',
          'libswresample3',
          'libavutil56',
          'libgtkmm-2.4-1v5',
          'libglademm-2.4-1v5',
          'libgtkglextmm-x11-1.2-0v5',
          'libgtkmm-2.4-dev',
          'libglademm-2.4-dev',
          'libgtkglextmm-x11-1.2-dev',
          'libusb-1.0-0',
        ]
        Apt(self).install(pack_names, update=True, check=True)

    def build(self):
        unzip(self, filename=os.path.join(self.build_folder, 'artifacts/flycapture2.tar.gz'))

    def package(self):
      copy(self, "*", src=os.path.join(self.source_folder, 'lib'), dst=os.path.join(self.package_folder, "lib"))
      copy(self, "*", src=os.path.join(self.source_folder, 'include'), dst=os.path.join(self.package_folder, "include"))

    def package_info(self):
        self.cpp_info.set_property("pkg_config_name", "flycapture2")
        self.cpp_info.set_property("cmake_file_name", "flycapture2")
        self.cpp_info.set_property("cmake_target_name", "flycapture2::flycapture2")
        self.cpp_info.components["flycapture2"].libs = [
          'flycapture',
          'flycapturegui',
          'multisync',
          'flycapturevideo',
        ]
