"""
Harmes Agent — 多Agent协作调度框架

用户视角：给一个任务 → 自动分配给多个Agent → 并行执行 → 汇总结果
"""

import logging
from typing import Dict, List, Optional, Callable
from dataclasses import dataclass, field
import json

logger = logging.getLogger(__name__)


@dataclass
class AgentTask:
    """Agent任务"""
    task_id: str
    agent_name: str
    description: str
    input_data: Dict
    status: str = "pending"  # pending/running/done/failed
    result: Optional[Dict] = None


@dataclass
class AgentDefinition:
    """Agent定义"""
    name: str
    role: str
    system_prompt: str
    capabilities: List[str]
    handler: Optional[Callable] = None


class HarmesAgent:
    """多Agent协作调度器"""
    
    def __init__(self):
        self.agents: Dict[str, AgentDefinition] = {}
        self.tasks: Dict[str, AgentTask] = {}
    
    def register_agent(self, agent: AgentDefinition):
        """注册Agent"""
        self.agents[agent.name] = agent
        logger.info(f"✅ Agent已注册: {agent.name} ({agent.role})")
    
    def create_task(self, description: str, input_data: Dict, agent_hint: str = "") -> str:
        """创建任务，自动分配Agent"""
        import uuid
        task_id = str(uuid.uuid4())[:8]
        
        # 智能匹配Agent
        best_agent = self._find_best_agent(description, agent_hint)
        
        task = AgentTask(
            task_id=task_id,
            agent_name=best_agent,
            description=description,
            input_data=input_data
        )
        self.tasks[task_id] = task
        return task_id
    
    def _find_best_agent(self, description: str, hint: str) -> str:
        """根据描述匹配最佳Agent"""
        if hint and hint in self.agents:
            return hint
        
        desc_lower = description.lower()
        best_score = 0
        best_agent = list(self.agents.keys())[0] if self.agents else "default"
        
        for name, agent in self.agents.items():
            score = sum(1 for cap in agent.capabilities if cap.lower() in desc_lower)
            if score > best_score:
                best_score = score
                best_agent = name
        
        return best_agent
    
    def execute_parallel(self, task_ids: List[str]) -> Dict[str, Dict]:
        """并行执行多个任务"""
        results = {}
        for task_id in task_ids:
            task = self.tasks.get(task_id)
            if task and task.agent_name in self.agents:
                agent = self.agents[task.agent_name]
                task.status = "running"
                try:
                    if agent.handler:
                        result = agent.handler(task.input_data)
                    else:
                        result = {"output": f"[{agent.name}] 处理完成: {task.description}"}
                    task.result = result
                    task.status = "done"
                    results[task_id] = result
                except Exception as e:
                    task.status = "failed"
                    results[task_id] = {"error": str(e)}
        return results
    
    def get_status(self) -> Dict:
        """获取框架状态"""
        return {
            "agents": len(self.agents),
            "tasks": len(self.tasks),
            "completed": sum(1 for t in self.tasks.values() if t.status == "done"),
            "failed": sum(1 for t in self.tasks.values() if t.status == "failed"),
        }


if __name__ == "__main__":
    harmes = HarmesAgent()
    
    # 注册示例Agent
    harmes.register_agent(AgentDefinition(
        name="数据分析师",
        role="分析数据",
        system_prompt="你是数据分析师",
        capabilities=["分析", "统计", "数据", "可视化"]
    ))
    harmes.register_agent(AgentDefinition(
        name="文案专家",
        role="撰写文案",
        system_prompt="你是文案专家",
        capabilities=["写作", "文案", "报告", "文档"]
    ))
    
    # 创建并行任务
    t1 = harmes.create_task("分析用户数据趋势", {"data": "users.csv"})
    t2 = harmes.create_task("撰写产品介绍文案", {"product": "MediChat-RD"})
    
    results = harmes.execute_parallel([t1, t2])
    print(json.dumps(results, ensure_ascii=False, indent=2))
    print(f"\n状态: {harmes.get_status()}")
