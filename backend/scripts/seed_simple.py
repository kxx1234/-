"""简化的seeder - 仅创建必要数据"""
from app.database import SessionLocal, engine
from app.models.database import Base, Event, Agent, AgentType

# 重建表
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)
print("✓ Tables recreated")

db = SessionLocal()

try:
    # Event 1
    event1 = Event(
        event_id="Event-ECS",
        name="东海争议",
        description="执法行为争议",
        dispute_type="海洋权益",
        our_side=["中国"],
        opponent_side=["日本"],
        legal_systems=["UNCLOS"],
        fact_summary="执法对峙"
    )
    db.add(event1)
    db.flush()
    
    # Agent 1: Blue
    agent1 = Agent(
        agent_id="AGENT-BLUE-001",
        name="海洋法专家-张律师",
        agent_type=AgentType.BLUE,
        event_id=event1.id,
        system_prompt="你是海洋法专家",
        stance="维护权益",
        goals=["maintain_rights"],
        llm_config={"temperature": 0.3}
    )
    db.add(agent1)
    
    # Agent 2: Red
    agent2 = Agent(
        agent_id="AGENT-RED-001",
        name="对手代理",
        agent_type=AgentType.RED,
        event_id=event1.id,
        system_prompt="你代表对方",
        stance="航行自由",
        goals=["freedom"],
        llm_config={"temperature": 0.6}
    )
    db.add(agent2)
    
    # Agent 3: Judge
    agent3 = Agent(
        agent_id="AGENT-JUDGE-001",
        name="法官",
        agent_type=AgentType.JUDGE,
        event_id=event1.id,
        system_prompt="你是法官",
        stance="中立",
        llm_config={"temperature": 0.2}
    )
    db.add(agent3)
    
    db.commit()
    print("✓ Created 1 Event and 3 Agents")
    print(f"Event: {event1.name}")
    print("Agents: Blue, Red, Judge")
    
except Exception as e:
    print(f"✗ Error: {e}")
    db.rollback()
    raise
finally:
    db.close()
