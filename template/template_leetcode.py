import itertools

abc = "abcdefghijklmnopqrstuvwxyz"
digits = "123456789"
abc_map = {c:i for i,c in enumerate(abc)}
digits_map = {c:i for i,c in enumerate(digits)}


class Solution:
    def possiblyEquals(self, s1: str, s2: str) -> bool:

        def split(s1):

            idxs = set()
            for i,(a,b) in enumerate(zip(s1, s1[1:])):
                if (a in abc_map) or (b in abc_map):
                    idxs.add(i)


            s_split = []
            cur = ""
            for i,x in enumerate(s1):
                cur += x
                if i in idxs:
                    s_split.append(cur)
                    cur = ""
            s_split.append(cur)
            return s_split

        s1_split = split(s1)
        s2_split = split(s2)

        print(s1_split)
        print(s2_split)

        s2_range = [list(range(2**len(x))) for x in s2_split]

        s1_map = {}
        s2_map = {}


        def get_mapping(s1_split):

            s1_range = [list(range(2**len(x))) for x in s1_split]

            for comb1 in itertools.product(*s1_range):
                s1_divide = []
                for a,b in zip(s1_split):
                    if len(a) == 1:
                        assert b == 0
                        if a in abc_map:
                            s1_divide.append(a)
                        else:
                            s1_divide.append(int(a))

                    if len(a) == 2 and b == 0:
                        s1_divide.append(int(a))

                    if len(a) == 2 and b == 1:
                        s1_divide.append(int(a[0]))
                        s1_divide.append(int(a[1]))

                    if len(a) == 3 and b == 0:
                        s1_divide.append(int(a[0]))
                        s1_divide.append(int(a[1]))
                        s1_divide.append(int(a[2]))

                    if len(a) == 3 and b == 1:
                        s1_divide.append(int(a[0]))
                        s1_divide.append(int(a[1:]))

                    if len(a) == 3 and b == 2:
                        s1_divide.append(int(a[:2]))
                        s1_divide.append(int(a[2]))

                    if len(a) == 3 and b == 3:
                        s1_divide.append(int(a))

                total_len = 0
                markers = {}
                for x in s1_divide:
                    if type(x) == int:
                        total_len += x
                    else:
                        markers[total_len] = x
                        total_len += 1
