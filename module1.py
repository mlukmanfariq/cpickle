#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      developer
#
# Created:     09/04/2018
# Copyright:   (c) developer 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

try:
    import cPickle as pickle
except:
    import pickle


data = [{'id':'P1','name':'Lukman'}, 2,  'test']
print data,'\n'

data_string = pickle.dumps(data)
print  data_string

load_data = pickle.loads(data_string)
print load_data