"""
创建测试用 PDF 文件的工具模块
"""
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from pathlib import Path
import os

def create_test_pdf(output_path):
    """
    创建一个包含三页不同内容的测试PDF文件
    """
    # 注册中文字体
    pdfmetrics.registerFont(UnicodeCIDFont('STSong-Light'))
    
    c = canvas.Canvas(str(output_path), pagesize=A4)
    
    # 第一页：文本和矩形
    c.setFont('STSong-Light', 12)
    c.drawString(100, 750, "这是第一页")
    c.drawString(100, 700, "这是一个包含中文的测试文档")
    c.rect(100, 600, 200, 100)
    
    # 第二页：文本和圆形
    c.showPage()
    c.setFont('STSong-Light', 12)
    c.drawString(100, 750, "这是第二页")
    c.drawString(100, 700, "这里有一个圆形")
    c.circle(200, 600, 50)
    
    # 第三页：文本和三角形
    c.showPage()
    c.setFont('STSong-Light', 12)
    c.drawString(100, 750, "这是第三页")
    c.drawString(100, 700, "这里有一个三角形")
    c.line(150, 550, 250, 650)
    c.line(250, 650, 350, 550)
    c.line(350, 550, 150, 550)
    
    # 添加文档大纲
    c.bookmarkPage('page1')
    c.addOutlineEntry('第一页', 'page1', 0)
    c.bookmarkPage('page2')
    c.addOutlineEntry('第二页', 'page2', 0)
    c.bookmarkPage('page3')
    c.addOutlineEntry('第三页', 'page3', 0)
    
    c.save()
    return output_path

if __name__ == "__main__":
    # 测试代码
    create_test_pdf("test.pdf")