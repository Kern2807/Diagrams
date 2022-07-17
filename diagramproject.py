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
with Diagram(name="", show=False):
    net = Internet("Internet")


    Gith = Git("Github")
    Gith << Edge(color="Black") << Users("Users")

    with Cluster("PROD VPS"):
        with Cluster("x"):
            alb = [ALB("ALB")]
            net >> alb

        with Cluster("y"):
            apa = EC2("Apache Webserver")
            mid = EC2("Middleware")
            apa >> mid


        alb >> Edge(color="black") >> apa
        s3 = S3("S3")
        apa >> s3
        mid >> s3
        with Cluster("z"):
            primary = RDS("Database")

        mid >> Edge(color="black") >> primary

        Gith >> mid
        Gith >> apa
    with Cluster("r"):
        slda = [Datadog("Datadog monitoring "),
                Slack("Slack")]
    primary >> slda
