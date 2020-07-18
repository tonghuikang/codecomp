class FixedNumberOfDigits:
    def sum(self, a,b,c):

        if c <= len(str(a)):
            return int(str(a)[:c])

        for i in range(40):

            if c//len(str(a)) < 10:
                # print("break")
                break

            forward = min((int("9"*len(str(a))) - a )//b, c//len(str(a)))
            # print("forward", forward, len(str(a)))

            c = c - forward*len(str(a))
            a = a + forward*b

            # print(a,b,c)

            if c//len(str(a)) < 10:
                # print("break")
                break

            forward = 3
            # print("forward", forward)

            c = c - len(str(a))
            a = a + b

            c = c - len(str(a))
            a = a + b

            c = c - len(str(a))
            a = a + b

            # print(a,b,c)

        res = list(range(a,a+b*c,b))

        # print(res)

        for r in res:
            if c <= len(str(r)):
                return int(str(r)[:c])
            c = c-len(str(r))

        return None

