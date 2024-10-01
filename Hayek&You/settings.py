import pysqlite3
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')