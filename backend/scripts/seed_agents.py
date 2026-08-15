"""
Seed agent data for the Legal Game Platform
"""
from app.database import SessionLocal
from app.models.database import Agent
import uuid

def seed_agents():
    """Seed initial agent data"""
    db = SessionLocal()
    try:
        # Check if agents already exist
        if db.query(Agent).count() > 0:
            print("Agents already seeded, skipping...")
            return
        
        agents_data = [
            {
                "id": str(uuid.uuid4()),
                "name": "国际法专家 - 张教授",
                "type": "法律专家",
                "model": "DeepSeek-Law",
                "avatar": "https://api.dicebear.com/7.x/avataaars/svg?seed=law1",
                "law_domains": ["国际法", "海洋法", "联合国海洋法公约"],
                "description": "资深国际法学者，专注于海洋法和国际争端解决，曾参与多起国际仲裁案件",
                "level": "高级",
                "config": {
                    "expertise": ["UNCLOS", "国际仲裁", "海洋划界"],
                    "language": ["中文", "英文"],
                    "experience_years": 20
                }
            },
            {
                "id": str(uuid.uuid4()),
                "name": "海洋权益顾问 - 李博士",
                "type": "专业顾问",
                "model": "DeepSeek-V3",
                "avatar": "https://api.dicebear.com/7.x/avataaars/svg?seed=ocean2",
                "law_domains": ["海洋权益", "专属经济区", "大陆架"],
                "description": "海洋法专家，擅长分析海洋权益争端和EEZ划界问题",
                "level": "高级",
                "config": {
                    "expertise": ["EEZ划界", "大陆架权利", "海洋资源"],
                    "language": ["中文", "英文"],
                    "experience_years": 15
                }
            },
            {
                "id": str(uuid.uuid4()),
                "name": "舆论策略师 - 王分析师",
                "type": "战略顾问",
                "model": "GPT-4o",
                "avatar": "https://api.dicebear.com/7.x/avataaars/svg?seed=media3",
                "law_domains": ["国际关系", "外交策略", "舆论分析"],
                "description": "国际关系专家，擅长外交策略和国际舆论分析",
                "level": "中级",
                "config": {
                    "expertise": ["外交策略", "舆论引导", "危机公关"],
                    "language": ["中文", "英文"],
                    "experience_years": 10
                }
            },
            {
                "id": str(uuid.uuid4()),
                "name": "领土法专家 - 陈律师",
                "type": "法律专家",
                "model": "DeepSeek-Law",
                "avatar": "https://api.dicebear.com/7.x/avataaars/svg?seed=territory4",
                "law_domains": ["领土法", "边界划定", "历史条约"],
                "description": "领土争端专家，精通边界划定和历史条约解释",
                "level": "高级",
                "config": {
                    "expertise": ["边界划定", "历史条约", "领土主权"],
                    "language": ["中文", "英文", "法文"],
                    "experience_years": 18
                }
            },
            {
                "id": str(uuid.uuid4()),
                "name": "国际贸易法专家 - 刘顾问",
                "type": "法律专家",
                "model": "Claude-3",
                "avatar": "https://api.dicebear.com/7.x/avataaars/svg?seed=trade5",
                "law_domains": ["国际贸易法", "WTO规则", "反倾销"],
                "description": "WTO专家，擅长国际贸易争端解决和反倾销案件",
                "level": "高级",
                "config": {
                    "expertise": ["WTO争端解决", "反倾销", "补贴与反补贴"],
                    "language": ["中文", "英文"],
                    "experience_years": 12
                }
            },
            {
                "id": str(uuid.uuid4()),
                "name": "外交法专家 - 赵大使",
                "type": "外交顾问",
                "model": "GPT-4o",
                "avatar": "https://api.dicebear.com/7.x/avataaars/svg?seed=diplomat6",
                "law_domains": ["外交法", "维也纳公约", "外交特权"],
                "description": "前外交官，精通外交法和国际礼仪，擅长外交谈判",
                "level": "资深",
                "config": {
                    "expertise": ["外交谈判", "维也纳公约", "外交特权与豁免"],
                    "language": ["中文", "英文", "法文"],
                    "experience_years": 25
                }
            },
            {
                "id": str(uuid.uuid4()),
                "name": "战术分析师 - 孙研究员",
                "type": "战略顾问",
                "model": "DeepSeek-V3",
                "avatar": "https://api.dicebear.com/7.x/avataaars/svg?seed=strategy7",
                "law_domains": ["战略分析", "博弈论", "风险评估"],
                "description": "战略分析专家，擅长博弈论和风险评估",
                "level": "中级",
                "config": {
                    "expertise": ["博弈论", "风险分析", "战略规划"],
                    "language": ["中文", "英文"],
                    "experience_years": 8
                }
            },
            {
                "id": str(uuid.uuid4()),
                "name": "危机公关顾问 - 周总监",
                "type": "公关顾问",
                "model": "GPT-4o",
                "avatar": "https://api.dicebear.com/7.x/avataaars/svg?seed=pr8",
                "law_domains": ["危机管理", "公共关系", "媒体沟通"],
                "description": "危机公关专家，擅长处理国际舆论和媒体关系",
                "level": "高级",
                "config": {
                    "expertise": ["危机管理", "媒体关系", "舆情监控"],
                    "language": ["中文", "英文"],
                    "experience_years": 14
                }
            }
        ]
        
        for agent_data in agents_data:
            agent = Agent(**agent_data)
            db.add(agent)
        
        db.commit()
        print(f"Successfully seeded {len(agents_data)} agents")
    except Exception as e:
        print(f"Error seeding agents: {e}")
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    print("Seeding agents...")
    seed_agents()
    print("Agent seeding complete!")
