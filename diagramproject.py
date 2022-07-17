from diagrams import Cluster, Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.onprem.vcs import Git
from diagrams.onprem.client import Users
from diagrams.aws.storage import S3
from diagrams.onprem.network import Internet
from diagrams.saas.chat import Slack
from diagrams.onprem.monitoring import Datadog
from diagram.aws.network import ALB
with Diagram("", show=False):
    net = Internet("Internet")

    with Cluster("PROD VPC"):
        with Cluster(""):
            alb = [ALB("")]

        with Cluster(""):
            apa = [EC2("Apache Webserver"),
                        EC2("Middleware")]

        s3 = S3("")



        with Cluster(""):
            data = [RDS("Database")]


        with Cluster(""):
            abc = [Datadog("Datadog"),
                Slack("Slack")]

        gith = Git("Github")
        user = Users("Users")



    net >> alb >> apa
    data >> abc
    apa >> s3
    EC2("Apache Webserver") >> EC2("Middleware")
    EC2("Middleware") >> data
    user >> gith
    gith >> apa
