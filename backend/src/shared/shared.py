from enum import Enum

class FolderTypeAccess(Enum):
    READ = 'Read'
    WRITE = 'Write'
    DELETE = 'Delete'