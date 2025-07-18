"""
Author: Alessandra Cappati

Script to read datacard and plot shapes

Requirements: python 2, ROOT
run with: python plotDatacardShapes.py
"""

from ROOT import (
    TCanvas,
    TFile,
    gPad,
    gSystem,
    kBlue,
    kGreen,
    kMagenta,
    kOrange,
    kRed,
    kViolet,
)


def readCardsAndPlot(out_dir, filenametxt, filenameroot):
    """
    Function to read datacard and plot shapes

    Parameters
    ----------
        filenametxt (str): path to card file .txt
        filenameroot (str): path to card file .root

    Returns
    -------
        none
    """

    # first read names of the processes from the datacard txt file

    # open file and save processes names in dictionary
    process_dict = {}
    process_find = True
    with open(filenametxt) as file:
        for line in file:
            # search for line starting with process
            # remove white spaces from all elements x of the line
            # remove endline
            # save all elements of the line (separated by " ") from the 1st on
            # take only the first line (there are two)
            if line.startswith("process") and process_find:
                process_dict["process"] = [
                    x.strip() for x in line.strip("\n").split(" ")[1:] if x != ""
                ]
                process_find = False

    print(process_dict)

    # open file root
    inhistofile = TFile.Open(filenameroot)
    histolist = []

    # get histograms from file root
    # print(process_dict["process"]) # process_dict["process"] is a list
    for item in process_dict["process"]:
        histoitem = inhistofile.Get(item)
        histoitem.SetName(item)  # set name bc the one they get is weird
        histolist.append(histoitem)
        # print(item)

        histoitem.SetTitle("")  # remove hist title
        histoitem.SetStats(0)  # remove stat box

        ## put colors and pretty things in the histos
        hist_name = histoitem.GetName()
        if hist_name.startswith("ggHH"):
            histoitem.SetLineColor(kRed + 1)
            histoitem.SetMarkerColor(kRed + 1)
        elif hist_name.startswith("qqHH"):
            histoitem.SetLineColor(kBlue + 1)
            histoitem.SetMarkerColor(kBlue + 1)
        elif hist_name == "DY":
            histoitem.SetLineColor(kOrange + 7)
            histoitem.SetMarkerColor(kOrange + 7)
        elif hist_name == "TT":
            histoitem.SetLineColor(kRed - 1)
            histoitem.SetMarkerColor(kRed - 1)
        elif hist_name == "qcd":
            histoitem.SetLineColor(kMagenta)
            histoitem.SetMarkerColor(kMagenta)
        elif (
            hist_name.lower().startswith("ggh_")
            or hist_name.lower().startswith("qqh_")
            or hist_name.lower().startswith("zh_")
            or hist_name.lower().startswith("wh_")
            or hist_name.lower().startswith("vh_")
            or hist_name.lower().startswith("tth_")
        ):
            histoitem.SetLineColor(kGreen + 1)
            histoitem.SetMarkerColor(kGreen + 1)
        else:
            histoitem.SetLineColor(kViolet + 2)
            histoitem.SetMarkerColor(kViolet + 2)
        histoitem.SetLineStyle(1)
        histoitem.SetLineWidth(2)
        histoitem.SetMarkerStyle(6)

    # --- do plot with all shapes together
    canvas = TCanvas("canvas", "canvas", 800, 600)
    canvas.cd()
    canvas.SetLogy()  # requires SetRangeUser starting from >0

    histolist[0].GetXaxis().SetTitle("NN score")
    histolist[0].GetYaxis().SetRangeUser(0.0001, 1000000.0)
    histolist[0].GetYaxis().SetTitle("Events")
    histolist[0].Draw("p")

    for item in histolist[1:]:
        item.Draw("same p")

    # legend, need to define coordinates
    gPad.BuildLegend(0.64, 0.58, 0.97, 0.97)

    canvas.SaveAs(out_dir + "/" + "all_shapes.png")

    # --- do plots for each shape separated
    for n, item in enumerate(histolist):
        canvas1 = TCanvas("c" + str(n), "c", 800, 600)
        canvas1.cd()
        canvas1.SetLogy()

        item.GetXaxis().SetRangeUser(0.0001, 100000.0)
        item.SetTitle("")  # remove hist title
        item.SetStats(0)  # remove stat box
        item.Draw("histo")
        gPad.BuildLegend(0.7, 0.87, 0.95, 0.95)
        canvas1.SaveAs(out_dir + "/" + item.GetName() + "_shape.png")


if __name__ == "__main__":
    # ----------------
    # --- card CCLUB
    # filenametxt = "../card_CCLUB/hhbbtt_res1b_etau_2022_13p6TeV.txt"
    # filenameroot = "../card_CCLUB/hhbbtt_res1b_etau_2022_13p6TeV.root"
    # text_outdir = "CCLUB"

    # --------------------
    # --- card Francisco
    filenametxt = "../card_Francisco_15Jul/ETau_BinaryTransf_Res1b_signal_2022.txt"
    filenameroot = "../card_Francisco_15Jul/ETau_BinaryTransf_Res1b_signal_2022.root"
    text_outdir = "Francisco_15Jul"

    # --- create output dir
    print("Creating output dir ...")
    out_dir = "plots_" + text_outdir
    gSystem.Exec("mkdir -p " + out_dir)

    # --- call function for plots
    print("Reading files", filenametxt, filenameroot, "...")
    readCardsAndPlot(out_dir, filenametxt, filenameroot)
