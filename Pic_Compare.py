# coding=utf-8
# 导入python包
import cv2
import matplotlib.pyplot as plt
import numpy as np
from skimage.measure import compare_ssim as ssim


def mse(imageA, imageB):
    # 计算两张图片的MSE指标
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])

    # 返回结果，该值越小越好
    return err


def compare_images(imageA, imageB, title):
    # 分别计算输入图片的MSE和SSIM指标值的大小
    m = mse(imageA, imageB)
    s = ssim(imageA, imageB)

    # 创建figure
    fig = plt.figure(title)
    plt.suptitle("MSE: %.2f, SSIM: %.2f" % (m, s))

    # 显示第一张图片
    ax = fig.add_subplot(1, 2, 1)
    plt.imshow(imageA, cmap=plt.cm.gray)
    plt.axis("off")

    # 显示第二张图片
    ax = fig.add_subplot(1, 2, 2)
    plt.imshow(imageB, cmap=plt.cm.gray)
    plt.axis("off")
    plt.tight_layout()
    plt.show()


# 读取图片
original1 = cv2.imread("test3.jpg")
contrast1 = cv2.imread("test3_adjust1.jpg")
shopped1 = cv2.imread("test2.jpg")

# 将彩色图转换为灰度图
original = cv2.cvtColor(original1, cv2.COLOR_BGR2GRAY)
contrast = cv2.cvtColor(contrast1, cv2.COLOR_BGR2GRAY)
shopped = cv2.cvtColor(shopped1, cv2.COLOR_BGR2GRAY)

# 初始化figure对象
fig = plt.figure("Images")
images = ("Original", original), ("Enhance", contrast), ("Others", shopped)

# 遍历每张图片
for (i, (name, image)) in enumerate(images):
    # 显示图片
    ax = fig.add_subplot(1, 3, i + 1)
    ax.set_title(name)
    plt.imshow(image, cmap=plt.cm.gray)
    plt.axis("off")
plt.tight_layout()
plt.show()

# 比较图片
compare_images(original, original, "Original vs Original")
compare_images(original, contrast, "Original vs Enhance")
compare_images(original, shopped, "Original vs Others")
