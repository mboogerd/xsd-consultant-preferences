# %%
import pandas as pd

sheet_url = "https://docs.google.com/spreadsheets/d/14-QWsay_buOeKuHlMlk9P0w4Zv9lEsUEKNHs6GkDFR8/edit?gid=1521745335"
export_url = sheet_url.replace(
    "/edit?gid=", "/export?format=csv&gid=")
# %%
df = pd.read_csv(export_url)
# %%
df

# %%

# %%

# %%
