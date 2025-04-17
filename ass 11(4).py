import pandas as pd
import numpy as np

data = {
    'John': [True, False, True, True, False, True, False, False, True, False],
    'Judy': [True, True, False, True, False, False, False, True, True, False]
}

df = pd.DataFrame(data)

party_days = df['John'] & df['Judy']
days_til_party = np.full(len(df), np.nan)

next_party_index = None
for i in reversed(range(len(df))):
    if party_days[i]:
        next_party_index = i
        days_til_party[i] = 0
    elif next_party_index is not None:
        days_til_party[i] = next_party_index - i

df['days_til_party'] = days_til_party.astype('Int64')

print(df)
