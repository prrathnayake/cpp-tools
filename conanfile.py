from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout, CMakeDeps
from conan.tools.files import copy

class baseRecipe(object):
    name = None
    version = None

    license = None
    author = None
    url = None
    description = None
    topics = None

    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": True}

    exports_sources = None
    requires = []
    req_len = len(requires)

    def configure(self):
        if self.name == None:
            raise ConanInvalidConfiguration("package name is required")
        if self.version == None:
            raise ConanInvalidConfiguration("package version is required")
        if self.exports_sources == None:
            raise ConanInvalidConfiguration(
                "package exports_sources are required")

    def requirements(self):
        if self.req_len != 0:
            for req in self.requires:
                self.requires(req)

    def layout(self):
        cmake_layout(self)

    def generate(self):
        tc = CMakeToolchain(self)
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = [self.name]

class Pkg(ConanFile):
    name = "cpp-tools"
    version = "1.0"
    package_type = "python-require"
