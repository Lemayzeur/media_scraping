import os
import pandas as pd
from media import hl_parser, ln_parser

hosts = ("lenouvelliste.com", "www.haitilibre.com")

data_set = []
data = []
paj = 1

for host in hosts:
    if host == "www.haitilibre.com":
        url = f"https://{host}/flash-infos-{paj}.html"
        data = hl_parser(url)
    elif host == "lenouvelliste.com":
        url = f"https://{host}/national?page={paj}"
        data = ln_parser(url)

    data_set.extend(data[0])

    print(f"Creating {host} DataFrame ...")
    dataframe = pd.DataFrame(data_set)
    dataframe.to_csv(f"./test_{host}.csv")
    print("Dataframe Save ...\n\n")

print("\n\nEND SCRIPT\n\n")
