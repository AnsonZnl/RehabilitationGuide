#第一步：pip install pillow PyPDF2

from PIL import Image
import os
from PyPDF2 import PdfMerger

def convert_to_jpg_and_merge_to_pdf(folder_path):
    pdf_files = []
    pdf_merger = PdfMerger()

    # 转换 .pdg 文件为 .jpg，然后每个 .jpg 转换为一个单独的 PDF
    for file in os.listdir(folder_path):
        if file.endswith('.pdg'):
            pdg_path = os.path.join(folder_path, file)
            jpg_path = pdg_path.replace('.pdg', '.jpg')
            pdf_path = pdg_path.replace('.pdg', '.pdf')

            # 将 .pdg 转换为 .jpg
            image = Image.open(pdg_path)
            image.convert('RGB').save(jpg_path)

            # 将 .jpg 转换为 PDF
            image = Image.open(jpg_path)
            image.convert('RGB').save(pdf_path, "PDF")
            pdf_files.append(pdf_path)

    # 合并所有 PDF 文件
    for pdf_file in sorted(pdf_files):
        pdf_merger.append(pdf_file)

    # 保存最终的 PDF 文件
    with open(os.path.join(folder_path, "output.pdf"), "wb") as output_pdf:
        pdf_merger.write(output_pdf)

    pdf_merger.close()

    # 删除所有 .jpg 和中间 .pdf 文件
    for file in os.listdir(folder_path):
        if file.endswith('.jpg') or (file.endswith('.pdf') and file != "output.pdf"):
            os.remove(os.path.join(folder_path, file))

# 使用示例
convert_to_jpg_and_merge_to_pdf('/Users/lxz/Desktop/RehabilitationGuide/颈椎病康复指南/实用颈椎病康复指南')