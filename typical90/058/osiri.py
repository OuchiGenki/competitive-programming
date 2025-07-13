import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  # x座標の値
y = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5]  # y座標の値

fig, ax = plt.subplots()
ax.scatter(x, y, s=200)  # sは点のサイズを指定するパラメータ

plt.show()
