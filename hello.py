import numpy as np
import pandas as pd

print("NumPy", np.__version__)
print("pandas", pd.__version__)

campaigns = pd.DataFrame({
    "campaign": ["Spring Sale", "Webinar", "Retargeting"],
    "spend": [500, 300, 200],
    "clicks": [1250, 400, 380],
})
campaigns["cpc"] = (campaigns["spend"] / campaigns["clicks"]).round(2)
print(campaigns)
