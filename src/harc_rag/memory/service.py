from harc_rag.memory.manager import MemoryManager


class MemoryService:

    def __init__(self):
        self.manager = MemoryManager()

    def manager_instance(self):
        return self.manager