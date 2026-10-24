class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def to_days(date_str):
            m = int(date_str[:2])
            d = int(date_str[3:])

            return sum(months[:m - 1]) + d


        start = max(to_days(arriveAlice) , to_days(arriveBob))
        end = min(to_days(leaveBob) , to_days(leaveAlice))

        return max(0, end - start + 1)

        # ar_alice = to_days(arriveAlice)
        # l_alice = to_days(leaveAlice)
        # ar_bob = to_days(arriveBob)
        # l_bob = to_days(leaveBob)

        # alice_days = []
        # bob_days = []
        # days = 0

        # for i in range(ar_alice , l_alice + 1):
        #     alice_days.append(i)
        
        # for i in range(ar_bob , l_bob + 1):
        #     bob_days.append(i)

        # for day in alice_days:
        #     if day in bob_days:
        #         days += 1
        
        # return days
