import cx_Oracle
import pandas as pd
import time
from prefect import flow, task
from tqdm import tqdm
from prefect.server.schemas.schedules import IntervalSchedule
from prefect.deployments import Deployment

user = ''
password = ''
dsn = ''
sap_machine_list = ["p47", "p45", "p72", "p79", "p81", "p87", "p99", "POE", "PS0"]

conn = cx_Oracle.connect(user=user, password=password, dsn=dsn)

@task
def read_query(query, *args):
        return(pd.read_sql(query, conn))

@flow(retries=2, retry_delay_seconds=5, name="Query")
def query_generator(): 
        data = pd.DataFrame()  
        
        for _sys in tqdm(sap_machine_list):
                # PROBLEMA 
                # CRIAR UM PROCEDIMENTO EM PL SQL QUE FAÇA LOOP POR TODAS AS MAQUINAS SAP                
                new_query = """
                        SELECT 
                                WERKS as Plant,
                                STRAS as "Address",
                                ORT01 as City,
                                EKORG as "Purchase Group",
                                LAND1 as Country,
                                NAME1 as "Plant Name",
                                GBKUR as "Business Area",
                                SYSID
                        FROM MARD_DALI_BBM.T001W_{_sys}
                        WHERE AKTIV = 'X'
                """.format(_sys = _sys)

                _data = read_query(new_query)
                data = data.append(_data, ignore_index=True)
                time.sleep(1)

        data = data.drop_duplicates()
        data.to_excel("parameterlist.xlsx")
        return 

cron = Deployment.build_from_flow(
        query_generator,
        "Generate Parameterlist",
        schedule=(IntervalSchedule(interval=3600))
        )

if __name__ == "__main__":
        cron.apply()
