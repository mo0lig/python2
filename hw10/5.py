import matplotlib as mpl
import matplotlib.pyplot as plt

data_names = ['Germany', 'Greece', 'USA', 'UK',
              'Italy', 'Ireland', 'Slovenia', 'Korea',
              'China', 'Denmark']
data_values = [1000, 400, 500, 147, 175, 125, 134, 111, 88, 77]

dpi = 80
fig = plt.figure(dpi = dpi, figsize = (512 / dpi, 384 / dpi) )
mpl.rcParams.update({'font.size': 9})
xs = range(len(data_names))
plt.pie(data_values, autopct='%.1f', radius = 1.1,explode = [0.15] + [0 for _ in range(len(data_names) - 1)] )
plt.legend(bbox_to_anchor = (-0.16, 0.45, 0.25, 0.25),loc = 'lower left', labels = data_names )
fig.savefig('pie.png')
plt.show()