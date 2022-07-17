from diagrams import Cluster, Diagram
from diagrams.aws.compute import Compute
from diagrams.aws.devtools import Cloud9Resource
from diagrams.aws.network import Route53

with Diagram("Test", show=False):
    blah = Route53("dns")
    service = Compute("service")

    with Cluster("Test Cluster"):
        db_primary = Cloud9Resource("primary")
        db_primary << [Cloud9Resource("replicax"),
                     Cloud9Resource("replicay")]

    blah - service << db_primary
