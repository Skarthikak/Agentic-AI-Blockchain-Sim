from abc import ABC, abstractmethod
from typing import Dict, Any, List
import json

class BaseAgent(ABC):
    """Base class for all AI agents in the system"""
    
    def __init__(self, name: str, capabilities: List[str]):
        self.name = name
        self.capabilities = capabilities
        self.performance_metrics = {}
        self.interaction_history = []
    
    @abstractmethod
    async def process_task(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """Process a task and return results"""
        pass
    
    def record_interaction(self, task: Dict, result: Dict):
        """Record agent interactions for learning and analysis"""
        self.interaction_history.append({
            'task': task,
            'result': result,
            'timestamp': self._get_timestamp()
        })
    
    def update_performance(self, metric: str, value: float):
        """Update agent performance metrics"""
        self.performance_metrics[metric] = value
    
    def _get_timestamp(self) -> str:
        from datetime import datetime
        return datetime.now().isoformat()
    
    def to_dict(self) -> Dict[str, Any]:
        """Serialize agent to dictionary"""
        return {
            'name': self.name,
            'capabilities': self.capabilities,
            'performance_metrics': self.performance_metrics,
            'interaction_count': len(self.interaction_history)
        }