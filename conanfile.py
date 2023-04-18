from conan import ConanFile
from conan.tools.files import copy

from module.conan.baseRecipe import *

class Pkg(ConanFile):
    name = "cpp-tools"
    version = "1.0"
    user = "pasan"
    channel = "testing"
    
    package_type = "python-require"
    
    def export(self):
        copy(self, "module/*", self.recipe_folder, self.export_folder)
    