# -*- coding: utf-8 -*-
"""
分析第一份文档的数据结构
"""

import json
import os

def analyze_first_file():
    """分析第一份文档的数据结构"""
    file_path = r"D:\ailun\xiaochengxumeituan.txt"
    
    print(f"分析文件: {file_path}")
    print(f"文件存在: {os.path.exists(file_path)}")
    
    if not os.path.exists(file_path):
        print("文件不存在，无法分析")
        return
    
    try:
        # 读取并分析文件
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        data = json.loads(content)
        
        if 'data' in data and 'food_spu_tags' in data['data']:
            food_spu_tags = data['data']['food_spu_tags']
            
            total_products = 0
            total_categories = len(food_spu_tags)
            
            print(f"\n=== 第一份文档数据分析 ===")
            print(f"总分类数: {total_categories}")
            
            # 分析每个分类的产品
            for i, category in enumerate(food_spu_tags):
                tag = category.get('tag', 'unknown')
                name = category.get('name', 'unknown')
                
                # 检查不同的产品字段
                spus_count = 0
                dynamic_spus_count = 0
                
                if 'spus' in category and category['spus']:
                    spus_count = len(category['spus'])
                
                if 'dynamic_spus' in category and category['dynamic_spus']:
                    dynamic_spus_count = len(category['dynamic_spus'])
                
                category_total = spus_count + dynamic_spus_count
                total_products += category_total
                
                print(f"\n分类{i+1}: {name} (tag: {tag})")
                print(f"  spus: {spus_count} 个产品")
                print(f"  dynamic_spus: {dynamic_spus_count} 个产品")
                print(f"  小计: {category_total} 个产品")
                
                # 显示前3个产品示例
                if 'dynamic_spus' in category and category['dynamic_spus']:
                    print("  产品示例 (dynamic_spus):")
                    for j, product in enumerate(category['dynamic_spus'][:3]):
                        name_p = product.get('name', 'unknown')
                        price = product.get('min_price', 0)
                        # 安全打印，避免Unicode问题
                        try:
                            print(f"    {j+1}. {name_p[:20]}... - {price}元")
                        except UnicodeEncodeError:
                            print(f"    {j+1}. [产品名称包含特殊字符] - {price}元")
                
                if 'spus' in category and category['spus']:
                    print("  产品示例 (spus):")
                    for j, product in enumerate(category['spus'][:3]):
                        name_p = product.get('name', 'unknown')
                        price = product.get('min_price', 0)
                        # 安全打印，避免Unicode问题
                        try:
                            print(f"    {j+1}. {name_p[:20]}... - {price}元")
                        except UnicodeEncodeError:
                            print(f"    {j+1}. [产品名称包含特殊字符] - {price}元")
            
            print(f"\n=== 总计 ===")
            print(f"总分类数: {total_categories}")
            print(f"总产品数: {total_products}")
            
        else:
            print("数据格式不正确")
    
    except Exception as e:
        print(f"分析过程中出错: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    analyze_first_file()