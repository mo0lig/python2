import matplotlib.pyplot as plt

plt.figure(figsize=(7,5))
x = [24, 27.2 , 16.5, 3.4, 9.2, 19.7]
country = ['UK', 'India', 'Germany', 'Austria', 'South Korea', 'US']
e = [0, 0, 0, 0, 0, 0.2]
plt.pie(x, labels = country, explode = e, autopct = '%1.1f%%', shadow=True);
plt.show()