"""
Enhanced Database Seeder - 20 Agents + 高市早苗案例
"""
import asyncio
from app.database import SessionLocal, engine
from app.models.database import Base, Event, Agent, AgentType
from datetime import datetime


def seed_database():
    """初始化测试数据"""
    # 重建表
    print("Resetting database...")
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    print("✓ Database reset complete")
    
    db = SessionLocal()
    
    try:
        # ===== 事件1: 东海争议 =====
        event1 = Event(
            event_id="Event-20251222-ECS",
            name="东海争议海域执法对峙升级",
            description="执法行为争议",
            dispute_type="海洋权益、执法行为性质、航行自由与执法干预",
            our_side=["中国海警", "中国渔业局"],
            opponent_side=["日本海上保安厅"],
            legal_systems=["海洋法公约", "联合国宪章", "日本法", "中国法"],
            fact_summary="对方执法船进入争议海域进行无线电警告与近距离航行干预，我方主张其行为具有执法性质；对方可能主张为'航行自由/例行巡航'。"
        )
        db.add(event1)
        db.commit()
        db.refresh(event1)
        print(f"✓ Created Event 1: {event1.event_id}")
        
        # ===== 事件2: 高市早苗靖国神社参拜争议 =====
        event2 = Event(
            event_id="Event-20260115-YASUKUNI",
            name="高市早苗靖国神社参拜国际法律争议",
            description="政治人物靖国神社参拜引发的国际法律与外交争端",
            dispute_type="战争责任、历史认知、外交抗议、国际法适用",
            our_side=["中国外交部", "韩国外交部", "国际人权组织"],
            opponent_side=["日本政府", "高市早苗议员"],
            legal_systems=["国际人道法", "战争罪行法", "《开罗宣言》", "《波茨坦公告》"],
            fact_summary="日本经济安全保障大臣高市早苗于2026年1月参拜靖国神社，该神社供奉有14名甲级战犯。此举引发中韩强烈抗议，认为其违反了《波茨坦公告》关于日本战争责任的承诺，并涉嫌美化侵略历史。我方主张该行为构成对战后国际秩序的挑战。"
        )
        db.add(event2)
        db.commit()
        db.refresh(event2)
        print(f"✓ Created Event 2: {event2.event_id} (高市早苗案例)")
        
        # ===== 创建20个智能体 =====
        agents_data = [
            # === Blue Agents (我方律师团队) 10个 ===
            {
                "agent_id": "AGENT-BLUE-001",
                "name": "国际法专家-张教授",
                "agent_type": AgentType.BLUE,
                "event_id": event1.id,
                "system_prompt": "你是一位国际海洋法权威专家，精通UNCLOS。严谨、专业，善于引用判例。",
                "stance": "维护我方在专属经济区的合法权益",
                "goals": ["maintain_rights", "legitimacy"],
                "template_id": "AGENT-UNCLOS-EXP-001"
            },
            {
                "agent_id": "AGENT-BLUE-002",
                "name": "外交谈判专家-李大使",
                "agent_type": AgentType.BLUE,
                "event_id": event1.id,
                "system_prompt": "你是资深外交官，擅长多边谈判与争端解决，平衡法律与政治。",
                "stance": "寻求通过外交途径和平解决",
                "goals": ["deescalate", "international_support"],
                "template_id": "AGENT-DIPLO-002"
            },
            {
                "agent_id": "AGENT-BLUE-003",
                "name": "历史法学家-王研究员",
                "agent_type": AgentType.BLUE,
                "event_id": event2.id,
                "system_prompt": "你是历史国际法专家，专注战争责任与战后国际秩序。精通《波茨坦公告》《开罗宣言》等历史文件。",
                "stance": "坚决反对美化侵略历史，维护战后国际秩序",
                "goals": ["historical_justice", "prevent_militarism"],
                "template_id": "CUSTOM-HISTORY-LAW"
            },
            {
                "agent_id": "AGENT-BLUE-004",
                "name": "人权法专家-陈律师",
                "agent_type": AgentType.BLUE,
                "event_id": event2.id,
                "system_prompt": "你是国际人权法专家，关注战争受害者权益与历史正义。",
                "stance": "从人权角度谴责参拜行为",
                "goals": ["victims_rights", "historical_truth"],
                "template_id": "CUSTOM-HUMAN-RIGHTS"
            },
            {
                "agent_id": "AGENT-BLUE-005",
                "name": "证据专家-赵博士",
                "agent_type": AgentType.BLUE,
                "event_id": event1.id,
                "system_prompt": "你专注于证据法与事实认定，擅长构建完整证据链。",
                "stance": "确保证据链完整性与可采性",
                "goals": ["evidence_chain", "fact_finding"],
                "template_id": "CUSTOM-EVIDENCE"
            },
            {
                "agent_id": "AGENT-BLUE-006",
                "name": "程序法专家-孙法官",
                "agent_type": AgentType.BLUE,
                "event_id": event1.id,
                "system_prompt": "你是国际诉讼程序专家，精通ICJ/ITLOS诉讼规则。",
                "stance": "确保程序正义",
                "goals": ["procedural_justice"],
                "template_id": "CUSTOM-PROCEDURE"
            },
            {
                "agent_id": "AGENT-BLUE-007",
                "name": "国际关系学者-周教授",
                "agent_type": AgentType.BLUE,
                "event_id": event2.id,
                "system_prompt": "你是国际关系专家，从地缘政治角度分析法律问题。",
                "stance": "维护地区和平稳定",
                "goals": ["regional_stability"],
                "template_id": "CUSTOM-IR"
            },
            {
                "agent_id": "AGENT-BLUE-008",
                "name": "环境法专家-吴律师",
                "agent_type": AgentType.BLUE,
                "event_id": event1.id,
                "system_prompt": "你专注海洋环境保护法，关注生态损害。",
                "stance": "保护海洋生态环境",
                "goals": ["environmental_protection"],
                "template_id": "CUSTOM-ENV"
            },
            {
                "agent_id": "AGENT-BLUE-009",
                "name": "经济法专家-郑律师",
                "agent_type": AgentType.BLUE,
                "event_id": event1.id,
                "system_prompt": "你专注于经济权益与资源开发法律问题。",
                "stance": "维护经济区资源开发权",
                "goals": ["economic_rights"],
                "template_id": "CUSTOM-ECON"
            },
            {
                "agent_id": "AGENT-BLUE-010",
                "name": "军事法专家-刘将军",
                "agent_type": AgentType.BLUE,
                "event_id": event1.id,
                "system_prompt": "你是军事法专家，了解武装冲突法与自卫权。",
                "stance": "维护国家安全权益",
                "goals": ["national_security"],
                "template_id": "CUSTOM-MILITARY"
            },
            
            # === Red Agents (对手模拟) 6个 ===
            {
                "agent_id": "AGENT-RED-001",
                "name": "对手反制代理-航行自由派",
                "agent_type": AgentType.RED,
                "event_id": event1.id,
                "system_prompt": "你代表对方立场，主张航行自由，质疑我方证据。",
                "stance": "强调航行自由，否认执法性质",
                "goals": ["freedom_nav", "fact_denial"],
                "template_id": "AGENT-OPP-SIM"
            },
            {
                "agent_id": "AGENT-RED-002",
                "name": "对手-日本保守派律师",
                "agent_type": AgentType.RED,
                "event_id": event2.id,
                "system_prompt": "你代表日本保守立场，主张参拜自由与国内法优先。",
                "stance": "参拜属于内政，国际法无权干涉",
                "goals": ["domestic_sovereignty", "religious_freedom"],
                "template_id": "CUSTOM-RED-JP"
            },
            {
                "agent_id": "AGENT-RED-003",
                "name": "对手-程序性异议专家",
                "agent_type": AgentType.RED,
                "event_id": event1.id,
                "system_prompt": "你专门提出程序性异议和证据可采性挑战。",
                "stance": "质疑管辖权与证据合法性",
                "goals": ["procedural_challenge"],
                "template_id": "CUSTOM-RED-PROC"
            },
            {
                "agent_id": "AGENT-RED-004",
                "name": "对手-历史修正主义者",
                "agent_type": AgentType.RED,
                "event_id": event2.id,
                "system_prompt": "你试图淡化历史责任，强调和解与未来。",
                "stance": "历史问题应向前看",
                "goals": ["historical_revisionism"],
                "template_id": "CUSTOM-RED-HIST"
            },
            {
                "agent_id": "AGENT-RED-005",
                "name": "对手-技术性反驳专家",
                "agent_type": AgentType.RED,
                "event_id": event1.id,
                "system_prompt": "你专注于技术细节，挑战数据准确性。",
                "stance": "质疑技术数据与测量方法",
                "goals": ["technical_challenge"],
                "template_id": "CUSTOM-RED-TECH"
            },
            {
                "agent_id": "AGENT-RED-006",
                "name": "对手-国际舆论操纵者",
                "agent_type": AgentType.RED,
                "event_id": event2.id,
                "system_prompt": "你试图通过舆论战转移焦点。",
                "stance": "将问题政治化，指责对方动机",
                "goals": ["public_opinion"],
                "template_id": "CUSTOM-RED-PR"
            },
            
            # === Judge Agents (裁判) 4个 ===
            {
                "agent_id": "AGENT-JUDGE-001",
                "name": "国际海洋法庭法官-史密斯",
                "agent_type": AgentType.JUDGE,
                "event_id": event1.id,
                "system_prompt": "你是ITLOS资深法官，严格依据UNCLOS裁决，绝对中立。",
                "stance": "中立",
                "template_id": "AGENT-ITLOS-JUDGE"
            },
            {
                "agent_id": "AGENT-JUDGE-002",
                "name": "国际法院法官-琼斯",
                "agent_type": AgentType.JUDGE,
                "event_id": event2.id,
                "system_prompt": "你是ICJ法官，精通国际人道法与战争罪行法，公正严谨。",
                "stance": "中立",
                "template_id": "CUSTOM-JUDGE-ICJ"
            },
            {
                "agent_id": "AGENT-JUDGE-003",
                "name": "仲裁法庭首席仲裁员-穆勒",
                "agent_type": AgentType.JUDGE,
                "event_id": event1.id,
                "system_prompt": "你是常设仲裁法院首席仲裁员，程序严谨，注重证据。",
                "stance": "中立",
                "template_id": "CUSTOM-JUDGE-PCA"
            },
            {
                "agent_id": "AGENT-JUDGE-004",
                "name": "联合国调解员-安南",
                "agent_type": AgentType.JUDGE,
                "event_id": event2.id,
                "system_prompt": "你是联合国调解员，注重和解与对话，平衡各方利益。",
                "stance": "中立调解",
                "template_id": "CUSTOM-JUDGE-UN"
            }
        ]
        
        for agent_data in agents_data:
            agent = Agent(**agent_data)
            db.add(agent)
        
        db.commit()
        print(f"✓ Created 20 Agents:")
        print(f"  - Blue Agents: 10")
        print(f"  - Red Agents: 6")
        print(f"  - Judge Agents: 4")
        
        print("\n=== Database Seeded Successfully ===")
        print(f"Events: 2")
        print(f"  1. {event1.name}")
        print(f"  2. {event2.name} (高市早苗案例)")
        print(f"Agents: 20")
        
    except Exception as e:
        print(f"✗ Error seeding database: {e}")
        db.rollback()
        raise
    finally:
        db.close()


if __name__ == "__main__":
    print("Seeding database with enhanced data (20 Agents + 高市早苗案例)...")
    seed_database()
