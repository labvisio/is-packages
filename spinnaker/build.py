from cpt.packager import ConanMultiPackager

if __name__ == "__main__":
    builder = ConanMultiPackager(username="is")
    builder.add(settings={"arch": "x86_64", "build_type": "Release"})
    builder.run()
