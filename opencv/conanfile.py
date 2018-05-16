from conans import ConanFile, CMake, tools


class OpencvConan(ConanFile):
    name = "opencv"
    version = "3.3.1"
    license = ""
    url = "https://github.com/labviros/is-packages"
    description = ""
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = ("shared=False", "fPIC=True")
    generators = "cmake"
    requires = ("zlib/[>=1.2]@conan/stable", "libjpeg/9b@bincrafters/stable",
                "libpng/[>=1.6]@bincrafters/stable", "libtiff/[>=4.0]@bincrafters/stable",
                "jasper/[>=2.0]@conan/stable", "Qt/[>=5.0]@bincrafters/stable")

    def system_requirements(self):
        pack_names = [
            "libavdevice-dev", "libavfilter-dev", "libavcodec-dev", "libavformat-dev",
            "libavresample-dev"
        ]
        installer = tools.SystemPackageTool()
        installer.update()  # Update the package database
        installer.install(" ".join(pack_names))  # Install the package

    def configure(self):
        if self.options.shared:
            self.options["jasper"].shared = True

    def source(self):
        self.run("git clone https://github.com/opencv/opencv")
        self.run("cd opencv && git checkout 3.3.1")
        self.run("cd opencv && git clone https://github.com/opencv/opencv_contrib")
        self.run("cd opencv/opencv_contrib && git checkout 3.3.1")
        tools.replace_in_file(
            "opencv/CMakeLists.txt", "project(OpenCV CXX C)", '''project(OpenCV CXX C)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()''')

    def build(self):
        cmake = CMake(self)
        if not self.options.shared:
            cmake.definitions["CMAKE_POSITION_INDEPENDENT_CODE"] = self.options.fPIC
        cmake.definitions["OPENCV_EXTRA_MODULES_PATH"] = "opencv/opencv_contrib/modules"
        cmake.definitions["BUILD_EXAMPLES"] = "OFF"
        cmake.definitions["BUILD_DOCS"] = "OFF"
        cmake.definitions["BUILD_TESTS"] = "OFF"
        cmake.definitions["BUILD_PERF_TESTS"] = "OFF"
        cmake.definitions["BUILD_opencv_apps"] = "OFF"
        cmake.definitions["BUILD_ZLIB"] = "OFF"
        cmake.definitions["BUILD_JPEG"] = "OFF"
        cmake.definitions["BUILD_PNG"] = "OFF"
        cmake.definitions["BUILD_TIFF"] = "OFF"
        cmake.definitions["BUILD_JASPER"] = "OFF"
        cmake.definitions["BUILD_PROTOBUF"] = "OFF"
        cmake.definitions["BUILD_JAVA"] = "OFF"
        cmake.definitions["BUILD_opencv_apps"] = "OFF"
        cmake.definitions["BUILD_opencv_java"] = "OFF"
        cmake.definitions["BUILD_opencv_java_bindings_generator"] = "OFF"
        cmake.definitions["BUILD_opencv_python2"] = "OFF"
        cmake.definitions["BUILD_opencv_python3"] = "OFF"
        cmake.definitions["BUILD_opencv_python_bindings_generator"] = "OFF"
        cmake.definitions["BUILD_opencv_dnn"] = "OFF"
        cmake.definitions["BUILD_opencv_dnn_modern"] = "OFF"
        cmake.definitions["BUILD_opencv_tracking"] = "OFF"
        cmake.definitions["WITH_FFMPEG"] = "ON"
        cmake.definitions["WITH_IPP"] = "ON"
        cmake.definitions["WITH_QT"] = "ON"
        cmake.definitions["WITH_ZLIB"] = "ON"
        cmake.definitions["WITH_WEBP"] = "OFF"
        cmake.configure(source_folder="opencv")
        cmake.build()
        cmake.install()

    def package(self):
        self.copy(
            pattern="*.a",
            dst="lib",
            src="3rdparty/ippicv/ippicv_lnx/lib/intel64/",
            keep_path=False)
        self.copy(pattern="*.a", dst="lib", src="lib", keep_path=False)
        self.copy(pattern="*.so*", dst="lib", src="lib", keep_path=False)

    def package_info(self):
        libs_opencv = [
            "opencv_aruco", "opencv_bgsegm", "opencv_bioinspired", "opencv_calib3d",
            "opencv_ccalib", "opencv_cvv", "opencv_dpm", "opencv_face", "opencv_features2d",
            "opencv_flann", "opencv_fuzzy", "opencv_highgui", "opencv_img_hash", "opencv_imgcodecs",
            "opencv_imgproc", "opencv_line_descriptor", "opencv_ml", "opencv_objdetect",
            "opencv_optflow", "opencv_phase_unwrapping", "opencv_photo", "opencv_plot",
            "opencv_reg", "opencv_rgbd", "opencv_saliency", "opencv_shape", "opencv_stereo",
            "opencv_stitching", "opencv_structured_light", "opencv_superres",
            "opencv_surface_matching", "opencv_video", "opencv_videoio", "opencv_videostab",
            "opencv_xfeatures2d", "opencv_ximgproc", "opencv_xobjdetect", "opencv_xphoto",
            "opencv_core"
        ]

        libs_linux = ["pthread", "dl", "IlmImf", "ittnotify", "ippiw", "ippicv"]

        self.cpp_info.libs.extend(libs_opencv + libs_linux)
