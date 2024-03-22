from temporalio import activity
from datetime import timedelta
import prometheus_client

# Define Prometheus gauge metrics
steps1_metric = prometheus_client.Gauge('steps1_success', 'Number of successful executions for steps1 activity')
steps1_metricf = prometheus_client.Gauge('steps1_failure', 'Number of successful executions for steps1 activity')
steps2_metric = prometheus_client.Gauge('steps2_success', 'Number of successful executions for steps2 activity')
steps2_metricf = prometheus_client.Gauge('steps2_failure', 'Number of successful executions for steps2 activity')
steps3_metric = prometheus_client.Gauge('steps3_success', 'Number of successful executions for steps3 activity')
steps4_metric = prometheus_client.Gauge('steps4_success', 'Number of successful executions for steps4 activity')
steps5_metric = prometheus_client.Gauge('steps5_success', 'Number of successful executions for steps5 activity')
steps6_metric = prometheus_client.Gauge('steps6_success', 'Number of successful executions for steps6 activity')


@activity.defn
def steps1(name: str) -> str:
    try:
        steps1_metric.inc()
        return f"Hello, 111!"
    except Exception as e:
        steps1_metric.dec()
        raise e

@activity.defn
def steps2(name: str) -> str:
    try:
        
        steps2_metric.inc()
        return f"Hello, 222222!"
    except Exception as e:
        
        raise e

@activity.defn
def steps3(name: str) -> str:
    try:
        steps3_metric.inc()
        return f"Hello, 222222!"
    except Exception as e:
        steps3_metric.dec()
        raise e


@activity.defn
def steps4(name: str) -> str:
    steps4_metric.inc()
    return f"Hello, 4!"

@activity.defn
def steps5(name: str) -> str:
    steps5_metric.inc()
    return f"Hello, 5!"

@activity.defn
def steps6(name: str) -> str:
    steps6_metric.inc()
    return f"Hello, 6!"

