#! /usr/bin/env python3

"""
Author: Alessandra Cappati

Script to read datacard and print table with processes and rates

Requirements: tabulate, python 3.12
Run with: python3 printYieldTable.py
"""

from pathlib import Path

from tabulate import tabulate


def printTable(filename: str) -> str:
    """
    Function to read datacard and print table with processes and rates

    Parameters
    ----------
        filename (str): path to card

    Returns
    -------
        str: if successful, path to card

    Raises
    ------
    FileNotFoundError
        if the file is not found
    """

    # check if file exists
    filename = Path(filename)
    if not filename.exists():
        raise FileNotFoundError(f"File {filename} not found!!!")

    # open file
    rows_dict = {}
    process_find, rate_find = True, True
    with open(filename) as file:
        for line in file:
            # search for line starting with process
            # remove white spaces from all elements x of the line
            # remove endline
            # save all elements of the line (separated by " ") from the 1st on
            # take only the first line (there are two)
            if line.startswith("process") and process_find:
                rows_dict["process"] = [
                    x.strip() for x in line.strip("\n").split(" ")[1:] if x != ""
                ]
                process_find = False
            # search for line starting with rate
            # remove white spaces from all elements x of the line
            # remove endline
            # save all elements of the line (separated by " ") from the 1st on
            if line.startswith("rate") and rate_find:
                rows_dict["rate"] = [
                    x.strip() for x in line.strip("\n").split(" ")[1:] if x != ""
                ]
                rate_find = False

    # print(rows_dict["process"])

    # print table
    table = tabulate(
        zip(rows_dict["process"], rows_dict["rate"]),
        headers=["process", "rate"],
        tablefmt="double_outline",
        disable_numparse=True,  # ignore floats, all things are strings
    )
    print(table)

    return str(filename)


if __name__ == "__main__":
    # card CCLUB
    # filename = "../card_CCLUB/hhbbtt_res1b_etau_2022_13p6TeV.txt"
    # card Francisco
    # filename = "../card_Francisco_11Jun/MuTau_BinaryTransf_Res1b_signal_2022.txt"
    # filename = "../card_Francisco_26Jun/MuTau_BinaryTransf_Res1b_signal_2022.txt"
    # filename = "../card_Francisco_15Jul/ETau_BinaryTransf_Res1b_signal_2022.txt"
    filename = "../card_Francisco_4Aug/ETau_BinaryTransf_Res1b_signal_2022.txt"

    print(f"Reading file {filename} ...\n")
    printTable(filename)
