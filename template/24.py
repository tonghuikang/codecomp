import sys, os, getpass
import heapq as hq
import math, random, functools, itertools
from collections import Counter, defaultdict, deque
input = sys.stdin.readline

# available on Google, AtCoder Python3
# not available on Codeforces
# import numpy as np
# import scipy

# if testing locally, print to terminal with a different color
OFFLINE_TEST = getpass.getuser() == "hkmac"
def log(*args):  
    if OFFLINE_TEST:
        print('\033[36m', *args, '\033[0m', file=sys.stderr)

@functools.lru_cache(maxsize=None)
def determine(arr, brr):
    cache = {}
    # log(arr, brr)
    arr = list(arr)
    brr = list(brr)
    while arr and brr:
        if (tuple(arr), tuple(brr)) in cache:
        #     # a = arr[0]
        #     # b = brr[0]
        #     # arr.append(a)
        #     # arr.append(b)
            log("cached", arr, brr)
            return True, arr
        atup = tuple(arr)
        btup = tuple(brr)
        cache[atup, btup] = (True, arr)

        a = arr[0]
        b = brr[0]

        del arr[0]
        del brr[0]

        if a <= len(arr) and b <= len(brr):
            a_wins = determine(tuple(arr)[:a], tuple(brr)[:b])[0]               

            if a_wins:
                arr.append(a)
                arr.append(b)
            else:
                brr.append(b)
                brr.append(a)
        else:
            if a > b:
                arr.append(a)
                arr.append(b)
            if a < b:
                brr.append(b)
                brr.append(a)

    if len(arr) == 0:
        # cache[tuple(arr), tuple(brr)] = False, brr
        return False, brr

    # cache[tuple(arr), tuple(brr)] = True, arr
    return True, arr

def solve_(arr):

    locs = set()
        
    for a in arr:
        a = a.replace("e", "e ").replace("w", "w ")
        a = a.strip().split()
        
        log(a)

        x,y = 0,0
        for z in a:

            if z == "e":
                x += 2
            if z == "w":
                x -= 2

            if z == "ne":
                x += 1
                y += 1
            if z == "nw":
                x -= 1
                y += 1

            if z == "se":
                x += 1
                y -= 1
            if z == "sw":
                x -= 1
                y -= 1

        if (x,y) in locs:
            locs.remove((x,y))
        else:
            locs.add((x,y))

    all_locs = {}

    for i in range(-300,300):
        for j in range(-300,300):
            if (i+j)%2 == 0:
                all_locs[i,j] = 0
    
    log(locs)
    for x,y in locs:
        all_locs[x,y] = 1

    log("init", sum(all_locs.values()))

    d6 = [(2,0),(-2,0),(1,1),(1,-1),(-1,1),(-1,-1)]

    for d in range(100):
        new_locs = {k:v for k,v in all_locs.items()}
        for x,y in all_locs:
            if abs(x) > 295 or abs(y) > 295:
                continue
            count = 0
            for dx,dy in d6:
                if all_locs[x+dx,y+dy] == 1:
                    count += 1
            if all_locs[x,y] == 1 and count == 0 or count > 2:
                new_locs[x,y] = 0
            if all_locs[x,y] == 0 and count == 2:
                new_locs[x,y] = 1
        all_locs = new_locs
        log(d, sum(all_locs.values()))

    return sum(all_locs.values())



def solve(*args):
    # screen input
    if OFFLINE_TEST:
        log("----- solving ------")
        log(*args)
        log("----- ------- ------")
    return solve_(*args)


def read_matrix(rows):
    return [list(map(int,input().split())) for _ in range(rows)]

def read_strings(rows):
    return [input().strip() for _ in range(rows)]



def process(string_input):
    arr = [x for x in string_input.strip().split("\n")]

    return arr



sample_input_1="""
sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew
"""

sample_input_1 = process(sample_input_1)
# sample_input_2 = process(sample_input_2)

# sample_res = solve(sample_input_1)
# print(sample_res)


