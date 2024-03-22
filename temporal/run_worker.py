import asyncio
import concurrent.futures
from temporalio.client import Client
from temporalio.worker import Worker
import prometheus_client
import activities
import workflows

def register_temporal_metrics():
    # Define your temporal metrics here, for example:
    global temporal_metric
    temporal_metric = prometheus_client.Gauge('temporal_metric', 'Description of temporal metric')


# Function to simulate your `MeterRegistry` setup
def meter_registry():
    # Create a CollectorRegistry
    registry = prometheus_client.CollectorRegistry()

    # Register temporal metrics
    register_temporal_metrics()
    return registry

# Function to start HTTP server
def start_server():
    prometheus_client.start_http_server(8000)
    # Register metrics for other activities as needed

    
async def main():
    # Create client connected to server at the given address
    client = await Client.connect("localhost:7233")

    # Run the worker
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as activity_executor:
        worker = Worker(
          client,
          task_queue="my-task-queue",
          workflows=[workflows.LoanProcess],
          activities=[activities.steps1, activities.steps2,activities.steps3,activities.steps4,activities.steps5,activities.steps6],
          activity_executor=activity_executor,
        )
        
        # Create your meter registry
        registry = meter_registry()
        
        # Start the HTTP server for Prometheus metrics
        start_server()
        await worker.run()

if __name__ == "__main__":
    asyncio.run(main())