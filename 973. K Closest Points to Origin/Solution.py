class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        def distance(point):
            x = point[0]
            y = point[1]
            return math.sqrt(math.pow(x, 2) + math.pow(y, 2))

        sorted_list = sorted(points, key=lambda x: distance(x))
        
        return sorted_list[0:k]
            