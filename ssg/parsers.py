from typing import List
from pathlib import Path
import shutil


class Parser:
    
    extensions: List[str] = []
    
    def valid_extension(self,extension):
        return extension in self.extensions
    
    def parse(path: Path, source: Path, dest: Path):
        raise NotImplementedError
    
    def read(path: Path):
        with open(path) as file:
            return file.read()
    
    def write(path:Path, dest: Path, content,ext = ".html"):
        full_path=dest / path.with_suffix(ext).name
        with open(full_path) as file:
            file.write(content)
    
    def copy(path: Path, source: Path, dest: Path):
        shutil.copy2(path, dest / path.relative_to(source))

class ResourceParser(Parser):
    
    extensions: List[str] = [".jpg",".png", ".gif", ".css",".html"]
    
    def parse(path: Path, source: Path, dest: Path):
        super.copy(path, source, dest)