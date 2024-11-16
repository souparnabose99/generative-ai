from typing import Optional, Literal
from langchain_core.tools import tool

from jobs import Job
from resume import Resume


def process_job() -> Job:
    """Process job data."""
    job = Job.mock()
    return job


def process_resume() -> Resume:
    """Process resume data."""
    resume = Resume.mock()
    return resume


