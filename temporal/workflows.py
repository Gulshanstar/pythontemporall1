from datetime import timedelta
from temporalio import workflow
from temporalio.common import RetryPolicy
from temporalio.common import RetryPolicy
# Import our activity, passing it through the sandbox
with workflow.unsafe.imports_passed_through():
    import activities
    

@workflow.defn
class LoanProcess:
    @workflow.run
    async def run(self, name: str) -> str:
         # Configure retry policy
        retry_policy = RetryPolicy(
            initial_interval=timedelta(seconds=5),  # Initial retry interval
            maximum_attempts=3,  # Maximum number of retry attempts
            maximum_interval=timedelta(seconds=60),  # Maximum interval between retries
            backoff_coefficient=2.0,  # Backoff coefficient for exponential backoff
            
        )
         
        steps1_res = await workflow.execute_activity(
            activities.steps1, name, schedule_to_close_timeout=timedelta(seconds=120),retry_policy= retry_policy
        )
        steps2_res = await workflow.execute_activity(
            activities.steps2, name, schedule_to_close_timeout=timedelta(seconds=120),retry_policy=retry_policy
        )
        steps3_res = await workflow.execute_activity(
            activities.steps3, name, schedule_to_close_timeout=timedelta(seconds=120),retry_policy=retry_policy
        )
        steps4_res = await workflow.execute_activity(
           activities.steps4, name, schedule_to_close_timeout=timedelta(seconds=120),retry_policy=retry_policy
        )
        steps5_res = await workflow.execute_activity(
            activities.steps5, name, schedule_to_close_timeout=timedelta(seconds=120),retry_policy=retry_policy
        )
        steps6_res = await workflow.execute_activity(
            activities.steps6, name, schedule_to_close_timeout=timedelta(seconds=120),retry_policy=retry_policy
        )
         
        return f"{steps2_res}"