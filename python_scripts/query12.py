#How much revenue has been generated for the government
import pymysql
import queue
import sys

def query(HOST,USER,PASSWORD,DATABASE):
  db = pymysql.connect(host=HOST,user=USER,passwd=PASSWORD,database=DATABASE)
  project=db.cursor()
  project.execute ("Select SUM(entry_fee*population) from place")
  k=0
  #k=int(k)
  for i in project:
    k+=i[0];
  print(k)
  return k
if __name__ == '__main__':
  if(len(sys.argv) == 1):
    query('37.59.55.185','OH7hLHUPZv','PCYgN41QXH','OH7hLHUPZv')
  else:
    query('127.0.0.1','shubham','randomNULL_123','tut1')
