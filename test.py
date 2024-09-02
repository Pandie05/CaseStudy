import pandas as pd

import matplotlib.pyplot as plt

jail = pd.read_csv("CaseStudy/csv/cty_jail_allSubgroups.csv")
grad = pd.read_csv("CaseStudy/csv/cty_hs_allSubgroups.csv")

print(jail.head())
print(grad.head())
