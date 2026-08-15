"""
Database initialization and seed data script
Run this to populate initial data for laws and events
"""
from app.database import SessionLocal, init_db
from app.models.database import Law, Event
from datetime import datetime
import uuid

def seed_laws():
    """Seed initial law data"""
    db = SessionLocal()
    try:
        # Check if laws already exist
        if db.query(Law).count() > 0:
            print("Laws already seeded, skipping...")
            return
        
        laws_data = [
            {
                "code": "UNCLOS-121",
                "name_zh": "联合国海洋法公约第121条 - 岛屿制度",
                "name_en": "UNCLOS Article 121 - Regime of Islands",
                "category": "海洋法",
                "content": "1. 岛屿是四面环水并在高潮时高于水面的自然形成的陆地区域。2. 除第3款另有规定外，岛屿的领海、毗连区、专属经济区和大陆架应按照本公约适用于其他陆地领土的规定加以确定。3. 不能维持人类居住或其本身的经济生活的岩礁，不应有专属经济区或大陆架。",
                "summary": "定义岛屿并规定其海洋权利",
                "source": "联合国海洋法公约",
                "tags": ["岛屿", "专属经济区", "领海"]
            },
            {
                "code": "UNCLOS-74",
                "name_zh": "联合国海洋法公约第74条 - 相向或相邻国家间专属经济区界限的划定",
                "name_en": "UNCLOS Article 74 - Delimitation of EEZ",
                "category": "海洋法",
                "content": "1. 海岸相向或相邻国家间专属经济区的界限，应在国际法院规约第38条所指国际法的基础上以协议划定，以便得到公平解决。2. 如果在合理期间内未能达成协议，有关各国应诉诸第十五部分所规定的程序。",
                "summary": "规定专属经济区界限划定原则",
                "source": "联合国海洋法公约",
                "tags": ["专属经济区", "界限划定", "公平原则"]
            },
            {
                "code": "UNCLOS-76",
                "name_zh": "联合国海洋法公约第76条 - 大陆架的定义",
                "name_en": "UNCLOS Article 76 - Definition of Continental Shelf",
                "category": "海洋法",
                "content": "1. 沿海国的大陆架包括其领海以外依其陆地领土的全部自然延伸，扩展到大陆边外缘的海底区域的海床和底土，如果从测算领海宽度的基线量起到大陆边的外缘的距离不到200海里，则扩展到200海里的距离。",
                "summary": "定义大陆架范围",
                "source": "联合国海洋法公约",
                "tags": ["大陆架", "自然延伸", "200海里"]
            },
            {
                "code": "UNCLOS-56",
                "name_zh": "联合国海洋法公约第56条 - 沿海国在专属经济区内的权利、管辖权和义务",
                "name_en": "UNCLOS Article 56 - Rights in EEZ",
                "category": "海洋法",
                "content": "1. 沿海国在专属经济区内有：(a) 以勘探和开发、养护和管理海床上覆水域和海床及其底土的自然资源(不论为生物或非生物资源)为目的的主权权利，以及关于在该区内从事经济性开发和勘探，如利用海水、海流和风力生产能等其他活动的主权权利；",
                "summary": "规定沿海国在专属经济区的主权权利",
                "source": "联合国海洋法公约",
                "tags": ["专属经济区", "主权权利", "自然资源"]
            },
            {
                "code": "UNCLOS-73",
                "name_zh": "联合国海洋法公约第73条 - 沿海国法律和规章的执行",
                "name_en": "UNCLOS Article 73 - Enforcement",
                "category": "海洋法",
                "content": "1. 沿海国可以在专属经济区内，按照本公约行使主权权利，勘探、开发、养护和管理生物资源，并可采取为确保其按照本公约制定的法律和规章得到遵守所必要的措施，包括登临、检查、逮捕和进行司法程序。",
                "summary": "规定沿海国在专属经济区的执法权",
                "source": "联合国海洋法公约",
                "tags": ["执法", "专属经济区", "登临检查"]
            }
        ]
        
        for law_data in laws_data:
            law = Law(**law_data)
            db.add(law)
        
        db.commit()
        print(f"Successfully seeded {len(laws_data)} laws")
    except Exception as e:
        print(f"Error seeding laws: {e}")
        db.rollback()
    finally:
        db.close()


