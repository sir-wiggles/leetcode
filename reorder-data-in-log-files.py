from typing import List

class Solution:
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        digits = []
        letters = []
		# divide logs into two parts, one is digit logs, the other is letter logs
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)
                
        letters.sort(key = lambda x: x.split()[1])            #when suffix is tie, sort by identifier
        letters.sort(key = lambda x: x.split()[1:])          #sort by suffix
        result = letters + digits                                        #put digit logs after letter logs
        return result

logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
print(Solution().reorderLogFiles(logs))
