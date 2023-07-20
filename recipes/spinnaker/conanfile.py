import os

from conan import ConanFile
from conan.tools.scm import Git
from conan.tools.files import get, copy, rmdir, unzip, load
from conan.tools.system.package_manager import Apt


class SpinnakerConan(ConanFile):
    name = "spinnaker"
    version = "3.1.0.79"
    license = ""
    url = ""
    description = ""
    settings = "os", "compiler", "build_type", "arch"
    exports_sources = 'artifacts/*'

    def system_requirements(self):
        pack_names = [
            'libavcodec58',
            'libavformat58',
            'libswscale5',
            'libswresample3',
            'libavutil56',
            'libusb-1.0-0',
        ]
        Apt(self).install(pack_names, update=True, check=True)

    def build(self):
        unzip(self, filename=os.path.join(self.build_folder, 'artifacts/spinnaker.tar.gz'))

    def package(self):
        copy(self, "*", src=os.path.join(self.source_folder, 'lib'), dst=os.path.join(self.package_folder, "lib"))
        copy(self, "*", src=os.path.join(self.source_folder, 'include'), dst=os.path.join(self.package_folder, "include"))

    def package_info(self):
        self.cpp_info.set_property("pkg_config_name", "spinnaker")
        self.cpp_info.set_property("cmake_file_name", "spinnaker")
        self.cpp_info.set_property("cmake_target_name", "spinnaker::spinnaker")
        self.cpp_info.components["spinnaker"].libs = [
            'GCBase_gcc11_v3_0',
            'GenApi_gcc11_v3_0',
            'log4cpp_gcc11_v3_0',
            'Log_gcc11_v3_0',
            'MathParser_gcc11_v3_0',
            'NodeMapData_gcc11_v3_0',
            'Spinnaker',
            'Spinnaker_C',  
            'SpinVideo',
            'SpinVideo_C',
            'XmlParser_gcc11_v3_0',
        ]
