import numpy as np
import os
from PIL import Image, ImageOps  
from matplotlib import pyplot as plt
from scipy import stats


def mean(list_of_nums):
    total = 0
    for num in list_of_nums:
        total = total + num
    return total / len(list_of_nums)


def mode(list_of_nums):
    mode = max(list_of_nums)
    mode_index = list(list_of_nums).index(mode)
    return (mode_index * 10, (mode_index + 1) * 10)


def median(list_of_nums):
    l = list(list_of_nums)
    l.sort()
    if len(l) % 2 != 0:
        middle_index = np.inf((len(l) - 1) / 2)
        return l[middle_index]
    elif len(l) % 2 == 0:
        middle_index_1 = int(len(l) / 2)
        middle_index_2 = int(len(l) / 2) - 1
        return_middle = (l[middle_index_1] + l[middle_index_2]) / 2
        return return_middle


def median_index(list_of_nums):
    l = list(list_of_nums)
    l.sort()
    if len(l) % 2 != 0:
        middle_index = np.inf((len(l) - 1) / 2)
        return middle_index
    elif len(l) % 2 == 0:
        middle_index_1 = int(len(l) / 2)
        middle_index_2 = int(len(l) / 2) - 1
        return (middle_index_2 * 10, middle_index_1 * 10)


def chech_hypothesis(value):
    stat, p = stats.normaltest(value)
    print("p-value={0}".format(p))

    alpha = 0.05
    if p > alpha:
        print('Гипотеза не отклонена')
    else:
        print('Гипотеза отклонена')


def main():
    os.chdir('/home/kirill/PythonProjects/SA/')

    image_1 = Image.open("planet.jpg")
    image_2 = Image.open("landscape.jpg")

    width_1, height_1 = image_1.size
    width_2, height_2 = image_2.size

    image_1_grayscale = image_1.convert('L')
    image_2_grayscale = image_2.convert('L')

    image_1_grayscale.save("gray_scale_planet.jpg")
    image_2_grayscale.save("gray_scale_landscape.jpg")

    bins = list(range(0, 255, 10))
    bins.append(255)
    print(bins)
    num_bins = int(255 / 10) + 1
    bins_range = 0, 255

    size = min(width_1, width_2), min(height_1, height_2)
    image_1_grayscale = image_1_grayscale.resize(size, Image.BICUBIC)
    image_2_grayscale = image_2_grayscale.resize(size, Image.BICUBIC)

    first_image_pixels = list(image_1_grayscale.getdata())
    second_image_pixels = list(image_2_grayscale.getdata())


    #Second image histogram
    first_bins_values, _, _ = \
        plt.hist(first_image_pixels, num_bins, bins_range,label = "Planet", facecolor='mediumseagreen', edgecolor='black', linewidth=1)

    plt.title("Histograms of grayscale planet",fontsize=15)
    plt.xlabel('Intensity value',fontsize=15)
    plt.ylabel('Count',fontsize=15)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.legend(loc='upper right',fontsize=9)
    plt.show()

    print(first_bins_values)

    #Second image histogram
    second_bins_values, _, _ = \
        plt.hist(second_image_pixels, num_bins, bins_range,label = "Landscape", facecolor='salmon', edgecolor='black', linewidth=1)

    plt.title("Histograms of grayscale landscape",fontsize=15)
    plt.xlabel('Intensity value',fontsize=15)
    plt.ylabel('Count',fontsize=15)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.legend(loc='upper right',fontsize=9)
    plt.show()

    print(second_bins_values)


    print('\t\t First histogram\t\t Second histogram')
    print('mode\t\t', mode(first_bins_values), '\t\t\t', mode(second_bins_values))
    print('mean\t\t', mean(first_bins_values), '\t\t', mean(second_bins_values))
    print('Stand. deviation', np.std(first_bins_values), '\t\t', np.std(second_bins_values))
    print('median \t\t', median(first_bins_values), '\t\t\t', median(second_bins_values))
    print('median interval\t', median_index(first_bins_values), '\t\t\t', median_index(second_bins_values))
    print('')

    print('Histograms corr coeff: ', np.corrcoef(first_bins_values, second_bins_values)[0, 1])
    print('Images corr coeff: ', np.corrcoef(first_image_pixels, second_image_pixels)[0, 1])

    chech_hypothesis(first_bins_values)
    chech_hypothesis(second_bins_values)


if __name__ == "__main__":
    main()