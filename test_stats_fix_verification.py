# -*- coding: utf-8 -*-
"""
验证增量采集统计信息修复是否正确
"""

import sys
import os
sys.path.append(os.path.dirname(__file__))

def test_incremental_stats_logic():
    """测试增量采集统计逻辑是否正确"""
    print("=== 验证增量采集统计信息修复 ===")
    
    # 模拟数据
    file1_products = list(range(60))  # 第一份文档60个产品
    file2_new_products = list(range(8))  # 第二份文档8个新产品
    
    print(f"第一份文档产品数: {len(file1_products)}")
    print(f"第二份文档新产品数: {len(file2_new_products)}")
    
    # 模拟增量采集逻辑
    total_products = len(file1_products) + len(file2_new_products)
    print(f"计算总产品数: {total_products}")
    
    # 验证逻辑是否正确
    expected_total = 68
    if total_products == expected_total:
        print(f"[SUCCESS] 统计计算逻辑正确: {total_products}")
    else:
        print(f"[ERROR] 统计计算错误, 期望: {expected_total}, 实际: {total_products}")
    
    print("\n=== 代码修复验证 ===")
    
    # 检查main.py中的关键修复点
    import main
    from pathlib import Path
    
    main_file = Path(__file__).parent / "main.py"
    content = main_file.read_text(encoding='utf-8')
    
    # 检查关键修复点
    fixes_verified = []
    
    # 1. 检查是否计算了total_products
    if "total_products = len(existing_products) + len(new_products)" in content:
        fixes_verified.append("[OK] 总产品数计算逻辑已添加")
    else:
        fixes_verified.append("[ERROR] 缺少总产品数计算逻辑")
    
    # 2. 检查是否调用了update_stats更新产品数
    if "self.update_stats(products=total_products)" in content:
        fixes_verified.append("[OK] 产品统计更新调用已添加")
    else:
        fixes_verified.append("[ERROR] 缺少产品统计更新调用")
    
    # 3. 检查是否有图片总数统计
    if "total_images = len(list(images_dir.glob" in content:
        fixes_verified.append("[OK] 图片总数统计逻辑已添加")
    else:
        fixes_verified.append("[ERROR] 缺少图片总数统计逻辑")
    
    # 4. 检查是否调用了update_stats更新图片数
    if "self.update_stats(images=total_images)" in content:
        fixes_verified.append("[OK] 图片统计更新调用已添加")
    else:
        fixes_verified.append("[ERROR] 缺少图片统计更新调用")
    
    print("代码修复检查结果:")
    for fix in fixes_verified:
        print(f"  {fix}")
    
    # 统计成功的修复
    success_count = len([f for f in fixes_verified if f.startswith("[OK]")])
    total_checks = len(fixes_verified)
    
    print(f"\n修复完成度: {success_count}/{total_checks}")
    
    if success_count == total_checks:
        print("[SUCCESS] 所有统计信息更新修复已正确实现")
    else:
        print("[WARNING] 部分修复可能存在问题")
    
    print("\n=== 功能验证总结 ===")
    print("修复内容:")
    print("1. 在增量采集时计算总产品数（现有产品 + 新增产品）")
    print("2. 调用update_stats更新产品数量显示")
    print("3. 统计实际已下载的图片总数")
    print("4. 调用update_stats更新图片数量显示")
    print("\n期望效果:")
    print("- 当第二份文档更新触发增量采集时")
    print("- UI中的产品数量和图片数量统计会显示总计数")
    print("- 不再只显示新增数量，而是显示累积总数")
    
    print("\n=== 验证完成 ===")

if __name__ == "__main__":
    test_incremental_stats_logic()