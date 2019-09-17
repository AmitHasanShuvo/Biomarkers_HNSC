import pandas

df = pandas.read_csv('GSE6631Processed.csv')

filename = 'GSE6631-Upregulated.csv'
upregulated = open(filename, 'w')

filename = 'GSE6631-Downregulated.csv'
downregulated = open(filename, 'w')

upregulated.write('Gene,p.value,logFC,GeneSym\n')
downregulated.write('Gene,p.value,logFC,GeneSym\n')

upDEGs = 0
downDEGs = 0
for i in range(0,len(df)):
    if float(df['P.Value'][i])< 0.05 and float(df['logFC'][i])>1.0:
        upregulated.write(str(df['Gene'][i]))
        upregulated.write(',')
        upregulated.write(str(df['p.value'][i]))
        upregulated.write(',')
        #upregulated.write(str(df['P.adjusted.BH'][i]))
        #upregulated.write(',')
        upregulated.write(str(df['logFC'][i]))
        upregulated.write(',')
        upregulated.write(str(df['Gene.symbol'][i]))
        upregulated.write('\n')
        upDEGs = upDEGs+1
    elif float(df['P.Value'][i])<0.01 and float(df['logFC'][i])<-1.0:
        downregulated.write(str(df['Gene'][i]))
        downregulated.write(',')
        downregulated.write(str(df['p.value'][i]))
        downregulated.write(',')
        ##downregulated.write(',')
        downregulated.write(str(df['logFC'][i]))
        downregulated.write(',')
        downregulated.write(str(df['Gene.symbol'][i]))
        downregulated.write('\n')
        downDEGs = downDEGs+1

print(upDEGs)
print(downDEGs)

upregulated.close()
downregulated.close()