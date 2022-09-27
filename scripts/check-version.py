import sys

class Version:

    def __init__(self, parts):
        self._parts = parts

    @classmethod
    def from_python_version(cls, string):
        return Version.from_version_string(string.split(" ")[1])

    @classmethod
    def from_version_string(cls, string):
        parts = [int(i) for i in string.split(".")]
        return Version(parts)

    def get_parts(self):
        return self._parts

    def _compare_to(self, other):
        this = self.get_parts()
        that = other.get_parts()
        n = max(len(this), len(that));
        for i in range(n):
            this_e = this[i] if i < len(this) else 0
            that_e = that[i] if i < len(that) else 0
            if this_e < that_e:
                return -1
            if this_e > that_e:
                return 1
        return 0

    def __ge__(self, other):
        return self._compare_to(other) in (0, 1)
        return(self.seq > other)

    def __lt__(self, other):
        return self._compare_to(other) == -1


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Not enough arguments provided")
        exit(100)

    v_val = Version.from_python_version(sys.argv[1])
    v_min = Version.from_version_string(sys.argv[2])
    v_max = Version.from_version_string(sys.argv[3])
    msg = sys.argv[4]

    if v_min < v_val < v_max:
        exit(0)
    else:
        print("Version incompatible.")
        print(msg)
        exit(1)

