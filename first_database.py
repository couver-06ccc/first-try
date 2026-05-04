import sqlite3
import os

# ========================================
# 花之测试网站 - SQLite 数据库创建脚本
# ========================================

# 1. 删除旧数据库（如果存在）
db_path = 'flower_test.db'
if os.path.exists(db_path):
    print(f"🗑️  发现旧数据库，正在删除...")
    os.remove(db_path)

# 2. 创建数据库连接（不存在则自动创建）
print(f"📦 正在创建数据库: {db_path}")
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# 3. 创建用户表
print("📋 创建 users 表...")
cursor.execute('''
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
''')

# 4. 创建测试记录表
print("📋 创建 test_records 表...")
cursor.execute('''
CREATE TABLE test_records (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    flower_type TEXT NOT NULL,
    traits TEXT NOT NULL,
    answers TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
)
''')

# 5. 创建统计信息表
print("📋 创建 statistics 表...")
cursor.execute('''
CREATE TABLE statistics (
    id INTEGER PRIMARY KEY,
    total_tests INTEGER DEFAULT 0,
    rose_count INTEGER DEFAULT 0,
    sunflower_count INTEGER DEFAULT 0,
    orchid_count INTEGER DEFAULT 0,
    lavender_count INTEGER DEFAULT 0,
    cherry_count INTEGER DEFAULT 0,
    tulip_count INTEGER DEFAULT 0,
    plum_count INTEGER DEFAULT 0,
    lotus_count INTEGER DEFAULT 0,
    last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
''')

# 6. 创建索引（提升查询速度）
print("⚡ 创建索引...")
cursor.execute('CREATE INDEX idx_test_records_user_id ON test_records(user_id)')
cursor.execute('CREATE INDEX idx_test_records_created_at ON test_records(created_at)')

# 7. 插入初始统计数据
print("📥 插入初始数据...")
cursor.execute('INSERT INTO statistics (id, total_tests) VALUES (1, 0)')

# 8. 保存更改并关闭连接
conn.commit()
conn.close()

# 完成提示
print("\n✅ 数据库创建完成！")
print("=" * 40)
print(f"📁 数据库文件: {os.path.abspath(db_path)}")
print("📊 已创建的表:")
print("  - users (用户表)")
print("  - test_records (测试记录表)")
print("  - statistics (统计信息表)")
print("=" * 40)