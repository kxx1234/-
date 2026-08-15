"""
直接使用SQLAlchemy创建事件，不依赖app模块
"""
from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timedelta
import random
import json

# 数据库连接
DATABASE_URL = "sqlite:///./law_game.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# 简化的Event模型
class Event(Base):
    __tablename__ = "events"
    
    id = Column(Integer, primary_key=True, index=True)
    event_id = Column(String, unique=True, index=True)
    name = Column(String, nullable=False)
    description = Column(Text)
    dispute_type = Column(String)
    our_side = Column(JSON)
    opponent_side = Column(JSON)
    legal_systems = Column(JSON)
    fact_summary = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

def create_events():
    db = SessionLocal()
    
    event_templates = [
        {"name": "日本违法扣押中国渔船事件", "dispute_type": "海洋权益", "our_side": ["中国渔业局", "中国海警"], "opponent_side": ["日本海上保安厅"]},
        {"name": "东海防空识别区争端", "dispute_type": "领空争议", "our_side": ["中国国防部"], "opponent_side": ["日本自卫队"]},
        {"name": "南海岛礁建设争议", "dispute_type": "领土主权", "our_side": ["中国外交部"], "opponent_side": ["菲律宾政府"]},
        {"name": "靖国神社参拜事件", "dispute_type": "历史问题", "our_side": ["中国外交部"], "opponent_side": ["日本首相"]},
        {"name": "专属经济区捕鱼纠纷", "dispute_type": "海洋权益", "our_side": ["中国渔业部门"], "opponent_side": ["韩国海警"]},
        {"name": "台湾海峡航行自由争议", "dispute_type": "海洋权益", "our_side": ["中国海军"], "opponent_side": ["美国海军"]},
        {"name": "钓鱼岛巡航执法", "dispute_type": "领土主权", "our_side": ["中国海警"], "opponent_side": ["日本海上保安厅"]},
        {"name": "黄岩岛对峙事件", "dispute_type": "领土主权", "our_side": ["中国海警"], "opponent_side": ["菲律宾海岸警卫队"]},
        {"name": "西沙群岛油气开发争端", "dispute_type": "资源开发", "our_side": ["中国海洋石油"], "opponent_side": ["越南政府"]},
        {"name": "东海油气田开发争议", "dispute_type": "资源开发", "our_side": ["中国外交部"], "opponent_side": ["日本经济产业省"]},
        {"name": "南海岛礁12海里巡航", "dispute_type": "海洋权益", "our_side": ["中国海军"], "opponent_side": ["美国海军"]},
        {"name": "中印边境对峙", "dispute_type": "领土主权", "our_side": ["中国边防部队"], "opponent_side": ["印度边防军"]},
        {"name": "渔业执法冲突", "dispute_type": "海洋权益", "our_side": ["中国渔政"], "opponent_side": ["印尼海警"]},
    ]
    
    legal_systems = ["《联合国海洋法公约》", "《中华人民共和国领海法》", "《中华人民共和国海警法》"]
    
    try:
        existing = db.query(Event).count()
        print(f"📊 当前事件数量: {existing}")
        
        base_time = datetime.now()
        for i, template in enumerate(event_templates):
            event_id = f"Event-{datetime.now().strftime('%Y%m%d')}-{str(i+100).zfill(3)}"
            
            event = Event(
                event_id=event_id,
                name=template["name"],
                description=f"争议事件：{template['name']}",
                dispute_type=template["dispute_type"],
                our_side=json.dumps(template["our_side"], ensure_ascii=False),
                opponent_side=json.dumps(template["opponent_side"], ensure_ascii=False),
                legal_systems=json.dumps(random.sample(legal_systems, k=2), ensure_ascii=False),
                fact_summary=f"{template['name']}相关法律争议",
                created_at=base_time - timedelta(days=random.randint(0, 30)),
                updated_at=base_time
            )
            db.add(event)
        
        db.commit()
        
        total = db.query(Event).count()
        print(f"✅ 新增事件后总数: {total}")
        
    finally:
        db.close()

if __name__ == "__main__":
    create_events()
