from typing import List, Optional
from pydantic import BaseModel, Field, validator


class WorkExperience(BaseModel):
    job_title: str = Field(description="Job title or position.")
    company: str = Field(description="The company name.")
    experience: int = Field(description="Years of experience in the job.")
    responsibilities: List[str] = Field(description="List of responsibilities in the job.")


class Education(BaseModel):
    degree: str = Field(description="Degree obtained.")
    school: str = Field(description="The university name.")
    major: str = Field(description="Major subject.")
    year: Optional[int] = Field(description="Year of graduation.")

    @validator('year', pre=True, always=True)
    def set_year(cls, v):
        if v is None:
            return 0
        return v


class Resume(BaseModel):
    """Structured resume data."""

    name: str = Field(description="Name of the person")
    professional_summary: str = Field(description="Professional summary of the person.")
    work_experience: List[WorkExperience] = Field(description="List of work experiences held by the person.")
    education: List[Education] = Field(description="List of educational qualifications of the person.")
    skills: List[str] = Field(description="List of skills relevant to the jobs.")