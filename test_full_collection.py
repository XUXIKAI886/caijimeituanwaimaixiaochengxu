# -*- coding: utf-8 -*-
"""
完整测试数据采集功能
"""

import sys
import os
sys.path.append(os.path.dirname(__file__))

from main import MeituanDataCollector
import asyncio

def test_full_collection():
    """完整测试数据采集功能"""
    collector = MeituanDataCollector()
    
    # 设置文件路径
    file1 = r"D:\ailun\xiaochengxumeituan.txt"
    file2 = r"D:\ailun\xiaochengxumeituan01.txt"
    
    print(f"测试文件1: {file1}")
    print(f"文件1存在: {os.path.exists(file1)}")
    print(f"测试文件2: {file2}")  
    print(f"文件2存在: {os.path.exists(file2)}")
    
    if not os.path.exists(file1) or not os.path.exists(file2):
        print("数据文件不存在，无法测试")
        return
        
    try:
        # 步骤1: 解析分类
        print("\n=== 步骤1: 解析分类 ===")
        categories = collector.parse_categories(file1)
        print(f"解析到 {len(categories)} 个分类")
        for tag, name in list(categories.items())[:5]:  # 显示前5个
            print(f"  {tag}: {name}")
            
        # 步骤2: 解析产品 (修复后)
        print("\n=== 步骤2: 解析产品 (修复后) ===")
        products = collector.parse_products(file2, categories)
        print(f"解析到 {len(products)} 个产品")
        
        # 显示所有产品的详细信息
        for i, product in enumerate(products):
            print(f"  产品{i+1}: {product['category_name']} - {product['product_name']} - {product['product_price']}元")
            print(f"    图片URL: {product['image_url'][:50]}...")
            
        # 步骤3: 测试生成Excel
        if products:
            print("\n=== 步骤3: 测试Excel生成 ===")
            excel_path = collector.generate_excel(products)
            print(f"Excel报告生成: {excel_path}")
            
            # 检查文件是否真的生成
            full_path = collector.output_dir / excel_path
            if full_path.exists():
                file_size = full_path.stat().st_size
                print(f"Excel文件确实存在，大小: {file_size} 字节")
            else:
                print("错误：Excel文件未生成！")
                
        # 步骤4: 测试图片下载 (下载前3张)
        if products:
            print("\n=== 步骤4: 测试图片下载 (前3张) ===")
            test_products = products[:3]  # 只测试前3个产品
            downloaded_count = asyncio.run(collector.download_images(test_products))
            print(f"图片下载测试完成，成功下载 {downloaded_count} 张")
            
            # 检查图片是否真的下载
            images_dir = collector.output_dir / "产品图片"
            if images_dir.exists():
                image_files = list(images_dir.glob("*.jpg"))
                print(f"图片文件夹中实际有 {len(image_files)} 个文件")
                for img_file in image_files[:3]:
                    print(f"  {img_file.name}")
                
        print("\n=== 测试完成 ===")
        print("如果看到上述输出且没有错误，说明程序运行正常")
        
    except Exception as e:
        print(f"测试过程中出错: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_full_collection()