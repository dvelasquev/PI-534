'''
Dag para la ejecución del contenedor del proyecto ci-345_controles-valores-de-unidad-de-fondo
'''
from datetime import timedelta
from airflow import models

from airflow.utils.dates import days_ago
from airflow.contrib.operators.gcp_container_operator import GKEPodOperator
from airflow.models import Variable


config_general = Variable.get("config_general",deserialize_json=True)
proyecto = config_general['proj_name']
namespaces = Variable.get("namespaces_k8s",deserialize_json=True)

default_dag_args = {
    'owner': 'gmontoya',
    'depends_on_past': False,
    'start_date': days_ago(2),
    'email': [config_general['notification_email']],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

with models.DAG('proceso_transformacion_calidad_datos_dbt',
                default_args=default_dag_args,
                description='''Proceso transformación calidad de datos''',
                schedule_interval='30 10 1 * *',
                catchup=False) as dag:


    operator = GKEPodOperator(task_id='contenedor_dbt_calidad_datos',
                            project_id=config_general['proj_name'],
                            location='us-east1-b',
                            cluster_name=config_general['cluster-k8s'],
                            name='ci-345_controles-valores-de-unidad-de-fondo',
                            namespace=namespaces['ci-345_controles-valores-de-unidad-de-fondo'],
                            image=f'gcr.io/{proyecto}/ci-345_controles-valores-de-unidad-de-fondo:latest',
                            cmds=["dbt"],
                            arguments=["run", "--profiles-dir", ".",
                                       "--fail-fast", "--target",
                                       config_general['dbt_target']],
                            image_pull_policy='Always',
                            service_account_name='servicio-k8s',
                            env_vars={
                                'GOOGLE_CLOUD_PROJECT': config_general['proj_name'],
                                'Z51_DATASET': config_general['z51_calidad']
                            })

operator # pylint: disable=pointless-statement
