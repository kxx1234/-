"""Add more laws to the database"""
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.database import SessionLocal
from app.models.database import Law

def add_more_laws():
    """Add additional law data"""
    db = SessionLocal()
    
    additional_laws = [
        # 更多UNCLOS条款
        {
            "code": "UNCLOS-03",
            "name_zh": "联合国海洋法公约第3条 - 领海的宽度",
            "name_en": "UNCLOS Article 3 - Breadth of Territorial Sea",
            "category": "海洋法",
            "content": "每一国家有权确定其领海的宽度，直至从按照本公约确定的基线量起不超过12海里的界限为止。",
            "summary": "领海宽度不得超过12海里",
            "source": "联合国海洋法公约",
            "tags": ["领海", "12海里", "基线"]
        },
        {
            "code": "UNCLOS-56",
            "name_zh": "联合国海洋法公约第56条 - 沿海国在专属经济区内的权利",
            "name_en": "UNCLOS Article 56 - Rights in EEZ",
            "category": "海洋法",
            "content": "1. 沿海国在专属经济区内有：\n(a) 以勘探和开发、养护和管理海床上覆水域和海床及其底土的自然资源为目的的主权权利；\n(b) 对于在该区内从事经济性开发和勘探的其他活动的主权权利；\n(c) 对下列事项的管辖权：\n(i) 人工岛屿、设施和结构的建造和使用；\n(ii) 海洋科学研究；\n(iii) 海洋环境的保护和保全。",
            "summary": "规定沿海国在专属经济区内的主权权利和管辖权",
            "source": "联合国海洋法公约",
            "tags": ["专属经济区", "主权权利", "管辖权", "自然资源"]
        },
        {
            "code": "UNCLOS-57",
            "name_zh": "联合国海洋法公约第57条 - 专属经济区的宽度",
            "name_en": "UNCLOS Article 57 - Breadth of EEZ",
            "category": "海洋法",
            "content": "专属经济区从测算领海宽度的基线量起，不应超过200海里。",
            "summary": "专属经济区宽度不超过200海里",
            "source": "联合国海洋法公约",
            "tags": ["专属经济区", "200海里", "基线"]
        },
        {
            "code": "UNCLOS-83",
            "name_zh": "联合国海洋法公约第83条 - 相向或相邻国家间大陆架界限的划定",
            "name_en": "UNCLOS Article 83 - Delimitation of Continental Shelf",
            "category": "海洋法",
            "content": "1. 海岸相向或相邻国家间大陆架的界限，应在国际法院规约第38条所指国际法的基础上以协议划定，以便得到公平解决。\n2. 如果在合理期间内未能达成协议，有关各国应诉诸第十五部分所规定的程序。",
            "summary": "大陆架划界应通过协议以达成公平解决",
            "source": "联合国海洋法公约",
            "tags": ["大陆架", "划界", "公平原则", "协议"]
        },
        {
            "code": "UNCLOS-298",
            "name_zh": "联合国海洋法公约第298条 - 适用第2节的限制性和任意性例外",
            "name_en": "UNCLOS Article 298 - Optional Exceptions",
            "category": "海洋法",
            "content": "1. 一国在签署、批准或加入本公约时，或在其后任何时间，在不妨害根据第1节所产生的义务的情形下，可以书面声明对于第2节规定的程序，不接受其中一类或多类的任何一种或多种程序。",
            "summary": "允许国家对某些争端解决程序作出保留",
            "source": "联合国海洋法公约",
            "tags": ["争端解决", "保留", "任意性例外"]
        },
        
        # 国际法院判例
        {
            "code": "ICJ-NICARAGUA-1986",
            "name_zh": "尼加拉瓜诉美国案（1986）",
            "name_en": "Nicaragua v. United States (1986)",
            "category": "国际公法",
            "content": "国际法院在本案中确认：\n1. 禁止使用武力原则是习惯国际法的一部分；\n2. 不干涉原则是国际法的基本原则；\n3. 自卫权的行使必须符合必要性和相称性原则；\n4. 集体自卫权的行使需要受攻击国的请求。",
            "summary": "确立了使用武力、不干涉和自卫权的重要法律原则",
            "source": "国际法院判例",
            "tags": ["使用武力", "不干涉", "自卫权", "习惯国际法"]
        },
        {
            "code": "ICJ-TEMPLE-1962",
            "name_zh": "柏威夏寺案（1962）",
            "name_en": "Temple of Preah Vihear (1962)",
            "category": "领土法",
            "content": "国际法院判决：\n1. 地图可以作为确定边界的证据；\n2. 默认（acquiescence）可以产生法律效力；\n3. 长期未提出异议可视为接受既定事实；\n4. 有效占领和行使主权的证据对领土争端至关重要。",
            "summary": "确立了领土争端中地图证据和默认原则的重要性",
            "source": "国际法院判例",
            "tags": ["领土争端", "地图证据", "默认", "有效占领"]
        },
        
        # 维也纳条约法公约
        {
            "code": "VCLT-26",
            "name_zh": "维也纳条约法公约第26条 - 条约必须遵守",
            "name_en": "VCLT Article 26 - Pacta Sunt Servanda",
            "category": "条约法",
            "content": "凡有效之条约对其各当事国有拘束力，必须由各该国善意履行。",
            "summary": "条约必须遵守原则（pacta sunt servanda）",
            "source": "维也纳条约法公约",
            "tags": ["条约必须遵守", "善意履行", "条约法"]
        },
        {
            "code": "VCLT-31",
            "name_zh": "维也纳条约法公约第31条 - 解释之通则",
            "name_en": "VCLT Article 31 - General Rule of Interpretation",
            "category": "条约法",
            "content": "1. 条约应依其用语按其上下文并参照条约之目的及宗旨所具有之通常意义，善意解释之。\n2. 就解释条约而言，上下文除指连同弁言及附件在内之约文外，并应包括：\n(a) 全体当事国因缔结条约所订与条约有关之任何协定；\n(b) 一个以上当事国因缔结条约所订并经其他当事国接受为条约有关文书之任何文书。",
            "summary": "条约解释的基本规则",
            "source": "维也纳条约法公约",
            "tags": ["条约解释", "善意", "目的解释"]
        },
        {
            "code": "VCLT-53",
            "name_zh": "维也纳条约法公约第53条 - 与一般国际法强制规律抵触之条约",
            "name_en": "VCLT Article 53 - Jus Cogens",
            "category": "条约法",
            "content": "条约在缔结时与一般国际法强制规律抵触者无效。就适用本公约而言，一般国际法强制规律指国家之国际社会全体接受并公认为不许损抑且仅有以后具有同等性质之一般国际法规律始得更改之规律。",
            "summary": "强制法（jus cogens）的定义和效力",
            "source": "维也纳条约法公约",
            "tags": ["强制法", "jus cogens", "条约无效"]
        },
        
        # 国际惯例
        {
            "code": "ESTOPPEL-PRINCIPLE",
            "name_zh": "禁反言原则",
            "name_en": "Principle of Estoppel",
            "category": "国际惯例",
            "content": "禁反言原则是指一国不得否认其先前的声明或行为，如果另一国基于对该声明或行为的信赖而采取了行动。该原则要求：\n1. 存在明确的声明或行为；\n2. 另一国基于该声明或行为产生了信赖；\n3. 该信赖是合理的；\n4. 另一国因信赖而改变了立场或遭受损失。",
            "summary": "国家不得否认其先前声明或行为的原则",
            "source": "国际法惯例",
            "tags": ["禁反言", "信赖", "善意"]
        },
        {
            "code": "GOOD-FAITH-PRINCIPLE",
            "name_zh": "善意原则",
            "name_en": "Principle of Good Faith",
            "category": "国际惯例",
            "content": "善意原则是国际法的基本原则，要求国家在履行国际义务和行使国际权利时应：\n1. 诚实、公正地行事；\n2. 不滥用权利；\n3. 考虑其他国家的合法利益；\n4. 避免采取可能损害条约目的和宗旨的行为。",
            "summary": "要求国家诚实公正地履行国际义务",
            "source": "国际法惯例",
            "tags": ["善意", "诚实", "不滥用权利"]
        },
        
        # 领土法
        {
            "code": "UTI-POSSIDETIS",
            "name_zh": "保持占有原则",
            "name_en": "Uti Possidetis Principle",
            "category": "领土法",
            "content": "保持占有原则（Uti Possidetis）主要适用于殖民地独立时的边界确定，其核心内容是：\n1. 新独立国家应继承殖民时期的行政边界；\n2. 边界的稳定性优先于其他考虑；\n3. 防止因边界争议而引发冲突；\n4. 该原则已被国际法院多次确认为习惯国际法。",
            "summary": "新独立国家继承殖民时期行政边界的原则",
            "source": "国际法惯例",
            "tags": ["边界", "独立", "殖民地", "习惯法"]
        },
        {
            "code": "TERRITORIAL-INTEGRITY",
            "name_zh": "领土完整原则",
            "name_en": "Principle of Territorial Integrity",
            "category": "领土法",
            "content": "领土完整原则是国际法的基本原则之一，规定：\n1. 国家的领土不可侵犯；\n2. 禁止以武力侵占他国领土；\n3. 不承认通过武力获得的领土；\n4. 该原则载于《联合国宪章》第2条第4款。",
            "summary": "保护国家领土不受侵犯的基本原则",
            "source": "联合国宪章",
            "tags": ["领土完整", "不可侵犯", "禁止武力"]
        },
        
        # 南海仲裁案相关
        {
            "code": "PCA-2016-AWARD",
            "name_zh": "南海仲裁案裁决（2016）",
            "name_en": "South China Sea Arbitration Award (2016)",
            "category": "国际公法",
            "content": "常设仲裁法院在菲律宾诉中国案中的主要裁决：\n1. 九段线内的历史性权利主张没有法律依据；\n2. 某些南海岛礁不符合UNCLOS第121条关于岛屿的定义；\n3. 中国在某些区域的活动违反了UNCLOS规定的义务。\n注：中国不接受、不参与该仲裁，认为仲裁庭没有管辖权。",
            "summary": "2016年南海仲裁案的主要裁决内容",
            "source": "常设仲裁法院",
            "tags": ["南海", "仲裁", "九段线", "岛屿定义"]
        }
    ]
    
    try:
        added_count = 0
        skipped_count = 0
        
        for law_data in additional_laws:
            # Check if law already exists
            existing = db.query(Law).filter(Law.code == law_data["code"]).first()
            if existing:
                print(f"Law {law_data['code']} already exists, skipping...")
                skipped_count += 1
                continue
            
            law = Law(**law_data)
            db.add(law)
            added_count += 1
        
        db.commit()
        print(f"\n✅ Successfully added {added_count} new laws!")
        print(f"⏭️  Skipped {skipped_count} existing laws")
        print(f"📊 Total laws in database: {db.query(Law).count()}")
        
    except Exception as e:
        db.rollback()
        print(f"❌ Error adding laws: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    print("Adding more laws to the database...\n")
    add_more_laws()
    print("\nDone!")
