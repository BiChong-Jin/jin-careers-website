from sqlalchemy import create_engine, text

# For security reasons, the plain context of dbinfo
# is not showing below, instead is has been stored in at 
# PlanetScale.com where the cloud database servered as a 
# seceret Key.
# mysql+pymysql://bbksk5gnsxjzyhv9vesk:pscale_pw_nwILVpjYaPHZE6jThp1BuCbXEryTJBwNi2eTkg7kKAF@aws.connect.psdb.cloud/jincareers?charset=utf8mb4
dbinfo = Key
engine = create_engine(dbinfo,
                       connect_args={
                           "ssl": {
                            "ssl_ca": "/etc/ssl/cert.pem"
                            }
                       })


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
      jobs.append(dict(row._mapping))
    return jobs
    
def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs where id = id"))
    rows = result.all()

    if len(rows) == 0:
      return None
    
    else:
      return dict(rows[int(id)-1]._mapping)

    
    # print("type-result-", type(result))
    # result_all = result.all()
    # print("type-result.all", type(result_all))
    # first_result = result_all[0]
    # print("type-first-result-", type(first_result))
    # first_result_dict = dict(result_all[0])
    # print("type-firstresultdict-", first_result_dict)

# def load_jobs_from_db():
#   with engine.connect() as conn:
#     result = conn.execute(text("select * from jobs"))
#     # print(result.all())


#     for row in result.all():
#       jobs = []
#       jobs.append(dict(row))
#       print(jobs)


# load_jobs_from_db()



###
# from dotenv import load_dotenv
# load_dotenv()
# import os
# import MySQLdb

# connection = MySQLdb.connect(
#   host= os.getenv("DB_HOST"),
#   user=os.getenv("DB_USERNAME"),
#   passwd= os.getenv("DB_PASSWORD"),
#   db= os.getenv("DB_NAME"),
#   autocommit = True,
#   ssl_mode = "VERIFY_IDENTITY",
#   ssl      = {
#     "ca": "/etc/ssl/cert.pem"
#   }
# )

###