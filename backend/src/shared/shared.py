from enum import Enum

class FolderAccessType(Enum):
    READ = 'Read'
    WRITE = 'Write'
    DELETE = 'Delete'