# try:
#     stream = open('output.txt', 'wt')
#     stream.write('Lorem ipsu dolar')
# finally:
#     stream.close() #THIS IS REALLY IMPORTANT!

with open('output.txt', 'wt') as stream:
    stream.write('Lorem ipsum dolar with WITH')