from diagrams import Cluster, Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.onprem.vcs import Git
from diagrams.onprem.client import Users
from diagrams.aws.storage import S3
from diagrams.onprem.network import Internet
from diagrams.saas.chat import Slack
from diagrams.onprem.monitoring import Datadog
from diagrams.aws.network import ALB
with Diagram("", show=False):
    net = Internet("Internet")

    with Cluster("PROD VPS"):
        with Cluster("y"):
            alb = [ALB(""),
                      ]

        sec = S3("")

        with Cluster("x"):
            apa = [EC2("Apache Webserver"),
            EC2("Middleware")]


        with Cluster(""):
            data = [RDS("Database")]

    with Cluster("z"):
        slda = [Datadog("Datadog Monitor"),
                Slack("Slack")]
    Gith = Git("Github")
    dw = Users("Users")

    net >> alb >> sec >> apa
    Gith << dw
    Gith >> apa
    data >> slda
