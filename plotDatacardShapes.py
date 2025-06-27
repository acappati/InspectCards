"""
Author: Alessandra Cappati

Script to read datacard and plot shapes

Requirements: python 2, ROOT
run with: python plotDatacardShapes.py
"""

from ROOT import TCanvas, TFile, THStack, TLegend, gPad


def readCardsAndPlot(filenametxt, filenameroot):
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
        histoitem.SetName(item) # set name bc the one they get is weird
        histolist.append(histoitem)
        #print(item)

    # do plot
    canvas = TCanvas("canvas", "canvas", 800, 600)
    canvas.cd()
    # canvas.SetLogy() understand why does not work

    histolist[0].SetLineColor(2)
    histolist[0].SetMarkerStyle(6)
    histolist[0].GetXaxis().SetTitle("NN score")
    histolist[0].GetYaxis().SetRangeUser(0.,700.)
    histolist[0].GetYaxis().SetTitle("Events")
    histolist[0].Draw("p")

    #histolist[1].Draw("same")

    for n, item in enumerate(histolist[1:]):
        item.SetLineColor(51+n)
        item.SetMarkerStyle(6)
        item.Draw("same p")

    # legend, need to define coordinates
    gPad.BuildLegend(0.64,0.38,0.94,0.87)

    canvas.SaveAs("shapes_CCLUB.png")

    #hs = THStack("hs","")



if __name__ == "__main__":
    # card CCLUB
    filenametxt = "../card_CCLUB/hhbbtt_res1b_etau_2022_13p6TeV.txt"
    filenameroot = "../card_CCLUB/hhbbtt_res1b_etau_2022_13p6TeV.root"
    # card Francisco
    # filename = "../card_Francisco_11Jun/MuTau_BinaryTransf_Res1b_signal_2022.txt"
    # filename = "../card_Francisco_26Jun/MuTau_BinaryTransf_Res1b_signal_2022.txt"

    print "Reading files", filenametxt, filenameroot, "..."
    readCardsAndPlot(filenametxt, filenameroot)
