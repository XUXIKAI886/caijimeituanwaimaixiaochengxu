# -*- coding: utf-8 -*-
"""
测试修复后的完整数据采集功能
"""

import sys
import os
sys.path.append(os.path.dirname(__file__))

from main import MeituanDataCollector
import asyncio

def test_fixed_collection():
    """测试修复后的完整数据采集功能"""
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
        # 步骤1: 完整解析第一份文档
        print("\n=== 步骤1: 完整解析第一份文档 ===")
        categories, products_file1 = collector.parse_complete_data(file1)
        print(f"第一份文档：解析到 {len(categories)} 个分类，{len(products_file1)} 个产品")
        
        # 显示前5个产品
        for i, product in enumerate(products_file1[:5]):
            try:
                print(f"  产品{i+1}: {product['category_name']} - {product['product_name'][:20]}... - {product['product_price']}元")
            except UnicodeEncodeError:
                print(f"  产品{i+1}: {product['category_name']} - [特殊字符] - {product['product_price']}元")
            
        # 步骤2: 解析第二份文档的更新产品
        print("\n=== 步骤2: 解析第二份文档的更新数据 ===")
        products_file2 = collector.parse_products(file2, categories)
        print(f"第二份文档：解析到 {len(products_file2)} 个更新产品")
        
        # 显示第二份文档的产品
        for i, product in enumerate(products_file2):
            print(f"  更新产品{i+1}: {product['category_name']} - {product['product_name']} - {product['product_price']}元")
        
        # 步骤3: 合并所有产品数据
        print("\n=== 步骤3: 合并数据 ===")
        all_products = products_file1 + products_file2
        print(f"合并数据：总共 {len(all_products)} 个产品")
        
        # 按分类统计
        category_stats = {}
        for product in all_products:
            cat_name = product['category_name']
            if cat_name not in category_stats:
                category_stats[cat_name] = 0
            category_stats[cat_name] += 1
        
        print("\n按分类统计:")
        for cat_name, count in category_stats.items():
            print(f"  {cat_name}: {count} 个产品")
            
        # 步骤4: 测试生成Excel
        if all_products:
            print("\n=== 步骤4: 测试Excel生成 ===")
            excel_path = collector.generate_excel(all_products)
            print(f"Excel报告生成: {excel_path}")
            
            # 检查文件是否真的生成
            full_path = collector.output_dir / excel_path
            if full_path.exists():
                file_size = full_path.stat().st_size
                print(f"Excel文件确实存在，大小: {file_size} 字节")
            else:
                print("错误：Excel文件未生成！")
                
        print("\n=== 测试完成 ===")
        print(f"最终结果：成功采集 {len(all_products)} 个产品")
        
    except Exception as e:
        print(f"测试过程中出错: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_fixed_collection()