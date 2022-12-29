import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import seaborn as sns

import os

pd.set_option('display.max_colwidth', None)

survey_data = pd.read_csv("/Dataset/input/survey_results_public.csv")
schema_data = pd.read_csv("/Dataset/input/survey_results_schema.csv")
currency_data = pd.read_csv("/Dataset/input/National Currencies Per US Dollar.csv", encoding="cp1252")