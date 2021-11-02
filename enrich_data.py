import pandas as pd
from os import listdir, mkdir
from os.path import isfile, join, isdir


def enhance_data(indir, outdir, ignore_list=None):
    if ignore_list is None:
        ignore_list = []

    if not isdir(outdir):
        mkdir(outdir)

    csvfiles = [f for f in listdir(indir) if isfile(join(indir, f))]

    for csvfile in csvfiles:
        if ".csv" not in csvfile:
            continue

        if csvfile in ignore_list:
            continue

        dataset = pd.read_csv(indir + csvfile, sep=",", header=0, decimal=".", index_col=False)

        new_feature = (dataset["SYN Flag Count"] - dataset["ACK Flag Count"]) * (dataset["ACK Flag Count"] + 1)
        dataset.insert(loc=dataset.columns.get_loc("ACK Flag Count"), column="(SYN - ACK)x(RST + 1) Flag Count", value=new_feature)

        dataset.to_csv(outdir + csvfile, sep=",", decimal=".", index=False)


# Enhance flow
enhance_data("data/flow_gen/", "data/enhanced_flow_gen/")


# # Enhance original testfiles
# enhance_data("data/testfiles/", "data/enhanced_testfiles/", ["overview_cyberhunttests.csv"])