def seed_events():
    """Seed initial event data"""
    db = SessionLocal()
    try:
        # Check if events already exist
        if db.query(Event).count() > 0:
            print("Events already seeded, skipping...")
            return
        
        events_data = [
            {
                "id": str(uuid.uuid4()),
                "title": "南海岛礁主权争议",
                "type": "maritime",
                "description": "关于南海某岛礁的主权归属争议，涉及《联合国海洋法公约》等国际法律框架",
                "location": {"lat": 9.8, "lng": 114.3},
                "parties": ["中国", "某邻国"],
                "severity": 8,
                "status": "pending"
            },
            {
                "id": str(uuid.uuid4()),
                "title": "钓鱼岛海域争端",
                "type": "maritime",
                "description": "东海钓鱼岛及其附属岛屿主权争议，涉及领海基线划定和专属经济区重叠问题",
                "location": {"lat": 25.7, "lng": 123.5},
                "parties": ["中国", "日本"],
                "severity": 9,
                "status": "pending"
            },
            {
                "id": str(uuid.uuid4()),
                "title": "南海九段线法律地位争议",
                "type": "maritime",
                "description": "关于南海九段线在国际法下的法律地位和历史性权利主张",
                "location": {"lat": 12.0, "lng": 112.0},
                "parties": ["中国", "菲律宾"],
                "severity": 9,
                "status": "pending"
            },
            {
                "id": str(uuid.uuid4()),
                "title": "中印边境实际控制线争议",
                "type": "territory",
                "description": "藏南地区和阿克赛钦地区边界争议，涉及历史条约解释和实际控制",
                "location": {"lat": 29.0, "lng": 91.0},
                "parties": ["中国", "印度"],
                "severity": 8,
                "status": "pending"
            },
            {
                "id": str(uuid.uuid4()),
                "title": "边境领土划界纠纷",
                "type": "territory",
                "description": "边境地区领土划界存在争议，需要依据历史条约和国际法进行分析",
                "location": {"lat": 28.5, "lng": 92.1},
                "parties": ["中国", "邻国A"],
                "severity": 7,
                "status": "pending"
            },
            {
                "id": str(uuid.uuid4()),
                "title": "渔业资源管辖权争议",
                "type": "maritime",
                "description": "专属经济区内渔业资源开发和管辖权重叠问题",
                "location": {"lat": 35.0, "lng": 125.0},
                "parties": ["中国", "韩国"],
                "severity": 6,
                "status": "pending"
            },
            {
                "id": str(uuid.uuid4()),
                "title": "国际贸易争端仲裁",
                "type": "economic",
                "description": "关于反倾销措施和补贴政策的WTO争端解决机制案件",
                "location": {"lat": 31.2, "lng": 121.5},
                "parties": ["中国", "美国"],
                "severity": 6,
                "status": "pending"
            },
            {
                "id": str(uuid.uuid4()),
                "title": "驻外使馆安全事件",
                "type": "diplomatic",
                "description": "驻外使馆遭受攻击，涉及《维也纳外交关系公约》下的保护义务",
                "location": {"lat": 33.5, "lng": 36.3},
                "parties": ["中国", "驻在国"],
                "severity": 7,
                "status": "pending"
            },
            {
                "id": str(uuid.uuid4()),
                "title": "外交人员待遇争议",
                "type": "diplomatic",
                "description": "关于外交人员特权与豁免的争议事件",
                "location": {"lat": 39.9, "lng": 116.4},
                "parties": ["中国", "国家B"],
                "severity": 5,
                "status": "pending"
            },
            {
                "id": str(uuid.uuid4()),
                "title": "边境水资源利用纠纷",
                "type": "territory",
                "description": "跨境河流水资源利用分配争议，涉及国际水法和双边协定",
                "location": {"lat": 25.0, "lng": 98.0},
                "parties": ["中国", "缅甸"],
                "severity": 5,
                "status": "pending"
            }
        ]
        
        for event_data in events_data:
            event = Event(**event_data)
            db.add(event)
        
        db.commit()
        print(f"Successfully seeded {len(events_data)} events")
    except Exception as e:
        print(f"Error seeding events: {e}")
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    print("Initializing database...")
    init_db()
    
    print("\nSeeding laws...")
    seed_laws()
    
    print("\nSeeding events...")
    seed_events()
    
    print("\nDatabase initialization complete!")
