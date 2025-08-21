# -*- coding: utf-8 -*-
"""
调试数据解析功能
"""

import sys
import os
sys.path.append(os.path.dirname(__file__))

from main import MeituanDataCollector
import json

def debug_parsing():
    """调试数据解析功能"""
    collector = MeituanDataCollector()
    
    # 设置文件路径
    file1 = r"D:\ailun\xiaochengxumeituan.txt"
    file2 = r"D:\ailun\xiaochengxumeituan01.txt"
    
    print(f"调试文件1: {file1}")
    print(f"文件1存在: {os.path.exists(file1)}")
    print(f"调试文件2: {file2}")  
    print(f"文件2存在: {os.path.exists(file2)}")
    
    if not os.path.exists(file1) or not os.path.exists(file2):
        print("数据文件不存在，无法调试")
        return
    
    # 读取文件1并分析结构
    print("\n=== 文件1数据结构分析 ===")
    with open(file1, 'r', encoding='utf-8') as f:
        content1 = f.read()
    
    data1 = json.loads(content1)
    if 'data' in data1 and 'food_spu_tags' in data1['data']:
        print(f"文件1包含 {len(data1['data']['food_spu_tags'])} 个分类")
        for i, category in enumerate(data1['data']['food_spu_tags']):
            tag = category.get('tag', 'unknown')
            name = category.get('name', 'unknown')
            print(f"  分类{i+1}: {tag} - {name}")
    
    # 读取文件2并分析结构
    print("\n=== 文件2数据结构分析 ===")
    with open(file2, 'r', encoding='utf-8') as f:
        content2 = f.read()
    
    data2 = json.loads(content2)
    if 'data' in data2 and 'food_spu_tags' in data2['data']:
        total_products = 0
        print(f"文件2包含 {len(data2['data']['food_spu_tags'])} 个分类")
        for i, category in enumerate(data2['data']['food_spu_tags']):
            tag = category.get('tag', 'unknown')
            
            # 检查不同的产品字段名
            spus_count = 0
            dynamic_spus_count = 0
            
            if 'spus' in category and category['spus']:
                spus_count = len(category['spus'])
            
            if 'dynamic_spus' in category and category['dynamic_spus']:
                dynamic_spus_count = len(category['dynamic_spus'])
            
            category_total = spus_count + dynamic_spus_count
            total_products += category_total
            
            print(f"  分类{i+1}: {tag}")
            print(f"    spus: {spus_count} 个产品")
            print(f"    dynamic_spus: {dynamic_spus_count} 个产品")
            print(f"    小计: {category_total} 个产品")
            
            # 显示前3个产品的详细信息
            if 'dynamic_spus' in category and category['dynamic_spus']:
                print("    产品示例:")
                for j, product in enumerate(category['dynamic_spus'][:3]):
                    name = product.get('name', 'unknown')
                    price = product.get('min_price', 0)
                    print(f"      {j+1}. {name} - {price}元")
        
        print(f"\n文件2总产品数: {total_products}")
    
    # 测试现有解析逻辑
    print("\n=== 测试现有解析逻辑 ===")
    try:
        categories = collector.parse_categories(file1)
        print(f"解析到 {len(categories)} 个分类")
        
        products = collector.parse_products(file2, categories)
        print(f"解析到 {len(products)} 个产品")
        
        # 按分类统计
        category_stats = {}
        for product in products:
            cat_name = product['category_name']
            if cat_name not in category_stats:
                category_stats[cat_name] = 0
            category_stats[cat_name] += 1
        
        print("按分类统计:")
        for cat_name, count in category_stats.items():
            print(f"  {cat_name}: {count} 个产品")
    
    except Exception as e:
        print(f"解析过程中出错: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    debug_parsing()