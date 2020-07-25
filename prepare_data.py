import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from utils import load_dframe


dframe = load_dframe(0)

# get intervals before the new episode
is_new_ha = dframe["ha_new"] == True

is_before_ha = np.roll(is_new_ha, -1)
is_before_ha[-1] = False

dframe_before_ha = dframe.iloc[is_before_ha, :]


# get intervals without HA and not preceeding new HA
not_ongoing_ha = dframe["ha_cont"] != True
no_ha = np.logical_and(not_ongoing_ha, np.logical_not(is_new_ha)).to_numpy()

dframe_no_ha = dframe.iloc[no_ha, :]


(dframe['ha_new'] + dframe['ha_cont']).astype(int).plot()
# dframe['more_light'].fillna(0).astype(int).plot()

# dframe[["ha_new", "smell_sens", "depression", "anxiety"]].fillna(False).astype(
#     int
# ).plot()
# plt.show()

# sns.catplot(x='date', y='sleepiness', data=dframe.reset_index(), order=[5, 4, 3, 2, 1])
sns.pairplot(dframe)
dframe[["sleepiness", "anxiety", "depression"]].fillna(1).astype(int).plot()
dframe["ha_new"].fillna(0).astype(int).plot()
plt.show()
