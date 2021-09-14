#!/usr/bin/env python3

# Created by: Haokai Li
# Created on: Sept 2021
# This is the "variable"Program, with proper style


def main():
    # This function calculate area and perimeter with variable

    length = int(input("enter length of the rectangle(mm)"))
    width = int(input("enter width of the rectangle(mm)"))
    area = length * width
    perimeter = (length + width) * 2
    print("a = L x W = {} mm²".format(area))
    print("p = (L + W) x 2 = {} mm".format(perimeter))
    print("")
    print("Done")


if __name__ == "__main__":
    main()
