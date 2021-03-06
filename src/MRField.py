from MREntity import *

class MRField(MREntity):
    def isMovable(self):
        return False
    def addOutgoingDep(self, dep):
        pass
    def removeOutgoingDep(self, dep):
        pass

    def __str__(self):
        ret = "\tfield "
        ret = ret + self.getName() + " {\n"
        for dep in self.incomingDeps:
            ret = ret + "\t\t<- " + dep.getName() + "(" + dep.getOwner() + ")\n"
        for dep in self.outgoingDeps:
            ret = ret + "\t\t-> " + dep.getName() + "(" + dep.getOwner() + ")\n"
        ret = ret + "\t}\n"
        return ret
    def __repr__(self):
        return self.getName()
    def __hash__(self):
        return hash(self.name)
    def __eq__(self, other):
        return self.name == other.name
