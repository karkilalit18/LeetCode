class Solution(object):
    def minProcessingTime(self, processorTime, tasks):
        """
        :type processorTime: List[int]
        :type tasks: List[int]
        :rtype: int
        """
        n = len(tasks)
        processorTime.sort()
        tasks.sort()
        j = n - 1
        m = len(processorTime)
        ans = 0
        for i in range(m):
            c = 0
            while c < 4:
                ans = max(ans, processorTime[i] + tasks[j])
                c += 1
                j -= 1
        return ans