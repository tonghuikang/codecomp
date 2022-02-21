#!/usr/bin/env python3

# sample usage
# python3 checker.py input_data/c_coarse.in.txt output/c_coarse.in.txt.0000000005

import sys
import shutil

# ---------------------------- template ends here ----------------------------


def input_parser(filename):
    with open(filename) as f:
        srr = [row.strip() for row in f.readlines()]  
    arr = [set(x.split()[1:]) for x in srr[1::2]]
    brr = [set(x.split()[1:]) for x in srr[2::2]]

    return arr, brr


def output_parser(filename):
    with open(filename) as f:
        srr = [row.strip() for row in f.readlines()]  
    crr = srr[0].split()[1:]

    assert len(crr) == int(srr[0].split()[0])

    return crr


def take_score(input_filename, output_filename):
    arr, brr = input_parser(input_filename)
    crr = output_parser(output_filename)

    # probably some validator to check that output matches input
    # for example all ingredient names are valid

    crr = set(crr)
    score = 0
    for a,b in zip(arr,brr):
        
        all_included = set(a) & crr == set(a)
        all_excluded = set(b) & crr == set()

        if all_included and all_excluded:
            score += 1
    return score


def rename_output(output_filename, score):
    output_filename_prefix = output_filename.split(".")[0]
    output_filename_renamed = output_filename_prefix + "." + str(score).zfill(10)
    shutil.copyfile(output_filename, output_filename_renamed)


if __name__ == "__main__":
    # input filename and output filename
    assert len(sys.argv[1:]) == 2
    input_filename, output_filename = sys.argv[1], sys.argv[2]

    score = take_score(input_filename, output_filename)
    rename_output(output_filename, score)

    print(score)
