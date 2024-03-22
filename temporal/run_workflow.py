# import asyncio
# from temporalio.client import Client

# # Import the workflow from the previous code
# import workflows

# async def main():
#     # Create client connected to server at the given address
#     client = await Client.connect("localhost:7233")

#     # Execute a workflow
#     for i in range(3):
#         result = await client.execute_workflow(workflows.LoanProcess.run, "gulshan mundri", id=f"loan_process-{i}", task_queue="my-task-queue")
#         print(f"Result: {result}-{i}")

# if __name__ == "__main__":
#     asyncio.run(main())

import asyncio
from temporalio.client import Client
import workflows

async def execute_workflow(client, name, workflow_id):
    # Execute the workflow asynchronously
    result = await client.execute_workflow(
        workflows.LoanProcess.run,
        name,
        id=workflow_id,
        task_queue="my-task-queue"
    )
    return result

async def main():
    # Create client connected to server at the given address
    client = await Client.connect("localhost:7233")

    # Execute workflows in parallel
    tasks = []
    for i in range(3):
        workflow_name = f"gulshan mundri-{i}"
        workflow_id = f"loan_process-{i}"
        tasks.append(
            execute_workflow(client, workflow_name, workflow_id)
        )

    # Gather all tasks and wait for them to complete
    results = await asyncio.gather(*tasks)

    # Print results
    for i, result in enumerate(results):
        print(f"Result: {result}-{i}")

if __name__ == "__main__":
    asyncio.run(main())
