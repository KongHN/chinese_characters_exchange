import os
from PIL import Image

# 直接在代码里指定输入和输出路径（修改为你的实际路径）
INPUT_DIR = r"F:\科研\06Machine Learning, EEG, and Word Reading in Children\Real characters\objects real 2\objects real 2"
OUTPUT_DIR = r"C:\Users\孔昊男\Desktop\000000"


def process_bmp_files(operation):
    """
    处理指定目录下的所有BMP文件

    参数:
    operation (str): 操作类型，'horizontal' 或 'vertical'
    """
    # 显示当前使用的路径
    print(f"输入目录: {INPUT_DIR}")
    print(f"输出目录: {OUTPUT_DIR}")

    try:
        # 确保输出目录存在
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        print(f"输出目录已准备好: {OUTPUT_DIR}")
    except Exception as e:
        print(f"创建输出目录时出错: {str(e)}")
        print(f"请检查路径: {OUTPUT_DIR}")
        return

    # 获取所有BMP文件
    try:
        bmp_files = [f for f in os.listdir(INPUT_DIR) if f.lower().endswith('.bmp')]
    except Exception as e:
        print(f"读取输入目录时出错: {str(e)}")
        print(f"请检查路径: {INPUT_DIR}")
        return

    if not bmp_files:
        print(f"在目录 {INPUT_DIR} 中未找到BMP文件")
        return

    # 处理每个BMP文件
    for filename in bmp_files:
        input_path = os.path.join(INPUT_DIR, filename)
        try:
            # 打开图片
            with Image.open(input_path) as img:
                width, height = img.size

                if operation == 'horizontal':
                    # 横向切割和交换
                    half_height = height // 2
                    top_half = img.crop((0, 0, width, half_height))
                    bottom_half = img.crop((0, half_height, width, height))

                    # 创建新图片
                    new_img = Image.new('RGB', (width, height))
                    new_img.paste(bottom_half, (0, 0))
                    new_img.paste(top_half, (0, half_height))

                elif operation == 'vertical':
                    # 纵向切割和交换
                    half_width = width // 2
                    left_half = img.crop((0, 0, half_width, height))
                    right_half = img.crop((half_width, 0, width, height))

                    # 创建新图片
                    new_img = Image.new('RGB', (width, height))
                    new_img.paste(right_half, (0, 0))
                    new_img.paste(left_half, (half_width, 0))
                else:
                    print(f"未知操作: {operation}")
                    continue

                # 保存新图片
                output_filename = f"{os.path.splitext(filename)[0]}_{operation}.bmp"
                output_path = os.path.join(OUTPUT_DIR, output_filename)
                new_img.save(output_path)
                print(f"已处理: {filename} -> {output_filename}")

        except Exception as e:
            print(f"处理文件 {filename} 时出错: {str(e)}")


if __name__ == "__main__":
    # 执行横向切割操作
    process_bmp_files('horizontal')

    # 执行纵向切割操作
    process_bmp_files('vertical')    