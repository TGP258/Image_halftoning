import cv2
import numpy as np

def generate_complementary_halftones(image_path, output1_path, output2_path):
    # 读取图像并转为灰度
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    h, w = img.shape

    # 创建棋盘掩模（2x2像素的棋盘格）
    mask = np.zeros((h, w), dtype=np.uint8)
    mask[::2, ::2] = 1  # 交替黑白
    mask[1::2, 1::2] = 1

    # 掩模1：保留棋盘白格，其余置白
    halftone1 = img.copy()
    halftone1[mask == 0] = 255

    # 掩模2：保留棋盘黑格，其余置白
    halftone2 = img.copy()
    halftone2[mask == 1] = 255

    # 对两张图分别应用半调处理（简化示例，实际可用误差扩散）
    # 此处可替换为更精细的半调算法（如Floyd-Steinberg）
    _, halftone1 = cv2.threshold(halftone1, 128, 255, cv2.THRESH_BINARY)
    _, halftone2 = cv2.threshold(halftone2, 128, 255, cv2.THRESH_BINARY)

    # 保存结果
    cv2.imwrite(output1_path, halftone1)
    cv2.imwrite(output2_path, halftone2)

# 使用示例
generate_complementary_halftones("input.jpg", "halftone1.png", "halftone2.png")