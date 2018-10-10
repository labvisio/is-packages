from conans import ConanFile, CMake, tools


class OpencvConan(ConanFile):
    name = "opencv"
    version = "3.4.2"
    license = ""
    url = "https://github.com/labviros/is-packages"
    description = ""
    settings = "os", "compiler", "build_type", "arch"
    options = {
        "shared": [True, False],
        "fPIC": [True, False],
        "with_zlib": [True, False],
        "with_jpeg": [True, False],
        "with_png": [True, False],
        "with_tiff": [True, False],
        "with_qt": [True, False],
        "with_tbb": [True, False],
        "with_ffmpeg": [True, False],
        "with_lapack": [True, False]
    }
    default_options = ("shared=True", "fPIC=True", "with_zlib=True", "with_jpeg=True",
                       "with_png=True", "with_tiff=True", "with_qt=False", "with_tbb=True",
                       "with_ffmpeg=True", "with_lapack=True")
    generators = "cmake"

    def requirements(self):
        if self.options.with_zlib:
            self.requires("zlib/1.2.11@conan/stable")
        if self.options.with_jpeg:
            self.requires("libjpeg-turbo/1.5.2@bincrafters/stable")
        if self.options.with_png:
            self.requires("libpng/1.6.34@bincrafters/stable")
        if self.options.with_tiff:
            self.requires("libtiff/4.0.9@bincrafters/stable")
        if self.options.with_tbb:
            self.requires("TBB/4.4.4@conan/stable")

    def system_requirements(self):
        dependencies = []
        if self.options.with_ffmpeg:
            dependencies.extend([
                "libavdevice-dev", "libavfilter-dev", "libavcodec-dev", "libavformat-dev",
                "libavresample-dev", "libswscale-dev"
            ])

        if self.options.with_lapack:
            dependencies.extend(
                ["libopenblas-dev", "liblapack-dev", "liblapacke-dev"])

        if self.options.with_qt:
            dependencies.extend(["qtbase5-dev"])

        if dependencies:
            installer = tools.SystemPackageTool()
            installer.update()  # Update the package database
            installer.install(" ".join(dependencies))  # Install the package

    def configure(self):
        if self.options.with_zlib and self.options.shared:
            self.options["zlib"].shared = True
        if self.options.with_jpeg and self.options.shared:
            self.options["libjpeg"].shared = True
        if self.options.with_png and self.options.shared:
            self.options["libpng"].shared = True
        if self.options.with_tiff and self.options.shared:
            self.options["libtiff"].shared = True
        if self.options.with_tbb and self.options.shared:
            self.options["TBB"].shared = True

    def source(self):
        self.run("git clone https://github.com/opencv/opencv")
        self.run("cd opencv && git checkout 3.4.2")
        self.run("cd opencv && git clone https://github.com/opencv/opencv_contrib")
        self.run("cd opencv/opencv_contrib && git checkout 3.4.2")
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

        cmake.definitions["WITH_ZLIB"] = "ON" if self.options.with_zlib else "OFF"
        cmake.definitions["WITH_JPEG"] = "ON" if self.options.with_jpeg else "OFF"
        cmake.definitions["WITH_PNG"] = "ON" if self.options.with_png else "OFF"
        cmake.definitions["WITH_TIFF"] = "ON" if self.options.with_tiff else "OFF"
        cmake.definitions["WITH_QT"] = "ON" if self.options.with_qt else "OFF"
        cmake.definitions["WITH_TBB"] = "ON" if self.options.with_tbb else "OFF"
        cmake.definitions["WITH_FFMPEG"] = "ON" if self.options.with_ffmpeg else "OFF"
        cmake.definitions["WITH_LAPACK"] = "ON" if self.options.with_lapack else "OFF"
        cmake.definitions["WITH_IPP"] = "ON"
        cmake.definitions["WITH_OPENMP"] = "ON"
        cmake.definitions["WITH_WEBP"] = "OFF"
        cmake.definitions["WITH_JASPER"] = "OFF"

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
        libs = [
            "opencv_stitching",
            "opencv_superres",
            "opencv_videostab",
            "opencv_aruco",
            "opencv_bgsegm",
            "opencv_bioinspired",
            "opencv_ccalib",
            "opencv_datasets",
            "opencv_dpm",
            "opencv_face",
            "opencv_photo",
            "opencv_fuzzy",
            "opencv_hfs",
            "opencv_img_hash",
            "opencv_line_descriptor",
            "opencv_optflow",
            "opencv_plot",
            "opencv_reg",
            "opencv_rgbd",
            "opencv_saliency",
            "opencv_stereo",
            "opencv_structured_light",
            "opencv_phase_unwrapping",
            "opencv_surface_matching",
            "opencv_xfeatures2d",
            "opencv_shape",
            "opencv_video",
            "opencv_ml",
            "opencv_ximgproc",
            "opencv_calib3d",
            "opencv_features2d",
            "opencv_highgui",
            "opencv_videoio",
            "opencv_flann",
            "opencv_xobjdetect",
            "opencv_imgcodecs",
            "opencv_objdetect",
            "opencv_xphoto",
            "opencv_imgproc",
            "opencv_core",
        ]

        if self.options.with_ffmpeg:
            libs.extend(["avformat", "avcodec", "avdevice",
                         "avresample", "avutil", "swscale"])

        if self.options.with_qt:
            libs.extend(["opencv_cvv"])

        if self.options.with_lapack:
            libs.extend(["lapacke", "lapack", "blas"])

        libs.extend(["pthread", "dl", "IlmImf",
                     "ittnotify", "ippiw", "ippicv"])

        self.cpp_info.libs = libs
