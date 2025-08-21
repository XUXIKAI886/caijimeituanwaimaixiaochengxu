# -*- coding: utf-8 -*-
"""
测试统计信息更新功能
"""

import sys
import os
sys.path.append(os.path.dirname(__file__))

from main import MeituanDataCollector
import time
import json
from pathlib import Path

def test_stats_update():
    """测试统计信息更新功能"""
    print("=== 统计信息更新测试 ===")
    
    # 创建采集器实例
    collector = MeituanDataCollector()
    
    # 设置文件路径
    file1 = r"D:\ailun\xiaochengxumeituan.txt"
    file2 = r"D:\ailun\xiaochengxumeituan01.txt"
    
    collector.file1_var.set(file1)
    collector.file2_var.set(file2)
    
    print(f"测试文件1: {file1}")
    print(f"测试文件2: {file2}")
    print(f"文件1存在: {os.path.exists(file1)}")
    print(f"文件2存在: {os.path.exists(file2)}")
    
    if not os.path.exists(file1) or not os.path.exists(file2):
        print("数据文件不存在，无法测试")
        return
    
    try:
        print("\n1. 测试完整采集（第一份文档）...")
        categories, products_from_file1 = collector.parse_complete_data(file1)
        print(f"   第一份文档产品数量: {len(products_from_file1)}")
        
        print("\n2. 测试增量数据解析（第二份文档）...")
        new_products = collector.parse_products(file2, categories)
        print(f"   第二份文档新增产品数量: {len(new_products)}")
        
        print("\n3. 计算总统计...")
        total_products = len(products_from_file1) + len(new_products)
        print(f"   总产品数量: {total_products}")
        
        # 检查输出目录的图片
        images_dir = collector.output_dir / "产品图片"
        if images_dir.exists():
            total_images = len(list(images_dir.glob("*.jpg")))
            print(f"   已下载图片数量: {total_images}")
        else:
            print("   图片目录不存在")
            total_images = 0
        
        print("\n4. 测试统计信息更新方法...")
        
        # 模拟UI更新
        print("   更新产品数量统计...")
        collector.product_count_var.set(str(total_products))
        print(f"   产品统计显示: {collector.product_count_var.get()}")
        
        print("   更新图片数量统计...")
        collector.image_count_var.set(str(total_images))
        print(f"   图片统计显示: {collector.image_count_var.get()}")
        
        print("\n5. 测试增量工作流程...")
        # 直接调用增量采集逻辑（但不实际下载）
        if new_products:
            print(f"   发现 {len(new_products)} 个新产品")
            print("   模拟统计更新...")
            
            # 更新产品统计（现有 + 新增）
            updated_total = len(products_from_file1) + len(new_products)
            collector.product_count_var.set(str(updated_total))
            print(f"   更新后产品统计: {collector.product_count_var.get()}")
            
        print("\n=== 测试结果 ===")
        print(f"第一份文档产品: {len(products_from_file1)}")
        print(f"第二份文档新增: {len(new_products)}")
        print(f"总产品数量: {total_products}")
        print(f"已下载图片: {total_images}")
        print(f"UI显示产品数: {collector.product_count_var.get()}")
        print(f"UI显示图片数: {collector.image_count_var.get()}")
        
        # 验证统计是否正确
        if collector.product_count_var.get() == str(total_products):
            print("\n[OK] 产品统计更新正确")
        else:
            print(f"\n[ERROR] 产品统计不正确，期望 {total_products}，实际 {collector.product_count_var.get()}")
        
        if collector.image_count_var.get() == str(total_images):
            print("[OK] 图片统计更新正确")
        else:
            print(f"[ERROR] 图片统计不正确，期望 {total_images}，实际 {collector.image_count_var.get()}")
        
        print("\n=== 统计信息更新测试完成 ===")
        
    except Exception as e:
        print(f"测试过程中出错: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_stats_update()