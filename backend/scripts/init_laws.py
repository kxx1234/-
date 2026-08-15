"""Initialize law database with initial data"""
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.database import SessionLocal, init_db
from app.models.database import Law

def seed_laws():
    """Seed initial law data"""
    db = SessionLocal()
    
    # Check if laws already exist
    existing_count = db.query(Law).count()
    if existing_count > 0:
        print(f"Database already has {existing_count} laws. Skipping seed.")
        db.close()
        return
    
    initial_laws = [
        {
            "code": "UNCLOS-121",
            "name_zh": "联合国海洋法公约第121条 - 岛屿制度",
            "name_en": "UNCLOS Article 121 - Regime of Islands",
            "category": "海洋法",
            "content": "1. 岛屿是四面环水并在高潮时高于水面的自然形成的陆地区域。\n2. 除第3款另有规定外，岛屿的领海、毗连区、专属经济区和大陆架应按照本公约适用于其他陆地领土的规定加以确定。\n3. 不能维持人类居住或其本身的经济生活的岩礁，不应有专属经济区或大陆架。",
            "summary": "定义岛屿及其海洋权利，区分岛屿和岩礁",
            "source": "联合国海洋法公约",
            "tags": ["岛屿", "专属经济区", "大陆架", "岩礁"]
        },
        {
            "code": "UNCLOS-74",
            "name_zh": "联合国海洋法公约第74条 - 相向或相邻国家间专属经济区界限的划定",
            "name_en": "UNCLOS Article 74 - Delimitation of EEZ",
            "category": "海洋法",
            "content": "1. 海岸相向或相邻国家间专属经济区的界限，应在国际法院规约第38条所指国际法的基础上以协议划定，以便得到公平解决。\n2. 如果在合理期间内未能达成协议，有关各国应诉诸第十五部分所规定的程序。\n3. 在达成第1款规定的协议以前，有关各国应基于谅解和合作的精神，尽一切努力作出实际性的临时安排。",
            "summary": "专属经济区划界应通过协议以达成公平解决",
            "source": "联合国海洋法公约",
            "tags": ["专属经济区", "划界", "协议", "公平原则"]
        },
        {
            "code": "UNCLOS-76",
            "name_zh": "联合国海洋法公约第76条 - 大陆架的定义",
            "name_en": "UNCLOS Article 76 - Definition of Continental Shelf",
            "category": "海洋法",
            "content": "1. 沿海国的大陆架包括其领海以外依其陆地领土的全部自然延伸，扩展到大陆边外缘的海底区域的海床和底土。\n2. 沿海国的大陆架从测算领海宽度的基线量起延伸到200海里。",
            "summary": "定义大陆架的范围和界限",
            "source": "联合国海洋法公约",
            "tags": ["大陆架", "自然延伸", "200海里"]
        },
        {
            "code": "UNCLOS-279",
            "name_zh": "联合国海洋法公约第279条 - 和平解决争端的义务",
            "name_en": "UNCLOS Article 279 - Obligation to Settle Disputes by Peaceful Means",
            "category": "海洋法",
            "content": "缔约各国应按照《联合国宪章》第二条第三项以和平方法解决它们之间有关本公约的解释或适用的任何争端，并为此目的以《宪章》第三十三条第一项所指的方法谋求解决。",
            "summary": "要求各国以和平方式解决海洋争端",
            "source": "联合国海洋法公约",
            "tags": ["争端解决", "和平方法", "联合国宪章"]
        },
        {
            "code": "UN-CHARTER-2-3",
            "name_zh": "联合国宪章第2条第3款 - 和平解决争端",
            "name_en": "UN Charter Article 2(3) - Peaceful Settlement",
            "category": "国际公法",
            "content": "各会员国应以和平方法解决其国际争端，俾免危及国际和平、安全及正义。",
            "summary": "联合国会员国必须以和平方式解决国际争端",
            "source": "联合国宪章",
            "tags": ["和平解决", "国际争端", "联合国"]
        },
        {
            "code": "UN-CHARTER-2-4",
            "name_zh": "联合国宪章第2条第4款 - 禁止使用武力",
            "name_en": "UN Charter Article 2(4) - Prohibition of Use of Force",
            "category": "国际公法",
            "content": "各会员国在其国际关系上不得使用威胁或武力，或以与联合国宗旨不符之任何其他方法，侵害任何会员国或国家之领土完整或政治独立。",
            "summary": "禁止在国际关系中使用武力或武力威胁",
            "source": "联合国宪章",
            "tags": ["禁止武力", "领土完整", "政治独立"]
        },
        {
            "code": "ICJ-STATUTE-38",
            "name_zh": "国际法院规约第38条 - 适用的法律",
            "name_en": "ICJ Statute Article 38 - Applicable Law",
            "category": "国际公法",
            "content": "1. 法院对于陈诉各项争端，应依国际法裁判之，裁判时应适用：\na. 不论普通或特别国际协约，确立诉讼当事国明白承认之规条者；\nb. 国际习惯，作为通例之证明而经接受为法律者；\nc. 一般法律原则为文明各国所承认者；\nd. 司法判例及各国权威最高之公法学家学说，作为确定法律原则之补助资料者。",
            "summary": "国际法院适用的法律来源",
            "source": "国际法院规约",
            "tags": ["国际法来源", "条约", "习惯法", "一般法律原则"]
        },
        {
            "code": "HISTORIC-RIGHTS",
            "name_zh": "历史性权利原则",
            "name_en": "Principle of Historic Rights",
            "category": "国际惯例",
            "content": "历史性权利是指一国基于长期的、持续的、和平的占有和行使主权而获得的权利。这种权利需要满足以下条件：\n1. 长期性：对相关区域的占有和使用具有相当长的历史；\n2. 持续性：占有和使用是连续不断的；\n3. 和平性：未受到其他国家的有效反对；\n4. 有效性：实际行使主权行为。",
            "summary": "基于历史占有和使用而产生的国际法权利",
            "source": "国际法惯例",
            "tags": ["历史性权利", "主权", "长期占有"]
        },
        {
            "code": "BILATERAL-TREATY-PRINCIPLE",
            "name_zh": "双边条约原则",
            "name_en": "Principle of Bilateral Treaties",
            "category": "条约法",
            "content": "双边条约是两个国家之间订立的国际协议。根据《维也纳条约法公约》，双边条约应遵循以下原则：\n1. 条约必须遵守（pacta sunt servanda）；\n2. 善意履行原则；\n3. 条约对第三国无效原则；\n4. 条约解释应依其用语按其上下文并参照条约之目的及宗旨所具有之通常意义。",
            "summary": "双边条约的基本法律原则",
            "source": "维也纳条约法公约",
            "tags": ["双边条约", "条约必须遵守", "善意履行"]
        },
        {
            "code": "EFFECTIVE-OCCUPATION",
            "name_zh": "有效占领原则",
            "name_en": "Principle of Effective Occupation",
            "category": "领土法",
            "content": "有效占领是获得领土主权的传统方式之一。要构成有效占领，需要满足：\n1. 实际占有（corpus）：对领土的实际控制；\n2. 占有意图（animus）：以主权者身份占有的意图；\n3. 持续性：占有必须是持续的；\n4. 和平性：未受到其他国家的有效抗议。",
            "summary": "通过实际占有获得领土主权的法律原则",
            "source": "国际法惯例",
            "tags": ["有效占领", "领土主权", "实际控制"]
        }
    ]
    
    try:
        for law_data in initial_laws:
            law = Law(**law_data)
            db.add(law)
        
        db.commit()
        print(f"Successfully seeded {len(initial_laws)} laws into the database!")
    except Exception as e:
        db.rollback()
        print(f"Error seeding laws: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    print("Initializing database...")
    init_db()
    print("Seeding initial law data...")
    seed_laws()
    print("Done!")
