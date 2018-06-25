from conan.packager import ConanMultiPackager

if __name__ == "__main__":
    builder = ConanMultiPackager(
        build_policy="missing", gcc_versions=["5"], archs=["x86_64"], username="is")

    builder.add({
        "compiler.version": 5,
        "compiler.libcxx": "libstdc++11",
        "arch": "x86_64",
        "build_type": "Release"
    }, {"opencv:with_qt": False})

    builder.add({
        "compiler.version": 5,
        "compiler.libcxx": "libstdc++11",
        "arch": "x86_64",
        "build_type": "Debug"
    }, {"opencv:with_qt": False})

    builder.add({
        "compiler.version": 5,
        "compiler.libcxx": "libstdc++11",
        "arch": "x86_64",
        "build_type": "Release"
    }, {"opencv:with_qt": True})

    builder.add({
        "compiler.version": 5,
        "compiler.libcxx": "libstdc++11",
        "arch": "x86_64",
        "build_type": "Debug"
    }, {"opencv:with_qt": True})

    builder.run()