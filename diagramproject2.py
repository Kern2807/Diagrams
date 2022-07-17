from diagrams import Cluster, Diagram, Edge
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.onprem.vcs import Git
from diagrams.onprem.client import Users
from diagrams.aws.storage import S3
from diagrams.onprem.network import Internet
from diagrams.saas.chat import Slack
from diagrams.onprem.monitoring import Datadog
from diagrams.aws.network import ALB
graph_attr = {
    "layout": "dot",
    "concentrate": "true",
    "compound": "true",
    "splines": "spline",
}
with Diagram(name="", graph_attr=graph_attr, show=False):
    net = Internet("Internet")


    Gith = Git("Github")
    Gith << Edge(color="darkgreen") << Users("Users")

    with Cluster("PROD VPC"):
        with Cluster("> Loadbalancer"):
            alb = [ALB("ALB")]
            net >> Edge(color="brown") >> alb

        with Cluster("EC2 Servers"):
            apa = EC2("Apache Webserver")
            mid = EC2("Middleware")
            apa >> Edge(color="darkred", style=("dotted")) >> mid


        alb >> Edge(color="darkblue") >> apa
        s3 = S3("S3")
        apa >> Edge(color="blue") >> s3
        mid >> Edge(color="blue") >> s3
        with Cluster("Database"):
            primary = RDS("Database")

        mid >> Edge(color="maroon") >> primary

        Gith >> Edge(color="black") >> mid
        Gith >> Edge(color="violet") >> apa
    with Cluster("Notifications"):
        slda = [Datadog("Datadog monitoring "),
                Slack("Slack")]
    primary >> Edge(color="purple") >> slda