test_input_1="""
nwnwesenenewnwswnwweewswwweswwsew
wswnewwwwwwwswswseswswswwwwesw
eeneeeeseswenweeswneneeneeneene
nwnwnwnwnwnwnwnwnwnwsenwnwnwnwnwnwwenwnw
swneswnwneseswenwnwnwwseneneswnenenene
nwnenwnenwnwneenwnwneneneneswnenene
seneswsesesesesesewnesesesesesewsesese
neseseesewwwnwswseseseswseneswswseee
eneneeeneeeneneeenewneneneee
seseeeneseseeseseseeeeseeewse
swneswewswwswwnwenwsewwnewwwww
wswwwwwwnwwwnwsewnew
neeeneeeeeeeweeeneneseneeenw
eneewenwnenwswnwneswnwnwswesenwnwne
eeeeeenewsweeeeseene
swnwseswseswsenenesenewsesesenwsesesesese
wswnwnwwwwwwwwwnwwseenwwnwnwnw
neeweseseeeenweewweesenwnee
swswnenwsweenwwswswswswswnwswwwswsee
nwseseewsenwswnenwnwsewneswewnwnwnwenw
nwnwnenwswnenwnwnenwnenwnenwnwnwnwswnwnwe
swneenwneneswnenenenenenenenenwnwneneswnene
senwnwneneneenewnwnwnwenwnenwnenwwnwnw
swwnwwwwwwwswneswewwwewwswe
neewneweswnwnweseswnwwneeneswnwnw
nenenweeeeneneswneswnesweenenenewe
seeswswwswswswswsweswswseswwswswswswsw
seseseseneeseseeswsesesesenwsesenwswse
ewenwsewnwwnwnwwnwwnwnwwwwww
sewnwwwnwwnwewnwwswwwwnwnwww
wswnweswswwswwesesweneseswneswwesw
sewswswneswswwswswwswswswswswwwswsw
swseswwseswswswseswseseneseseneseseswswse
seswswesewseswsesenwseseesewneseswswswsw
neeenwneneswneneneeneswenewnwenesw
wsewenewwwwwwwnwwwswenwnwswe
neseswseseswswswsenwnwswwswseswseneesee
swnenenwenesweeneeeeswnwneenenee
wwwwwnwwwswwswwwwwseww
seenwseeseseseeweseseeeeenwsese
seeswnwsesenenweneseenwswswseswsesese
swswweneweeeeswseneenwnwneeene
wnwwswwwwwswwseswswswswwwwsw
nwwnewewnwewswwswewnwwwnwwswe
eeewseeneesweeeenwwnwseeeese
wswswneswswswnwswswwwswwswswswswwesww
neweneeswnwnwenenenwnenwnwnwwnwsesw
seswesesenenwewnwneewnewnwnewneew
swwenewsenenewneneneneneneeswswewe
nwnwnwseenwwnwnwwnwnwwneswwnwwwnw
nwnwswswwwnewswneewwnwwwwwnww
wnwnwwwnwenwnwewwnwswnw
swswswswswwswswneswswswswswseswwswswnw
sesewswseseseseeseswsesenwseseseesesw
eeweneeneeeeesweeneeeenee
wnwnwnesenenwnwswswwnwnwnenenwneeseswnw
seswseswswsesesesesesesewseseseseneese
seseseeseseweseseseeseseeseese
enweneseseeseeseseseseeeeseew
eneneneeneenenenenesenwnene
nenwnenesenenwwnewnwnwenenwe
wwneseneswswsenewwwwwwseeswwnwe
seseeeseseseseswnwwseesweenenesewnee
wwneseswsewseeseseswsesesenwsesesesee
swswswswswswesewwwswswswnewswswsww
eesweeswswwswenwenwnwnwsenwnwswe
nenenewneneneneneneenewneneneneenene
wwswnenwnwnwenwswnenwswswewnewesesw
eeseeeseeseeeseseweneeseeeewse
ewwwnwnwwsenwwwwnwwwwwwwww
seseneswsesenewseseswseseswsesesesesesesese
seneseneseswwseesesesesesenewseswesenw
nwswswnewswswswwwswwwewnewsewse
swnwswseseswneweseseseseswswenenwnwsw
eeneenenewweeeeeneeseewnee
wwnwwwwnwwewnwswwwnwewwne
swwswswswwnwsweswwswwwswnwseswswsw
wwswwwwsewewswnenwwsewswswnwswsw
nwsenwnwswnwnwnwnwnwnwwnwnwnwnwwenwnw
nenwnwnwnwnwnwnwnwnwnwsenwneswwnwnwnene
nwseeswesenwseseswsewnesenww
nenwwnwnwnwsenwnenwwwnwnwnwswnwwnwnw
swwwswswwwswswswnewsw
nenenwneneneneswnwsenenwnenenenwnenwnwnw
wwwnewwswswseswwwwwwsenwwwwwsw
nwnwewwwnwswnwwnwneeenwswewswsw
swswswswseswswswswswnweswswswswswswsweswnw
nenwenewnenweswneneenwnenenenenwseneswne
seswsenwwnenwseseseswsewsenesesesenw
neenweneneeeeneeeneeesweneeesw
nwnwsenwnwnwwnwnwnwnwwnwnwnwsenenwnenwnwnw
swseswseswwswswseseseneswswseswsesesese
sesesesesesenwseseeswswseseeseneeese
wwnenewwwwwsewwnwwswwwwnwse
nweeeswnweswesenwsenweweenwswe
swseswswseswwswswswswswswswswswwneeswse
wwnwnwwnwnewnwnwnwnwsewwewnwnwse
enewwswneeneswe
sweneswswswnwwseswswwswewseswnenenesww
ewwwswwwnesewwsenweneswnwneswesw
swwwneswswswnwswwswwswwsewnenwswewne
seeseswseswseswsenwswseseswseseesewse
senewnesewnwwsewseseneseswneseseenwse
swwnwwewwwnwwwnwwwwnwnwwnwnw
wsenwswswswseseswswneseswseseswswsesese
nenenwnwnenwenwwnwnwneeswnwswnenwwesw
weeseneeeeeneneeeneeeewenenee
nenwneeseenenenenenenenenwneswnwnenewwnw
eeeeeeseeeswneeseenwesenwesew
nwnwnenenwnwnwneeswenenenwnenenwwnene
swwnwnwnwnwnwnwnwnweeneenwnwsenwwnw
nenenenwnwneswnwswsenenwnwneenenenenwnene
eeeeeeeeeeeeewe
swnwseswsesenwsenwseswnenesenwewswswse
neswneneeneneneneseneneneneneenwnewne
nwwnwsewnwwsenwwnwnwnewwnwnwwnwnwnwnw
neswsenwnenwnenewwsesesewnwseneenwnwne
nwnwnwswnewnwnenenwnenwenwnenwnewsenw
eneewneseseneseswseseeenwsww
seesenwsweseseseeseseeesesesesesenw
senwnwnwswwnwwnesewwnwnwnenwenw
eseswneswseswnwnwsweseenewnenwnwsese
senwewseenwswneeeeeeeeeneee
swnwsenwwnwnwneneswnwewwwnwnwnwnwnwwnw
swwsesenwsesenwseeeseneseeweseseee
wwwwswwswwswwnwwswsewseneswswswsw
nenwwsewswnwnwenwnwnwnwenwnwweenwnw
swseeseeseeeeeeeeeeeeeenw
eeswweeeeneenweeee
seseseeeewseenewseeseseseseneesese
wnwnwnwnwnwnwnwnenwnwnwwsenwnwnwnwnwnw
wwswwwwswwwwwwewwwwnewww
seswnwsweweswneswseswswsesewswnwsese
swwwswswseswwswswswwswswwnwwnwwswe
swnwwnwwewnwnwwnwnwnwwnwwwwnww
nenenenwnwswswewsenwnwsenwnwesenwwnwse
seswneseneseswseseseseswseswwsewsesese
neswnenenenwnewneneeneenene
swnwswnenwneenwenwswsenwnwnewnenenene
swneswswswswwwswswswswswswswswnewswswsw
enwnwewnwswwwwnwwnwwneswwesww
senenwnenwnwnwneewnwnwnwnwnwswnenwnwsw
senwnenwwnwnwneeswnwseswnwnwseenwenwnw
wswwwwseswswwwwwwwwwneew
swwswsenwswswswswswswnwswswswswnesweeswsw
nenenenwnenenwneswneseseneneswnenew
nwewnwnwneswnwswswseseeeesweewseee
neswswwwswneswwswswsweswswswswwswsw
nwnenwnenwswneeneneneneneneswnwenenwnenw
eseeneeeseweeneseesesweeeee
neneneenwnenwewsewnenwwnenenwnwew
sweeswnwnwneeswnwwswnwnwe
nenwnenenwnenwneswneenenenenwnenesenwne
eneseswswseswneneswswwwswswsesesewsese
nwnewwnwwnwnwswwwnwwwnwwenwwsww
ewswseeeseeneneneenew
esesesenewnwwseneseseseseswnwse
nenwnwnwnwnwnwsenwsenwnenwnwnwwnewwsese
ewwwwnewswwswnewwwww
ewwwnewwnwewswnwnwwswwwnwwew
nweswswswswnwswsweswswseswwnwswseswee
seenwsesenwsewnweneseswseseseseseesese
senewseswesenwsenw
swneswswseweswseswseswneswwseswsewsesw
wnwwwswnwswnewneswseswsesewweew
nwnwsenwnwnwwnwnwnwnwnwnwnenwnw
ewenwneenwnenwneseseswneswnenenenwnwsw
seseseseseenwsweseeeseseesesenewse
eseseseseseeeeenwneeeseswwesenwee
wnwesweeswenweeeeeeeeeneee
newwnwwewswweeewnenwwswnwwsw
wwwwwwnenwwswswswweewwswswsww
senwseswsweswswswseswswwswsweswwswswsw
neneneeweneneweeeeseeenenenenee
nwswnwnweneneswsesweneneneneswsenewnene
swswnewwswnwsewwwswswwwswwwwswe
nweswsewenweeswweewneeeseesese
eeeswseeeeweeeenenwe
wswwwwnwnenwwwnwnwwnwswnwwwew
swwsweeswswwswswwseswswseswseswswe
sweswnwsweseswnwsenwswseswswwne
swsesesenwswseswnwswswneseeswseseswweswse
newwwnwwswnwnesewnwnwenwnwnwnw
eneswsesesewwenewneswseeseneneseswse
neswswwwwwswwwsenwsweswswneswww
sweneeeeneeeswesweneneneeenee
senweseneseswwswswenw
wweswwsewneswnewswneswwwsw
eeseseseesesenewsesewsesesesesesese
enwenesesesweeseeeeeeseeswesenwnw
nenenwnenenenwwswneneneneneneneneneenene
seswnewnenwswnwnwnwnwwnwnwswnenenwwnwsw
nwnenenwnenenwnwsenenenwneswnwnenenwnenee
seseswsewsesesweseswwsesesweseseswse
nesenwnwnenenenenenewneneeneneneswnenenene
nwswseswswseswswswseeseswswseswswnwswswnwse
eeeseeseneewnweeseeswseesewsee
nwnwnwswnwnwnenwnwnw
eeneeneenweeneneswenenenenweesw
wswseswswswswswseweneswsenenweswww
nwnenenwnwnwnwswenwnwsenwwnwnenenenenenwnw
wnwnenenenenwnwnenwnenwnwsenenw
seesesesweseeeseseseseseesenwse
swseseseswseseswwsesesesesesesenwseeswse
nwwnwwwwwwnwnwwsewnwsenwnwwnee
nwwnwnwwnwwnwsewwnwnwnw
eeneneneseeneswneneneeeneweewee
eneewneneneneneneeseneneswneneswnww
seswnwsesesesesweseseswswseeseswswsesesew
neeseneneenenewne
sesesweewweseseeseeenenesesewew
wsewswneswwwswswswswseesweswwnesww
eswswwswnwewneseneswwswnweenwwsw
swswswwesweswnwnwswswswswsewswsewsw
ewwswwwwnwsewnwswnewswswswwsww
eneeenewneeeneseneeneeeswnenenwne
swwwwwenwwwnwwwewseeswwwne
enwenweewsweswseeeeeseeeee
wnwwwwswwwwwswnewnewwsewenesw
seeseesesesesesewse
sewnewnwsewsewnwewnenwwwwnwswnewnw
swswswswswseswswnwswnwswseseswsesw
nwnwnwwsewnwnwnwnwnewnwnwnwnwnwnwnw
nwswswseswseswseneseseneeswswseswwswsenwse
seewneseseeeweseeeeseseseeeswsenw
eneseeweeneeeeneeeweeneneee
swswswswswswwweswwswnwseswswswswswnee
nenesewnenenwnenenene
ewwnwsesewnenwsewseneweswwnwswnw
sweneneneneesenenenenewenenenenenene
neeneneneneneeewneeeswneeneneew
wnwsenwewnwnwenwnwseswnwneweswnenenw
swswseseenwswewswswsewswswnwswseeenw
nwswwswenewewwwswswwwswwwwse
eeseseeeeeswenweeseeseeenw
neswnesenwnenenenesenwneenene
seseneseseseseeseswsesesewswsesenwsesesese
eseswseeseeseewnwwseesesesesesee
nwnwnenwnwewswnwnenenenw
weeseneeseenweneeeneeneeeee
neneneneeneneneneneneneeenenew
swwswswswswswswsenwswswswswseswneswesw
nenwnwnwnenwsewnenwenwenwsenwnwwsenwne
senwwwwneseewsenewnewwwwswnwwsw
swswswwsesewwswwwneneseenewswswswsw
newseeeeeneeseeseeweseeeseww
neneseeenenenenewnesenenwnenenenenenene
seseseesesesesesesesesesewseseseswse
newswswswswswneseswswneswswseswswwwnesw
eewneseneesenwenwneswsesewesesewse
seseseseseneseseeeeeswee
ewnenenenwnwnwnwnwnenwwnenwnwnenwenene
eweweneeswneeneeneesweenenenene
seseseseseswseewesewnesenwseseesenese
neswwseeseeswsenewnenwneswnwsenwneene
sewnwewwwnwewnwewswnewnwwswww
nenenesweeneenenwnwenenenesweeneese
nwneeseesesesesesewnwseswseweesese
nwnwnwnwnwsenesesenenenenwswnwwnwnenwwnwne
swnweswsesesesenwseseseseseseseneswnwse
eseseeseseeseseseseewsesesesewenesee
eswnwnenenwneenwneswneneneswnwswnwswne
neseseseeswsewswswswneenwwsww
eeweeesenwwsenweeeeseeee
swwswsweswswswswswsewne
senwwwweneseneweesenwnenenwnwwnw
seseseseeesesenwseesweeseseesesee
eeeneseeweeneneeeene
nwswwwenwnwnwnenwnwswswnenwnwnenenwnwsesw
nenenenwnwnwnwnenenenenwsenenwwnenenene
swswsweswswewswswswswswswswnwswnwswsw
ewswswswwwswwswnewseswwneneswwsww
swswswswnwswswswswseswsw
eswswswswwwnwswwe
esesweeseseeenesenwseeseseeseseese
swswnewswswwswswwswswswswswwseswsw
wnwnwwwnwewwwwnwwsenwnwww
seeweesesesesesenwenwswseeeeswe
swesenwnwnwnwwnwnwneenwnwswnwnwnenwnwnw
nwnwnwwwnwnwnwnwnwnwenwwsenwnenwnwnw
nenenenenenesenewneneneneneneneswenene
neswswswswnwseswswsewwwswwswsweneesw
nweseseseeseesweseneeseeseseeswsee
swswwwwwswwswwneswseewwwwwww
seeseseseseseeseesesesewsesesese
enwneswnwnenenenenwsenwswnenenenwnwse
swseswnwwswswswswswswsweswswswswsesesw
wnwwnenewneneseswswnesenwswwesewnesew
neseseseseswseseswswseseseseseswse
wwswewwneswswwwwswnwwseswwswwse
seseseseswwneseneneswswnewewenwwne
sweweseseswsenwneswwseseswsesesese
eeeeneeneeeeseeeeeswseweese
nwenwenwnwswnwswnwnwnenwnwnwnwne
nenenenewneeneesenwewneweeswseesee
nwnewewwwwwseswswwsewweneswnww
sewwnwnwneswwwnwwwnwnwwwsewwww
eeeeneeswneeeeenwnwewseswee
eswnwwwwswnesweswnesewswnwwwswswsw
nenwnwneswnenwnewnenesenwnenesenwenese
seseseseseseswnwsesesesesesenwe
nweswnwswseesenenenwswseesenww
eeeeswneweneeeeeenwnwseeesese
wswnwneswswseenenwswneswwswwnee
seenwnewneewwsenenenewnwnwseneswswse
nwswwswnwswneneswsweseswse
newnenenwnwneswnewnenesesenenwsenwnwnwne
swswwswwnwswswswneswswswewwswswswsw
swwswswneswwswnewwswwswswswsewww
wwwwenewnwsenweseewwseewww
wwwwseewwwwwwwwwwneww
seswseneseseseswnesesesesesenwswswsesese
swswneswswseenwnwseswswnwsesewswnesese
nwnenenenwneneneseneneenewnenenenenenw
eeeewesweneneneeweeswnweswnenw
seeseesesesewsenesese
nwnwseenweenenenenesweeswneneswnenenene
wswwwwswwnwwwswnwwwsewwwwwse
eseswewnwnwesesewswsweneseswnwesw
swswnwswswswseseswswswswswewswswswnwsw
ewsenenwneswseneswneswnenw
swnwnwnwnwnwnwnwnenwnwnwnweewswnwwwnw
eeeenwsenewwswswwnwwwnwwwnew
seseesewseseseseseneswweseseseseese
neswswwewswwswnew
nenenwneneenwseneneneneseeswneenewne
seenweseswseeseeese
wwwnwwwnenwesesenwnwnwnww
nwsweeswnwneseseneenwswseneswwseseneswse
sesewswsenwseseseseseswsenese
enenenenwneenesweneneeeneneeeene
nwnwneeswneneswnwnwnenenenenwenwnwnwne
swneesesesewswwnwseseneseswnwnwnesew
swsesesesenesenesesesesew
seneewnesweneneeneneneeneneenenene
ewwswseswwswsenwswwwwwswnwnwswsesw
eeeswseeneeeeeswseneseesewnewnw
seseswsewswnwseseseeswseesesewsesese
nenwswseeswnwnweenwnwneswneeswswsewnwse
seseesesweneseesese
eswnwewsweseeseeweseeesenenwse
eesenweenwswweswnweeeeseswenwse
nwneneneneneneneneneswnenene
nwnwwnenewwnwnwnwswnwwwswnwwnwwnw
seeneeewseeewsenwseesweeeseee
sewnesewweneeeenwwnewwswswwswnw
neswswwnwnwnenwnwnwwsenwnwnwnesenwnwnenw
swnwswswnenwseswneeswnweesenwnw
neswswnewnenwseeneewenene
nenwneneseswneneneneneneenenenwswnenwsene
seswwswwwneseseswswswnwnewwsesenwnesw
eeeseenwseeneseenwseeeeseweee
nwnenenesenenewnwnenwnwswenwsenenenew
nwneneeseneswsenenewnwnwnewne
wwwswswswwwsewswswwneswwneswnewse
wnwnewsenenwnwenwnw
nwwseswsenwwseswswwswwnweenwwwnwsw
nenwseneswnenwswnwenwnenwnenwnwnwwnwswe
nenweneeseenweenenwsweneseneenene
sweswswwnwswswwwwwswswswswsweww
wwneseswesewsenwwnwnenwnw
wswswswewwswwwwwsewwwswnwwww
swswneeswswswswseswseswnwewnwsenwswsesese
swwnwswsweeswneswsweseswswsenwswnwsw
wneswneseswseseswswseeseseswwseseswsese
seswnwnwswswswswsenweseswswwnwswswese
swneseseeseeseseseseseseesewneseseseese
swswswswseswswswswswswswseseneseswneswse
sewwswwswweneswswswwswswswwwswwwsw
swswswswswswswswswswswnwswswswswswswnese
wwwswwwwwwswwsenwwwwwwnesww
seseseeseswwseeneseswsesesesesenwsesesese
enwnwnenwwnwnenwnwnwnwnenwnwnenwwnee
swswsewneneswsenwseeswseseneeswsenwsenesw
sweswswswswswswsenwswswswswswswswsww
seseseseseswsenesesesewseseswswnwseseswse
seneenwweenwsesewwneeswnenwwenee
enwenewseeneeewnweseswnesenenene
wwseswswswneswswswswswwswwswsw
swseseswwneswwnenwew
eseweswswnesenweneneesee
nwnwnwnesenwnwnwnwnwnwswnwenwnwnenwnwne
swwwwwseswwwswneswswwwwswwww
nenwnwswnesweseeswnenenwneenene
neenwwewneeseneswsenwswswewnese
nwnwwnwwwenwnwnwnwnwnwswenwnwwnwnwnwnw
wwnwwwwwwwwwwwwewwww
newweeneseseenwneseswnwneeesenwnw
esweeenewneswnenenenwenee
swswwswwneswswswswwwwswwswswsw
nenenenenenenenenesenenenenewneneneswne
seseseswsesesewsesesesesenesese
ewnwseswwswswwneswswswwneswwwswnw
newnesenenenenenenenenenwweneswnenene
swneseneseseneswwsenesesesewseswswswnw
nwnwnwwnwnwwwnwnwnwnwsewnw
ewneseeeseeneeeneeewneeeeeswne
nwwnwswenwswwwnwwnenwnwnwnwwnww
sewweswwwswwenwwwwwwnwwswesw
swnwneswwsweenwwwwnwnwwnwwnwnww
neswnenwwneneswwnenwnwenwsenenesenenwnwnw
nwnwsenwswnwwwenwnwnewswswnene
seneseswseswswswswseseswseswseseseswwswne
nenwnenwnenwnwnenenwnenenwsenenenwswnwswnw
enwnweneneneneneeswneneneesweenene
swswswswswnwswswswseseswswswswneswswswsw
eeeneneenweeeeeneneeeswnwesw
eneeswsweeneeesee
seseeeseseseeeswseseseseenwnwesese
eneneneneenenenenewswneneneneeeene
enwswneenenweseswneeewswesese
wseeeswsweswnewnesesesesenwewnwnw
seseswseswseswswnesesenwseseswswswseswsenw
nenwneneneneneneewnenwnene
nwnwwenenwnenwnwseneswnwnwnwenenwnwnenw
sesewnweseswseseseseseseseseseseseseseenw
neeneeswneenwnenenenenenwneneneneswnenene
neneswneswneeswneneneneneswenenenenwnene
senewnwenweewsesesewneseswneeeswnw
nwneeewsewseneneenwnwneswenewnenwnw
sweeenwwneswnewnweeeewnenwnwswswne
esweeneweneeeeeewenwsweesw
neswnenwwwwewsenweswwnwseeewnwe
newwwwwwwwwwwwwwseeswsww
nweeseeeeesenweeeeeesweee
wnwwenwwwnwnwnwwnesww
wewswwseneswwwswnwwnwwwwwnesww
nenenenenwsweeneneeeweseswnwneene
eeeeeewsweeesenweeesenweee
eeeeeneneneneswnenewneneeeneeese
nwswswnenesenenenenesenwnenenenenenw
neeeeseseeeseeswneseeeseseeew
seswseswnwseswseseswsesesesw
swwwswwwwnwwseswwnewewwwwswsww
ewwwewsewnwwwwwwwwwwwnww
swsesesesewsesesenwseseneseseewswsese
nenenenewneneeneneswneeneneneeenenee
nwnwwwswnwwnwwenwwnwnw
senenenweswnweweneneswesenwneneneneene
enenewneneneeeneeneeseenewnenenene
sesenwnwseseeseeseeeee
seewnwswswseswswseeswswswswseswsewesw
swswswswnwwswseswswwwewwwswwwnwww
nwnwnwnwnwnwnwnwnwnwnwwnwnenwnwnenwsenw
eeeeeeeeeneweeesweeeee
eswswwwwswwswswwswswnwwwwswwsw
neneneneneenwneneneenewsewweenese
nenenwnenwneneneneneswnenwswnwnwnwnwenwnwe
nwnwsenwnwwwenwnwenwwnwsewnwnwnenw
nwsenenwnwnwnwnwnwnenwnenene
eeseneseseswnweeenwneswnwsenweseswse
enwnenesenenewnenwwwnwnenenenwnwene
nwenwnweswnwwnwnenenenenwsewnwnwnwnene
seneseseneweeweseseeenesesweee
nenenesenenwwnwnwnwnwnwsenwnwnwnwnwnwnwnwne
swswswewenwneswswnweseswnwweswswnw
nenwsenenenwnwnewnwswnenenwnenenenenenesw
nweswseenewewnwewwnwsewswnwswnww
ewseneeneeneneeneneewseneneewnenw
wwnwnwnwnwwwwnwenenwnwseswwnwwww
senenenenwnenenwnwnesenenwwswnwnwnenwnwe
eseseesweseeeeseeesweeesenenwe
neneswnenwenwsenenwsweeneneneeswsenwe
neswswsweswswswnwswswneswswswwswseswnesw
swseseseeswseswnwseseseswseseswnwsesesw
seswswseseseseswneseseswswseseseswseswnesw
ewwwwnwwwwwwwwwwwwswww
seneswwwseseseseseswsenwseneseseswseswse
wsenwsenwwnweneswseewnwnewneseseswsenw
seswswneswswneseswswseswseswseswseswsesw
weseeeenweneeeneeeneeesweeee
neneneneneswneneneenwenene
eewseesesweeeenwweeneswewene
swswswswswwswswwswsweswswnwswswswswswse
wnenwneswnwnewswnwnwsenwewnwneenenwse
neneeneneneneneewnenenesenene
eeeseenwsesweeeeweeeseeenee
wswswseswneswsweneswswneswswseswswsww
nwnwwwnwsewnwwwwnewwwnwwwww
nwnwwnwnenenenwnenesenwnenenwnenenwnwne
wswswswweswnwswswswwswswswwswswwsw
newneneneneseneneneew
eeswsweseseneenenenewseswseenwese
seenwseeswwnwwseenenenwnewnewnew
neeneeneenesesweneeneweenenweeee
swsewwnwswwswswwsenwnewswwwneswe
nenenewneneeneeeneneneneeneneneneswne
seeesewseeeeeneeesenweeeswse
sesenwseswnwswsweseswnwswnweswseswnwswsw
ewwwwwwsewwwwnwwwwwwnewwnw
nwswseswnwwwsesenwenwnewnwnwwneswnwe
swnwswswswswswswswswswswswswsweswswswsw
sesesewnwseswnwseseswseswswswesweswsw
eeseeeenwswsweeeeeeneeeeeee
nenenenenenenewseneeeeseneneenewnenene
eeeeneneeneswneneeewneneseeene
nenesenenenenenewnwnenenenenenenenenene
nwswwnwweswsweswswneneswswswsw
sewnenenenenweenew
weeswenwswsenwsenwnwnweeeswesee
esenwsenenwsesenwneswwseseswsesesesewse
nwwnwnwnwnwnwswenwneswesesenenwnwenwwsw
wwnwnwnwnwnwwwnwnwswnewwwnwwnw
nwswenweswnwnwenwenwsenwnwwnwwnenwnw
eneneweeeneesenenenwenenewneeswne
seeseeesesenesesesesewsenweswseswne
eeneneeswwneneeeneenenenenewnenene
sesenewwwwewwwwwnewswwwnwnwne
senweeswnwseseneswnwsewswesene
sesesewwsenwseneesweseeeneswsesee
wnwnwnwwwwnwwwewswnw
swwwwwewwwwwwswesw
wwnwsewsewwesenwswsenwnewwnwsenww
nwnwenwnwnenwswnenwnwnwnwnwwnwnwsenwnwse
swsewswswseseswswwwswneneewswwswne
eeeeeenweeeswweeeeenwesee
wwnenwwwnewwswwwnwsewswwwsew
nwnwnesewsenwnwenwnwnwnwnwnww
nweswnesenenenesenenewsenewneneneswne
enwseseneenwwwnwnwnewnwsw
wwwenwwswwnwwnwnwnwnwnwnwwsenwwnw
swneswswswswswwswswswswswseswswnewswsw
seseenwneseweeesweneenwseswseee
senwswnwneswwwnwseewwnewnwnwnwee
swswswswnwwwseswneneswswwwswsweswsw
nwnewsenwsewnwnwsenwwwnwnwwwwnw
nwwnwswwswswwwwwnwseeswwseswswww
seweesesenwseseenesesweneewswwse
seweenewswnwwwwwwsenenewewwsew
nwnenenenewnenwneneneneneneneswneenwnene
eeeeeeneswneseeeeeseseeeeeew
seseesesesewseseeseseseewse
nweseneseeeseseseeseseesesweeswsenwsw
seneneswnesenenenenenenenwwnwnwswnenene
swnwseseseneseswswswsweswswswswsesesewsw
wseseeneseseeneewenewneenwnenenene
enwnenesenenewseswnwnwnenenenwnewnene
eneeeeneeewee
swwswwwewesewwnesewswswnw
swwseswseeswnewsewnwnwnwwneeswesw
weeswseeneeenwsewenenwweeewe
nwswnwnenwwnwnenewwewwwwseswwenww
seeseenwnwwewwneswwnewswwwsewsw
wswswswwswswswswswseswswswwwwnwesw
newseneeneswnenwwweneneswseeeeene
seswswseswseeswwswswnwswswswsweswnw
seseseseseseseseseneseseswseseseseneswsese
nenenwnwswneeneneenenwnwnwsew
nwswwnesewswsenwswweenesesew
wswswwenwswwwsenewswswneweseswsw
seswseswswswswswnwseseneseseswsw
wswswswswswswsenweswswswswswneseswsew
eneeenenweneneneneneneswneeeene
nwwwwwwwnewwwwwwwsewwwwswe
eseseseseseseneseseswwnweseseseseese
eweseeenweeeeseseweeese
nwnenwwnwwnwnwswnwsenwnwsenwenwnewsw
nwnenwnenwnenwswnenwswnenwnwnwnenwnenenwe
eeeeeeeeneweeneeeeeeswe
esenwnewnwnwnwwsenwnwnewnewwswswne
eenwseseeeeweseeeeeeeesesese
seseswswseswswswswseseeneseswswnwswsewswsw
nwnwnwneneneneneswenenenenenenwnenene
nwnwwnwnwnwwnwwsenwenwenwnwnwnwneswsw
sewwnwwnesesesewnewewswewnwwe
sweswswwnewswswweewswnwwseswsewnwsw
wsweeeneewenwneswene
eewseseeeesesenweeseseseseseeene
wwsweeswwwnwwwwswwewswwenw
eneeneneeenweeeeeseneeeee
neseneneswwneneeneeswnewneneseenene
eeeeeseseseseeewseswsenwwseeeese
wwswwswnewswwswwswwneswwswwwsw
wswwwswewswwswswwnwwwwswe
eseeweeeeeneeeeneeneeweeee
swswswswswseswnwsweswswswswswswswswswne
sesesenwwseesenwseseseesesesesesesesese
seenwnwwneeenwswwsesweeeenwse
nwwwwwwneseewwwww
eeeeeseenwsesw
nwnenwnwnenwnwnenwnwsenenwnenewnwnwnenw
seseseseseneseeeenwseseeseseeseseew
swswnwsweseneswwswswswwswswnewswwwsw
neneeesewneneeseneeneweeeeswnew
swswswsesesweswweswswswswsweswswwnwsw
nwswseseseswseswenwseswsesw
nwneneswnwnenenesenwnwneswne
sweseseeseseesewseswsesenwseswnwsesw
swnewsenenweneneneneneesewwnwnenenwnwse
nwnwsenwnwwnwnwnwnwwnenwwnweenwnwsw
nwwnwewnwnwnwwwwnwnwwnwnwnwswwnw
swswswewswseswseseswswswswsesewswsenesesw
eeweeeeeeeeseeeeeee
neenwswsenenewneew
seswneseenwswnwseswswswswswe
nwnenwnwsesenwnwwnwnwnenwnwnenenwsenwnw
sesenwsweseeswnwseswsewwseesesesesesw
"""


test_input_1 = process(test_input_1)
# test_input_2 = process(test_input_2)

test_res = solve(test_input_1)
print(test_res)



