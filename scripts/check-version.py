import sys

def versionToList(version):
    return [int(i) for i in version.split(".")]


# check if version is inbetween min and max version
# returns
#    0 if it is,
#    1 if it exceed the maximum,
#   -1 if it does not meet the minimum
def check(v_val, v_min, v_max):
    m = max([len(v_val), len(v_min), len(v_max)])
    for l in [v_val, v_min, v_max]:
        for i in range(len(l), m):
            l.append(0)

    s_val = 0
    s_min = 0
    s_max = 0
    for i in range(m):
        base = m - i
        s_val += v_val[i] * (10**base)
        s_min += v_min[i] * (10**base)
        s_max += v_max[i] * (10**base)

    if s_min <= s_val <= s_max:
        return 0
    elif s_val > s_max:
        return 1
    elif s_val < s_min:
        return -1


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Not enough arguments provided")
        exit(100)

    v_val = versionToList(sys.argv[1])
    v_min = versionToList(sys.argv[2])
    v_max = versionToList(sys.argv[3])
    msg = sys.argv[4]

    r = check(v_val, v_min, v_max)
    if r == 0:
        exit(0)
    if r > 0:
        print("Version too low")
        print(msg)
        exit(1)
    if r < 0:
        print("Version too high")
        print(msg)
        exit(2)

