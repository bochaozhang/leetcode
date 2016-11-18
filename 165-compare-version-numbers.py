# Compare two version numbers version1 and version2.
# If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.

class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        version1 = map(int, version1.split("."))
        version2 = map(int, version2.split("."))
        l1 = len(version1)
        l2 = len(version2)
        if l1 > l2:
            version2.extend([0] * (l1-l2))
        elif l2 > l1:
            version1.extend([0] * (l2-l1))
        r = 0;
        for i in range(max(l1,l2)):
            if version1[i] > version2[i]:
                r = 1
                break
            elif version1[i] < version2[i]:
                r = -1
                break
        return r

if __name__ == "__main__":
    version1 = "0.0.1"
    version2 = "0.1"
    print Solution().compareVersion(version1,version2)
    version1 = "1.0"
    version2 = "1"
    print Solution().compareVersion(version1,version2)
