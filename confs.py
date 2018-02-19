import psycopg2

def get_conn():
	conn = psycopg2.connect("\
	dbname='teste'\
	user='postgres'\
	host='localhost'\
	password='postgres'\
	");

	return conn.cursor()