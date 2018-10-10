from conan.packager import ConanMultiPackager

if __name__ == "__main__":
    builder = ConanMultiPackager(build_policy="missing")

    builder.add({
        "compiler.libcxx": "libstdc++11",
        "build_type": "Release"
    }, {
        "opencv:with_qt": False,
        "opencv:shared": True
    })

    builder.add({
        "compiler.libcxx": "libstdc++11",
        "build_type": "Release"
    }, {
        "opencv:with_qt": True,
        "opencv:shared": True
    })

    # TODO: Check why the build for this option is failing
    #builder.add({
    #    "compiler.libcxx": "libstdc++11",
    #    "build_type": "Release"
    #}, {
    #    "opencv:with_qt": False,
    #    "opencv:shared": False
    #})

    builder.add({
        "compiler.libcxx": "libstdc++11",
        "build_type": "Release"
    }, {
        "opencv:with_qt": True,
        "opencv:shared": False
    })

    builder.run()