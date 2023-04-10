from conan import ConanFile

def getRequires():
    return []

class baseRecipe(object):
    name = None
    version = None

    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": True}

    exports_sources = None
    requires = None
    
    def validate(self):
        if self.settings.name == None:
            raise ConanInvalidConfiguration("package name is required")
        if self.settings.version == None:
            raise ConanInvalidConfiguration("package version is required")
        if self.settings.exports_sources == None:
            raise ConanInvalidConfiguration("package exports_sources are required")
        
    def requirements(self):
         if self.settings.exports_sources != None:
            requires = getRequires()
            for req in requires:
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