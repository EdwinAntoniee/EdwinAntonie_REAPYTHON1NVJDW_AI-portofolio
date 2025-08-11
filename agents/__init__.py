from .education_agent import education_agent
from .finance_agent import finance_agent
from .health_agent import health_agent
from .daily_agent import daily_agent

AGENT_MAP = {
    "education": education_agent,
    "finance": finance_agent,
    "health": health_agent,
    "daily": daily_agent
}
